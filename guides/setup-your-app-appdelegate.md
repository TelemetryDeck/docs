---
title: Setting Up Your Application using AppDelegate
tags:
  - Setup
  - Quickstart
  - Code
testedOn: Xcode 12.2 & Swift 5.3
description: How to configure TelemetryClient in AppDelegate based applications
lead: If you use `AppDelegate` to manage your app's life cycle, this is how you setup your application so it can send TelemetryDeck signals
order: 12
---

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

Now, import the `TelemetryClient` package and configure the `TelemetryManager` using the **Unique Identifier of your app** that you copied into your clipboard earlier. If you don't have that anymore you can get it at any time from the TelemetryDeck Viewer app.

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

## You did it!

You've finished setting up your application and are now ready to send some signals.

<a href="/pages/sending-signals.html" class="btn btn-secondary btn-large">Next Up: Sending Signals &rarr;</a>
