---
title: Using TelemetryDeck with Superwall iOS
tags:
  - how-to
  - iOS
testedOn: SuperWall iOS SDK 3.2
description: Integrate TelemetryDeck with SuperWall to get insights into your paywalls.
lead: Integrate TelemetryDeck with SuperWall to get insights into your paywalls.
order: 100
---

[Superwall](https://superwall.com/) lets you experiment with different paywalls and monetization strategies. Combined with TelemetryDeck, you can see how users interact with your paywalls.

Superwall provides hooks that forward events to TelemetryDeck. This guide shows you how to wire them up.

## Installing Superwall and TelemetryDeck

Integrate both SDKs into your app:

1. [Install and set up the TelemetryDeck SDK](/guides/swift-setup/)
2. [Install and set up the Superwall SDK](https://docs.superwall.com/docs/installation-via-spm)

If you've already set up either SDK, skip that step. The initialization order doesn't matter.

## Creating a Superwall delegate

Create a new file `SuperwallService.swift`:

```swift
import SuperwallKit
import TelemetryDeck

class SuperwallService: SuperwallDelegate {
    func handleSuperwallEvent(withInfo eventInfo: SuperwallEventInfo) {
        var stringifiedParams: [String: String] = [:]

        for param in eventInfo.params {
            stringifiedParams[param.key] = String(describing: param.value)
        }

        Task {
            await TelemetryDeck.event(
                eventInfo.event.description,
                parameters: stringifiedParams
            )
        }
    }
}
```

## Registering the delegate

In the function where you initialize TelemetryDeck and Superwall (usually your `App` struct or `AppDelegate`), add:

```swift
let superwallService = SuperwallService()
Superwall.shared.delegate = superwallService
```

Paywall shown, dismissed, and subscription events will now appear in your TelemetryDeck dashboard.
