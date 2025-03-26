---
title: Android Setup Guide
tags:
  - Setup
  - Quickstart
  - Code
  - Kotlin
testedOn: Android Studio Meerkat
featured: true
description: Include the TelemetryDeck SDK in Your Android Application
lead: You have an account, and you have an app ID. Now let's include the TelemetryClient Kotlin Package in your application.
order: 200
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

Sending signals requires access to the internet so the following permission should be added to the app's `AndroidManifest.xml`

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

## Verify Your Setup

Build and run your app to verify that TelemetryDeck is properly integrated. The SDK automatically tracks user activity when the app starts or returns from the background.

{% notewarning "Test Mode for Development Signals" %}
If you're running the app from your IDE or development environment, signals will be tagged as **Test Signals**. You'll see them show up in the TelemetryDeck Dashboard when the **Test Mode** toggle under the tab bar is turned on.
{% endnotewarning %}

Open the TelemetryDeck Dashboard, navigate to "Explore > Recent Signals" and make sure "Test Mode" is enabled. You should see automatic signals appear after launching your app.

---

{% noteinfo "Ready for Basic Insights" %}
Congratulations! With just the SDK integration you've completed, TelemetryDeck will automatically track user sessions, app launches, and device information. This basic setup provides valuable built-in insights without any additional code.

You can now build and release your app. Once users start using it, your TelemetryDeck dashboard will begin showing data about user behavior, device types, and other key metrics.
{% endnoteinfo %}

## Privacy Policy and Opt-Out

You don't need to update your privacy policy, [but we recommend you do it anyway](/docs/guides/privacy-faq/#do-i-need-to-add-telemetrydeck-to-my-privacy-policy%3F).

## Enhancing Your Analytics (Optional)

While basic session tracking provides valuable information, sending custom signals lets you answer questions specific to how users engage with *your* app.

### Sending Custom Signals

Navigate to a Kotlin file and add the following code at the top:

```kotlin
import com.telemetrydeck.sdk.TelemetryDeck
```

Then, in an appropriate function, you can send your first custom signal:

```kotlin
TelemetryDeck.signal("pizzaOrderConfirmed")
```

By default, you're not sending signals immediately; you're _enqueing_ them. This batches them up to be sent every now and then, and is the recommended way to send signals, as it will conserve a lot of battery life for your users.

You can also add a user identifier and parameters to your signals:

```kotlin
TelemetryDeck.signal("pizzaOrderConfirmed", myUser.emailAddress, mapOf("pizzaType" to "hawaii"))
```

{% noteinfo "About Signal Data" %}
A user identifier is any string that uniquely identifies a user of your application. We will _hash_ this string before sending it to the server, and there we'll salt+hash it again for privacy protection.

The payload is a map of parameters to be sent with the signal. We'll automatically send information about the user's device, system version, and app version with each signal, but you can add custom parameters either with each call or by using [enrich providers](https://github.com/TelemetryDeck/KotlinSDK#custom-telemetry).
{% endnoteinfo %}

For more advanced configuration options, programmatic usage and information about signals, parameters and all other aspects of the SDK, check out the [README file](https://github.com/TelemetryDeck/KotlinSDK?tab=readme-ov-file#programmatic-usage).

## Troubleshooting

- `Could not find method implementation() for arguments on object of type org.gradle.api.internal.artifacts.dsl.dependencies.DefaultDependencyHandler.` – Make sure you're adding the entries to `android/app/build.gradle`, not `android/build.gradle`. [More Info](https://stackoverflow.com/questions/45615474/gradle-error-could-not-find-method-implementation-for-arguments-com-android)

## SDK Requirements

The TelemetryDeck SDK requires Android SDK 21 or later. For a complete list of requirements, see the [Requirements section](https://github.com/TelemetryDeck/KotlinSDK?tab=readme-ov-file#requirements) of the README.

## What to Do Next

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
