"""
Copyright (c) 2021-, Haibin Wen, sunnypilot, and a number of other contributors.

This file is part of sunnypilot and is licensed under the MIT License.
See the LICENSE.md file in the root directory for more details.
"""
import pyray as rl

from openpilot.common.params import Params
from openpilot.selfdrive.ui.mici.onroad.hud_renderer import HudRenderer
from openpilot.selfdrive.ui.sunnypilot.onroad.blind_spot_indicators import BlindSpotIndicators
from openpilot.selfdrive.ui.ui_state import ui_state
from openpilot.system.ui.lib.application import gui_app, FontWeight


class JoystickDebugOverlay:
  def __init__(self):
    self._params = Params()
    self._font = None

  def _ensure_font(self):
    if self._font is None:
      self._font = gui_app.font(FontWeight.BOLD)

  def render(self, rect: rl.Rectangle) -> None:
    if not self._params.get_bool("JoystickDebugMode"):
      return
    if not ui_state.started:
      return

    self._ensure_font()

    actuators = ui_state.sm['carControl'].actuators
    accel = actuators.accel
    lateral = actuators.torque
    damp = actuators.dampFactor if actuators.dampFactor > 0 else 100.0

    font_size = 48
    line_height = 60
    x = rect.x + rect.width - 300
    y = rect.y + 120

    labels = [
      ("ACCEL", f"{accel:+.2f}"),
      ("LATERAL", f"{lateral:+.2f}"),
      ("DAMP", f"{damp:.0f}"),
    ]

    for label, value in labels:
      rl.draw_text_ex(self._font, f"{label}: {value}", rl.Vector2(x, y), font_size, 0, rl.WHITE)
      y += line_height


class HudRendererSP(HudRenderer):
  def __init__(self):
    super().__init__()
    self.blind_spot_indicators = BlindSpotIndicators()
    self._joystick_overlay = JoystickDebugOverlay()

  def _update_state(self) -> None:
    super()._update_state()
    self.blind_spot_indicators.update()

  def _render(self, rect: rl.Rectangle) -> None:
    super()._render(rect)
    self.blind_spot_indicators.render(rect)
    self._joystick_overlay.render(rect)

  def _has_blind_spot_detected(self) -> bool:

    return self.blind_spot_indicators.detected
