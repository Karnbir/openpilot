---
title: Auto Lane Change
---

# Auto Lane Change

## What It Does

Automatically executes lane changes when you activate the turn signal. You can choose between nudge-based confirmation, nudgeless (immediate), or timed delays before the lane change begins.

## How It Works

1. Activate your turn signal in the desired direction
2. The system verifies that clear lane markings are detected by the vision system in the target lane — a lane change will not execute without visible lane lines
3. The driver monitoring system checks that the driver is attentive before proceeding
4. Depending on your setting:
    - **Nudge:** Give a light steering nudge to confirm the lane change
    - **Nudgeless:** The lane change begins immediately
    - **Timed (0.5s–3s):** The lane change begins after the configured delay
5. If BSM Delay is enabled and a vehicle is detected in your blind spot, the lane change waits until the path is clear

## Requirements

!!! info "Requirements"
    - Lateral control must be active (sunnypilot must be engaged)
    - Vehicle must be traveling above a minimum speed threshold
    - Clear lane markings must be visible to the vision system
    - Driver must be attentive (monitored by the driver monitoring system)

## How to Enable

**Settings** → **sunnypilot** → **Steering** → **Lane Change Settings**

## Modes

| Mode | Behavior |
|------|----------|
| **Off** | Auto lane change is disabled |
| **Nudge** | Requires a light steering nudge to confirm |
| **Nudgeless** | Lane change begins as soon as you signal |
| **0.5s – 3s** | Lane change begins after a set delay |

## Blind Spot Monitoring Integration

If your vehicle supports BSM and the BSM Delay option is enabled, the system checks for vehicles in your blind spot before executing the lane change. The lane change is delayed until the adjacent lane is clear.

!!! info "BSM Requirements"
    - Vehicle must support Blind Spot Monitoring
    - Auto Lane Change Timer must be set beyond Nudge mode

## Settings Reference

See [Lane Change Settings](../settings/lane-change.md) for all options.

!!! warning "Safety"
    Always check your mirrors and blind spots before initiating a lane change. The system assists but does not replace driver awareness.
