"""Teal glass-electrode instrument, drawn entirely with Raylib geometry."""
import math
from functools import lru_cache
import pyray as rl
from openpilot.selfdrive.ui.mici.onroad.speedometer_state import SEGMENTS, SpeedometerState

TEAL = (139, 202, 195)
RED = (193, 112, 115)
CORE = (200, 229, 221)
DIGITS = ('abcdef', 'bc', 'abdeg', 'abcdg', 'bcfg', 'acdfg', 'acdefg', 'abc', 'abcdefg', 'abcdfg')


def color(rgb, alpha):
  return rl.Color(*rgb, round(255 * min(max(alpha, 0), 1)))


def clip_line(a, b, polygon):
  """Clip a wire to a convex, clockwise-on-screen electrode outline."""
  low, high = 0.0, 1.0
  dx, dy = b[0] - a[0], b[1] - a[1]
  for p, q in zip(polygon, polygon[1:] + polygon[:1], strict=True):
    ex, ey = q[0] - p[0], q[1] - p[1]
    distance = ex * (a[1] - p[1]) - ey * (a[0] - p[0])
    slope = ex * dy - ey * dx
    if abs(slope) < 1e-9:
      if distance < 0:
        return None
    elif slope > 0:
      low = max(low, -distance / slope)
    else:
      high = min(high, -distance / slope)
    if low > high:
      return None
  return ((a[0] + low * dx, a[1] + low * dy), (a[0] + high * dx, a[1] + high * dy))


@lru_cache(maxsize=128)
def electrode_mesh(polygon):
  """Cache clipped octagonal lattice; no mesh spills onto the OLED black."""
  wires = []
  step, radius = 13, 6
  for y in range(math.floor((min(p[1] for p in polygon) - radius) / step) * step,
                 math.ceil(max(p[1] for p in polygon) + radius), step):
    for x in range(math.floor((min(p[0] for p in polygon) - radius) / step) * step,
                   math.ceil(max(p[0] for p in polygon) + radius), step):
      vertices = [(x + radius * math.cos(math.pi / 8 + j * math.pi / 4),
                   y + radius * math.sin(math.pi / 8 + j * math.pi / 4)) for j in range(8)]
      for a, b in zip(vertices, vertices[1:] + vertices[:1], strict=True):
        if clipped := clip_line(a, b, polygon):
          wires.append(clipped)
  return wires


def stroke_polygon(a, b, width):
  """Six-sided LCD segment with pointed, machined ends."""
  dx, dy = b[0] - a[0], b[1] - a[1]
  length = math.hypot(dx, dy)
  ux, uy = dx / length, dy / length
  nx, ny = -uy * width / 2, ux * width / 2
  bevel = width * 0.48
  return (a, (a[0] + ux * bevel - nx, a[1] + uy * bevel - ny),
          (b[0] - ux * bevel - nx, b[1] - uy * bevel - ny), b,
          (b[0] - ux * bevel + nx, b[1] - uy * bevel + ny),
          (a[0] + ux * bevel + nx, a[1] + uy * bevel + ny))


@lru_cache(maxsize=4)
def digit_shapes(count):
  scale = 1.24 if count <= 2 else 1.08
  start = 645 - count * 102 * scale
  strokes = {'a': ((15, 0), (74, 0)), 'g': ((15, 62), (74, 62)), 'd': ((15, 124), (74, 124)),
             'f': ((9, 8), (9, 54)), 'b': ((80, 8), (80, 54)),
             'e': ((9, 70), (9, 116)), 'c': ((80, 70), (80, 116))}
  shapes = []
  for index in range(count):
    digit = {}
    for key, (a, b) in strokes.items():
      digit[key] = tuple((start + index * 102 * scale + (x + (124 - y) * 0.10) * scale,
                          121 + y * scale) for x, y in stroke_polygon(a, b, 18))
    shapes.append(digit)
  return shapes


