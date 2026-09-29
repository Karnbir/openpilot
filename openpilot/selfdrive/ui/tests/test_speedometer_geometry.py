import unittest
from openpilot.selfdrive.ui.mici.onroad.speedometer_renderer import clip_line, electrode_mesh, arc_shapes, digit_shapes


class TestElectrodeMesh(unittest.TestCase):
  def test_clips_wire_to_electrode(self):
    box = ((0, 0), (10, 0), (10, 10), (0, 10))
    self.assertEqual(clip_line((-5, 5), (15, 5), box), ((0, 5), (10, 5)))
    self.assertIsNone(clip_line((-5, -1), (15, -1), box))

  def test_mesh_is_inside_all_electrodes(self):
    polygons = list(arc_shapes()) + [p for digit in digit_shapes(3) for p in digit.values()]
    for polygon in polygons:
      wires = electrode_mesh(polygon)
      self.assertTrue(wires)
      for wire in wires:
        for x, y in wire:
          for a, b in zip(polygon, polygon[1:] + polygon[:1], strict=True):
            self.assertGreaterEqual((b[0] - a[0]) * (y - a[1]) - (b[1] - a[1]) * (x - a[0]), -1e-7)


if __name__ == '__main__':
  unittest.main()
