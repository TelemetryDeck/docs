---
title: Android Setup Guide
tags:
  - Setup
  - Quickstart
  - Code
  - Kotlin
testedOn: Android Studio Electric Eel | 2022.1.1 Patch 2
featured: true
description: Include the TelemetryDeck SDK in Your Android Application
lead: You have an account, and you have an app ID. Now let's include the TelemetryClient Kotlin Package in your application.
order: 200
---

## Include the SDK

Let's add the TelemetryDeck SDK to your app! Open Android Studio and open the project you want to add TelemetryDeck to. Then open the project's `settings.gradle` file.

The TelemetryDeck is distributed using [jitpack](https://jitpack.io/), so you'll need to add the jitpack dependency to your `settings.gradle` file:

```python
dependencyResolutionManagement {
    repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)
    repositories {
        google()
        mavenCentral()
        maven { url 'https://jitpack.io' } // <-- add this line
    }
}
```

After that is done, add the following to your `build.gradle` file, under `dependencies`:

```python
dependencies {
    // ...
    // Please replace 1.1.0 with the latest version of the SDK
    implementation 'com.github.TelemetryDeck:KotlinSDK:1.1.0'
}
```

## Permission for internet access

Sending signals requires access to the internet so the following permission should be added to the app's `AndroidManifest.xml`

```xml
<uses-permission android:name="android.permission.INTERNET" />
```

## Store your TelemetryDeck App ID

The TelemetryManager can be initialized automatically by adding the application key to the `application` section of the app's `AndroidManifest.xml`:

```xml
<application>

    <meta-data android:name="com.telemetrydeck.sdk.appID" android:value="XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX" />
</application>
```

And that's it! Your app is now ready to use TelemetryDeck. Hit the build button to check if everything is working – if not, check out the troubleshooting section below.

Feel free to browse the [TelemetryDeck SDK's source code](https://github.com/TelemetryDeck/KotlinSDK), it's tiny and you'll see for yourself how TelemetryDeck is hashing user identifiers before they ever reach the server. Privacy, yay!

The [README file](https://github.com/TelemetryDeck/KotlinSDK/blob/main/README.md) also goes into more detail regarding the default configuration of TelemetryDeck, and how to customize it.

## You're all set!

By default, the TelemetryDeck SDK will automatically send signals when the app starts, or when it returns from the background. This means, that this is all you need to do to start sending signals to TelemetryDeck.

After launching the app once, you can now go to the [Dashboard](https://dashboard.telemetrydeck.com/) and watch your signals pour in, for example in the "Recent Signals" list. Signals produced while working in your IDE will automatically be tagged as **Test Signals** so remember to enable Test Mode in the Dashboard to see your testing data your Insights and charts. Disable Test Mode in the dashboard to see your production data once your app is live.

---

## Advanced: Sending Signals Manually

Let's send a signal manually. Navigate to a Kotlin file and add the following code at the top:

```kotlin
import com.telemetrydeck.sdk.TelemetryManager
```

Then, in an appropriate function, you can send your manual first signal.

By default, you're not sending signals immediately; you're _enqueing_ them. This batches them up to be sent every now and then, and is the recommended way to send signals, as it will conserve a lot of battery life for your users. To enqueue a signal to be sent by TelemetryManager use this line:

```kotlin
TelemetryManager.queue("pizzaOrderConfirmed")
```

Of course you can replace `somethingSpecificHappened` by any other name you'd like.

## Advanced: Sending Signals with Parameters, and enriching signals

The `queue` function takes an optional parameter for the **user** of your application, and any additional **payload** you want to send.

```kotlin
TelemetryManager.queue("pizzaOrderConfirmed", myUser.emailAddress, mapOf("pizzaType" to "hawaii"))
```

A user identifier is any string that uniquely identifies a user of your application. For example, you might use the user's email address, or the user's Facebook ID. We will _hash_ this string before we send it to the server, and there we'll salt+hash it again, so that it's impossible to guess the user's identifier but still making it possible to count and recognize users.

The payload is a map of parameters to be sent with the signal, and can be any key-value pair. We'll automatically send information about the user's device, the system version, and the app's version with each signal, but you can add to that list of parameters either with each call to `enqueue` or by using [enrich providers](https://github.com/TelemetryDeck/KotlinSDK#custom-telemetry).

---

## Troubleshooting

- `Could not find method implementation() for arguments on object of type org.gradle.api.internal.artifacts.dsl.dependencies.DefaultDependencyHandler.` – Make sure you're adding the entries to `android/app/build.gradle`, not `android/build.gradle`. [More Info](https://stackoverflow.com/questions/45615474/gradle-error-could-not-find-method-implementation-for-arguments-com-android)
- `Manifest merger failed : uses-sdk:minSdkVersion 21 cannot be smaller than version 24`: Your minimum SDK version must be at least 24. You can change this in `android/app/build.gradle`.

---

## Requirements:

- SDK 21 or later
- Kotlin 1.6.10 or later
- Java Compatibility Version 1.8


