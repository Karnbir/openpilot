---
title: Steering Settings
---

# Steering Settings

Configure lateral (steering) control behavior including MADS, lane changes, and torque settings.

**Location:** Settings → sunnypilot → Steering

---

## MADS (Modular Assistive Driving System)

| Property | Value |
|----------|-------|
| **Param** | `Mads` |
| **Type** | Toggle (On/Off) |
| **Default** | Off |

Enables the Modular Assistive Driving System, which decouples lateral (steering) control from longitudinal (speed) control. This means steering assistance can remain active even when cruise control is not engaged.

See the dedicated [MADS Settings](mads.md) page for sub-panel options.

---

## Blinker Pause Lateral Control

| Property | Value |
|----------|-------|
| **Param** | `BlinkerPauseLateralControl` |
| **Type** | Toggle (On/Off) |
| **Default** | Off |

When enabled, lateral (steering) control is temporarily paused while the turn signal is active. This gives you full manual steering control during turns without needing to disengage.

---

## Blinker Minimum Lateral Control Speed

| Property | Value |
|----------|-------|
| **Param** | `BlinkerMinLateralControlSpeed` |
| **Type** | Option selector |
| **Range** | 0–255 km/h (step: 5) |
| **Default** | 0 |

Sets the minimum speed (in your preferred unit) below which lateral control pauses when the blinker is active. At 0, lateral control pauses at all speeds when the blinker is on.

---

## Blinker Lateral Re-engage Delay

| Property | Value |
|----------|-------|
| **Param** | `BlinkerLateralReengageDelay` |
| **Type** | Option selector |
| **Range** | 0–10 seconds |
| **Default** | 0 |

Configures the delay (in seconds) before lateral control re-engages after the turn signal is turned off. Useful for completing a turn before steering assistance resumes.

---

## Enforce Torque Control

| Property | Value |
|----------|-------|
| **Param** | `EnforceTorqueControl` |
| **Type** | Toggle (On/Off) |
| **Default** | Off |

Forces torque-based lateral control on your vehicle, even if it natively uses angle-based control.

!!! info "Requirements"
    - Not available on vehicles with angle-based steering (`steerControlType == angle`)
    - Mutually exclusive with NNLC — enabling Torque Control disables NNLC
    - Device must be offroad to toggle

See the dedicated [Torque Settings](torque.md) page for advanced tuning.

---

## Neural Network Lateral Control (NNLC)

| Property | Value |
|----------|-------|
| **Param** | `NeuralNetworkLateralControl` |
| **Type** | Toggle (On/Off) |
| **Default** | Off |

Enables a neural network model to handle lateral control instead of the traditional PID/torque controller. NNLC can provide smoother steering in some situations.

!!! info "Requirements"
    - Not available on vehicles with angle-based steering (`steerControlType == angle`)
    - Mutually exclusive with Enforce Torque Control — enabling NNLC disables Torque Control
    - Device must be offroad to toggle

---

## Sub-Panels

The Steering section contains these additional sub-panels with their own settings:

- **[MADS Settings](mads.md)** — Configure MADS engagement modes and behavior
- **[Lane Change Settings](lane-change.md)** — Configure auto lane change timing and BSM integration
- **[Torque Settings](torque.md)** — Fine-tune torque lateral control parameters

---

## Related Features

- [Modular Assistive Driving System](../features/mads.md)
- [Neural Network Lateral Control](../features/nnlc.md)
- [Auto Lane Change](../features/auto-lane-change.md)
- [Torque Control](../features/torque-control.md)
