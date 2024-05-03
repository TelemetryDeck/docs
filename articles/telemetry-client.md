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

<div class="alert alert-secondary" role="alert">
<h4 class="alert-heading">Note on User Identifiers on Mac</h4>
<p><small>If you are writing a Mac App, TelemetryDeck can not create a unique user identifier, and will instead default to a concatenation of your OS Version and App Build number, which is not exactly unique, so user counting will be less accurate.</small></p>

<p><small>We therefore strongly recommend to either use a unique identifier for your users, such as an email address, or to generate and store a `UUID().uuidString`, for example in `UserDefaults`, and always pass that to TelemetryDeck as User ID.</small></p>

<p><small>The reason why TelemetryDeck can't do that itself is that it feels like crossing a line if this simple tool would generate IDs itself and write those to a directory on disk. We feel that this is not expected behaviour for a privacy-first analytics package.</small></p>

</div>

## Payload Data

You can also send additional parameters with each signal:

```swift
TelemetryDeck.signal"databaseUpdated", parameters: ["numberOfDatabaseEntries": "3831"])
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
