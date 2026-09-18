---
icon: fontawesome/solid/file-code
title: Objective-C Setup Guide
tags:
  - setup
  - ios
  - macos
  - objective c
---

Objective-C apps (or mixed Swift/ObjC projects) can use the TelemetryDeck Swift SDK through Objective-C interop.

## Installing the package

1. Open Xcode and navigate to your project
1. Select <kbd>File</kbd> → <kbd>Add Package Dependencies...</kbd>
1. Paste `https://github.com/TelemetryDeck/SwiftSDK` into the search field
1. Select the `SwiftSDK` package
1. Set the <kbd>Dependency Rule</kbd> to <kbd>Up to Next Major Version</kbd>
1. Click <kbd>Add Package</kbd>

## Linking the package

In the <kbd>Choose Package Products for SwiftSDK</kbd> screen, select the `TelemetryDeck` library and click <kbd>Add Package</kbd>.

!!! note "Multiple targets"

    If Xcode doesn't prompt you, add it manually: select your target → <kbd>Build Phases</kbd> → <kbd>Link Binary With Libraries</kbd> → <kbd>+</kbd> → select `TelemetryDeck`.

## Initializing TelemetryDeck

Add initialization to your App Delegate's `application:didFinishLaunchingWithOptions:`:

```objc
@import TelemetryDeck;

- (BOOL)application:(UIApplication *)application
    didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {

    [TelemetryDeck initializeWithAppID:@"YOUR-APP-ID"
                             namespace:@"YOUR-NAMESPACE"];

    return YES;
}
```

!!! note "You need your app's unique identifier and namespace"

    Both values are available in the [TelemetryDeck Dashboard](https://dashboard.telemetrydeck.com) under your app's settings.

## Verify your setup

Run your app. The SDK automatically sends a `TelemetryDeck.Session.started` event on launch.

!!! warning "Test signals"

    Events from `DEBUG` builds are tagged as test signals. Enable **Test Mode** in the TelemetryDeck Dashboard to see them.

Open the Dashboard → "Explore > Recent Signals" with Test Mode enabled.

---

## Sending custom events

```objc
[TelemetryDeck event:@"pizzaModeActivated"];
```

With parameters:

```objc
[TelemetryDeck event:@"pizzaModeActivated"
           parameters:@{@"cheeseMode": @"extraCheesy"}];
```

## App Store requirements

See our [Apple App Privacy guide](/articles/apple-app-privacy/) and [Privacy FAQ](/guides/privacy-faq/#do-i-need-to-add-telemetrydeck-to-my-privacy-policy%3F).

## What's next

<div class="grid cards" markdown>

-   **📊 Analytics Walkthrough**

    Learn how to navigate TelemetryDeck, interpret insights, and use analytics to make data-driven decisions that improve your app and grow your user base.

    [:fontawesome-solid-right-long: Start here to get real value from your analytics](../basics/index.md)
</div>
