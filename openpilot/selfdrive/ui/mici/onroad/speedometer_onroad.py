"""Vertical instrument toggle layered around the unmodified stock road view."""
from openpilot.cereal import log
from openpilot.selfdrive.ui.ui_state import ui_state
from openpilot.selfdrive.ui.mici.onroad.augmented_road_view import AugmentedRoadView
from openpilot.selfdrive.ui.mici.onroad.speedometer import SpeedometerView
from openpilot.selfdrive.ui.mici.onroad.speedometer_state import swipe_target



class SpeedometerOnroadView(AugmentedRoadView):
  def __init__(self, bookmark_callback=None):
    super().__init__(bookmark_callback)
    self._instrument = self._child(SpeedometerView())
    self._custom = False
    self._touch_start = None
    self._vertical_drag = False
    self._suppress_click = False

  @property
  def lock_horizontal_scroll(self):
    return ui_state.started and (self._custom or self._vertical_drag or self.is_swiping_left())

  def _handle_mouse_event(self, event):
    if event.left_pressed:
      self._touch_start = (event.pos.x, event.pos.y)
      self._vertical_drag = False
      self._suppress_click = False
    if self._touch_start is not None:
      dx, dy = event.pos.x - self._touch_start[0], event.pos.y - self._touch_start[1]
      self._vertical_drag = abs(dy) > 15 and abs(dy) > 1.5 * abs(dx)
      if event.left_released:
        target = swipe_target(dx, dy, self._custom)
        self._suppress_click = self._vertical_drag or self._custom or target != self._custom
        if ui_state.started:
          self._custom = target
        self._touch_start = None
        self._vertical_drag = False

  def _handle_mouse_release(self, pos):
    if not self._suppress_click and not self._custom:
      super()._handle_mouse_release(pos)

  def _render(self, rect):
    if not self._custom or not ui_state.started:
      return super()._render(rect)
    self._instrument.render(rect)
    # No stock HUD, camera, bookmark or status decoration on the custom face.
    # Critical takeover alerts are the sole exception and retain upstream rendering.
    alert, _ = self._alert_renderer.will_render()
    if alert is not None and alert.status == log.SelfdriveState.AlertStatus.critical:
      self._alert_renderer.render(rect)
