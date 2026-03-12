---
title: Tesla Settings
---

# Tesla Vehicle Settings

Settings specific to Tesla vehicles. These settings only appear when a Tesla vehicle is connected.

**Location:** Settings → sunnypilot → Vehicle

---

## Cooperative Steering (Beta)

| Property | Value |
|----------|-------|
| **Param** | `TeslaCoopSteering` |
| **Type** | Toggle (On/Off) |
| **Default** | Off |

Allows the driver to provide limited steering input while sunnypilot is engaged. Without this feature, the driver must fully override or disengage to steer manually.

!!! warning "Important"
    **May experience steering oscillations below 48 km/h (30 mph) during turns.** Recommend disabling this feature if you experience oscillations.

- Only works above **23 km/h** (14 mph)
- Speed thresholds are displayed in your preferred unit (km/h or mph)

!!! info "Requirements"
    - Device must be offroad to toggle
    - Use "Always Offroad" in [Device Settings](../device.md) if you need to change this while the vehicle is running

---

## MADS Limitations

Tesla vehicles **without a vehicle bus connection** operate in limited MADS mode:

| Setting | Forced Value |
|---------|-------------|
| Main Cruise Allowed | Off (locked) |
| Unified Engagement Mode | On (locked) |
| Steering Mode on Disengage | Disengage (locked) |

See [MADS Settings](../mads.md) for details on these settings.

---

## Speed Limit Assist Restrictions

On **release branches**, Speed Limit Assist mode is disabled for Tesla vehicles. Info and Warning modes remain available.

See [Speed Limit Settings](../speed-limit.md) for details.
