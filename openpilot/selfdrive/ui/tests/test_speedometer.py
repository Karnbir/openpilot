import math
import unittest
from openpilot.selfdrive.ui.mici.onroad.speedometer_state import SpeedometerState, swipe_target


class TestSpeedometer(unittest.TestCase):
  def update(self, state, speed=20, cluster=0, accel=1, speed_valid=True, control_active=True, dt=1 / 60):
    state.update(speed, cluster, accel, speed_valid=speed_valid, control_active=control_active, dt=dt)

  def test_cluster_fallback_and_stopped_cluster(self):
    state = SpeedometerState()
    self.update(state)
    self.assertEqual(state.speed, 72)
    self.update(state, cluster=21)
    self.assertAlmostEqual(state.speed, 75.6)
    self.update(state, cluster=0)
    self.assertEqual(state.speed, 0)

  def test_invalid_speed_does_not_display_zero(self):
    state = SpeedometerState()
    self.update(state, speed_valid=False)
    self.assertIsNone(state.speed)
    self.update(state, speed=math.nan)
    self.assertIsNone(state.speed)

  def test_inactive_clears_requested_acceleration(self):
    state = SpeedometerState()
    for _ in range(60):
      self.update(state)
    self.assertGreater(state.positive[0], 0.99)
    self.update(state, control_active=False)
    self.assertFalse(any(state.positive + state.negative))

  def test_direction_and_bounds(self):
    state = SpeedometerState()
    for _ in range(120):
      self.update(state, accel=-100)
    self.assertFalse(any(state.positive))
    self.assertTrue(all(0.99 < level <= 1 for level in state.negative))
    self.update(state, accel=math.nan)
    self.assertTrue(all(math.isfinite(level) for level in state.negative))

  def test_swipe_direction_and_persistence(self):
    self.assertTrue(swipe_target(5, 60, False))
    self.assertFalse(swipe_target(5, -60, True))
    for dx, dy in ((0, 0), (0, 20), (60, 5), (60, 60)):
      self.assertTrue(swipe_target(dx, dy, True))
      self.assertFalse(swipe_target(dx, dy, False))

  def test_animation_frame_rate_independent(self):
    slow, fast = SpeedometerState(), SpeedometerState()
    for _ in range(30):
      self.update(slow, dt=1 / 30)
    for _ in range(120):
      self.update(fast, dt=1 / 120)
    for a, b in zip(slow.positive, fast.positive, strict=True):
      self.assertAlmostEqual(a, b)


if __name__ == '__main__':
  unittest.main()
