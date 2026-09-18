---
icon: fontawesome/brands/flutter
title: Flutter Setup Guide
tags:
  - setup
  - flutter
  - dart
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

## Verify your setup

Build and run your app to verify that TelemetryDeck is properly integrated. The SDK automatically begins collecting data when initialized.

!!! warning "When running from your IDE, you're sending test signals"

     If your app is configured with a debug build type (i.e. the default build variant running from Android Studio), 
    your signals will be tagged as **Test Signals**, meaning that you can easily filter them out later. 
    You'll see them show up in the TelemetryDeck Dashboard when [**Test Mode**](../articles/test-mode.md) is turned on.

Open the TelemetryDeck Dashboard, navigate to **Explore -> Recent Signals** and make sure [Test Mode](../articles/test-mode.md) is enabled. 
You should see automatic signals appear after launching your app.

Congratulations! With just the SDK integration you've completed, TelemetryDeck will automatically track 
user sessions, app launches, and device information. This basic setup provides valuable built-in insights without any additional code. 
You can now build and release your app. Once users start using it, your TelemetryDeck dashboard will begin showing data about user behavior, device types, and other key metrics.

## Enhancing your analytics (optional)

While basic session tracking provides valuable information, sending custom events lets you answer questions specific to how users engage with *your* app.

### Sending custom events

Send a simple event using the following method:

```dart
Telemetrydecksdk.send("signal_type")
```

You can append any number of custom attributes to a signal:

```dart
Telemetrydecksdk.send("signal_type",
  additionalPayload: {"attributeName": "value"});
}
```

To temporarily stop sending signals (for example, if a user opts out):

```dart
Telemetrydecksdk.stop()
```

In order to restart sending events, you will need to call the `start` method again.

### Additional configuration options

#### Manual Test Mode control

If you want to manually control whether test mode is active, you can set the `testMode` field:

```dart
Telemetrydecksdk.start(
  const TelemetryManagerConfiguration(
    appID: "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX",
    testMode: true
  ),
);
```

#### Logging output

Enable additional logs by setting the `debug` field to `true`:

```dart
void main() {
  Telemetrydecksdk.start(
    const TelemetryManagerConfiguration(
      appID: "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX",
      debug: true
    ),
  );
}
```

#### Custom server

A tiny subset of our customers will want to use a custom signal ingestion server or a custom proxy server. To do so, you can pass the URL of the custom server to the `TelemetryManagerConfiguration`:

```dart
Telemetrydecksdk.start(
  const TelemetryManagerConfiguration(
    appID: "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX",
    apiBaseURL: "https://nom.telemetrydeck.com",
  ),
);
```

For more advanced configuration options, programmatic usage and information about signals, parameters and all other aspects of the SDK, check out the [README file](https://github.com/TelemetryDeck/FlutterSDK?tab=readme-ov-file#sending-signals).

## App Store requirements

When publishing your Flutter app, you'll need to address privacy requirements:

- **iOS Apps**: Disclose analytics usage in Apple's App Store Connect privacy details. TelemetryDeck is privacy-focused, but disclosure is still required.
- **All Platforms**: Consider updating your privacy policy to mention analytics collection.

For guidance, see our [Apple App Privacy guide](/docs/articles/apple-app-privacy/) and [Privacy FAQ](/docs/guides/privacy-faq/#do-i-need-to-add-telemetrydeck-to-my-privacy-policy%3F).

## What to do next

Now that you've integrated TelemetryDeck, learn how to use the analytics platform to gain valuable insights about your users:

<div class="grid cards" markdown>

-   **📊 Analytics Walkthrough**

    Learn how to navigate TelemetryDeck, interpret insights, and use analytics to make data-driven decisions that improve your app and grow your user base.

    [:fontawesome-solid-right-long: Start here to get real value from your analytics](../basics/index.md)
</div>
