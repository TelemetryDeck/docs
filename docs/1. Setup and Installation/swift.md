# Swift (iOS and macOS Apps)

!!! info inline end

    This was tested on Xcode 12.2 & Swift 5.3

## Including the Package

Let's add TelemetryDeck to your app! Open Xcode and navigate to the project you want to add TelemetryDeck to.

In the menu, select <kbd>File</kbd> -> <kbd>Add Packages...</kbd>. This will open the Swift Package Manager view. Add the following as package repository and click <kbd>Next</kbd>: 

```swift
https://github.com/TelemetryDeck/SwiftClient
```

There will be one or two additional screens, but you can just click <kbd>Next</kbd> and <kbd>Finish</kbd> on them – Xcode will do the right thing of linking the package against your target. (In the unlikely case that you have multiple targets, link them each with the package's library.)

This will include the TelemetryDeck Swift Client into your app by downloading the source code. Feel free to browse the client's source code, it's very tiny and you'll see for yourself how TelemetryDeck is hashing user identifers before they ever reach the server. Privacy, yay! 

## Coding Time!

The `TelemetryClient` package will provide you with a class `TelemetryManager` that you'll use for all interaction with TelemetryDeck. Before you can use that class, you'll need to initialize it at the start of your app. I strongly recommend doing so as soon as possible, as you won't be able to send Signals before the `TelemetryManager` is initialized.

This is slightly different depending on wether you use SwiftUI or UIKit's `AppDelegate` to manage your app's lifecycle, so let's look at these individually. In the next few code examples, please select the one that applies.


!!! info

    If you're unsure wether you're using SceneKit or AppDelegate, here's a way to distinguish them:

    - **SceneKit**: You should have a file in your project called `YourAppName.swift` that contains a `@main` struct or function. Apps created in the last few years will generally be SceneKit.
    - **AppDelegate**: You should have a file in your project called `AppDelegate.swift` that contains an `AppDelegate` class

    If you're still unsure, look at both code examples and see which one is more familiar.

## Configuring Telemetry Manager at App Launch

Find the method that calls when your app launches and import the TelemetryClient package and configure the TelemetryManager using the Unique Identifier of your app. 

You can find the unique identifier of your app in the Telemetry Viewer app: If you haven't already, create a new app, then navigate to <kbd>Edit App</kbd> and copy the identifier from there.

=== "SceneKit"
    Import the TelemetryClient Package by adding `import TelemetryClient`. Then add an `init()` method to your App struct that creates a `TelemetryManagerConfiguration` instance and hands it to the `TelemetryManager`, using the **Unique Identifier of your app** that you can get from the Telemetry Viewer app.

    Your code should now look like this:

    ```swift
    import SwiftUI
    import TelemetryClient

    @main
    struct Example_AppApp: App {
        var body: some Scene {
            WindowGroup {
                ContentView()
            }
        }
        
        init() {
            let configuration = TelemetryManagerConfiguration(
                appID: "YOUR-APP-UNIQUE-IDENTIFIER")
            TelemetryManager.initialize(with: configuration)
        }
    }
    ```

    If you already have an `init()` method, add this to its end.

=== "AppDelegate"

    If you use `AppDelegate` to manage your app's life cycle, open the file `AppDelegate.swift` and look for and modify the method `application(:didFinishLaunchingWithOptions:)`. Import the TelemetryClient Package by adding `import TelemetryClient`.

    ```swift
    import UIKit
    import TelemetryClient

    @main
    class AppDelegate: UIResponder, UIApplicationDelegate {
        func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
            
            let configuration = TelemetryManagerConfiguration(
                appID: "YOUR-APP-UNIQUE-IDENTIFIER")
            TelemetryManager.initialize(with: configuration)

            return true
        }
        // ...
    }
    ```

    By default, Xcode even adds a comment here to tell you where to add stuff that should happen right after launch. 

You are now ready to send signals. Read the next article, [Sending Signals](../2. Sending Signals/TelemetryManager.md)