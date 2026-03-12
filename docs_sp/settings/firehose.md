---
title: Firehose
---

# Firehose

Firehose Mode allows your device to upload the maximum amount of training data to comma's servers, helping improve openpilot's autonomous driving models.

!!! info "First Fork with Official Support"
    sunnypilot is the first and currently only major fork to receive official Firehose Mode support, after comma.ai merged it into their backend infrastructure.

## How It Works

When Firehose Mode is enabled, the system randomly samples a portion of your drives rather than uploading everything. It queues approximately 10 segments at a time for transmission, whether openpilot is actively engaged or not. Both engaged and disengaged driving data contributes to simulator training.

No special driving behavior is needed. Normal driving patterns work fine.

## Requirements

- **Compatible branch**: You must be running one of the following branches:
    - `staging`, `dev`, or `master`
    - `staging-tici`, `master-tici`
    - `release-tizi` or `release-tici`
- **Weekly connectivity**: Connect to Wi-Fi with a reliable USB-C power adapter at minimum once per week.
- **Supported vehicle**: Only vehicles officially supported in [upstream openpilot](https://github.com/commaai/opendbc/blob/master/docs/CARS.md) qualify for model training data collection.

## Optional: Mobile Upload

Devices with hotspot access or unlimited data plans can upload data while driving, removing the need for weekly Wi-Fi sessions.

## Learn More

For the latest information, see the [Firehose Mode announcement](https://community.sunnypilot.ai/t/firehose-mode-now-supported-on-sunnypilot/385) on the sunnypilot community forum.
