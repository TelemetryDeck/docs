---
title: Swift Setup Guide
tags:
  - Setup
  - iOS
  - macOS
  - watchOS
  - tvOS
featured: true
testedOn: Xcode 12.2 & Swift 5.3
description: Configure the TelemetryDeck SDK in Your Swift Application for iOS, macOS, watchOS and tvOS
lead: Let's include the TelemetryClient Swift Package in your application and send signals!
order: 100
---

## Prerequisites

This guide assumes you have already created a TelemetryDeck account. If you haven't yet, please [sign up now](https://dashboard.telemetrydeck.com/registration/organization)!

## Installing the Swift Package

The TelemetryDeck Swift package uses Swift Package Manager.

- Open Xcode and navigate to the project you want to add TelemetryDeck to.
- In the menu, select <kbd>File</kbd> -> <kbd>Add Packages...</kbd>. This will open the Swift Package Manager view.
- Add the following as package repository and click <kbd>Next</kbd>:

```swift
https://github.com/TelemetryDeck/SwiftClient
```

There will be one or two additional screens, but you can just click <kbd>Next</kbd> and <kbd>Finish</kbd> on them – Xcode will do the right thing by linking the package against your target. (In the unlikely case that you have multiple targets, link them each with the package's library.)

This will include the TelemetryDeck Swift Client into your app by downloading the source code. Feel free to browse the client's source code, it's very tiny and you'll see for yourself how TelemetryDeck is hashing user identifiers before they ever reach the server. Privacy, yay!

## Initializing the TelemetryDeck Swift Package

The `TelemetryClient` package will provide you with a class `TelemetryManager` that you'll use for all interactions with TelemetryDeck. Before you can use that class, you'll need to initialize it at the start of your app. We strongly recommend doing so as soon as possible, as you won't be able to send Signals before the `TelemetryManager` is initialized.

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
struct Example_AppApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
    }
}
```

This is the entry point to your app. Now let's add the initialization here.

Import the TelemetryClient Package by adding `import TelemetryClient`. Then add an `init()` method to your App struct that creates a `TelemetryManagerConfiguration` instance and hands it to the `TelemetryManager`, using the **Unique Identifier of your app** that you copied into your clipboard earlier. If you don't have that anymore, you can get it at any time from the TelemetryDeck Dashboard.

Your code should now look like this:

```swift
import SwiftUI
import TelemetryClient

@main
struct Example_AppApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
    }

    init() {
        let configuration = TelemetryManagerConfiguration(
            appID: "YOUR-APP-UNIQUE-IDENTIFIER")
        TelemetryManager.initialize(with: configuration)
    }
}
```

If you already have an `init()` method, add the two lines to its end.

Your app is now ready. You can skip the AppDelegate part if you're using SwiftUI and SceneKit.

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

Now, import the `TelemetryClient` package and configure the `TelemetryManager` using the **Unique Identifier of your app** that you copied into your clipboard earlier. If you don't have that anymore you can get it at any time from the TelemetryDeck Dashboard.

```swift
import UIKit
import TelemetryClient

@main
class AppDelegate: UIResponder, UIApplicationDelegate {
    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {

        let configuration = TelemetryManagerConfiguration(
            appID: "YOUR-APP-UNIQUE-IDENTIFIER")
        TelemetryManager.initialize(with: configuration)

        return true
    }
    // ...
}
```

If you already have code in this function, add the two new lines to the end.

You are now ready to send signals!

## Sending Signals

Let's send a signal to show the app has launched correctly.

{% noteinfo "What is a signal?" %}

Signals are an indication that **an event** happened in your app, which is used by a **user**. Signals consist of these parts:

- **Signal Type** – A string that indicates which kind of event happened
- **User Identifer** – A string that identifies your user
- **Metadata Payload** – A dictionary of additional data about your app or the event triggering the signal

See the [Signals Reference](/docs/api/signals-reference/) for more information about how you can effectively use Signals.
{% endnoteinfo %}

{% notewarning "When running from Xcode, you're sending testing signals" %}

If you app is built in `DEBUG` configuration (i.e. running from Xcode), your signals will be tagged as **Testing Signals**, meaning that you can easily filter them out later. You'll see them show up in the TelemetryDeck Dashboard when it is set to **Test Mode**.
{% endnotewarning %}

See the [TelemetryDeck SDK's `README.md` file](https://github.com/TelemetryDeck/SwiftClient/blob/main/README.md) for more information on how to send signals. For now, let's just send one signal that tells us the app has launched. Go to the place where you just added the initialization, and directly below add this line:

```swift
let configuration = TelemetryManagerConfiguration(appID: "YOUR-APP-UNIQUE-IDENTIFIER")
TelemetryManager.initialize(with: configuration)

TelemetryManager.send("applicationDidFinishLaunching")
```

Aaaand done. This is all you need to send a signal. You do not need to keep an instance of TelemetryManager and hand it around, just call the `send` function on the class directly. If you want to add a custom user identifer or metadata payload, add them to the function call like this:

```swift
TelemetryManager.send(
    "applicationDidFinishLaunching",
    for: "my very cool user",
    with: [
        "numberOfTimesPizzaModeHasActivated": "\(dataStore.pizzaMode.count)",
        "pizzaCheeseMode": "\(dataStore.pizzaCheeseMode)"
    ])
```

And you're done! You are now sending signals to the TelemetryDeck server.

## You're all set!

You can now send signals! Don't overdo it in the beginning. It's okay if you only send **one** signal, named `applicationDidFinishLaunching` in the beginning. This will already give you number of users, number of launches, retention... a lot!

After a while, you can add a send call for each screen in your app, so you can see which screens are used most. I also recommend adding all your custom settings to your metadata each time (except the ones that might identify an individual user of course). This way you can see which settings most of your users use.
