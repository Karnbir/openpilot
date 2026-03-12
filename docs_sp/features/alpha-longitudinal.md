---
title: Alpha Longitudinal
---

# Alpha Longitudinal

## What It Does

Alpha Longitudinal provides experimental longitudinal (speed and acceleration) control for vehicles that are openpilot-compatible but do not have official sunnypilot longitudinal support. This enables throttle and brake control on cars that would otherwise be limited to lateral (steering) assistance only.

For officially supported vehicles, sunnypilot provides refined longitudinal tuning tailored to each platform. Alpha Longitudinal extends this capability to additional vehicles using a more generalized approach, allowing drivers of these cars to experience full ACC-like functionality through sunnypilot.

## How It Works

Alpha Longitudinal uses the vehicle's existing communication interfaces to send throttle and brake commands, bypassing the need for the vehicle's stock cruise control system. The system:

- Reads vehicle speed, pedal position, and other sensor data through the car's CAN bus
- Calculates desired acceleration based on the driving model's output
- Sends throttle and brake commands directly to the vehicle's powertrain controllers

Because this operates outside the vehicle manufacturer's intended cruise control pathway, the tuning is less refined than on officially supported platforms.

## Requirements

!!! info "Requirements"
    - Vehicle must be openpilot-compatible (listed on the [comma.ai vehicle compatibility list](https://comma.ai/vehicles))
    - Vehicle does not have official sunnypilot longitudinal support
    - Feature is experimental and under active development

!!! warning "Alpha Quality Software"
    This feature is **alpha quality**. Expect rough edges, less smooth acceleration and braking behavior, and less refined stop-and-go performance compared to officially supported vehicles. Longitudinal behavior may vary significantly between vehicle models and driving conditions.

## How to Enable

**Settings** → **sunnypilot** → **Cruise Control** → **Alpha Longitudinal**

## Settings Reference

See [Cruise Control Settings](../settings/cruise.md) for configuration details.
