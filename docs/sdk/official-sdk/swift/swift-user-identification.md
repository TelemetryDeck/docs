---
title: User Identification
tags:
  - Swift
  - SDK
  - advanced
testedOn: SwiftSDK 3.0.0
description: How the TelemetryDeck Swift SDK resolves, hashes, and transmits user identifiers across Apple platforms and Linux.
lead: The SDK assigns each user a stable, anonymous identifier. Here's how it resolves that identifier on each platform, how you can override it, and how it's hashed before transmission.
---

## Resolution order

When an event is processed, the SDK picks the user identifier from the first available source:

1. **Per-event override** — the `customUserID` parameter on `TelemetryDeck.event(...)`
2. **Explicit identifier** — set at runtime via `TelemetryDeck.setUserIdentifier(_:)`
3. **Default identifier** — from the `defaultUser` initialization parameter, or auto-resolved from the platform

If you never call `setUserIdentifier` and don't pass `defaultUser` at init, the SDK resolves a default automatically.

## Platform defaults

| Platform | Source |
|---|---|
| iOS, tvOS, visionOS | [`UIDevice.identifierForVendor`](https://developer.apple.com/documentation/uikit/uidevice/identifierforvendor) |
| watchOS | `WKInterfaceDevice.identifierForVendor` |
| macOS | Random UUID, generated once and persisted in `UserDefaults` |
| Linux / server | Static string derived from platform and app version |

### identifierForVendor (iOS, tvOS, visionOS, watchOS)

On Apple's mobile and wearable platforms, the SDK uses `identifierForVendor` (IDFV). This is a UUID assigned by the OS that:

- Stays stable across launches and app updates
- Is shared across all apps from the same vendor on a given device
- Resets when the user uninstalls **all** of that vendor's apps from the device
- Differs between TestFlight and the App Store, even for the same build — a tester's IDFV in TestFlight will not match their IDFV after installing from the App Store

See Apple's [identifierForVendor documentation](https://developer.apple.com/documentation/uikit/uidevice/identifierforvendor) for the full lifecycle rules, including edge cases around app groups and enterprise distribution.

If `identifierForVendor` returns `nil` — which can happen before the device is first unlocked after a restart — the SDK falls back to a generic string based on platform and app version. Different users on the same app version temporarily share this identifier until IDFV becomes available. The identifier is resolved once at startup with no retry.

### macOS

macOS has no `identifierForVendor`. On first launch, the SDK generates a random UUID and stores it in a `UserDefaults` suite scoped to your app ID. Subsequent launches read the same UUID. Deleting the app's UserDefaults data resets the identifier.

### Linux and server-side Swift

The SDK returns a static string derived from the platform name and app version. Every user on the same deployment gets the same identifier. For server-side use, pass an explicit user identifier:

```swift
await TelemetryDeck.event("API.requestHandled", customUserID: request.authenticatedUserID)
```

## Setting a user identifier

Override the default at any point after initialization:

```swift
await TelemetryDeck.setUserIdentifier("user@example.com")
```

Pass `nil` to revert to the platform default:

```swift
await TelemetryDeck.setUserIdentifier(nil)
```

For a single event:

```swift
await TelemetryDeck.event("checkout.completed", customUserID: order.userID)
```

## Hashing

The raw identifier is SHA256-hashed at the end of the processor pipeline, just before the event enters the cache. The hash input is `identifier + salt`, where `salt` is the value you pass to `initialize(appID:namespace:salt:)` (empty string by default).

The result is a 64-character lowercase hex string. The unhashed identifier never leaves the device. The TelemetryDeck server applies an additional server-side salt, so even if two apps use the same user email with the same client salt, the final stored hashes differ between apps.

## Recommendations

- **Most apps**: the platform default (IDFV) is sufficient. Users are tracked per-device, anonymously.
- **Cross-device identity**: if you want to correlate the same user across iPhone and iPad, call `setUserIdentifier` with a stable account identifier (email, user ID). It gets hashed before transmission.
- **Server-side Swift**: always pass `customUserID` — the default identifier is meaningless on servers.
- **Salt**: adding a `salt` at initialization provides an extra layer — even if someone intercepts the hashed identifier, they can't reverse it against a known-plaintext attack without knowing your salt.
