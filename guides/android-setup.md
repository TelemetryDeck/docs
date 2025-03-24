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

For more advanced configuration options, programatic usage and information about signals, parameters and all other aspects of the SDK, check out the [README file](https://github.com/TelemetryDeck/KotlinSDK?tab=readme-ov-file#programmatic-usage).

Feel free to browse the [TelemetryDeck SDK's source code](https://github.com/TelemetryDeck/KotlinSDK) as well. It's tiny and you'll see for yourself how TelemetryDeck is hashing user identifiers before they ever reach the server. Privacy, yay!

## You're all set!

By default, the TelemetryDeck SDK will automatically track user activity based on when the app starts, or when it returns from the background. This means, that this is all you need to do to start sending signals to TelemetryDeck.

You can now go to the [Dashboard](https://dashboard.telemetrydeck.com/) and watch your signals pour in, for example in the "Recent Signals" list. Signals produced while working in your IDE will automatically be tagged as **Test Signals** so remember to enable Test Mode in the Dashboard to see your testing data your Insights and charts. Disable Test Mode in the dashboard to see your production data once your app is live.

## Privacy Policy and Opt-Out

You don't need to update your privacy policy, [but we recommend you do it anyway](/docs/guides/privacy-faq/#do-i-need-to-add-telemetrydeck-to-my-privacy-policy%3F).


## Advanced: Sending Signals Manually

Let's send a signal manually. Navigate to a Kotlin file and add the following code at the top:

```kotlin
import com.telemetrydeck.sdk.TelemetryDeck
```

Then, in an appropriate function, you can send your manual first signal.

By default, you're not sending signals immediately; you're _enqueing_ them. This batches them up to be sent every now and then, and is the recommended way to send signals, as it will conserve a lot of battery life for your users. To enqueue a signal to be sent by TelemetryDeck use this line:

```kotlin
TelemetryDeck.signal("pizzaOrderConfirmed")
```

Of course you can replace `somethingSpecificHappened` by any other name you'd like.

## Advanced: Sending Signals with Parameters, and enriching signals

The `signal` function takes an optional parameter for the **user** of your application, and any additional **payload** you want to send.

```kotlin
TelemetryDeck.signal("pizzaOrderConfirmed", myUser.emailAddress, mapOf("pizzaType" to "hawaii"))
```

A user identifier is any string that uniquely identifies a user of your application. For example, you might use the user's email address, or the user's Facebook ID. We will _hash_ this string before we send it to the server, and there we'll salt+hash it again, so that it's impossible to guess the user's identifier but still making it possible to count and recognize users. You can read more about how we manage user identifiers [here](https://github.com/TelemetryDeck/KotlinSDK?tab=readme-ov-file#user-identifiers).

The payload is a map of parameters to be sent with the signal, and can be any key-value pair. We'll automatically send information about the user's device, the system version, and the app's version with each signal, but you can add to that list of parameters either with each call to `enqueue` or by using [enrich providers](https://github.com/TelemetryDeck/KotlinSDK#custom-telemetry).

---

## Troubleshooting

- `Could not find method implementation() for arguments on object of type org.gradle.api.internal.artifacts.dsl.dependencies.DefaultDependencyHandler.` – Make sure you're adding the entries to `android/app/build.gradle`, not `android/build.gradle`. [More Info](https://stackoverflow.com/questions/45615474/gradle-error-could-not-find-method-implementation-for-arguments-com-android)
---

## Requirements:

The TelemetryDeck SDK requires Android SDK 21 or later. For a complete list of requirements, see the [Requirements section](https://github.com/TelemetryDeck/KotlinSDK?tab=readme-ov-file#requirements) of the README.
