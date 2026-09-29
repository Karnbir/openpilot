"""Display-only telemetry and frame-rate independent segment animation."""
import math
from dataclasses import dataclass, field

SEGMENTS = 5
ACCEL_SCALE = 2.0  # m/s² at full scale (display scale, not a control limit)
BRAKE_SCALE = 3.5


@dataclass
class SpeedometerState:
  speed: float | None = None
  cluster_seen: bool = False
  positive: list[float] = field(default_factory=lambda: [0.0] * SEGMENTS)
  negative: list[float] = field(default_factory=lambda: [0.0] * SEGMENTS)

  def update(self, speed: float, cluster: float, accel: float, *, speed_valid: bool,
             control_active: bool, dt: float) -> None:
    if speed_valid:
      self.cluster_seen |= math.isfinite(cluster) and cluster > 0
      velocity = cluster if self.cluster_seen else speed
      self.speed = max(0.0, velocity * 3.6) if math.isfinite(velocity) else None
    else:
      self.speed = None
    accel = accel if control_active and math.isfinite(accel) else 0.0
    if not control_active:
      self.positive[:] = self.negative[:] = [0.0] * SEGMENTS
      return
    dt = min(max(dt, 0.0), 0.1)
    for levels, amount in ((self.positive, max(accel, 0) / ACCEL_SCALE),
                           (self.negative, max(-accel, 0) / BRAKE_SCALE)):
      for i, current in enumerate(levels):
        target = min(max(amount * SEGMENTS - i, 0.0), 1.0)
        tau = 0.16 if target > current else 0.24
        levels[i] += (target - current) * (1 - math.exp(-dt / tau))


def swipe_target(dx: float, dy: float, current: bool) -> bool:
  if abs(dy) >= 45 and abs(dy) > 1.5 * abs(dx):
    return dy > 0
  return current

