---
title: Migrating the TelemetryDeck SDK to Swift 6
description: What we've learned while migrating our code to the new world of data-race safety in Swift 6 mode.
lead: We like to be good citizens in the Swift community and therefore followed Apple's call for migrating any 3rd-party SDKs to Swift 6 language mode. This way, when our customers decide to make the switch, our SDK is ready and provides full data-race safety enforced by the Swift compiler.
searchEngineTitle: Migrating the TelemetryDeck SDK to Swift 6
searchEngineDescription: What we've learned while migrating our code to the new world of data-race safety in Swift 6 mode.
---


## Motivation

Many experienced developers are hesitant to add many outside dependencies to their apps – and for good reason. Successful projects are here to stay for a long time, and the amount of maintenance required is a key consideration when deciding if one should add a new dependency or not. We at TelemetryDeck try to make this decision as simple as possible for our customers, by making sure to follow Apple's latest guidelines and best practices in a timely manner.

And this summer at WWDC 2024 the longest session of them all was [Migrating your app to Swift 6](https://wwdcnotes.com/documentation/wwdcnotes/wwdc24-10169-migrate-your-app-to-swift-6) for a reason. This major new update to the language brings a new level of safety – namely [data-race safety](https://www.swift.org/migration/documentation/swift-6-concurrency-migration-guide/dataracesafety/) – which is awesome news for more correct code, but also comes with a lot of new requirements we all need to adapt to.

While the Swift team did a great job at making sure you can turn on these new safety checks at your own pace, we wanted to make sure our SDK is ready ahead of time and documented the entire migration process in this article for others to learn from. This is our contribution to help the community migrate.


## First Steps

In their WWDC session, Apple recommends to enable "complete concurrency checking" while staying in Swift 5 mode first. This will give you warnings instead of errors, so you can tackle the warnings step by step over time. Our SDK is small and consists of just ~2k lines of code, so we opted for fixing everything in one go.

To turn these checks on we need to add `.enableExperimentalFeature("StrictConcurrency")` to our targets' `swiftSettings` like so:

```swift
// swift-tools-version: 5.9
import PackageDescription

let package = Package(
    // ...
    targets: [
        .target(
            name: "TelemetryDeck",
            resources: [.copy("PrivacyInfo.xcprivacy")],
            swiftSettings: [.enableExperimentalFeature("StrictConcurrency")]
        ),
        .testTarget(
            name: "TelemetryDeckTests",
            dependencies: ["TelemetryDeck"],
            swiftSettings: [.enableExperimentalFeature("StrictConcurrency")]
        )
    ]
)
```

Note that you need to set `swift-tools-version` to at least `5.8` in order to set this flag.

> Tip: Make sure to use Xcode 16 (beta) when building and preparing for Swift 6 compatibility. It contains the Swift 6 compiler which has improved checking logic and might find issues you might miss in Xcode 15. And it also contains the latest system SDKs where more types were checked and marked for data-race safety by Apple, which can prevent some unnecessary code adjustments.

With these steps out of the way, we can finally build the project to see all the issues the project has when it comes to data-race safety in Swift 6. The following 3 sections explain how we fixed the 21 issues we've run into in our code base grouped by the solution we applied and an explanation why we opted for that solution with a code sample.


## @MainActor

While most of our SDK code is designed to run perfectly fine in background threads, there is one exception:

```
/// Keeps track of the last used navigation path for ``navigationPathChanged(to:)`` to have a `from`.
class NavigationStatus {
    static let shared = NavigationStatus()

    var previousNavigationPath: String?
}
```

And we do get a warning for the `shared` property stating this:

```
Static property 'shared' is not concurrency-safe because non-'Sendable' type 'NavigationStatus' may have shared mutable state; this is an error in the Swift 6 language mode
```

In this particular case, because the navigation path change is directly related to an apps UI which always runs on the main thread, we can simply mark the entire type as `@MainActor`:


```swift
@MainActor
class NavigationStatus {
    static let shared = NavigationStatus()

    var previousNavigationPath: String?
}

```

This tells the compiler to restrict access to the main thread (or "actor", or "queue"). Calls from other contexts will require an async context with an `await` call. This is probably gonna be a very common solution in app projects that consists mostly of UI code.

Marking the entire type as `@MainActor` immediately created errors for all functions where `NavigationStatus.shared` was being accessed, such as:

```
Main actor-isolated property 'previousNavigationPath' can not be referenced from a non-isolated context
```

Marking these functions as `@MainActor` resolved these errors. For example:

```swift
@MainActor
public static func navigationPathChanged(to destination: String) {
    let source = NavigationStatus.shared.previousNavigationPath ?? ""

    // ...
}
```

Note that when in a SwiftUI view, you already are in the `@MainActor` context implicitly and can call these functions normally. So this change of requirement shouldn't affect existing usage of this function by our customers.


## Computed Properties vs. Stored Properties

The most common kind of warning we ran into was stating something like this:

```
Static property 'iso8601' is not concurrency-safe because non-'Sendable' type 'ISO8601DateFormatter' may have shared mutable state; this is an error in the Swift 6 language mode
```

The related Swift code looked like this:

```swift
extension Formatter {
    static let iso8601: ISO8601DateFormatter = {
        let formatter = ISO8601DateFormatter()
        formatter.formatOptions = [.withInternetDateTime, .withFractionalSeconds]
        return formatter
    }()
}
```

The reason why this code is not concurrency-safe is because `ISO8601DateFormatter` is a `class` and therefore a reference type. And the properties of a reference type can be changed even when they are defined as a `let` constant. So while the `iso8601` formatter is being accessed in one context it might get changed from another context due to its mutable nature. This is a race condition and could lead to unexpected behavior.

As `ISO8601DateFormatter` is a type defined within Foundation, we can't make it concurrency-safe itself, so we just need to deal with its mutable nature and work around it. The easiest way to this in our case was to turn our `let` constant into a get-only computed property like so:

```swift
extension Formatter {
    static var iso8601: ISO8601DateFormatter {
        let formatter = ISO8601DateFormatter()
        formatter.formatOptions = [.withInternetDateTime, .withFractionalSeconds]
        return formatter
    }
}
```

What makes this concurrency-safe is the fact that we don't have a setter. In our SDK, this exact solution could be applied in 6 different places, reducing our warnings from 21 to 15.


## Value Types vs. Reference Types

Another common warning we ran into was this:

```
Capture of 'configuration' with non-sendable conforming `TelemetryManagerConfiguration` to `Sendable`, we ran into a couple of new issues stating:

```

```error in the Swift 6 language mode
```

The related Swift code for the warning:

```swift
  func processSignal(configuration: TelemetryManagerConfiguration) {
      DispatchQueue.global(qos: .utility).async {
          let enrichedMetadata: [String: String] = configuration.metadataEnrichers

          // ...
      }
  }
```

First, the reason why we are in a `Sendable` (one could also say "concurrency-safe") closure is that we are calling into `DispatchQueue.async` which marks the trailing closure as `@Sendable`. Inside a `Sendable` ("concurrency-safe") context, the Swift 6 compiler makes sure that all types and functions used within are also `Sendable`. So if one is not marked or inferred as such, we need to tell the compiler ourselves that the type or function is concurrency-safe.

So let's check if we can conform our type to be `Sendable`, it looks something like this:

```swift
public final class TelemetryManagerConfiguration {
    /// Your app's identifier on TelemetryDeck. Set this during initialization.
    public let telemetryAppID: String


    /// Globally set your user's hashed name/email/identifier here.
    public var defaultUser: String?
}
```

According to the [docs](https://developer.apple.com/documentation/swift/sendable#Sendable-Classes), a class can only be `Sendable` if it's marked as `final` (check!), has no superclass or `NSObject` (check!), and all stored properties are immutable (oh no!). Since we need `defaultUser` to be mutable, we can't conform it to `Sendable`.

But looking at how the `configuration` is being used in the SDK, we couldn't find a good reason why this was marked as `final class` in the first place. So we decided to switch it up to be a `struct` instead, which only has the requirement that all its members are `Sendable` themselves. `String` and `Optional<String>` conform to `Sendable`, so now we can mark the whole type to conform to `Sendable`:

```swift
public struct TelemetryManagerConfiguration: Sendable {
    /// Your app's identifier on TelemetryDeck. Set this during initialization.
    public let telemetryAppID: String


    /// Globally set your user's hashed name/email/identifier here.
    public var defaultUser: String?
}
```

This change lead to the error `Cannot assign to property: 'configuration' is a 'let' constant` in a couple of places. The fix was easy though, we just had to change any stored properties from being a `let` constant to a `var` like so:

```swift
// Before: (TelemetryManagerConfiguration was a reference type)
private let configuration: TelemetryManagerConfiguration

// After: (TelemetryManagerConfiguration is a value type)
private var configuration: TelemetryManagerConfiguration
```

It was always a best practice in Swift to use value types wherever possible (for various reasons). Now, with data-race safety checked by the compiler, this advantage becomes even more apparent.


## When `@unchecked Sendable` is appropriate

In some other places we ran into this warning:

```
Capture of 'self' with non-sendable type 'SignalManager' in a `@Sendable` closure; this is an error in the Swift 6 language mode
```

The related code was in the same function as above, but for a different reason:

```swift
func processSignal(configuration: TelemetryManagerConfiguration) {
        DispatchQueue.global(qos: .utility).async {
            let userID = self.defaultUserIdentifier

            // ...
        }
    }

```

Again, we are in a concurrency-safe context (`Dispatch.async`) and are calling into `self`, which is of type `SignalManager` and does not conform to `Sendable` as you can see here:

```swift
class SignalManager: SignalManageable {
    private var signalCache: SignalCache<SignalPostBody>
    let configuration: TelemetryManagerConfiguration
    private var sendTimer: Timer?

    // ...
}
```

This time, we had a good reason the type needs to be a class: Due to linking into `NotificationCenter` observers, it needs to support the old `#selector` API which requires a class with functions marked as `@objc`. So let's conform the class itself to `Sendable`:

```swift
final class SignalManager: SignalManageable, Sendable {
    private var signalCache: SignalCache<SignalPostBody>
    let configuration: TelemetryManagerConfiguration
    private var sendTimer: Timer?

    // ...
}
```

Unfortunately, this does not work, we're getting a new warning:

```
Stored property 'signalCache' of 'Sendable'-conforming class 'SignalManager' is mutable; this is an error in the Swift 6 language mode
```

And while the compiler doesn't emit it immediately, surely when commenting out `signalCache` we also get the same warning for the `sendTimer` stored property. Remember that a class can't have a mutable stored property if it wants to conform to `Sendable`. So how to fix this?

A deeper look at these two parameters and their usage can either uncover a data race in our code that always existed and we are now made aware of. Or it might reveal that we actually can't have a data-race due to our existing logic and just need to tell the compiler to assume our type is `Sendable`.

Digging deeper, I found that `sendTimer` is only set upon `init` no app start and when returning the app from the background. Those are not things that can happen concurrently, so there's no potential for a race condition.

As for the `signalCache`, a look into the type's implementation reveals that it uses a `DispatchQueue` internally and runs any changes using the `sync` method on it, which blocks concurrent access and therefore also avoids race conditions:

```swift
internal class SignalCache<T> where T: Codable {
    private var cachedSignals: [T] = []

    let queue = DispatchQueue(label: "telemetrydeck-signal-cache", attributes: .concurrent)

    /// Insert a Signal into the cache
    func push(_ signal: T) {
        queue.sync(flags: .barrier) {
            self.cachedSignals.append(signal)
        }
    }

    // ...
}
```

So, we now know that we didn't have a data-race safety issue in our `SignalManager` type (and `SignalCache` type) in the first place. And that means we can mark (both) as `@unchecked Sendable` to tell the compiler that it doesn't need to check its data-race safety and we, the developers, take responsibility for doing that instead:

```swift
final class SignalManager: SignalManageable, @unchecked Sendable {
    private var signalCache: SignalCache<SignalPostBody>
    let configuration: TelemetryManagerConfiguration
    private var sendTimer: Timer?

    // ...
}
```

While this is not perfect because we might introduce race conditions in these types at a later point without noticing (and the compiler wouldn't detect them), we need to live with this situation for years to come for compatibility reasons. Apple engineers also use this all over the place, for example the `Timer` type itself is marked as `@unchecked Sendable`.


## Long-Hanging Fruits

When conforming types to `Sendable`, it's common to run into a warning like this for stored properties:

```
Stored property 'logHandler' of 'Sendable'-conforming struct 'TelemetryManagerConfiguration' has non-sendable type 'LogHandler?'; this is an error in the Swift 6 language mode
```

The related stored property code was this:

```swift
public var logHandler: LogHandler? = LogHandler.stdout(.info)
```

The fix in these cases often is as simple as adding the `Sendable` protocol conformance to your public structs and enums. Internal value types don't even need this as they are [automatically inferred](https://developer.apple.com/documentation/swift/sendable#Sendable-Structures-and-Enumerations) to be `Sendable`. For example, we just added a couple of `Sendable` conformances to our types and `@Sendable` to closures in this code and the warnings disappeared:

```swift
public struct LogHandler: Sendable {
    public enum LogLevel: Int, Sendable {
        case debug = 0, info = 1, error = 2
    }

    let logLevel: LogLevel
    let handler: @Sendable (LogLevel, String) -> Void

    public init(logLevel: LogHandler.LogLevel, handler: @escaping @Sendable (LogHandler.LogLevel, String) -> Void) {
        self.logLevel = logLevel
        self.handler = handler
    }
}

```

Note also the added `@Sendable` in the function parameter `handler` right behind `@escaping`.


## Confirm full Swift 6 compatibility

After fixing all warnings, it's a good idea to double-check that everything would work as expected in Swift 6 mode. The easiest way to do this in a Swift package is (to open it in Xcode 16 and) setting the `swift-tools-version` to `6.0` at the top of the `Package.swift` manifest file:

```swift
// swift-tools-version: 6.0
```

Now, if the project builds without any errors – which it did for us – then we're all set! Of course, we won't be comitting this change as it would bump the minimum requirement to use our SDK to Xcode 16, which is not what we want. But our project is ready for Swift 6 now!


## Conclusion

Migrating to Swift 6 mode with all of its data-race safety glory was not an easy task. Despite our small project size, we ran into many warnings that all looked similar on the surface, but each of them needed careful consideration. We outlined the different solutions that worked for us above and explained why we opted for them. We hope this will help others with their migration to Swift 6.
