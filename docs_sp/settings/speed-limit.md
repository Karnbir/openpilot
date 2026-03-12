---
title: Speed Limit Settings
---

# Speed Limit Settings

Configure how sunnypilot responds to detected speed limits from maps, signs, and navigation data.

**Location:** Settings → sunnypilot → Cruise Control → Speed Limit Assist

---

## Speed Limit Mode

| Property | Value |
|----------|-------|
| **Param** | `SpeedLimitMode` |
| **Type** | Multi-button selector |
| **Options** | Off · Info · Warning · Assist |
| **Default** | Off |

Controls how sunnypilot uses speed limit information:

| Mode | Behavior |
|------|----------|
| **Off** | Speed limit data is not used |
| **Info** | Displays the current speed limit on the HUD |
| **Warning** | Displays speed limit and alerts you when exceeding it |
| **Assist** | Automatically adjusts cruise speed to match the speed limit (with optional offset) |

!!! info "Requirements"
    - Longitudinal control must be available, **or** ICBM must be enabled

!!! warning "Vehicle Restrictions"
    - **Tesla:** Speed Limit Assist mode is disabled on release branches
    - **Rivian:** Speed Limit Assist mode is always disabled

---

## Speed Limit Offset Type

| Property | Value |
|----------|-------|
| **Param** | `SpeedLimitOffsetType` |
| **Type** | Multi-button selector |
| **Options** | None · Fixed · % |
| **Default** | None |

Choose how the speed offset is calculated:

| Type | Description |
|------|-------------|
| **None** | No offset — cruise matches exact speed limit |
| **Fixed** | A fixed value (in km/h or mph) is added to or subtracted from the limit |
| **%** | A percentage is applied to the speed limit |

---

## Speed Limit Value Offset

| Property | Value |
|----------|-------|
| **Param** | `SpeedLimitValueOffset` |
| **Type** | Option selector |
| **Range** | -30 to +30 |
| **Default** | 0 |

The offset value applied to the detected speed limit. Only active when **Offset Type** is set to Fixed or %.

- **Positive values:** Cruise faster than the limit (e.g., +5 means 5 over)
- **Negative values:** Cruise slower than the limit (e.g., -5 means 5 under)

---

## Speed Limit Policy

Speed Limit Policy is a sub-panel that controls the priority of speed limit data sources. See your device for available options.

---

## Related Features

- [Speed Limit Assist](../features/speed-limit.md)
- [OSM Maps](../features/osm-maps.md)
