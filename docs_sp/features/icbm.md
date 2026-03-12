---
title: Intelligent Cruise Button Management
---

# Intelligent Cruise Button Management (ICBM)

## What It Does

ICBM allows sunnypilot to intercept and dynamically manage your vehicle's cruise control button presses. Instead of directly changing the set speed, button presses are routed through sunnypilot's logic, enabling features like Speed Limit Assist and Smart Cruise Control on vehicles that don't natively support sunnypilot longitudinal control.

This is particularly useful for vehicles where sunnypilot cannot directly control the gas and brakes — ICBM gives you many of the same benefits by intelligently managing the cruise buttons.

## When to Use

ICBM is designed specifically for vehicles where sunnypilot cannot directly control the throttle and brakes (i.e., no native longitudinal control). On these vehicles, the stock cruise control system still handles all actual acceleration and deceleration. ICBM bridges the gap by intelligently managing cruise button commands so you can still benefit from sunnypilot's speed planning features.

## How It Works

1. You press the cruise speed button on your steering wheel
2. ICBM intercepts the button press
3. sunnypilot applies its logic (speed limits, map curves, etc.) to determine the appropriate speed change
4. ICBM simulates the corresponding cruise button presses over the CAN bus, sending the adjusted command to the vehicle's stock cruise control system

This happens transparently — from your perspective, the buttons work normally but with smarter behavior. Under the hood, ICBM is communicating with the vehicle's cruise control module by simulating physical button presses on the CAN bus, which is why it works even on vehicles without direct throttle/brake control.

!!! tip "Safety"
    ICBM preserves all of your vehicle's stock safety systems. Forward Collision Avoidance (FCA), Automatic Emergency Braking (AEB), and other factory safety features remain fully active and unaffected, since the vehicle's own cruise control system is still performing the actual speed control.

## Requirements

!!! info "Requirements"
    - Your vehicle must support ICBM — not all vehicles are compatible
    - If the ICBM toggle does not appear in settings, your vehicle is not supported

## How to Enable

**Settings** → **sunnypilot** → **Cruise Control** → **Intelligent Cruise Button Management**

## Features Unlocked by ICBM

When ICBM is enabled, the following features become available even on vehicles without native longitudinal control:

- **[Smart Cruise Control — Vision](scc-v.md)** — Vision-based adaptive speed adjustments
- **[Smart Cruise Control — Map](scc-m.md)** — Map-aware speed adjustments
- **[Custom ACC Increments](custom-acc-increments.md)** — Custom button press speed steps
- **[Speed Limit Assist](speed-limit.md)** — Automatic speed limit matching

## Settings Reference

See [Cruise Control Settings](../settings/cruise.md) for all available options.
