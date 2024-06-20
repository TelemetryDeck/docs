---
title: Navigation Route Signals
tags: setup
description: TelemetryDeck can track how users navigate through your app when you send route signals. Here's how these need to look like.
lead: TelemetryDeck can track how users navigate through your app when you send route signals. Here's how these need to look like.
testedOn: SwiftSDK 2.2.0, WebSDK 1.0.0
---

{% notewarning "Upcoming Feature" %}

This feature is still in development and will take a while to be available in all SDKs and the Dashboard UI. We encourage you to start sending Route signals now so you'll have data to play around with once we launch the feature fully.
{% endnotewarning %}

{% noteinfo "Web Analytics already tracks navigation" %}

If you're using TelemetryDeck's Web SDK to track your website, you don't need to send route signals. The Web SDK already tracks navigation automatically.
{% endnoteinfo %}

## Format

A route signal is a regular TelemetryDeck signal of type `TelemetryDeck.Route.Transition.navigation`. It has parameters for version number, source and destination paths, and a route identifier, which is the source path and destination path concatenated with `->`. Using this identifier, we can track how users navigate through your app.

```json
{
  "appID": "<AAAA-BBBBBBBB-CCCC-DDDD>",
  "clientUser": "<myClientUserHash>",
  "type": "TelemetryDeck.Navigation.pathChanged",
  "payload": {
    "TelemetryDeck.Navigation.schemaVersion": "1",
    "TelemetryDeck.Navigation.identifier": "<source> -> <destination>",
    "TelemetryDeck.Navigation.sourcePath": "<source>",
    "TelemetryDeck.Navigation.destinationPath": "<destination>"
  }
}
```

Values in angle brackets (`< >`) are placeholders and should be replaced with actual values.

The signal type should always be `TelemetryDeck.Route.Transition.navigation` for route signals.

Here's what each parameter should contain:

| Key                                        | Description                                                                                                                                                                                   |
| ------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `TelemetryDeck.Navigation.schemaVersion`   | The version of the schema. Should always be `"1"`. We'll use this to account for if we ever need to update this schema.                                                                       |
| `TelemetryDeck.Navigation.identifier`      | The source navigation path, followed by `->`, followed by the destination navigation path. This is the most important part of the navigation schema, we'll use this to build directed graphs. |
| `TelemetryDeck.Navigation.sourcePath`      | A navigation path that describes the source of the navigation.                                                                                                                                |
| `TelemetryDeck.Navigation.destinationPath` | A navigation that describes the destination of the navigation.                                                                                                                                |

## Navigation Paths

Navigation Paths are strings that describe a location or view in your application or website. They must be
delineated by either `.` or `/` characters. Delineation characters at the beginning and end of the string are
ignored. Use the empty string `""` for navigation from outside the app.

Examples:

- `index`
- `settings.user.changePassword`
- `/blog/ios-market-share`

## Automatic Navigation Tracking

Since TelemetryDeck navigation signals are slightly cumbersome to create manually, we're aiming to provide convenience methods for our SDKs that will automatically track navigation signals for you. These methods will be in one of two flavors, either a method that you call with a source and destination, or a method that you call with just a destination.

### `TelemetryDeck.navigate(from: <source>, to <destination>)`

Calling this method will automatically create a navigation signal with the given source and destination.

### `TelemetryDeck.navigate(to: <destination>)`

Calling this method with just a destination will use the previously last used source as the source for the navigation signal.

This is very convenient, but might produce incorrect graphs if you don't call it from every screen in your app.
Suppose you have 3 tabs "Home", "User" and "Settings", but only set up navigation in "Home" and "Settings". If
a user taps "Home", "User" and "Settings" in that order, that'll produce an incorrect navigation signal with
source "Home" and destination "Settings", a path that the user did not take.
