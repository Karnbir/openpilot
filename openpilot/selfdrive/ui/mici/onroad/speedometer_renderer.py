"""OLED instrument face. Pure Raylib geometry; no textures, shaders or font assets."""
import math
import pyray as rl
from openpilot.selfdrive.ui.mici.onroad.speedometer_state import SEGMENTS, SpeedometerState

TEAL = (139, 202, 195)
RED = (193, 112, 115)
DIGITS = ('abcdef', 'bc', 'abdeg', 'abcdg', 'bcfg', 'acdfg', 'acdefg', 'abc', 'abcdefg', 'abcdfg')
STROKES = {
  'a': ((12, 0), (64, 0)), 'b': ((68, 8), (68, 51)), 'c': ((68, 63), (68, 106)),
  'd': ((12, 114), (64, 114)), 'e': ((8, 63), (8, 106)), 'f': ((8, 8), (8, 51)),
  'g': ((12, 57), (64, 57)),
}


def color(rgb, alpha):
  return rl.Color(*rgb, round(255 * min(max(alpha, 0), 1)))


def draw_speedometer(rect, state: SpeedometerState, now: float, font=None):
  """Render in a 720×322 design space, preserving aspect ratio inside any viewport."""
  rl.draw_rectangle_rec(rect, rl.BLACK)
  scale = min(rect.width / 720, rect.height / 322)
  ox, oy = rect.x + (rect.width - 720 * scale) / 2, rect.y + (rect.height - 322 * scale) / 2

  def point(x, y):
    return rl.Vector2(ox + x * scale, oy + (y - 50) * 0.66 * scale)

  def line(a, b, width, rgb, alpha):
    rl.draw_line_ex(point(*a), point(*b), width * scale, color(rgb, alpha))

  def label(text, x, y, size, alpha=0.65):
    rl.draw_text_ex(font or rl.get_font_default(), text, point(x, y), size * scale, scale, color(TEAL, alpha))

  # Quiet octagonal wire mesh confined to the instrument, leaving the OLED background black.
  for row in range(7):
    for col in range(12):
      x, y = 125 + col * 40, 145 + row * 40
      vertices = [(x + 17 * math.cos(math.pi / 8 + j * math.pi / 4),
                   y + 17 * math.sin(math.pi / 8 + j * math.pi / 4)) for j in range(8)]
      for j in range(8):
        line(vertices[j], vertices[(j + 1) % 8], 0.7, TEAL, 0.055)

  # Segments climb from lower left to upper right; braking fills from the other end.
  shimmer = 0.96 + 0.025 * math.sin(now * 17) + 0.015 * math.sin(now * 31)
  for i in range(SEGMENTS):
    angle = math.radians(178 + i * 6.7)
    end = angle + math.radians(4.8)
    outer, inner = 330, 287
    corners = [(405 + r * math.cos(a), 401 + r * math.sin(a))
               for r, a in ((inner, angle), (outer, angle), (outer, end), (inner, end))]
    for j in range(4):
      line(corners[j], corners[(j + 1) % 4], 1, TEAL, 0.16)
    for rgb, level in ((TEAL, state.positive[i]), (RED, state.negative[SEGMENTS - 1 - i])):
      if level < 0.005:
        continue
      # Filled trapezoids with a thin, low-opacity halo along their long edges.
      vertices = [point(*p) for p in corners]
      rl.draw_triangle(vertices[0], vertices[2], vertices[1], color(rgb, level * 0.65 * shimmer))
      rl.draw_triangle(vertices[0], vertices[3], vertices[2], color(rgb, level * 0.65 * shimmer))
      for j in range(4):
        line(corners[j], corners[(j + 1) % 4], 5, rgb, level * 0.06 * shimmer)
        line(corners[j], corners[(j + 1) % 4], 1.2, rgb, level * 0.8)

  text = '---' if state.speed is None else str(min(999, round(state.speed)))
  digit_scale = 1.65
  x0 = 604 - len(text) * 94 * digit_scale
  for index, digit in enumerate(text):
    active = 'g' if digit == '-' else DIGITS[int(digit)]
    for key, (a, b) in STROKES.items():
      def digit_point(p, index=index):
        x, y = p
        return (x0 + index * 94 * digit_scale + (x + (114 - y) * 0.15) * digit_scale, 222 + y * digit_scale)
      start, finish = digit_point(a), digit_point(b)
      # Ghost electrodes and a soft teal halo evoke a tube without flashing the speed.
      line(start, finish, 2, TEAL, 0.10)
      if key in active:
        line(start, finish, 23, TEAL, 0.025 * shimmer)
        line(start, finish, 17, TEAL, 0.06 * shimmer)
        line(start, finish, 10, TEAL, 0.91)
        line(start, finish, 2, (204, 234, 226), 0.48)
  label('KM/H', 509, 432, 22)
  label('DESIRED ACCEL', 78, 458, 13, 0.45)
