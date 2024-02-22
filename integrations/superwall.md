---
title: Using TelemetryDeck with Superwall iOS
tags:
  - how-to
  - iOS
testedOn: SuperWall iOS SDK 3.2..
description: Here's how to integrate TelemetryDeck with SuperWall to get insights into your paywalls.
lead: Here's how to integrate TelemetryDeck with SuperWall to get insights into your paywalls.
order: 100
---

[Superwall](https://superwall.com/) is a service that lets you experiment and try out different paywalls and monetization strategies. It's a great way to get started with monetization and to get insights into what works and what doesn't.

It pairs excellently with TelemetryDeck, as you can use TelemetryDeck to get insights into how your users interact with your paywalls. Superwall has various hooks that you can use to send events to TelemetryDeck, and this guide will show you how to do that.

## Installing Superwall and TelemetryDeck

First, we have to integrate both TelemetryDeck and Superwall into your app. You can find guides for both here:

1. [Install and setup the TelemetryDeck SDK](/docs/guides/swift-setup/)
2. [Install and set up the Superwall SDK](https://docs.superwall.com/docs/installation-via-spm)

If you've already set up TelemetryDeck or Superwall, you can skip the installation steps. Just make sure that you've set up both SDKs correctly. The order in which you initialize the SDKs doesn't matter.

## Creating a Superwall delegate

Superwall allows you to set a delegate that gets notified when a paywall is shown, dismissed, or when a user subscribes. We're going to use this delegate to send events to TelemetryDeck.

If you want to dive deeper, check out [Superwall's documentation on how to pass information to various analytics providers](https://docs.superwall.com/docs/3rd-party-analytics).

Create a new Swift file in your project and name it `SuperwallService.swift`. This file will contain the code that sends events to TelemetryDeck.

Paste the following code into the file:

```swift
import SuperwallKit
import TelemetryClient

class SuperwallService: SuperwallDelegate {
    func handleSuperwallEvent(withInfo eventInfo: SuperwallEventInfo) {
        var stringifiedParams: [String: String] = [:]

        for param in eventInfo.params {
            stringifiedParams[param.key] = String(describing: param.value)
        }

        TelemetryManager.send(eventInfo.event.description, with: stringifiedParams)
    }
}
```

Because TelemetryDeck only accepts strings as event metadata, this method accepts all data from Superwall, stringifies it, and hands it off to TelemetryDeck. The TelemetryManager takes care of queuing and sending the events to TelemetryDeck.

## Registering the Superwall delegate

Now that we have a delegate, we have to register it with Superwall. We can do this in the function that you initialize TelemetryDeck and Superwall in. This is usually in your `App` struct or `AppDelegate`. When in doubt, search for `TelemetryManager.initialize` in your project.

Add the following line to the function, making sure it is below the initialization code for both TelemetryDeck and Superwall:

```swift
let superwallService = SuperwallService()
Superwall.shared.delegate = superwallService
```

This initializes the Superwall delegate and registers it with Superwall. Now, whenever a paywall is shown, dismissed, or a user subscribes, the delegate will be notified and you'll get analytics data in your TelemetryDeck dashboard.
