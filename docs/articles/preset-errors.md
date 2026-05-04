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

A smooth experience without bugs & issues is one of the key factors contributing to a lower churn rate. If you do a good job in continuously fixing the most common issues with your product, you're on the right track for success. That's why it's important that you detect any common issues your users get stuck at while using your app.

{% noteinfo "What Error Handling Really Is" %}
Error Handling is any logic that detects that something unexpected happened and reacts to that information in some useful way. It's commonly interpreted as 'showing an error message to a user', but that's just the most basic form of Error Handling. Other common things you can do to improve your app are Empty States (Why is this empty?), Call-to-Actions (What can I do?), and Auto-Repair (resiliency against common unexpected user input). But always make sure to give some form of feedback instead of failing silently, which makes your app feel broken.
{% endnoteinfo %}

## Using the TelemetryDeck Swift SDK

If you're using the TelemetryDeck Swift SDK, tracking errors is simple. Use the convenience method we've prepared:

```swift
TelemetryDeck.errorOccurred(id: error.localizedDescription)
```

### Better Error Identification

While `error.localizedDescription` works, it's not optimal because the same error will be reported differently based on user language settings. For better error grouping, provide a consistent ID:

```swift
do {
  let object = try JSONDecoder().decode(Object.self, from: data)
} catch {
  // Option 1: Using error.with(id:)
  TelemetryDeck.errorOccurred(
    identifiableError: error.with(id: "ImportObject.jsonDecode")
  )

  // Option 2: Using explicit parameters
  TelemetryDeck.errorOccurred(
    id: "ImportObject.jsonDecode",
    message: error.localizedDescription
  )
}
```

### Custom Error Types

For your own error types, conform to the `IdentifiableError` protocol (built into the Swift SDK):

```swift
enum MyError: String, IdentifiableError {
  case fileMissing
  case invalidFormat

  var id: String { self.rawValue }
}

// Then report directly:
TelemetryDeck.errorOccurred(identifiableError: myError)
```

### Error Categories

The Swift SDK provides three built-in error categories for better organization:

```swift
// Thrown exceptions (parsing errors, I/O errors, permission errors)
TelemetryDeck.errorOccurred(
  id: "FileNotFound",
  category: .thrownException,
  message: error.localizedDescription
)

// User input errors (invalid format, invalid range)
TelemetryDeck.errorOccurred(
  id: "ProjectForm.hourlyRateConversionFailed",
  category: .userInput,
  message: "Text '\(self.textFieldInput)' could not be converted to type 'Int'."
)

// App state errors (inconsistent navigation, invalid combinations)
TelemetryDeck.errorOccurred(
  id: "NavigationState.invalidTransition",
  category: .appState,
  message: "Cannot navigate from login to dashboard without authentication"
)
```

{% noteinfo "Default Category" %}
When using `TelemetryDeck.errorOccurred(identifiableError:)`, the category defaults to `.thrownException`, but you can override it if needed.
{% endnoteinfo %}

The `errorOccurred` function accepts the same optional arguments as the `signal` function (namely `parameters`, `floatValue`, `customUserID`) in case you want to provide additional context info.

## Manual Signal Construction for Other Platforms

If you're not using the TelemetryDeck Swift SDK (for example, on Android, Web, or other platforms), you'll need to manually build the error signal.

### Signal Structure

**Event name**: `TelemetryDeck.Error.occurred`

**Required parameter**:

- `TelemetryDeck.Error.id`: A consistent identifier for grouping similar errors

**Optional parameters**:

- `TelemetryDeck.Error.message`: The full error message or description
- `TelemetryDeck.Error.category`: One of `thrown-exception`, `user-input`, or `app-state`

## Built-In Error Categories

Unexpected behavior generally falls into one of three categories, each with a dedicated chart in the "Errors" tab:

1. **Thrown Exceptions** (`thrown-exception`): Parsing errors, I/O errors, permission errors
2. **User Input** (`user-input`): Invalid text format, invalid number format, invalid date range
3. **App State** (`app-state`): Inconsistent navigation request, invalid combination of form options

### When to Use Each Category

- **thrown-exception**: Use in `try-catch` blocks or when handling `null`/`nil` returns from operations that might fail
- **user-input**: Use when converting or validating user input with fallback behavior
- **app-state**: Use for assertion failures or unexpected application states that shouldn't occur in normal operation

## Effect on Privacy & App Tracking Transparency

If you are sending dynamic values such as `error.localizedDescription` or if any of the parameter fields contain user-dynamic data such as file paths or input data, some user data might be sent to TelemetryDeck. It really depends on the nature of this data and how you plan to use it that influences what fields in App Tracking Transparency you need to add. You might need to adjust your privacy report accordingly.

TelemetryDeck does not attempt to link collected data to the users identity, nor do we use data for tracking purposes. To protect your users privacy, we urge you to not send any data that might identify your users.
