---
title: Prohibited Modifications
---

# Prohibited Modifications

Certain modifications to sunnypilot are prohibited for safety reasons.

!!! danger "Zero Tolerance Policy"
    All official sunnypilot branches strictly adhere to [comma.ai's safety policy](https://github.com/commaai/openpilot/blob/master/docs/SAFETY.md). Any changes against this policy will result in your fork and your device being **banned from both comma.ai and sunnypilot channels**.

## Panda Safety Violations

The following modifications to panda safety logic are strictly prohibited:

- **Preventing longitudinal disengagement on brake** — The system must disengage longitudinal control when the brake pedal is pressed. Overriding this behavior is prohibited.
- **Automatic re-engagement after braking** — Automatically re-engaging longitudinal control upon brake release without explicit driver input is prohibited.
- **Operating with cruise main off** — The system must disengage when cruise control main is in the off state. Bypassing this check is prohibited.
- **Removing steering torque limits** — Modifying or removing the safety-enforced steering torque limits is prohibited.
- **Bypassing vehicle safety interlocks** — Disabling or circumventing any vehicle-level safety interlock is prohibited.

## Driver Monitoring Violations

- **Reducing or weakening driver monitoring parameters** — Any modification that lowers the sensitivity, delays the response, or otherwise weakens the driver monitoring system is prohibited. This includes increasing allowed distraction time, reducing alert thresholds, or disabling monitoring entirely.

## General Prohibitions

- Disabling or bypassing driver monitoring
- Modifying braking safety thresholds
- Any modification that reduces the driver's ability to take manual control

## Why These Restrictions Exist

These restrictions protect you, your passengers, and other road users. Safety-critical systems have been carefully tuned and tested. Unauthorized modifications can have unpredictable and dangerous consequences.

!!! info "References"
    - [comma.ai Safety Policy](https://github.com/commaai/openpilot/blob/master/docs/SAFETY.md)
    - [Official sunnypilot Branches](../references/recommended-branches.md)
