---
title: Preserve Local Changes
---

# Preserve Local File Changes on Your comma Device

## Overview

By default, the comma device automatically updates sunnypilot, which overwrites any local file modifications you have made. To keep your local changes across reboots, you must disable automatic updates **before** making modifications.

!!! warning "Complete These Steps First"
    Local modifications applied **before** completing the steps below will **not** be retained. The automatic update process will overwrite them on the next reboot. Complete all steps first, then make your changes.

## Steps

### 1. Enable Advanced Controls

Navigate to **Settings** → **Developer** → **Show Advanced Controls** and toggle it **ON**.

This reveals additional settings options that are hidden by default, including the update toggle.

### 2. Disable Updates

Navigate to **Settings** → **Software** → **Disable Updates** and toggle it **ON**.

This prevents the device from automatically pulling and applying updates from the remote branch.

### 3. Reboot the Device

Navigate to **Settings** → **Device** → **Reboot** to restart the device.

The reboot applies the settings change and ensures the update service is fully stopped.

### 4. Verify

After the device restarts:

1. Confirm that your settings from steps 1 and 2 are still active
2. Make your desired local file changes (via SSH or other methods)
3. Reboot again to confirm your changes persist

!!! info "Automatic Updates Are Paused"
    With updates disabled, your device will **not** receive new sunnypilot releases automatically. You will need to re-enable updates manually when you want to update to a newer version. To re-enable, reverse step 2: **Settings** → **Software** → **Disable Updates** → **OFF**.

!!! tip "When to Use This"
    This is useful for testing custom parameter values, experimental configurations, or developer modifications that you want to persist across device reboots without being overwritten by the update system.