@lru_cache(maxsize=1)
def arc_cells():
  # Separate swept boundaries give the ribbon a flat foot and a clean diagonal tip.
  # Unlike offsetting a centerline, this cannot create flared or hooked end caps.
  def curve(t, inner=False):
    u = 1 - t
    points = ((222, 272), (319, 106), (299, 102), (622, 102)) if inner else (
      (50, 272), (236, 36), (266, 36), (668, 36))
    return tuple(u**3 * points[0][axis] + 3*u*u*t * points[1][axis] +
                 3*u*t*t * points[2][axis] + t**3 * points[3][axis] for axis in (0, 1))

  samples = [curve(i / 240) for i in range(241)]
  distances = [0.0]
  for a, b in zip(samples, samples[1:], strict=False):
    distances.append(distances[-1] + math.hypot(b[0] - a[0], b[1] - a[1]))

  def parameter(distance):
    for i in range(1, len(distances)):
      if distances[i] >= distance:
        blend = (distance - distances[i - 1]) / (distances[i] - distances[i - 1])
        return (i - 1 + blend) / 240
    return 1.0

  sections = []
  for i in range(SEGMENTS):
    inner, outer = [], []
    start = i / SEGMENTS + (0.005 if i else 0)
    end = (i + 1) / SEGMENTS - (0.005 if i < SEGMENTS - 1 else 0)
    for j in range(13):
      t = parameter(distances[-1] * (start + (end - start) * j / 12))
      inner.append(curve(t, inner=True))
      outer.append(curve(t))
    sections.append(tuple((inner[j], outer[j], outer[j + 1], inner[j + 1]) for j in range(12)))
  return sections


@lru_cache(maxsize=1)
def arc_shapes():
  return [tuple([cell[0] for cell in cells] + [cells[-1][3], cells[-1][2]] +
                [cell[1] for cell in reversed(cells)]) for cells in arc_cells()]


def draw_speedometer(rect, state: SpeedometerState, now: float, font=None):
  rl.draw_rectangle_rec(rect, rl.BLACK)
  scale = min(rect.width / 720, rect.height / 322)
  ox, oy = rect.x + (rect.width - 720 * scale) / 2, rect.y + (rect.height - 322 * scale) / 2

  def point(p):
    return rl.Vector2(ox + p[0] * scale, oy + p[1] * scale)

  def line(a, b, width, rgb, alpha):
    rl.draw_line_ex(point(a), point(b), width * scale, color(rgb, alpha))

  def electrode(polygon, rgb, brightness, phase, cells=None):
    # Multi-width low-opacity outlines simulate local bloom without a full-screen shader.
    glow = brightness * (0.99 + 0.006 * math.sin(now * 7 + phase) + 0.004 * math.sin(now * 13 + phase))
    edges = list(zip(polygon, polygon[1:] + polygon[:1], strict=True))
    cells = cells or (polygon,)
    if brightness > 0.01:
      for width, alpha in ((15, 0.012), (8, 0.03), (3, 0.10)):
        for a, b in edges:
          line(a, b, width, rgb, glow * alpha)
      for cell in cells:
        for i in range(1, len(cell) - 1):
          rl.draw_triangle(point(cell[0]), point(cell[i + 1]), point(cell[i]), color(rgb, brightness * 0.44))
    for cell in cells:
      for a, b in electrode_mesh(cell):
        line(a, b, 0.65, rgb, 0.025 + brightness * 0.24)
    for a, b in edges:
      line(a, b, 1.1, rgb, 0.075 + brightness * 0.64)
    if brightness > 0.01:
      # A thin warm-white cathode edge provides depth inside the desaturated teal glass.
      line(polygon[0], polygon[1], 0.55, CORE, brightness * 0.48)

  for i, polygon in enumerate(arc_shapes()):
    positive, negative = state.positive[i], state.negative[SEGMENTS - 1 - i]
    electrode(polygon, TEAL, positive, i * 0.4, arc_cells()[i])
    if negative > 0.005:
      electrode(polygon, RED, negative, i * 0.4, arc_cells()[i])

  # Keep dense wire geometry in separate batches so subsequent digits remain visible.
  rl.rl_draw_render_batch_active()
  text = '---' if state.speed is None else str(min(999, round(state.speed)))
  for digit, shapes in zip(text, digit_shapes(len(text)), strict=True):
    active = 'g' if digit == '-' else DIGITS[int(digit)]
    for key, polygon in shapes.items():
      electrode(polygon, TEAL, 0.95 if key in active else 0, 0)
    rl.rl_draw_render_batch_active()

  def label(text, x, y, size, alpha):
    rl.draw_text_ex(font or rl.get_font_default(), text, point((x, y)), size * scale, scale, color(TEAL, alpha))

  label('KM/H', 579, 294, 16, 0.68)
  label('DESIRED ACCEL', 78, 294, 11, 0.46)
