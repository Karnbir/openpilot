---
title: How to Share a Route
---

# How to Share a Route

## Overview

Sharing driving routes is essential for debugging issues, getting support, and helping developers improve sunnypilot. Routes are shared through [comma Connect](https://connect.comma.ai), comma's web-based route management tool.

## Step 1: Prepare the Route

Before sharing, ensure the route data is fully uploaded and preserved.

### Upload Raw Logs

1. Go to [connect.comma.ai](https://connect.comma.ai)
2. Select the route you want to share
3. Open the **Files** tab
4. Upload the raw logs for the route

!!! warning "Upload Before Sharing"
    Raw logs must be **fully uploaded** before they can be reviewed by others. If the logs are not uploaded, reviewers will not have access to the detailed data needed for debugging.

### Preserve the Route

Routes are automatically deleted after a retention period. To prevent this:

1. Select the route in comma Connect
2. Click **More info**
3. Toggle **Preserved** to **ON**

This ensures the route remains available for as long as you need it.

## Step 2: Choose Sharing Method

### Option A: Public Route (Recommended)

The simplest way to share a single route for support or debugging.

1. Select the route in comma Connect
2. Toggle **Public access** to **ON**
3. Copy the **Route ID** from the route details
4. Share the Route ID in the support channel or forum thread

!!! info "Privacy"
    Making a route public means **anyone with the Route ID can access it**. Route data includes GPS coordinates and video footage. For privacy, start and end your recorded drives at public places such as parking lots or gas stations. Avoid starting or ending at your home, workplace, or other private locations.

### Option B: Device Sharing

Grants another user access to **all routes** on your device. Use this when ongoing collaboration is needed.

1. Rename your device with your vehicle's **Year/Make/Model** and your **username** (e.g., "2023 Hyundai Ioniq 6 - jasonwen")
2. Go to device settings in comma Connect
3. Share the device via the other user's email address

!!! tip "When to Use Device Sharing"
    Device sharing is best for long-term collaboration with a developer or when multiple routes need to be reviewed. For one-off support requests, prefer Option A (Public Route) to limit access to only the relevant route.
