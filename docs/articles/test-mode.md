---
title: Test Mode
tags:
  - setup
  - testmode
  - quickstart
  - beginner
testedOn: SwiftSDK 3.0.0
description: Use Test Mode to verify your TelemetryDeck setup without polluting production data.
lead: Test Mode keeps your development and testing signals separate from real user data.
searchEngineTitle: How to run test signals
searchEngineDescription: With test mode, you can review your analytics setup without compromising live data.
---

During development and testing, your app sends events that aren't from real users. Test Mode keeps these separate from production analytics.

Benefits of sending test signals:

- Verify your TelemetryDeck SDK configuration before release
- Confirm new event types and parameters work as expected
- Set up insights and dashboards ahead of launch

## How it works

Every event has an `isTestMode` flag. The TelemetryDeck Dashboard has a Test Mode toggle in the upper left — flip it to switch between test and production data. A banner reminds you when you're viewing test data.

![Screenshot of the dashboard showing the Test Mode toggle in the upper left corner.](/assets/test_mode.png)

## Automatic detection

The SDKs detect test mode automatically. In the Swift SDK, events sent from `DEBUG` builds are marked as test signals by default.

## Manual override

### Swift SDK

Override test mode at initialization:

```swift
try await TelemetryDeck.initialize(
    appID: "YOUR-APP-ID",
    namespace: "YOUR-NAMESPACE",
    testMode: true
)
```

Check the current test mode state at runtime:

```swift
let isTest = await TelemetryDeck.isTestMode()
```

### JavaScript SDK

```javascript
const td = new TelemetryDeck({
    app: "YOUR-APP-ID",
    user: "anonymous",
    testMode: true
});
```

Or set it per-signal:

```javascript
td.signal("eventName", { isTestMode: "true" });
```
