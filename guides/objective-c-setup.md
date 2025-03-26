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
1. Paste `https://github.com/TelemetryDeck/SwiftSDK` into the search field.
1. Select the `SwiftSDK` package that appears in the list
1. Set the <kbd>Dependency Rule</kbd> to <kbd>Up to Next Major Version</kbd>.
1. Click <kbd>Add Package</kbd>.

![A screenshot of Xcode adding the TelemetryDeck Package](/docs/images/xcode-swift-package.png)

This will include the TelemetryDeck Swift Client into your app by downloading the source code. Feel free to browse the client's source code. It's tiny and you'll see for yourself how TelemetryDeck is hashing user identifiers before they ever reach the server. Privacy, yay!

## Including the package in your target

Xcode will ask you to link the package with your target in the next screen, titles <kbd>Choose Package Products for SwiftSDK</kbd>. Select the `TelemetryClient` library and click <kbd>Add Package</kbd>.

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

## Verify Your Setup

Run your app to verify that TelemetryDeck is properly integrated. Let's send a signal to show the app has launched correctly:

```objc
[TelemetryManager send:@"applicationDidFinishLaunching"];
```

{% notewarning "When running from Xcode, you're sending test signals" %}
If your app is built in `DEBUG` configuration (i.e. running from Xcode), your signals will be tagged as **Test Signals**, meaning that you can easily filter them out later. You'll see them show up in the TelemetryDeck Dashboard when the **Test Mode** toggle under the tab bar is turned on.
{% endnotewarning %}

Open the TelemetryDeck Dashboard, navigate to "Explore > Recent Signals" and make sure "Test Mode" is enabled. You should see your signal appear after launching your app.

---

{% noteinfo "Ready for Basic Insights" %}
Congratulations! With just the SDK initialization, TelemetryDeck will automatically track user sessions, app launches, and device information. This basic setup provides valuable built-in insights without any additional code.

You can now build and ship your app. Once users start using it, your TelemetryDeck dashboard will begin showing data about user behavior, device types, and other key metrics.
{% endnoteinfo %}

## Enhancing Your Analytics (Optional)

While basic session tracking provides valuable information, sending custom signals lets you answer questions specific to how users engage with *your* app.

### Sending Custom Signals

{% noteinfo "What's a signal?" %}
Signals represent an **event** or a **view** that happened in your app, which is used by a **user**. Signals consist of these parts:

- **Signal Type**: A string that indicates which kind of event happened
- **Metadata Payload**: A dictionary of additional data about your app or the event triggering the signal

See the [Signals Reference](/docs/api/signals-reference/) for more information about how you can effectively use Signals.
{% endnoteinfo %}

You don't need to keep an instance of TelemetryManager and hand it around, just call the `send` function on the class directly. If you want to add custom metadata payload, add it to the function call as a dictionary:

```objc
[
    TelemetryManager
    send:@"applicationDidFinishLaunching"
    with:@{@"pizzaCheeseMode": @"extraCheesy"}
];
```

The metadata is helpful for additional parameters for filtering or grouping signals. We'll automatically add some metadata for you, like the app version, device model, and more.

For more information on how to send signals, see the [TelemetryDeck package's `README.md` file](https://github.com/TelemetryDeck/SwiftSDK/blob/main/README.md).

## App Store Requirements

Before uploading your app to the App Store, you'll need to complete Apple's privacy details on App Store Connect. Although TelemetryDeck is privacy-focused, you still need to disclose analytics usage.

For guidance on completing these requirements, see our [Apple App Privacy guide](/docs/articles/apple-app-privacy/).

For privacy policy recommendations, check our [Privacy FAQ](/docs/guides/privacy-faq/#do-i-need-to-add-telemetrydeck-to-my-privacy-policy%3F).

### Next Steps

Once your app is collecting data, learn how to get useful insights:

<div class="not-prose ">
  <div class="my-10 grid grid-cols-1 gap-6 sm:grid-cols-2">
    <div class="group relative rounded-xl border bg-white border-slate-200 flex">
      <div class="absolute -inset-px rounded-xl border-2 border-transparent opacity-0 [background:linear-gradient(var(--quick-links-hover-bg,theme(colors.mars.50)),var(--quick-links-hover-bg,theme(colors.mars.100)))_padding-box,linear-gradient(to_top,theme(colors.mars.400),theme(colors.mars.500))_border-box] group-hover:opacity-100"></div>
      <div class="shadow relative overflow-hidden rounded-xl p-6 h-full">
        <h2 class="font-semibold text-sm text-mars-500">
          <a href="/docs/pirate-metrics/understanding-app-analytics/">
            <span class="absolute -inset-px rounded-xl"></span>Explore Built-in Insights</a>
        </h2>
        <p class="mt-1 text-sm text-slate-700">Discover the automatically generated insights and how to interpret them.</p>
      </div>
    </div>
    <div class="group relative rounded-xl border bg-white border-slate-200 flex">
      <div class="absolute -inset-px rounded-xl border-2 border-transparent opacity-0 [background:linear-gradient(var(--quick-links-hover-bg,theme(colors.mars.50)),var(--quick-links-hover-bg,theme(colors.mars.100)))_padding-box,linear-gradient(to_top,theme(colors.mars.400),theme(colors.mars.500))_border-box] group-hover:opacity-100"></div>
      <div class="shadow relative overflow-hidden rounded-xl p-6 h-full">
        <h2 class="font-semibold text-sm text-mars-500">
          <a href="/docs/articles/what-are-insights/">
            <span class="absolute -inset-px rounded-xl"></span>Create Custom Insights</a>
        </h2>
        <p class="mt-1 text-sm text-slate-700">Learn how to build your own custom insights to track specific metrics.</p>
      </div>
    </div>
  </div>
</div>
