---
title: Navigation Signals
tags: setup
description: TelemetryDeck tracks how users navigate through your app when you send navigation signals.
lead: TelemetryDeck tracks how users navigate through your app when you send navigation signals. Here's the format and convenience methods.
testedOn: SwiftSDK 3.0.0, WebSDK 1.0.0
---

!!! note "Web Analytics already tracks navigation"

    If you're using TelemetryDeck's Web SDK, navigation is tracked automatically. This guide is for native app SDKs.

## Format

A navigation signal has the type `TelemetryDeck.Navigation.pathChanged` with these parameters:

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

| Key | Description |
|---|---|
| `TelemetryDeck.Navigation.schemaVersion` | Always `"1"`. |
| `TelemetryDeck.Navigation.identifier` | `<source> -> <destination>`. Used to build directed navigation graphs. |
| `TelemetryDeck.Navigation.sourcePath` | Where the user came from. |
| `TelemetryDeck.Navigation.destinationPath` | Where the user went. |

## Navigation paths

Navigation paths are `.`-delimited strings in apps and `/`-delimited in websites. Leading and trailing delimiters are ignored. Use the empty string `""` for navigation from outside the app.

Examples:

- `index`
- `settings.user.changePassword`
- `/blog/ios-market-share`

## Convenience methods

### With source and destination

```swift
await TelemetryDeck.navigationPathChanged(from: "home", to: "settings")
```

### Destination only

```swift
await TelemetryDeck.navigationPathChanged(to: "settings")
```

This uses the previous destination as the source. Be careful — if you don't call it from every screen, the navigation graph will show paths the user didn't take.

### SwiftUI view modifier

```swift
struct SettingsView: View {
    var body: some View {
        Form {
            NavigationLink("Account") {
                AccountSettingsView()
                    .trackNavigation(path: "settings.account")
            }
        }
        .trackNavigation(path: "settings")
    }
}
```

The `.trackNavigation(path:)` modifier calls `navigationPathChanged(to:)` when the view appears. Apply it consistently to all navigation destinations to get accurate graphs.
