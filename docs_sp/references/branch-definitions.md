---
title: Branch Definitions
---

# Branch Definitions

Understanding sunnypilot's branching strategy and device compatibility.

!!! tip "Calling All Testers"
    Testers, even without software development experience, are encouraged to run **staging** or **dev** branches and report issues. Your feedback is invaluable for improving sunnypilot before each release.

---

## Release Branches

### release-tizi (C3X)

- **Stability:** :material-check-circle: Highly stable
- **Target devices:** Comma 3X (TIZI)
- **Description:** The recommended branch for most Comma 3X users. This branch contains thoroughly tested features and fixes that have passed through staging and dev. Use this for daily driving.

### release-tici (C3)

- **Stability:** Not yet available
- **Target devices:** Comma Three (TICI)
- **Description:** A dedicated release branch for Comma Three is not yet available. C3 users should use `staging-tici` in the meantime.

---

## Pre-Release Branches

### staging (C4 / C3X)

- **Stability:** :material-alert-circle: Generally stable
- **Target devices:** Comma Four (MICI), Comma 3X (TIZI)
- **Description:** Pre-release testing branch. Features here are being validated before promotion to a release branch. Suitable for users who want early access to upcoming features and are willing to report issues.

### staging-tici (C3)

- **Stability:** :material-alert-circle: Generally stable
- **Target devices:** Comma Three (TICI)
- **Description:** Pre-release testing branch for Comma Three. Provides the most stable experience currently available for C3 devices.

---

## Development Branches

### dev (C4 / C3X)

- **Stability:** :material-close-circle: Least stable
- **Target devices:** Comma Four (MICI), Comma 3X (TIZI)
- **Description:** Active development branch with the latest features and fixes. Intended for testers and developers who want to try the newest changes and provide feedback. Expect occasional issues.

### master (C4 / C3X)

- **Stability:** :material-close-circle: Unstable
- **Target devices:** Comma Four (MICI), Comma 3X (TIZI)
- **Description:** The primary development branch where pull requests are merged. Not recommended for daily driving. Use this branch if you are contributing code to sunnypilot.

### master-dev (C4 / C3X)

- **Stability:** :material-close-circle: Unstable
- **Target devices:** Comma Four (MICI), Comma 3X (TIZI)
- **Description:** CI branch used to build prebuilt artifacts for the `dev` branch. Not intended for direct installation.

---

## Which Branch Should I Use?

| Use Case | Recommended Branch |
|----------|--------------------|
| Daily driving (C3X) | `release-tizi` |
| Daily driving (C3) | `staging-tici` |
| Early access to features (C4/C3X) | `staging` |
| Testing and feedback (C4/C3X) | `dev` |
| Contributing code | `master` |
