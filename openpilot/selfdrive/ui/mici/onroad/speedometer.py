"""Comma four on-road instrument, retaining upstream alerts and navigation."""
import pyray as rl
from openpilot.selfdrive.ui.ui_state import ui_state
from openpilot.selfdrive.ui.mici.onroad.speedometer_renderer import draw_speedometer
from openpilot.selfdrive.ui.mici.onroad.speedometer_state import SpeedometerState
from openpilot.system.ui.lib.application import gui_app, FontWeight
from openpilot.system.ui.widgets import Widget


class SpeedometerView(Widget):
  def __init__(self):
    super().__init__()
    self._state = SpeedometerState()
    self._started = False

  def _update_state(self):
    if ui_state.started != self._started:
      self._state = SpeedometerState()
      self._started = ui_state.started
    sm = ui_state.sm

    def fresh(service):
      return bool(ui_state.started and sm.valid[service] and sm.alive[service] and
                  sm.recv_frame[service] >= ui_state.started_frame)

    cs, cc = sm['carState'], sm['carControl']
    active = fresh('carControl') and fresh('longitudinalPlan') and fresh('selfdriveState') and cc.longActive and ui_state.engaged
    self._state.update(cs.vEgo, cs.vEgoCluster, sm['longitudinalPlan'].aTarget,
                       speed_valid=fresh('carState'), control_active=active and fresh('carState'), dt=rl.get_frame_time())

  def _render(self, rect):
    draw_speedometer(rect, self._state, rl.get_time(), gui_app.font(FontWeight.MEDIUM))
    if not ui_state.started:
      rl.draw_rectangle_rec(rect, rl.BLACK)
      rl.draw_text_ex(gui_app.font(FontWeight.MEDIUM), 'start the car to use openpilot',
                      rl.Vector2(rect.x + 32, rect.y + rect.height / 2 - 12), 24, 0, rl.WHITE)
      return
