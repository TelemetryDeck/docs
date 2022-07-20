---
title: Sending Signals
featured: true
tags:
  - Setup
  - Quickstart
  - Code
TestedOn: Xcode 12.2 & Swift 5.3
description: How to quickly get up and running with TelemetryDeck.
lead: This document should get you up and running with TelemetryDeck as quickly as possible!
order: 4000
date: git Last Modified
---

Let's send a signal to show the app has launched correctly. To do that, first, what is a signal?

Signals are an indication that **an event** happened in your app, which is used by a **user**. Signals consist of these parts:

- **Signal Type** – A string that indicates which kind of event happened.<br>In this case we'll use `applicationDidFinishLaunching`, but it can be `databaseUpdated` or `settingsScreenOpened` or `pizzaModeActivated` (I totally love that last one!)
- **User Identifer** – A string that identifies your user.<br>This can be an email address or a username, or a random ID that you generate once and store somewhere. It should always be the same for all the signals you send from a certain instance of the app. If you don't supply a user identifier, `TelemetryManager` will generate one for you.
- **A Metadata Payload** – Metadata is a dictionary `[String: String]` of additional data about your app that might be interesting to analyze.<br>`TelemetryManager` will always add the user's OS Version, Platform, Build Number and App Version to the metadata, but you can specify additional info like, `numberOfEntriesInDatabase` (an int cast to string) or `pizzaModeAnchoviesEnabled` (a boolean cast to string).

See the [Signals Reference?](signal-reference.html) for more information about how you can effectively use Signals.

Side note: If you app is built in `DEBUG` configuration (i.e. running from Xcode), your signals will be tagged as **Testing Signals**, meaning that you can easily filter them out later. You'll see them show up in the TelemetryDeck Viewer when it is set to **Test Mode**.

See the [TelemetryDeck SDK's `README.md` file](https://github.com/TelemetryDeck/SwiftClient/blob/main/README.md) for more information on how to send signals. For now, let's just send one signal that tells us the app has launched. Go to the place where you just added the initialization, and directly below add this line:

```swift
let configuration = TelemetryManagerConfiguration(appID: "YOUR-APP-UNIQUE-IDENTIFIER")
TelemetryManager.initialize(with: configuration)

TelemetryManager.send("applicationDidFinishLaunching")
```

Aaaand done. This is all you need to send a signal. You do not need to keep an instance of TelemetryManager and hand it around, just call the `send` function on the class directly. If you want to add a custom user identifer or metadata payload, add them to the function call like this:

```swift
TelemetryManager.send(
    "applicationDidFinishLaunching",
    for: "my very cool user",
    with: [
        "numberOfTimesPizzaModeHasActivated": "\(dataStore.pizzaMode.count)",
        "pizzaCheeseMode": "\(dataStore.pizzaCheeseMode)"
    ])
```

And you're done! You are now sending signals to the TelemetryDeck server.

## Weee! We made it!

You can now send signals! Don't overdo it in the beginning. It's okay if you only send **one** signal, named `applicationDidFinishLaunching` in the beginning. This will already give you number of users, number of launches, retention... a lot!

After a while, you can add a send call for each screen in your app, so you can see which screens are used most. I also recommend adding all your custom settings to your metadata each time (except the ones that might identify an individual user of course). This way you can see which settings most of your users use.

<a href="/pages/insights-reference.html" class="btn btn-secondary btn-large">Read More about Insights in the Insights Reference Document &rarr;</a>
