---
title: Swift Setup Guide
tags:
  - Setup
  - iOS
  - macOS
  - watchOS
  - tvOS
featured: true
testedOn: Xcode 16 & Swift 5.9
description: Configure the TelemetryDeck SDK in Your Swift Application for iOS, macOS, watchOS and tvOS
lead: Let's include the TelemetryDeck Swift Package in your application and send events!
order: 100
---

## Prerequisites

This guide assumes you have already created a TelemetryDeck account. If you haven't yet, please [sign up now](https://dashboard.telemetrydeck.com/register)!

## Installing the Swift Package

The TelemetryDeck Swift package uses Swift Package Manager.

1. Open Xcode and navigate to the project you want to add TelemetryDeck to
1. In the menu, select <kbd>File</kbd> -> <kbd>Add Package Dependencies...</kbd>. This will open the Swift Package Manager view
1. Paste `https://github.com/TelemetryDeck/SwiftSDK` into the search field.
1. Select the `SwiftSDK` package that appears in the list
1. Set the <kbd>Dependency Rule</kbd> to <kbd>Up to Next Major Version</kbd>
1. Press <kbd>Add Package</kbd> to continue

![A screenshot of Xcode adding the TelemetryDeck Package](/docs/images/xcode-swift-package1.png)

This will include the TelemetryDeck Swift SDK into your app by downloading the source code. Feel free to browse the client's source code, it's tiny and you'll see for yourself how TelemetryDeck is hashing user identifiers before they ever reach the server. Privacy, yay!

