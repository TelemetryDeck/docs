---
title: Test Mode
tags: Docs, Insights, Testing
testedOn: Xcode 13.1 & Swift 5.5 & TelemetryDeck SDK 1.1.5
description: Here's how to use Test Mode to get started with TelemetryDeck
lead: Test Mode helps you make sure that TelemetryDeck is set up correctly in your app and allows you to set up your Insights even during development.
---

If you don't tell it otherwise, the TelemetryDeck SDK will automatically mark all Signals sent while you develop your app as _Testing Signals_. Testing Signals are only included in your Insights if _Test Mode_ is on in the TelemetryDeck app. In Test Mode, your charts will only show testing data. If Test Mode is off, your charts will only show live data.

This helps you in two ways:

1. One, even during development, you can immediately see that your setup is working, and that signals are in fact being sent to TelemetryDeck.
2. And two, because you can play around with the types of signals that you will receive, it helps you set up your Insights during development. This way, they are ready to receive the real data once you release your version.

## Controlling whether to send Test Signals

By default, the TelemetryDeck SDK will mark all signals you send as Testing Signals exactly when your build configuration is set to `DEBUG`.

This means that in most Xcode setups, whenever you run your app in the simulator or directly from Xcode, you'll send testing signals.

If you want to override this behavior, you can set the [`TelemetryManagerConfiguration.testMode`](https://github.com/TelemetryDeck/SwiftClient/blob/main/Sources/TelemetryClient/TelemetryClient.swift#L62) property by hand.

However, we estimate that most people will not have to do this. Let us know if you think differently, we'd love to hear from you!
