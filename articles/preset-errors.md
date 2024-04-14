---
title: Setting Up the 'Errors' Preset to Reduce Churn
tags:
  - setup
  - beginner
  - insights
  - presets
lead: TelemetryDeck ships with a set of insights that can be useful to learn what kind of issues your users encounter most in your apps. Here's how to set them up.
---

## Why Track Errors?

Success is often defined in numbers such as Monthly Active Users (MAU) or Monthly Recurring Revenue (MRR). Churn is a metric that tracks the percentage of active/paying users who stopped using/paying for your app.

A smooth experience without bugs & issues is one of the key factors contributing to a lower churn rate. If you do a good job in continuuously fixing the most common issues with your product, you're on the right track for success. That's why it's important that you detect any common issues your users get stuck at while using your app.

{% noteinfo "What Error Handling Really Is" %}
Error Handling is any logic that detects that something unexpected happened and reacts to that information in some useful way. It's commonly interpreted as 'showing an error message to a user', but that's just the most basic form of Error Handling. Other common things you can do to improve your app are Empty States (Why is this empty?), Call-to-Actions (What can I do?), and Auto-Repair (resiliency against common unexpected user input). But always make sure to give some form of feedback instead of failing silently, which makes your app feel broken.
{% endnoteinfo %}


## Sending the Signal

To report unexpected events to TelemetryDeck, send the event name `TelemetryDeck.Error.occurred` with the parameter `TelemetryDeck.Error.id` set to something that can be used to group errors of the same kind. For example, using the Swift SDK you could simply use `error.localizedDescription` whenever an exception is thrown that you don't expect to happen:

```swift
do {
  let object = try JSONDecoder().decode(Object.self, from: data)
} catch {
  // your error handling code
  TelemetryManager.send("TelemetryDeck.Error.occurred", with: ["TelemetryDeck.Error.id": error.localizedDescription])
}
```

## Separation of ID & Message

While the above code is a good starting point, the localized nature of the `localizedDescription` message attached to all thrown exceptions in Swift isn't optimal. The same issue will be reported with different messages simply because the text will differ based on the users language settings. And you might have even created your own error types that provide dynamic content such as the file path in the error message, which makes things even worse. To see which errors affect most users, it's best to give the same kind of errror the same ID.

So, whenever possible, it's recommended that you instead pass a made-up value to the `TelemetryDeck.Error.id` parameter that rather represents the context of the error. The full message can be provided with the optional parameter `TelemetryDeck.Error.message` like so:

```swift
do {
  let object = try JSONDecoder().decode(Object.self, from: data)
} catch {
  // your error handling code
  TelemetryManager.send(
    "TelemetryDeck.Error.occurred",
    with: [
      "TelemetryDeck.Error.id": "ImportObjectScreen.decodeFromJSONFailed",
      "TelemetryDeck.Error.message": error.localizedDescription
    ]
  )
}
```

For your own `Error` types, you could introduce an `IdentifiableError` protocol and conform to that to make this process easier:

```swift
protocol IdentifiableError: Error {
  var id: String { get }
}

enum MyError: String, IdentifiableError {
  case fileMissing
  case invalidFormat

  var id: String { self.rawValue }
}
```

Now you can pass `error.id` for the `TelemetryDeck.Error.id` parameter whenever you encounter an error that can be casted to `IdentifiableError`. For system errors, you could fall back to something like `String(describing: type(of: error))`.

## Built-In Error Categories

Reporting exceptions that you didn't expect to happen isn't enough to cover all "unexpected behaviors" that you will encounter in your app. We found that unexpected behavior generally falls into one of the following 3 categories:

1. Unexpected **Exceptions** (e.g. parsing errors, I/O errors, permission errors)
2. Unexpected **User Input** (e.g. invalid text format, invalid number format, invalid date range)
3. Unexpected **App State** (e.g. inconsistent navigation request, invalid combination of form options)

Each of these has a dedicated chart in the "Errors" tab, you just need to report one of `exception`, `user-input`, or `app-state` to the parameter `TelemetryDeck.Error.category`.

Here's some guidance on when to use which category in Swift:
* A clear sign to report an `exception` error is a `do-catch` clause or uses of `try?` in Swift where you can send the error signal when it returns `nil`.
* Whenever you you make use of the nil-coalescing operator `??` or unwrap an Optional with `if-let` or `guard-let`, potentially some kind of conversion of user input into another type might happen with a fallback behavior – this is a typical `user-input` error.
* Search for any uses of [`assert`](https://developer.apple.com/documentation/swift/assert(_:_:file:line:)) or [`assertionFailure`](https://developer.apple.com/documentation/swift/assertionfailure(_:file:line:)) in your code and additionally report these detected unexpected states of your app during runtime as `app-state` errors. If you weren't aware, the `assert`/`assertionFailure` functions are similar to `fatalError`/`precondition`/`preconditionFailure` with the difference that they only stop program execution during DEBUG builds, not in production builds.

A full signal that reports a `user-input` category error could end up looking something like this in Swift:

```swift
var hourlyRate: Int {
  if let hourlyRate = Int(self.textFieldInput) {
    return hourlyRate
  } else {
    TelemetryManager.send(
      "TelemetryDeck.Error.occurred",
      with: [
        "TelemetryDeck.Error.id": "ProjectForm.hourlyRateConversionFailed",
        "TelemetryDeck.Error.category": "user-input",
        "TelemetryDeck.Error.message": "Text '\(self.textFieldInput)' could not be converted to type 'Int'."
      ]
    )
    return 0  // fallback value
  }
}
```

## Effect on Privacy & App Tracking Transparency

If you are sending dynamic values such as `error.localizedDescription` or if any of the parameter fields contain user-dynamic data such as file paths or input data, some user data might be sent to TelemetryDeck. It really depends on the nature of this data and how you plan to use it what fields in App Tracking Transparency you need to add. You might need to adjust your privacy report accordingly.

But TelemetryDeck does not attempt to link collected data to the users identity, nor do we use data for tracking purposes.
To protect your users privacy, we urge you to not send any data that might identify your users.