**Watch our [Quick Start video](https://www.youtube.com/watch?v=FA71bSnK_B8) to setup TelemetryDeck in 4 Minutes!**

[![TelemetryDeck Setup in 4 Minutes – Swift SDK Integration](/docs/images/yt-4-minute-setup.png)](https://www.youtube.com/watch?v=FA71bSnK_B8)

## Including the package in your target

Xcode will ask you to link the package with your target in the next screen, titled <kbd>Choose Package Products for SwiftSDK</kbd>. Set the <kbd>Add to target</kbd> column to your app target for <kbd>TelemetryDeck</kbd> (not "TelemetryClient", which is deprecated) and click <kbd>Add Package</kbd> to complete the integration.

![A screenshot of Xcode setting the target for the TelemetryDeck library](/docs/images/xcode-swift-package2.png)

{% noteinfo "Link Library with more than one Target" %}

In case Xcode forgets to ask you to link the library with your target, you can do so manually by selecting your target in the project navigator and selecting the <kbd>Build Phases</kbd> tab. Click the <kbd>+</kbd> button in the <kbd>Link Binary With Libraries</kbd> section and select the `TelemetryDeck` library.
{% endnoteinfo %}

## Initializing the TelemetryDeck Swift package

The `TelemetryDeck` package will provide you with a class `TelemetryDeck` that you'll use for all interactions with TelemetryDeck. Before you can use that class, you'll need to initialize it at the start of your app. We strongly recommend doing so as soon as possible, as you won't be able to send events before the `TelemetryDeck` is initialized.

This is slightly different depending on whether you use SwiftUI or UIKit's `AppDelegate` to manage your app's lifecycle, so let's look at these individually.

{% noteinfo "You need your app's Unique Identifier" %}
TelemetryDeck assigns a unique identifier to your app, and you need to hand that identifier to the TelemetryDeck SDK.

Use the [TelemetryDeck Dashboard](https://dashboard.telemetrydeck.com) to create a new app and copy its unique identifier into your computer's clipboard.
{% endnoteinfo %}

You only need **one** way of initializing the TelemetryDeck SDK, either SwiftUI/SceneKit or AppDelegate. If your app is new, you'll likely want to use SwiftUI/SceneKit.

### Initialization with SwiftUI

For Scene-based SwiftUI applications, we recommend adding the initialization to your `@main` App struct! Open `YourAppNameApp.swift` and look for code that looks like this:

```swift
import SwiftUI

@main
struct YourAppNameApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
    }
}
```

This is the entry point to your app. Now let's add the initialization here.

Import the TelemetryDeck Package by adding `import TelemetryDeck`. Then add an `init()` method to your App struct that creates a `TelemetryDeck.Config` instance and hands it to `TelemetryDeck.initialize(config:)`, using the **Unique Identifier of your app** that you copied into your clipboard earlier. If you don't have that anymore, you can get it at any time from the TelemetryDeck Dashboard.

Your code should now look like this:

```swift
import SwiftUI
import TelemetryDeck

@main
struct YourAppNameApp: App {
    init() {
        let config = TelemetryDeck.Config(appID: "YOUR-APP-ID")
        TelemetryDeck.initialize(config: config)
    }

    var body: some Scene {
        WindowGroup {
            ContentView()
        }
    }
}
```

If you prefer to have it on a single line, you can also write:

```swift
TelemetryDeck.initialize(config: .init(appID: "YOUR-APP-ID"))
```

Your app is now ready to use TelemetryDeck. You can skip the next section which explains setup for UIKit-based apps.

### Initialization in an AppDelegate based app

If you use `AppDelegate` to manage your app's life cycle, open the file `AppDelegate.swift` and look for the method `application(:didFinishLaunchingWithOptions:)`. It will probably look similar to this:

```swift
import UIKit

@main
class AppDelegate: UIResponder, UIApplicationDelegate {
    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
        // Override point for customization after application launch.
        return true
    }

    // ...
}
```

By default, Xcode even adds a comment here to tell you where to add stuff that should happen right after launch.

Now, import the `TelemetryDeck` package and configure the `TelemetryDeck` using the **Unique Identifier of your app** that you copied into your clipboard earlier. If you don't have that anymore you can get it at any time from the TelemetryDeck Dashboard.

```swift
import UIKit
import TelemetryDeck

@main
class AppDelegate: UIResponder, UIApplicationDelegate {
    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {

        let config = TelemetryDeck.Config(appID: "YOUR-APP-ID")
        TelemetryDeck.initialize(config: config)

        return true
    }
    // ...
}
```

## Verify your setup

Run your app to verify that TelemetryDeck is properly integrated. The SDK automatically sends a `TelemetryDeck.Session.started` signal when your app launches.

{% notewarning "When running from Xcode, you're sending test events" %}

If your app is built in `DEBUG` configuration (i.e. running from Xcode), your events will be tagged as **Test Signals**, meaning that you can easily filter them out later. You'll see them show up in the TelemetryDeck Dashboard when the **Test Mode** toggle under the tab bar is turned on.
{% endnotewarning %}

Open the TelemetryDeck Dashboard, navigate to "Explore > Recent Signals" and make sure "Test Mode" is enabled. You should see the automatic session signal appear after launching your app.

---

{% noteinfo "Ready for basic insights" %}
Congratulations! With just the SDK initialization, TelemetryDeck will automatically track user sessions, app launches, and device information. This basic setup provides valuable built-in insights without any additional code.

You can now build and ship your app. Once users start using it, your TelemetryDeck dashboard will begin showing data about user behavior, device types, and other key metrics.
{% endnoteinfo %}

## Enhancing your analytics (optional)

While basic session tracking provides valuable information, sending custom events lets you answer questions specific to how users engage with *your* app.

### Common questions you can answer with custom events

- Which features do users engage with most frequently?
- Where in the onboarding flow do users drop off?
- How are users navigating between different screens?
- Which settings or configurations are most popular?

### Sending custom events

{% noteinfo "What is a signal?" %}
Signals are an indication that **an event** happened in your app, which is used by a **user**. Signals consist of these parts:

- **Signal Name** – A string that indicates which kind of event happened
- **User Identifier** – A string that identifies your user (we auto-generate one for you)
- **Optional Parameters** – A dictionary of additional data about your app or the event triggering the signal

See the [Signals Reference](/docs/api/signals-reference/) for more information about how you can effectively use Signals.
{% endnoteinfo %}

Let's imagine your app is a pizza oven monitor and we want to send a signal that tells us the user has tapped the "Start Baking" button. Go to the place in your code where the user taps the button and add the following code:

```swift
TelemetryDeck.signal("Oven.Bake.startBaking")
```

That's all you need to send a signal. You do not need to keep an instance of TelemetryDeck and hand it around, just call the static `signal` function on the class directly. If you want to add custom parameters, add them to the function call like this:

```swift
TelemetryDeck.signal(
    "Oven.Bake.startBaking",
    parameters: [
        "numberOfTimesPizzaModeHasActivated": "\(dataStore.pizzaMode.count)",
        "pizzaCheeseMode": "\(dataStore.pizzaCheeseMode)"
    ]
)
```

{% noteinfo "Privacy Note" %}
The value you pass to `customUserID` will be automatically hashed before being sent to our servers to protect the users privacy. This does not happen for the values in `parameters` though, so hash yourself where needed.
{% endnoteinfo %}

## Configuring default signal properties (optional)

When initializing TelemetryDeck, you can configure some defaults to help keep your signals organized and consistent:

```swift
let config = TelemetryDeck.Config(appID: "YOUR-APP-ID")

// Add a prefix to all signal names
config.defaultSignalPrefix = "App."
// With this set, calling signal("launched") will actually send "App.launched"

// Add a prefix to all parameter names
config.defaultParameterPrefix = "MyApp."
// This prefixes all keys in your parameters dictionary

// Set parameters that will be included with every signal
config.defaultParameters = {[
    "theme": UserDefaults.standard.string(forKey: "theme") ?? "default",
    "isPayingUser": FreemiumKit.shared.hasPurchased ? "true" : "false",
]}
// These parameters will be merged with any additional parameters you specify in signal() calls
```

## App Store requirements

Before uploading your app to the App Store, you'll need to complete Apple's privacy details on App Store Connect. Although TelemetryDeck is privacy-focused, you still need to disclose analytics usage.

For guidance on completing these requirements, see our [Apple App Privacy guide](/docs/articles/apple-app-privacy/). For privacy policy recommendations, check our [Privacy FAQ](/docs/guides/privacy-faq/#do-i-need-to-add-telemetrydeck-to-my-privacy-policy%3F).

## What to do next

Now that you've integrated TelemetryDeck, learn how to use the analytics platform to gain valuable insights about your users:

<div class="not-prose ">
  <div class="my-10 grid grid-cols-1 gap-6">
    <div class="group relative rounded-xl border-2 border-mars-300 bg-white flex">
      <div class="absolute -inset-px rounded-xl border-2 border-transparent opacity-0 [background:linear-gradient(var(--quick-links-hover-bg,theme(colors.mars.50)),var(--quick-links-hover-bg,theme(colors.mars.100)))_padding-box,linear-gradient(to_top,theme(colors.mars.400),theme(colors.mars.500))_border-box] group-hover:opacity-100"></div>
      <div class="shadow relative overflow-hidden rounded-xl p-6 h-full">
        <h2 class="font-semibold text-lg text-mars-500">
          <a href="/docs/basics/index">
            <span class="absolute -inset-px rounded-xl"></span>📊 Analytics Walkthrough</a>
        </h2>
        <p class="mt-2 text-sm text-slate-700">Learn how to navigate TelemetryDeck, interpret insights, and use analytics to make data-driven decisions that improve your app and grow your user base.</p>
        <p class="mt-4 text-sm text-mars-500 font-semibold flex justify-between">
          <span>Start here to get real value from your analytics</span>
          <span>→</span>
        </p>
      </div>
    </div>
  </div>
</div>
