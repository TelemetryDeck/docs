---
title: Objective-C Setup Guide
tags:
  - Setup
  - iOS
  - macOS
  - watchOS
  - tvOS
  - ObjectiveC
featured: false
testedOn: Xcode 14.1 & Swift 5.5
description: Configure the TelemetryDeck SDK in Your Objective-C Application for iOS and macOS
lead: Let's include the TelemetryClient Swift Package in your Objective-C application and send signals!
order: 1000
---

Lots of iOS and macOS application are still written in Objective-C, or a mixture of Swift and ObjC. We've got you covered either way, and this guide will show you how to set up the TelemetryDeck SDK in your Objective-C application.

## Installing the package

The TelemetryDeck Swift package uses Swift Package Manager.

1. Open Xcode and navigate to the project you want to add TelemetryDeck to.
1. In the menu, select <kbd>File</kbd> -> <kbd>Add Packages...</kbd>. This will open the Swift Package Manager view.
1. Paste `https://github.com/TelemetryDeck/SwiftClient` into the search field.
1. Select the `SwiftClient` package that appears in the list
1. Set the <kbd>Dependency Rule</kbd> to <kbd>Up to Next Major Version</kbd>.
1. Click <kbd>Add Package</kbd>.

![A screenshot of Xcode adding the TelemetryDeck Package](/docs/images/xcode-swift-package.png)

This will include the TelemetryDeck Swift Client into your app by downloading the source code. Feel free to browse the client's source code. It's tiny and you'll see for yourself how TelemetryDeck is hashing user identifiers before they ever reach the server. Privacy, yay!

## Including the package in your target

Xcode will ask you to link the package with your target in the next screen, titles <kbd>Choose Package Products for SwiftClient</kbd>. Select the `TelemetryClient` library and click <kbd>Add Package</kbd>.

{% noteinfo "Link Library with more than one Target" %}

In case Xcode forgets to ask you to link the library with your target, you can do so manually by selecting your target in the project navigator. Selecting the <kbd>Build Phases</kbd> tab. Click the <kbd>+</kbd> button in the <kbd>Link Binary With Libraries</kbd> section and select the `TelemetryClient` library.
{% endnoteinfo %}

## Initializing the TelemetryDeck package

The `TelemetryClient` package will provide you with a class `TelemetryManager` that you'll use for all interactions with TelemetryDeck. Before you can use that class, you'll need to initialize it at the start of your app. The ideal place for this is your **App Delegate**'s `application:didFinishLaunchingWithOptions:` method:

```objc
// Import the TelemetryClient library
@import TelemetryClient;

// ...

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {

    // Your other initialization code here ...

    // Initialize the TelemetryDeck client
    TelemetryManagerConfiguration *telemetryConfig =
        [[TelemetryManagerConfiguration alloc] initWithAppID:@"YOUR-APP-ID"];
    [TelemetryManager initializeWith:telemetryConfig];

    // Optional: Set a default user ID. If you don't do this,
    // the SDK will generate a random user ID for you.
    // [TelemetryManager updateDefaultUserTo:@"myuserwhojustloggedin@example.com"];

    return YES;
}

```

{% noteinfo "You need your app's Unique Identifier" %}
TelemetryDeck assigns a unique identifier to your app, and you need to hand that identifier to the TelemetryDeck SDK.

Use the [TelemetryDeck Dashboard](https://dashboard.telemetrydeck.com) to create a new app and copy its unique identifier into your computer's clipboard.
{% endnoteinfo %}

## Sending signals

Let's send a signal to show the app has launched correctly.

{% noteinfo "What's a signal?" %}

Signals represent an **event** or a **view** that happened in your app, which is used by a **user**. Signals consist of these parts:

- **Signal Type**: A string that indicates which kind of event happened
- **Metadata Payload**: A dictionary of additional data about your app or the event triggering the signal

See the [Signals Reference](/docs/api/signals-reference/) for more information about how you can effectively use Signals.
{% endnoteinfo %}

See the [TelemetryDeck package's `README.md` file](https://github.com/TelemetryDeck/SwiftClient/blob/main/README.md) for more information on how to send signals. For now, let's just send one signal that tells us the app has launched. Go to your app delegate and below the initialization add this line:

```objc
[TelemetryManager send:@"applicationDidFinishLaunching"];
```

We're done. This is all you need to send a signal. You don't need to keep an instance of TelemetryManager and hand it around, just call the `send` function on the class directly. If you want to add custom metadata payload, add it to the function call like as a dictionary.

This is helpful for additional parameters for filtering or grouping signals. We'll auto add some metadata for you, like the app version, device model, etc.

```swift
[
    TelemetryManager
    send:@"applicationDidFinishLaunching"
    with:@{@"pizzaCheeseMode": @"extraCheesy"}
];
```

And you're done! You are now sending signals to the TelemetryDeck server (the signals are marked as **Testing Signals** in the dashboard, switch on **Testing Mode** to see them).

{% notewarning "When running from Xcode, you're sending testing signals" %}

If you app is built in `DEBUG` configuration (that is running from Xcode), your signals will be tagged as **Testing Signals**, meaning that you can filter them out later. You'll see them show up in the TelemetryDeck Dashboard when it's set to **Test Mode**.
{% endnotewarning %}

## You're all set!

You can now send signals! Don't overdo it in the beginning. It's okay if you only send **one** signal, named `applicationDidFinishLaunching` in the beginning. This will already give you number of users, number of launches, retention... a lot!

After a while, you can add a send call for each screen in your app, so you can see which screens are used most. We also recommend adding all your custom settings to your metadata each time (except the ones that might identify an individual user of course). This way you can see which settings most of your users use.
