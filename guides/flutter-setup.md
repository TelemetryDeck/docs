---
title: Flutter Setup Guide
tags:
  - Setup
  - Flutter
  - Dart
featured: true
description: How to include the TelemetryDeck SDK in Your Flutter and Dart app
lead: You have an account, and you have an app ID. Now let's include the TelemetryClient Package in your Flutter application
order: 400
---

## Prerequisites

- You'll need a TelemetryDeck account. [Sign up for free](https://dashboard.telemetrydeck.com/register?source=websdk) if you don't have one yet.
- You'll need a TelemetryDeck App ID. [Create a new app](https://dashboard.telemetrydeck.com/apps/create) if you don't have one yet.
- Follow the installing instructions on [pub.dev](https://pub.dev/packages/telemetrydecksdk/install).

## Initializion

Initialize the TelemetryClient like so:

```dart
void main() {
  // ensure the platform channels are available
  WidgetsFlutterBinding.ensureInitialized();
  // configure and start the TelemetryClient
  Telemetrydecksdk.start(TelemetryManagerConfiguration(
      appID: "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX"));
  runApp(const MyApp());
}
```

## Permission for internet access

Sending signals requires access to the internet so the following permission should be added to the app's `AndroidManifest.xml`:

```xml
<uses-permission android:name="android.permission.INTERNET" />
```

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

The Flutter SDK uses the native SDKs for Android and iOS which offer a number of built-in attributes which are submitted with every signal. You can overwrite these attributes by providing a custom value with the same key. For more information on how each value is calcualted, check the corresponding platform library:

- `majorMinorSystemVersion`
- `telemetryClientVersion`
- `isTestFlight` (iOS only)
- `isDebug`
- `architecture`
- `modelName`
- `isAppStore`
- `appVersion`
- `operatingSystem`
- `systemVersion`
- `majorSystemVersion`
- `targetEnvironment`
- `isSimulator` (iOS only)
- `platform` (iOS only)
- `buildNumber` (iOS only)
- `locale`
- `dartVersion`
- `brand` (Android only)

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

A very small subset of our customers will want to use a custom signal ingestion server or a custom proxy server. To do so, you can pass the URL of the custom server to the `TelemetryManagerConfiguration`:

```swift
Telemetrydecksdk.start(TelemetryManagerConfiguration(
  appID: "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX",
  apiBaseURL: "https://nom.telemetrydeck.com"));
```

## Logging output

By default, some logs helpful for monitoring TelemetryDeck are printed out to the console. You can enable additional logs by setting the `debug` field to `true`:

```dart
void main() {
  Telemetrydecksdk.start(TelemetryManagerConfiguration(
      appID: "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX",
      debug: true));
}
```
