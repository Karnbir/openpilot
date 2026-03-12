---
title: Reporting a Bug
---

# Reporting a Bug

Help us improve sunnypilot by reporting issues you encounter.

## Before Reporting

!!! warning "Remove Customizations First"
    If you have any custom modifications (forks, patches, config tweaks), **remove them and reproduce the issue on an official sunnypilot branch** before reporting. This rules out your modifications as the cause and helps maintainers focus on real bugs.

1. **Upgrade** to the latest version — the bug may already be fixed
2. **Remove customizations** — reproduce on a stock official branch
3. **Search** [GitHub Issues](https://github.com/sunnypilot/sunnypilot/issues) and the [Discord Community](https://discord.sunnypilot.ai) for known reports
4. **Preserve the route** — upload raw logs via [Comma Connect](https://connect.comma.ai) and keep the route available

## What to Include

### Required Information

- **Dongle ID** — Your comma Dongle ID (found in **Settings** → **Device** or in Comma Connect)
- **Route ID** — The route ID from Comma Connect for the drive where the issue occurred
- **Device info** — Hardware model (C3, C3X, C4), software version, branch
- **Vehicle info** — Make, model, year

### Bug Report Template

Use the following structure when filing your report:

!!! example "Bug Report Format"

    **Title:** One-sentence summary of the issue

    **Description:** 1-2 sentences providing additional context about the problem.

    **Steps to Reproduce:**

    1. Step one
    2. Step two
    3. Step three

    **Expected behavior:** What should have happened

    **Actual behavior:** What actually happened

    **Related Links:** Route link, log files, screenshots, or references to related issues

## Pre-Submission Checklist

Before submitting, confirm the following:

- [ ] I am running the latest version of sunnypilot
- [ ] I have removed all custom modifications and reproduced the issue on an official branch
- [ ] I have searched existing issues and community channels for duplicates
- [ ] I have preserved the route and uploaded raw logs via Comma Connect
- [ ] I have included my comma Dongle ID
- [ ] I have included the Route ID for the affected drive

## How to Report

1. Go to [GitHub Issues](https://github.com/sunnypilot/sunnypilot/issues/new)
2. Use the bug report template
3. Fill in all requested information using the format above
4. Submit the issue

!!! tip
    The more detail you provide, the faster we can diagnose and fix the issue. Incomplete reports without Dongle IDs or route information may be closed.
