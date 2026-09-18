---
title: Writing Custom Processors
tags:
  - Swift
  - SDK
  - processors
  - advanced
testedOn: SwiftSDK 3.0.0
description: Build your own EventProcessor to enrich, filter, or transform events in the TelemetryDeck Swift SDK pipeline.
lead: Add domain-specific metadata to every event by writing your own processor and plugging it into the pipeline.
---

## The EventProcessor protocol

A processor is any `Sendable` type that conforms to `EventProcessor`:

```swift
public protocol EventProcessor: Sendable {
    func process(
        _ input: EventInput,
        context: EventContext,
        next: @Sendable (EventInput, EventContext) async throws -> Event
    ) async throws -> Event

    func start(
        storage: any ProcessorStorage,
        logger: any Logging,
        emitter: any EventSending
    ) async

    func stop() async
}
```

Only `process` is required. The `start` and `stop` methods have default no-op implementations.

## A minimal processor

Here's a processor that adds the current A/B test variant to every event:

```swift
struct ABTestProcessor: EventProcessor {
    let variant: String

    func process(
        _ input: EventInput,
        context: EventContext,
        next: @Sendable (EventInput, EventContext) async throws -> Event
    ) async throws -> Event {
        var ctx = context
        ctx.addParameter("ABTest.variant", value: variant)
        return try await next(input, ctx)
    }
}
```

Key points:

- Mutate `context` to add metadata parameters. These are merged with the event at finalization.
- Mutate `input` to change the event name, parameters, or float value.
- Always call `next(input, context)` to pass the event down the pipeline — unless you want to drop it.
- Input parameters override context parameters when keys collide.

## Registering your processor

Pass your processors when initializing TelemetryDeck. Use `defaultProcessors()` to keep the built-in ones:

```swift
try await TelemetryDeck.initialize(
    configuration: TelemetryDeck.Config(
        appID: "YOUR-APP-ID",
        namespace: "YOUR-NAMESPACE"
    ),
    processors: TelemetryDeck.defaultProcessors() + [
        ABTestProcessor(variant: "B")
    ]
)
```

Your processor runs after all default processors. To insert it at a specific position, build the array manually:

```swift
var processors = TelemetryDeck.defaultProcessors()
processors.insert(ABTestProcessor(variant: "B"), at: 0)

try await TelemetryDeck.initialize(
    configuration: config,
    processors: processors
)
```

## Filtering events

Drop events by throwing `ProcessorError.eventFiltered`:

```swift
struct InternalScreenFilter: EventProcessor {
    func process(
        _ input: EventInput,
        context: EventContext,
        next: @Sendable (EventInput, EventContext) async throws -> Event
    ) async throws -> Event {
        if input.name.hasPrefix("Internal.") {
            throw ProcessorError.eventFiltered
        }
        return try await next(input, context)
    }
}
```

Filtered events are silently discarded.

## Transforming events

Modify the event name or parameters before passing them on:

```swift
struct ScreenNameSanitizer: EventProcessor {
    func process(
        _ input: EventInput,
        context: EventContext,
        next: @Sendable (EventInput, EventContext) async throws -> Event
    ) async throws -> Event {
        var modified = input
        modified.name = modified.name
            .replacingOccurrences(of: " ", with: ".")
        return try await next(modified, context)
    }
}
```

## Using persistent storage

Processors that need to persist state across app launches get access to `ProcessorStorage` in their `start` method:

```swift
actor SubscriptionTierProcessor: EventProcessor {
    private var storage: (any ProcessorStorage)?
    private var tier: String = "free"

    func start(
        storage: any ProcessorStorage,
        logger: any Logging,
        emitter: any EventSending
    ) async {
        self.storage = storage
        if let saved = await storage.string(forKey: "subscriptionTier") {
            tier = saved
        }
    }

    func updateTier(_ newTier: String) async {
        tier = newTier
        await storage?.set(newTier, forKey: "subscriptionTier")
    }

    func process(
        _ input: EventInput,
        context: EventContext,
        next: @Sendable (EventInput, EventContext) async throws -> Event
    ) async throws -> Event {
        var ctx = context
        ctx.addParameter("Subscription.tier", value: tier)
        return try await next(input, ctx)
    }
}
```

`ProcessorStorage` supports `Data`, `String`, `Int`, and `Bool` types. The default implementation backs onto `UserDefaults` with a suite scoped to your app ID.

## Emitting events from a processor

The `emitter` parameter in `start` lets a processor send its own events back into the pipeline — for example, system-level events the processor generates independently:

```swift
actor WatchdogProcessor: EventProcessor {
    private var emitter: (any EventSending)?

    func start(
        storage: any ProcessorStorage,
        logger: any Logging,
        emitter: any EventSending
    ) async {
        self.emitter = emitter
    }

    func reportAnomaly(_ description: String) async {
        await emitter?.send(EventInput(
            name: "Watchdog.anomalyDetected",
            parameters: ["description": description]
        ))
    }

    func process(
        _ input: EventInput,
        context: EventContext,
        next: @Sendable (EventInput, EventContext) async throws -> Event
    ) async throws -> Event {
        return try await next(input, context)
    }
}
```

Events sent via `emitter` go through the entire pipeline, including your processor.

## Replacing built-in processors

If a built-in processor doesn't fit your needs, leave it out of the pipeline and supply your own. For example, to replace the session tracking logic:

```swift
try await TelemetryDeck.initialize(
    configuration: config,
    processors: TelemetryDeck.defaultProcessors()
        .filter { $0 is SessionTrackingProcessor == false }
        + [MyCustomSessionProcessor()]
)
```

!!! warning

    If you remove built-in processors, features that depend on them (like retention metrics or test mode detection) will stop working. Only do this when you have a specific reason.

## Testing with SpyEventTransmitter

The SDK provides `SpyEventTransmitter` and `InMemoryEventCache` for testing. Inject them to capture events without hitting the network:

```swift
let spy = SpyEventTransmitter()

try await TelemetryDeck.initialize(
    configuration: config,
    processors: [MyProcessor()],
    cache: InMemoryEventCache(),
    transmitter: spy
)

await TelemetryDeck.event("test.event")
await TelemetryDeck.flush()

let transmitted = await spy.transmittedEvents
assert(transmitted.contains { $0.type == "test.event" })
```
