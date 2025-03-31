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

## Verify your setup

Build and run your app to verify that TelemetryDeck is properly integrated. The SDK automatically begins collecting data when initialized.

{% notewarning "Test Mode for Development Signals" %}
If your app's build configuration is set to "Debug", all signals sent will be marked as testing signals. You'll see them show up in the TelemetryDeck Dashboard when the **Test Mode** toggle under the tab bar is turned on. Remember to disable Test Mode in the dashboard to see your production data once your app is live.
{% endnotewarning %}

Open the TelemetryDeck Dashboard, navigate to "Explore > Recent Signals" and make sure "Test Mode" is enabled. You should see automatic signals appear after launching your app.

---

{% noteinfo "Ready for Basic Insights" %}
Congratulations! With just the SDK integration you've completed, TelemetryDeck will automatically track user sessions, app launches, and device information. This basic setup provides valuable built-in insights without any additional code.

You can now build and release your app. Once users start using it, your TelemetryDeck dashboard will begin showing data about user behavior, device types, and other key metrics.
{% endnoteinfo %}

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
Telemetrydecksdk.start(TelemetryManagerConfiguration(
  appID: "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX",
  testMode: true));
```

#### Logging output

Enable additional logs by setting the `debug` field to `true`:

```dart
void main() {
  Telemetrydecksdk.start(TelemetryManagerConfiguration(
      appID: "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX",
      debug: true));
}
```

#### Custom server

A tiny subset of our customers will want to use a custom signal ingestion server or a custom proxy server. To do so, you can pass the URL of the custom server to the `TelemetryManagerConfiguration`:

```dart
Telemetrydecksdk.start(TelemetryManagerConfiguration(
  appID: "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX",
  apiBaseURL: "https://nom.telemetrydeck.com"));
```

For more advanced configuration options, programmatic usage and information about signals, parameters and all other aspects of the SDK, check out the [README file](https://github.com/TelemetryDeck/FlutterSDK?tab=readme-ov-file#sending-signals).

## App Store requirements

When publishing your Flutter app, you'll need to address privacy requirements:

- **iOS Apps**: Disclose analytics usage in Apple's App Store Connect privacy details. TelemetryDeck is privacy-focused, but disclosure is still required.
- **All Platforms**: Consider updating your privacy policy to mention analytics collection.

For guidance, see our [Apple App Privacy guide](/docs/articles/apple-app-privacy/) and [Privacy FAQ](/docs/guides/privacy-faq/#do-i-need-to-add-telemetrydeck-to-my-privacy-policy%3F).

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
