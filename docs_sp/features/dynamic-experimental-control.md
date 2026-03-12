---
title: Dynamic Experimental Control
---

# Dynamic Experimental Control (DEC)

## What It Does

DEC automatically switches between openpilot's standard and experimental driving modes based on real-time road conditions. Instead of manually toggling between modes, the system chooses the most appropriate mode for the current situation.

To understand DEC, it helps to know the three driving modes in the system:

| Mode | Description |
|------|-------------|
| **Chill Mode** (Standard) | The default openpilot driving mode. Follows the lead car and stays in lane at a steady speed. Best suited for highway and open-road driving where stops and complex maneuvers are rare. |
| **Experimental Mode** | An enhanced mode that can handle stops at traffic lights and stop signs, navigate turns, and respond to more complex urban scenarios. Designed for city driving. |
| **DEC** | Not a driving mode itself, but a dynamic switcher that automatically selects between Chill and Experimental modes in real time based on road conditions. |

## How It Works

DEC monitors multiple driving signals and conditions to decide which mode is most appropriate at any given moment:

- **Current speed** — Lower speeds suggest city driving, favoring Experimental Mode
- **Turn detection** — Upcoming turns trigger a switch to Experimental Mode for better handling
- **Stop signs and traffic lights** — Intersections benefit from Experimental Mode's ability to stop and respond to signals
- **Road type** — Highway vs. urban driving informs the mode selection

Based on these signals, DEC switches between:

| Mode | When DEC Activates It |
|------|----------|
| **Chill Mode** | Highway driving with steady speeds, clear lanes, and no upcoming stops or complex intersections |
| **Experimental Mode** | City driving with stops, turns, traffic lights, and complex intersections where the vehicle needs to slow down or stop |

The switching happens seamlessly — DEC continuously evaluates conditions and transitions between modes without requiring any driver input.

## Requirements

!!! info "Requirements"
    - Longitudinal control must be available
    - Device must be offroad to enable/disable

## How to Enable

**Settings** → **sunnypilot** → **Cruise Control** → **Dynamic Experimental Control**

## Settings Reference

See [Cruise Control Settings](../settings/cruise.md) for configuration details.
