---
icon: fontawesome/brands/android
title: Android Setup Guide
tags:
  - setup
  - quickstart
  - code
  - kotlin
---

## Include the SDK

The Kotlin SDK for TelemetryDeck is available from Maven Central at the following coordinates:

```kotlin
// `app/build.gradle.kts`
dependencies {
    implementation("com.telemetrydeck:kotlin-sdk:6.0.1")
}
```

## Permission for internet access

Sending events requires access to the internet so the following permission should be added to the app's `AndroidManifest.xml`

```xml
<uses-permission android:name="android.permission.INTERNET" />
```

## Your TelemetryDeck App ID

A quick way to start is by adding your App ID to the `application` section of the app's `AndroidManifest.xml`:

```xml
<application>
    ...

    <meta-data android:name="com.telemetrydeck.appID"
        android:value="XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX" />

</application>
```

And that's it! Your app is now ready to use TelemetryDeck. Hit the build button to check if everything is working – if not, check out the troubleshooting section below.

Feel free to browse the [TelemetryDeck SDK's source code](https://github.com/TelemetryDeck/KotlinSDK) as well. It's tiny and you'll see for yourself how TelemetryDeck is hashing user identifiers before they ever reach the server. Privacy, yay!

## Verify your setup

Build and run your app to verify that TelemetryDeck is properly integrated. The SDK automatically tracks user activity when the app starts or returns from the background.

!!! warning "When running from Android Studio, you're sending test signals"

    If your app is configured with a debug build type (i.e. the default build variant running from Android Studio), 
    your signals will be tagged as **Test Signals**, meaning that you can easily filter them out later. 
    You'll see them show up in the TelemetryDeck Dashboard when [**Test Mode**](../../articles/test-mode.md) is turned on.

Open the TelemetryDeck Dashboard, navigate to **Explore -> Recent Signals** and make sure [Test Mode](../../articles/test-mode.md) is enabled. 
You should see automatic signals appear after launching your app.

Congratulations! With just the SDK integration you've completed, TelemetryDeck will automatically track 
user sessions, app launches, and device information. This basic setup provides valuable built-in insights without any additional code. 
You can now build and release your app. Once users start using it, your TelemetryDeck dashboard will begin showing data about user behavior, device types, and other key metrics.

---

## Privacy Policy

You don't need to update your privacy policy, [but we recommend you do it anyway](../../guides/privacy-faq).

## Enhancing your analytics (optional)

While basic session tracking provides valuable information, sending custom events lets you answer questions specific to how users engage with *your* app.

### Sending custom events

Navigate to a Kotlin file and add the following code at the top:

```kotlin
import com.telemetrydeck.sdk.TelemetryDeck
```

Then, in an appropriate function, you can send your first custom event:

```kotlin
TelemetryDeck.signal("pizzaOrderConfirmed")
```

You can also add a user identifier and parameters to your events:

```kotlin
TelemetryDeck.signal("pizzaOrderConfirmed", myUser.emailAddress, mapOf("pizzaType" to "hawaii"))
```

!!! info "About Signal Data"

    A user identifier is any string that uniquely identifies a user of your application. 
    We will _hash_ this string before sending it to the server, and there we'll salt+hash it again for privacy protection.
    The payload is a map of parameters to be sent with the signal. We'll automatically send information 
    about the user's device, system version, and app version with each signal, but you can add custom parameters 
    either with each call or by using [enrich providers](https://github.com/TelemetryDeck/KotlinSDK#custom-telemetry).

For more advanced configuration options, programmatic usage and information about signals, parameters and all other aspects of the SDK, check out the [README file](https://github.com/TelemetryDeck/KotlinSDK?tab=readme-ov-file#programmatic-usage).

## Troubleshooting

- `Could not find method implementation() for arguments on object of type org.gradle.api.internal.artifacts.dsl.dependencies.DefaultDependencyHandler.` – Make sure you're adding the entries to `android/app/build.gradle`, not `android/build.gradle`. [More Info](https://stackoverflow.com/questions/45615474/gradle-error-could-not-find-method-implementation-for-arguments-com-android)

## SDK requirements

The TelemetryDeck SDK requires Android SDK 21 or later. For a complete list of requirements, see the [Requirements section](https://github.com/TelemetryDeck/KotlinSDK?tab=readme-ov-file#requirements) of the README.

## What to do next

Now that you've integrated TelemetryDeck, learn how to use the analytics platform to gain valuable insights about your users:

<div class="grid cards" markdown>

-   **📊 Analytics Walkthrough**

    Learn how to navigate TelemetryDeck, interpret insights, and use analytics to make data-driven decisions that improve your app and grow your user base.

    [:fontawesome-solid-right-long: Start here to get real value from your analytics](../../basics/index.md)
</div>
