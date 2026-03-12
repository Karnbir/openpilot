---
title: Toggles
---

# Toggles

Core openpilot toggles inherited from upstream. These control fundamental driving assist behavior.

## Available Toggles

| Toggle | Description |
|--------|-------------|
| Enable openpilot | Enable or disable the openpilot driving assist system |
| Experimental Mode | Use the neural network for longitudinal control on city streets (alpha quality) |
| Disengage on Accelerator Pedal | Disengage openpilot when the gas pedal is pressed |
| Enable Lane Departure Warnings | Receive alerts when the vehicle drifts out of the detected lane without a turn signal |
| Record and Upload Driver Camera | Upload driver-facing camera data for improved driver monitoring models |
| Use 24h Format for Clock | Display the onroad clock in 24-hour format |

!!! note
    These are upstream openpilot toggles. sunnypilot-specific toggles and customizations are found in the dedicated settings panels (Steering, Cruise, Visuals, etc.).
