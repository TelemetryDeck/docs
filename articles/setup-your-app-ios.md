---
title: Setting Up Your Swift Application
tags: Docs, Setup, Quickstart, Code
testedOn: Xcode 12.2 & Swift 5.3
description: How to configure TelemetryClient in Your Application
lead: You have an account, and you have an app ID. Now let's include the TelemetryClient Swift Package in your application.
---

## Get TelemetryClient

This concludes the preparation. Let's add TelemetryDeck to your app! Open Xcode and navigate to the project you want to add TelemetryDeck to.

<img class="img img-fluid" alt="A screenshot of Xcode adding TelemetryDeck SwiftClient" src="/images/addswiftclientstep1.png">

In the menu, select <kbd>File</kbd> -> <kbd>Add Packages...</kbd>. This will open the Swift Package Manager view. Add the following as package repository and click <kbd>Next</kbd>:

```swift
https://github.com/TelemetryDeck/SwiftClient
```

There will be one or two additional screens, but you can just click <kbd>Next</kbd> and <kbd>Finish</kbd> on them – Xcode will do the right thing by linking the package against your target. (In the unlikely case that you have multiple targets, link them each with the package's library.)

This will include the TelemetryDeck Swift Client into your app by downloading the source code. Feel free to browse the client's source code, it's very tiny and you'll see for yourself how TelemetryDeck is hashing user identifiers before they ever reach the server. Privacy, yay!

## Coding Time!

The `TelemetryClient` package will provide you with a class `TelemetryManager` that you'll use for all interactions with TelemetryDeck. Before you can use that class, you'll need to initialize it at the start of your app. I strongly recommend doing so as soon as possible, as you won't be able to send Signals before the `TelemetryManager` is initialized.

This is slightly different depending on whether you use SwiftUI or UIKit's `AppDelegate` to manage your app's lifecycle, so let's look at these individually. Please select the one that applies:

<p>
<a href="/pages/setting-up-your-application-in-swiftui.html" class="btn btn-secondary btn-large">I use SwiftUI and SceneKit &rarr;</a>
</p>
<p>
<a href="/pages/setting-up-your-application-using-appdelegate.html" class="btn btn-secondary btn-large">I use an AppDelegate &rarr;</a>
</p>
