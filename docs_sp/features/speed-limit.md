---
title: Speed Limit Assist
---

# Speed Limit Assist

## What It Does

Speed Limit Assist detects the current speed limit using map data and can automatically adjust your cruise speed to match. It offers four operating modes ranging from passive information display to active speed management.

## How It Works

1. sunnypilot reads speed limit data from one or more configured sources (see below)
2. Based on your chosen mode, it displays, warns, or actively adjusts your set speed
3. When a speed limit change is detected, the system either applies it automatically or prompts you to confirm, depending on the confirmation mode
4. An optional offset (fixed or percentage) lets you cruise slightly above or below the limit

## Speed Limit Sources

Speed Limit Assist can pull speed limit data from multiple sources. You can configure which source takes priority via the **Speed Limit Policy** setting.

| Source | Description |
|--------|-------------|
| **OSM Map Data** | Speed limits from downloaded OpenStreetMap data. Requires [OSM Maps](osm-maps.md) to be configured and downloaded. |
| **Car's Stock Speed Limit Data** | Some vehicles provide speed limit information from their built-in sensors (e.g., Traffic Sign Recognition cameras). Availability depends on the vehicle. |
| **Navigation Data** | Speed limits embedded in navigation route data, when a navigation destination is active. |
| **Camera Vision** | Speed limit signs detected by the device's road-facing camera using the vision model. |

!!! tip "Source Priority"
    When multiple sources detect different speed limits, the **Speed Limit Policy** setting determines which source is used. Configure this under **Settings** → **sunnypilot** → **Cruise Control** → **Speed Limit Policy**.

## Confirmation Modes

When the detected speed limit changes, you can choose how the system responds:

| Mode | Behavior |
|------|----------|
| **Auto** | The cruise set speed adjusts automatically when a new speed limit is detected — no driver input required |
| **User Confirm** | The system displays the new speed limit and waits for the driver to confirm before adjusting the set speed |

## Driver Notifications

Speed Limit Assist provides visual indicators on the driving HUD:

- The currently detected speed limit is shown on the display
- When a speed limit change is detected, a notification appears showing the new limit
- In Warning and Assist modes, alerts notify you when you are exceeding the posted limit

## Requirements

!!! info "Requirements"
    - Longitudinal control must be available, **or** [ICBM](icbm.md) must be enabled
    - For map-based limits: [OSM Maps](osm-maps.md) must be configured and downloaded

## How to Enable

**Settings** → **sunnypilot** → **Cruise Control** → **Speed Limit Assist**

## Operating Modes

| Mode | Behavior |
|------|----------|
| **Off** | Speed limit data is not used |
| **Info** | Shows the current speed limit on the driving display |
| **Warning** | Shows the speed limit and alerts you when you're exceeding it |
| **Assist** | Automatically adjusts cruise speed to match the speed limit |

## Speed Offset

You can set an offset so your cruise speed differs from the exact limit:

- **Fixed offset:** Add or subtract a set number of km/h or mph (range: -30 to +30)
- **Percentage offset:** Apply a percentage above or below the limit

## Vehicle Restrictions

!!! warning "Vehicle Restrictions"
    - **Tesla:** Assist mode is disabled on release branches (Info and Warning still work)
    - **Rivian:** Assist mode is always disabled

## Settings Reference

See [Speed Limit Settings](../settings/speed-limit.md) for all configuration options.
