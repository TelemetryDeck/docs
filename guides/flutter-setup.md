---
title: Flutter Setup Guide
tags:
  - Setup
  - Flutter
  - Dart
featured: true
description: How to include the TelemetryDeck SDK in Your Flutter and Dart app
lead: You have an account, and you have an app ID. Now let's include the TelemetryClient Package in your Flutter application
order: 225
---

## Prerequisites

<!-- vale proselint.Cliches = NO -->

- You'll need a TelemetryDeck account. [Sign up for free](https://dashboard.telemetrydeck.com/register?source=fluttersdk) if you don't have one yet.
- You'll need a TelemetryDeck App ID. [Create a new app](https://dashboard.telemetrydeck.com/apps/create) if you don't have one yet.
- Follow the installing instructions on [pub.dev](https://pub.dev/packages/telemetrydecksdk/install).
<!-- vale proselint.Cliches = YES -->

## Initialization

Initialize the TelemetryClient like so:

```dart
void main() {
  // ensure the platform channels are available
  WidgetsFlutterBinding.ensureInitialized();
  // configure and start the client
  Telemetrydecksdk.start(
    const TelemetryManagerConfiguration(
      appID: "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX",
    ),
  );

  runApp(const MyApp());
}
```

## Permission for internet access

Sending signals requires access to the internet so the following permissions should be granted. You can also take this from [Flutter's Cross-platform HTTP networking guide](https://docs.flutter.dev/data-and-backend/networking).

### Android

Change the app's `AndroidManifest.xml` to include:

```xml
<uses-permission android:name="android.permission.INTERNET" />
```

### macOS

Set the `com.apple.security.network.client` entitlement to `true` in the `macos/Runner/DebugProfile.entitlements` and `macos/Runner/Release.entitlements` files. You can also do this in Xcode by selecting the `macos` target, then the `Signing & Capabilities` tab, and checking `Outgoing connections (Client)` for both the Release and Debug targets of your app.


## Sending signals

Send a signal using the following method:

```dart
Telemetrydecksdk.send("signal_type")
```

## Signals with additional attributes

Append any number of custom attributes to a signal:

```dart
Telemetrydecksdk.send("signal_type",
  additionalPayload: {"attributeName": "value"});
}
```

## Stop sending signals

Prevent signals from being sent using the stop method:

```dart
Telemetrydecksdk.stop()
```

In order to restart sending events, you will need to call the `start` method again.

## Test mode

If your app's build configuration is set to "Debug", all signals sent will be marked as testing signals. In the Telemetry Viewer app, activate **Test Mode** to see those.

If you want to manually control whether test mode is active, you can set the `testMode` field:

```swift
Telemetrydecksdk.start(TelemetryManagerConfiguration(
  appID: "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX",
  testMode: true));
```

## Custom Server

A tiny subset of our customers will want to use a custom signal ingestion server or a custom proxy server. To do so, you can pass the URL of the custom server to the `TelemetryManagerConfiguration`:

```swift
Telemetrydecksdk.start(TelemetryManagerConfiguration(
  appID: "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX",
  apiBaseURL: "https://nom.telemetrydeck.com"));
```

## Logging output

By default, some logs helpful for monitoring TelemetryDeck are printed out to the native console of each platform. You can enable additional logs by setting the `debug` field to `true`:

```dart
void main() {
  Telemetrydecksdk.start(TelemetryManagerConfiguration(
      appID: "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX",
      debug: true));
}
```

For more advanced configuration options, programmatic usage and information about signals, parameters and all other aspects of the SDK, check out the [README file](https://github.com/TelemetryDeck/FlutterSDK?tab=readme-ov-file#sending-signals).
