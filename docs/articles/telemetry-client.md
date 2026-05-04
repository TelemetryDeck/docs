---
title: TelemetryDeck Swift Client Reference
tags:
  - Swift
  - SDK
testedOn: Xcode 12.4 & Swift 5.3
description: Reference documentation for the Swift Client for TelemetryDeck-using apps
lead: The TelemetryDeck Swift Client is a Swift Package to include in your app
searchEngineTitle: How to add the TelemetryDeck Swift Client
searchEngineDescription: Learn how to add the Swift Client for TelemetryDeck-using apps
---

## Include the Swift Client in your Xcode Project

See the [Swift Guide](/docs/guides/swift-setup/) on how to set up your app to use the TelemetryDeck Swift Client.

## Initialization

Init the TelemetryDeck at app startup, so it knows your App ID (you can retrieve the App ID in the TelemetryDeck Viewer app, under App Settings)

```swift
let config = TelemetryDeck.Config(appID: "<YOUR-APP-ID>")
TelemetryDeck.initialize(config: config)
```

For example, if you're building a scene based app, in the `init()` function for your `App`:

```swift
import SwiftUI
import TelemetryDeck

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
        let config = TelemetryDeck.Config(appID: "<YOUR-APP-ID>")
        TelemetryDeck.initialize(config: config)
    }
}
```

## Sending Signals

Once you've included the TelemetryDeck Swift Client, send signals like so:

```swift
TelemetryDeck.signal"appLaunchedRegularly")
```

TelemetryDeck will create a user identifier for your user that is specific to app installation and device. If you have a better user identifier available, you can use that instead: (the identifier will be hashed before sending it)

```swift
let email = MyConfiguration.User.Email
TelemetryDeck.signal"userLoggedIn", customUserID: email)
```

## Payload Data

You can also send additional parameters with each signal:

```swift
TelemetryDeck.signal("databaseUpdated", parameters: ["numberOfDatabaseEntries": "3831"])
```

TelemetryDeck will automatically send base parameters with these keys:

- `TelemetryDeck.AppInfo.buildNumber`
- `TelemetryDeck.AppInfo.dartVersion`
- `TelemetryDeck.AppInfo.version`
- `TelemetryDeck.AppInfo.versionAndBuildNumber`
- `TelemetryDeck.Device.architecture`
- `TelemetryDeck.Device.brand`
- `TelemetryDeck.Device.modelName`
- `TelemetryDeck.Device.operatingSystem`
- `TelemetryDeck.Device.orientation`
- `TelemetryDeck.Device.platform`
- `TelemetryDeck.Device.screenResolutionWidth`
- `TelemetryDeck.Device.screenResolutionHeight`
- `TelemetryDeck.Device.systemMajorVersion`
- `TelemetryDeck.Device.systemMajorMinorVersion`
- `TelemetryDeck.Device.systemVersion`
- `TelemetryDeck.Device.timeZone`
- `TelemetryDeck.RunContext.extensionIdentifier`
- `TelemetryDeck.RunContext.isAppStore`
- `TelemetryDeck.RunContext.isDebug`
- `TelemetryDeck.RunContext.isSimulator`
- `TelemetryDeck.RunContext.isTestFlight`
- `TelemetryDeck.RunContext.language`
- `TelemetryDeck.RunContext.locale`
- `TelemetryDeck.RunContext.targetEnvironment`
- `TelemetryDeck.SDK.name`
- `TelemetryDeck.SDK.nameAndVersion`
- `TelemetryDeck.SDK.version`
- `TelemetryDeck.UserPreference.region`
- `TelemetryDeck.UserPreference.language`

## Debug Mode

TelemetryDeck will _not_ send any signals if you are in `DEBUG` Mode. You can override this by setting `configuration.telemetryAllowDebugBuilds = true` on your `TelemetryDeck.Configuration` instance.
