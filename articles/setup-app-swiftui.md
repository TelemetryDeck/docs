---
title: Setting Up Your Application in SwiftUI
tags:
  - Setup
  - Quickstart
  - Code
testedOn: Xcode 12.2 & Swift 5.3
description: How to configure TelemetryClient in SwiftUI based applications
lead: In Scene-based SwiftUI applications, this is how you configure TelemetryClient
order: 2000
---

For Scene-based SwiftUI applications, I recommend adding the initialization to your `@main` App struct! Open `YourAppNameApp.swift` and look for code that looks like this:

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

Import the TelemetryClient Package by adding `import TelemetryClient`. Then add an `init()` method to your App struct that creates a `TelemetryManagerConfiguration` instance and hands it to the `TelemetryManager`, using the **Unique Identifier of your app** that you copied into your clipboard earlier. If you don't have that anymore, you can get it at any time from the TelemetryDeck Viewer app.

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

If you already have an `init()` method, add this to its end.

## You did it!

You've finished setting up your application and are now ready to send some signals.

<a href="/pages/sending-signals.html" class="btn btn-secondary btn-large">Next Up: Sending Signals &rarr;</a>
