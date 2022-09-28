---
title: Getting Started With Test Mode
tags:
  - setup
  - testmode
  - quickstart
  - beginner
testedOn: Xcode 13.1 & Swift 5.5 & TelemetryDeck SDK 1.1.5
description: Here's how to use Test Mode to get started with TelemetryDeck
lead: Test Mode helps you make sure that TelemetryDeck is set up correctly in your app and allows you to set up your insights even during development.
searchEngineTitle: How to Run Test Signals
searchEngineDescription: Enable Test Mode now in your TelemetryDeck dashboard to easily send signals through debug mode.
---

During the development of your TelemetryDeck-enabled app - or even while you test it - your app sends signals. These signals are not from your users but rather from yourself or your development team. You might even send hundreds of signals during tests, which would mess up your insights if mixed with actual analytics data. Not cool!

We do not recommend not doing any testing. The benefits of sending signals during test phases are enormous! If you have not considered it yet, here are some nifty reasons why you should start now:
- You will be able to find errors in the configuration of the TelemetryDeck SDK
- Working with test signals means you will know if your app works even before releasing your app
- As well as being able to make preparations for new signal types or payload types until your app is released

Test Mode will let you easily and quickly test new features for your app, giving you the power to release the best product possible! Let's dive right in.

## How It Works

Each sent signal has a `isTestMode` parameter, which can either be `true` or `false`.
Navigate to your TelemetryDeck [dashboard](https://dashboard.telemetrydeck.com/), where you will find the Test Mode toggle on the top left side, just above the sidebar.
You can toggle it to show your signals either in `isTestMode == true` or `isTestMode == false`. While toggled to `true`, you will see a banner at the top displaying **Test Data** to remind you that you are currently in Test Mode, and all signals get sent in said mode. All charts will display test data only while in Test Mode.

## Sending Signals in Test Mode

The SDKs try to infer the isTestMode parameter as best as they can. For example, if a DEBUG parameter is present in your development environment, that is used as the value for isTestMode.
You can also override the isTestMode parameter just as you would add any other payload parameter to a signal
Note: since signal payloads only support strings, the parameter needs to be either "true" or "false"

### Manually Set Test Mode in Swift SDK

````swift
// An example variable to manually set test mode.
// Set this to `true` or `false` depending on your app's configuration
// or environment or state
let customTestModeParameter = true

TelemetryManager.send(
    "pizzaModeActivated",
    for: "myUserIdentifier",
    with: ["isTestMode": customTestModeParameter ? "true" : "false"]
)`
````

### Manually Set Test Mode in Javascript SDK

````javascript
// Example initialisation of TelemetryDeck SDK
`td = new TelemetryDeck({
  app: ENV.APP.telemetryAppID,
  user: this.user.current?.email ?? 'anonymous',
});`

// In our example, the app has a `send` function wrapping the TelemetryDeck SDK
send(payload) {
  // ENV.APP.telemetryIsDebug is an example variable that represents your app's
  // configuration or environment. Replace it with an implementation that fits your
  // app's needs.
  if (ENV.APP.telemetryIsDebug) {
    this.td.signal({...payload, isTestMode: "true"})
    return;
  }

  this.td.signal(payload);
}
````