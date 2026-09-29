# Teal speedometer

Based on `commaai/openpilot:boooost` at `a535f04f592f9e74d07b43786ee9b615317851e7`
(PR #39015). The comma four (`mici`) stock on-road screen remains the default.
Swipe down at least 45 UI pixels to show the instrument; swipe up to return.
Horizontal gestures and taps cannot leave the custom face. The selection stays
until the opposite swipe (or UI process restart). The normal off-road transition
still works, and the selection is retained when driving resumes.

The custom face contains only the speed, units, arc and subdued octagonal mesh clipped inside each electrode.
There is no camera, path, stock HUD, bookmark icon or driver-monitoring overlay.
Critical takeover alerts temporarily overlay it through the upstream alert renderer.
Stock on-road rendering and gestures are unchanged when the instrument is hidden.

- Speed is `carState.vEgoCluster` in km/h, falling back to `vEgo` until a nonzero
  cluster speed has been seen in the current drive, matching upstream selection.
  This is vehicle telemetry, not predicted model velocity or cruise set speed.
  A stopped cluster correctly reads zero. Stale/invalid telemetry reads dashes.
- The arc uses `longitudinalPlan.aTarget`: desired acceleration, not measured
  acceleration or actuator output. It is active only with valid, live car/control/
  plan/selfdrive messages and active longitudinal control. Stock ACC and manual
  braking do not produce a requested-acceleration indication here.
- Teal fills bottom-left to top-right; soft red fills the reverse direction.
  Full scale is +2.0 or -3.5 m/s². These are display scales only. Each of the five
  segments eases in over 0.16 s and out over 0.24 s (exponential time constants).
  Inactive or stale control data clears the arc immediately.
- Custom beveled, slanted LCD digits, ghost electrodes and a layered Nixie halo need no
  added assets. Five broad, smoothly curved sections form a racing-inspired shoulder and horizontal
  top rail. The broad bottom sweep has a flat foot, with smooth boundaries and a straight diagonal tip.
  Shimmer varies only the outer halo by at most 2%; fills, mesh and digit edges
  remain steady for legibility.
  Background is RGB (0, 0, 0). No driving/control code is changed.

## Desktop preview

From a configured checkout:

```sh
python -m tools.speedometer_preview
python -m tools.speedometer_preview --screenshot speedometer.png
python -m tools.speedometer_preview --braking --screenshot braking.png
python -m unittest openpilot.selfdrive.ui.tests.test_speedometer
```

The preview runs the production Raylib renderer with explicitly simulated data;
it does not publish messages. It requires only the existing `comma-deps-raylib`
package. The full UI additionally requires the normal openpilot build/submodules.

Validation performed: desktop Raylib render, Python compilation, Ruff and isolated
telemetry/animation/swipe tests. Device touch interaction, full-process alert
integration, OLED appearance and device frame timing require comma four testing.

## Size and label timing

At the top of `speedometer_renderer.py`, `DIGIT_SCALE` controls one/two-digit
speeds and `THREE_DIGIT_SCALE` controls three-digit speeds. Increase to enlarge.
`LABEL_HOLD_SECONDS` is 5 and `LABEL_FADE_SECONDS` is 3: labels hold for five
seconds after opening the custom view, then smoothly fade to invisible over three
seconds. Swiping back into the custom view restarts the timer.
