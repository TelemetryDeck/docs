---
title: Migrating from SwiftSDK 2.x to 3.0
tags:
  - Swift
  - SDK
  - migration
testedOn: SwiftSDK 3.0.0
description: What changed in TelemetryDeck SwiftSDK 3.0 and how to update your code.
lead: SwiftSDK 3.0 replaces providers with processors, requires a namespace, and makes the API async. Here's how to migrate.
order: 200
---

## Platform requirements

SwiftSDK 3.0 raises minimum deployment targets:

| Platform | V2 | V3 |
|---|---|---|
| iOS | 12 | 15 |
| macOS | 10.13 | 12 |
| watchOS | 5 | 8 |
| tvOS | 13 | 15 |
| visionOS | 1 | 1 |

Swift 6.2 and Xcode 26 are required.

## Breaking changes

### Namespace is required

`TelemetryDeck.Config` now requires a `namespace` parameter. You'll find your namespace in the TelemetryDeck Dashboard alongside your app ID.

=== "Before (V2)"

    ```swift
    let config = TelemetryDeck.Config(appID: "YOUR-APP-ID")
    TelemetryDeck.initialize(config: config)
    ```

=== "After (V3)"

    ```swift
    try await TelemetryDeck.initialize(
        appID: "YOUR-APP-ID",
        namespace: "YOUR-NAMESPACE"
    )
    ```

### Initialization is async

`initialize` is now `async throws`. Wrap it in a `Task` when calling from synchronous contexts like `init()`:

```swift
init() {
    Task {
        try? await TelemetryDeck.initialize(
            appID: "YOUR-APP-ID",
            namespace: "YOUR-NAMESPACE"
        )
    }
}
```

Events sent before initialization completes are buffered and delivered automatically.

### signal() → event()

The `signal` function is deprecated. Replace it with `event`:

=== "Before (V2)"

    ```swift
    TelemetryDeck.signal("buttonTapped")
    TelemetryDeck.signal("purchase", parameters: ["item": "widget"])
    ```

=== "After (V3)"

    ```swift
    await TelemetryDeck.event("buttonTapped")
    await TelemetryDeck.event("purchase", parameters: ["item": "widget"])
    ```

### Event methods are async

All event-sending methods now require `await`:

```swift
await TelemetryDeck.event("myEvent")
await TelemetryDeck.navigationPathChanged(from: "home", to: "settings")
await TelemetryDeck.errorOccurred(id: "ParseError")
await TelemetryDeck.purchaseCompleted(transaction: transaction)
await TelemetryDeck.setUserIdentifier("user@example.com")
```

In SwiftUI view bodies and `@MainActor` contexts, wrap calls in a `Task`:

```swift
Button("Tap") {
    Task {
        await TelemetryDeck.event("buttonTapped")
    }
}
```

### Configuration properties moved to initialize parameters

Properties that were set on `TelemetryDeck.Config` in V2 are now parameters of the `initialize` function:

=== "Before (V2)"

    ```swift
    let config = TelemetryDeck.Config(appID: "YOUR-APP-ID")
    config.defaultSignalPrefix = "App."
    config.defaultParameterPrefix = "MyApp."
    config.defaultParameters = {["theme": "dark"]}
    TelemetryDeck.initialize(config: config)
    ```

=== "After (V3)"

    ```swift
    try await TelemetryDeck.initialize(
        appID: "YOUR-APP-ID",
        namespace: "YOUR-NAMESPACE",
        eventPrefix: "App.",
        parameterPrefix: "MyApp.",
        defaultParameters: ["theme": "dark"]
    )
    ```

### Typed parameters

Parameters are no longer `[String: String]`. The new `EventParameters` type accepts `String`, `Bool`, `Int`, `Double`, `UUID`, and `Date` values:

=== "Before (V2)"

    ```swift
    TelemetryDeck.signal("event", parameters: [
        "count": "\(items.count)",
        "premium": isPremium ? "true" : "false"
    ])
    ```

=== "After (V3)"

    ```swift
    await TelemetryDeck.event("event", parameters: [
        "count": items.count,
        "premium": isPremium
    ])
    ```

The old `[String: String]` overloads still compile but are deprecated.

### Duration methods renamed

=== "Before (V2)"

    ```swift
    TelemetryDeck.startDurationSignal("loading")
    TelemetryDeck.stopAndSendDurationSignal("loading")
    TelemetryDeck.cancelDurationSignal("loading")
    ```

=== "After (V3)"

    ```swift
    await TelemetryDeck.startDurationEvent("loading")
    await TelemetryDeck.stopAndSendDurationEvent("loading")
    await TelemetryDeck.cancelDurationEvent("loading")
    ```

### updateDefaultUserID → setUserIdentifier

=== "Before (V2)"

    ```swift
    TelemetryDeck.updateDefaultUserID(to: "user@example.com")
    ```

=== "After (V3)"

    ```swift
    await TelemetryDeck.setUserIdentifier("user@example.com")
    ```

## Removed APIs

| Removed | Replacement |
|---|---|
| `TelemetryManager.shared` | Use static methods on `TelemetryDeck` |
| `TelemetryClient` (typealias) | `TelemetryDeck` |
| `TelemetryManagerConfiguration` | `TelemetryDeck.Config` or `initialize(appID:namespace:...)` |
| `Provider` protocol | `EventProcessor` protocol |
| `configuration.telemetryAllowDebugBuilds` | `testMode` parameter in `initialize` |

## Providers → Processors

The V2 provider system (`register`, `stop`, `enrich`, `transform`) is replaced by the `EventProcessor` protocol. The new model is a middleware chain where each processor calls `next` to pass control downstream.

If you wrote custom providers, see [Writing Custom Processors](/articles/swift-custom-processors/) for the new approach.

## Data migration

The SDK includes an automatic `V2DataMigrator` that converts V2 session data (stored in UserDefaults) to the V3 format on first launch. No action needed — your users' session continuity and retention metrics are preserved.

## Payload format

Event payloads are now typed JSON. Values are sent as native `bool`, `int`, `double`, or `string`. V2 sent everything as strings. If you have server-side code parsing payloads, update it to handle typed values.
