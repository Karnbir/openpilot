---
title: OSM Maps Settings
---

# OSM Maps Settings

Manage OpenStreetMap (OSM) data used for speed limit information, curve detection, and other map-aware features.

**Location:** Settings → sunnypilot → OSM Maps

---

## Overview

The OSM Maps panel provides tools for downloading and managing offline map data. Unlike other settings panels, this section is primarily action-based rather than toggle-based.

---

## Country Selection

Select the country for which you want to download map data. This sets the regional map database used by sunnypilot for speed limit lookups and road information.

| Property | Value |
|----------|-------|
| **Param (state)** | `OsmLocationName`, `OsmLocationTitle` |
| **Type** | Selector |

---

## State Selection (US Only)

If you selected the United States as your country, you can further narrow the download to a specific state. This reduces download size and improves performance.

| Property | Value |
|----------|-------|
| **Param (state)** | `OsmStateName`, `OsmStateTitle` |
| **Type** | Selector |
| **Visibility** | Only shown when country is United States |

---

## Database Update

Check for and download updates to your selected region's OSM map data.

| Property | Value |
|----------|-------|
| **Param (state)** | `OsmDbUpdatesCheck` |
| **Type** | Action button |

---

## Delete Maps

Remove all downloaded map data from the device to free up storage space.

| Property | Value |
|----------|-------|
| **Type** | Action button |

---

## Status Information

The panel displays the following read-only information:

| Field | Param | Description |
|-------|-------|-------------|
| **Local Maps** | `OsmLocal` | Whether map data is stored locally |
| **Last Downloaded** | `OsmDownloadedDate` | When the map data was last downloaded |
| **Map Daemon Version** | `MapdVersion` | Version of the map processing daemon |

---

## Related Features

- [OSM Maps](../features/osm-maps.md)
- [Speed Limit Assist](../features/speed-limit.md)
- [Smart Cruise Control — Map](../features/scc-m.md)
