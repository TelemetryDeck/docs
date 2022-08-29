---
title: TelemetryDeck Swift Client Reference
tags:
  - TelemetryManager
  - SwiftClient
testedOn: Xcode 12.4 & Swift 5.3
description: Reference documentation for the Swift Client for TelemetryDeck-using apps
lead: The TelemetryDeck Swift Client is a Swift Package to include in your app
---

## Include the Swift Client in your Xcode Project

See the [Swift Guide](/docs/guides/swift-setup/) on how to set up your app to use the TelemetryDeck Swift Client.

## Initialization

Init the TelemetryDeck Manager at app startup, so it knows your App ID (you can retrieve the App ID in the TelemetryDeck Viewer app, under App Settings)

```swift
let configuration = TelemetryManagerConfiguration(appID: "<YOUR-APP-ID>")
TelemetryManager.initialize(with: configuration)
```

For example, if you're building a scene based app, in the `init()` function for your `App`:

```swift
import SwiftUI
import TelemetryClient

@main
struct TelemetryTestApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
    }

    init() {
        // Note: Do not add this code to `WindowGroup.onAppear`, which will be called
        //       *after* your window has been initialized, and might lead to out initialization
        //       occurring too late.
        let configuration = TelemetryManagerConfiguration(appID: "<YOUR-APP-ID>")
        TelemetryManager.initialize(with: configuration)
    }
}
```

## Sending Signals

Once you've included the TelemetryDeck Swift Client, send signals like so:

```swift
TelemetryManager.send("appLaunchedRegularly")
```

TelemetryDeck Manager will create a user identifier for your user that is specific to app installation and device. If you have a better user identifier available, you can use that instead: (the identifier will be hashed before sending it)

```swift
let email = MyConfiguration.User.Email
TelemetryManager.send("userLoggedIn", for: email)
```

<div class="alert alert-secondary" role="alert">
<h4 class="alert-heading">Note on User Identifiers on Mac</h4>
<p><small>If you are writing a Mac App, TelemetryDeck Manager can not create a unique user identifier, and will instead default to a concatenation of your OS Version and App Build number, which is not exactly unique, so user counting will be less accurate.</small></p>

<p><small>I therefore strongly recommend to either use a unique identifier for your users, such as an email address, or to generate and store a `UUID().uuidString`, for example in `UserDefaults`, and always pass that to TelemetryDeck Manager as User ID.</small></p>

<p><small>The reason why TelemetryDeck Manager can't do that itself is that it feels like crossing a line if this very simple tool would generate IDs itself and write those to a directory on disk. I feel that this is not expected behaviour for a privacy-first analytics package.</small></p>

</div>

## Payload Data

You can also send additional payload data with each signal:

```swift
TelemetryManager.send("databaseUpdated", with: ["numberOfDatabaseEntries": "3831"])
```

TelemetryDeck Manager will automatically send a base payload with these keys:

- platform
- systemVersion
- appVersion
- buildNumber
- isSimulator
- isTestFlight
- isAppStore
- modelName
- architecture
- operatingSystem
- targetEnvironment

## Debug Mode

TelemetryDeck Manager will _not_ send any signals if you are in `DEBUG` Mode. You can override this by setting `configuration.telemetryAllowDebugBuilds = true` on your `TelemetryManagerConfiguration` instance.
