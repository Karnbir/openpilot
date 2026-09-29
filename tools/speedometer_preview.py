#!/usr/bin/env python3
"""Standalone Raylib preview; does not connect to the car or publish control messages."""
import argparse
import math
import pyray as rl
from openpilot.selfdrive.ui.mici.onroad.speedometer_renderer import draw_speedometer
from openpilot.selfdrive.ui.mici.onroad.speedometer_state import SpeedometerState


def main():
  parser = argparse.ArgumentParser(description=__doc__)
  parser.add_argument('--screenshot', help='Save a deterministic 81 km/h preview and exit')
  parser.add_argument('--braking', action='store_true')
  args = parser.parse_args()
  rl.set_config_flags(rl.ConfigFlags.FLAG_MSAA_4X_HINT)
  rl.init_window(1072, 480, 'Speedometer / simulated telemetry')
  rl.set_target_fps(60)
  capture = rl.load_render_texture(1072, 480) if args.screenshot else None
  state = SpeedometerState()
  shown_at = rl.get_time()
  try:
    frame = 0
    while not rl.window_should_close():
      now = rl.get_time()
      accel = (-2.3 if args.braking else 1.4) if args.screenshot else 2.2 * math.sin(now * 0.5)
      speed = 22.5 if args.screenshot else (81 + 12 * math.sin(now * 0.25)) / 3.6
      state.update(speed, speed, accel, speed_valid=True, control_active=True, dt=1 / 60)
      rl.begin_drawing()
      if capture is not None:
        rl.begin_texture_mode(capture)
      rl.clear_background(rl.BLACK)
      draw_speedometer(rl.Rectangle(0, 0, 1072, 480), state, now, visible_seconds=now - shown_at)
      if capture is not None:
        rl.end_texture_mode()
        rl.draw_texture_rec(capture.texture, rl.Rectangle(0, 0, 1072, -480), rl.Vector2(0, 0), rl.WHITE)
      rl.end_drawing()
      frame += 1
      if args.screenshot and frame >= 90:
        image = rl.load_image_from_texture(capture.texture)
        rl.image_flip_vertical(image)
        rl.export_image(image, args.screenshot)
        rl.unload_image(image)
        break
  finally:
    if capture is not None:
      rl.unload_render_texture(capture)
    rl.close_window()


if __name__ == '__main__':
  main()
