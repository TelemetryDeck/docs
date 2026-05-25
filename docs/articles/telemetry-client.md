---
title: TelemetryClient (Legacy)
tags:
  - Swift
  - SDK
  - legacy
description: Legacy reference for the TelemetryClient/TelemetryManager API. Replaced by the TelemetryDeck API in SwiftSDK 2.x and removed in 3.0.
lead: This page documents the original TelemetryClient API, which was replaced by the TelemetryDeck static API. If you're still using these APIs, migrate to the current SDK.
---

!!! warning "Outdated"

    The APIs on this page (`TelemetryManager`, `TelemetryClient`, `TelemetryManagerConfiguration`) were removed in SwiftSDK 3.0. See the [Swift Setup Guide](/guides/swift-setup/) for current documentation or the [V3 Migration Guide](/guides/swift-migration-v3/) if upgrading.

## Historical context

The original Swift SDK (called "SwiftClient") used a `TelemetryManager` singleton with a `TelemetryManagerConfiguration` class. These were replaced by the `TelemetryDeck` static API in the [Grand Rename](/articles/grand-rename/) and formally removed in SwiftSDK 3.0.

## Quick migration reference

| Old API | Current API |
|---|---|
| `TelemetryManagerConfiguration(appID:)` | `TelemetryDeck.initialize(appID:namespace:)` |
| `TelemetryManager.initialize(config:)` | `TelemetryDeck.initialize(appID:namespace:)` |
| `TelemetryManager.send("event")` | `await TelemetryDeck.event("event")` |
| `TelemetryManager.send("event", for: user)` | `await TelemetryDeck.event("event", customUserID: user)` |
| `TelemetryManager.send("event", with: params)` | `await TelemetryDeck.event("event", parameters: params)` |
| `TelemetryManager.shared.hashedDefaultUser` | Not exposed directly; use `setUserIdentifier(_:)` |
| `configuration.telemetryAllowDebugBuilds = true` | `testMode: false` parameter in `initialize` |
| `import TelemetryClient` | `import TelemetryDeck` |
