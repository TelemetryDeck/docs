---
title: Tracking Errors
tags:
  - setup
  - beginner
  - insights
  - presets
lead: Track errors in your app to identify common issues and reduce churn. The TelemetryDeck SDK provides convenience methods for structured error reporting.
---

## Why track errors?

A smooth experience directly impacts retention. Tracking errors lets you find the most common issues your users hit, prioritize fixes, and measure improvement over time.

## Using the TelemetryDeck Swift SDK

```swift
await TelemetryDeck.errorOccurred(id: error.localizedDescription)
```

### Better error identification

`error.localizedDescription` varies by user language, making it hard to group the same error. Provide a consistent ID instead:

```swift
do {
    let object = try JSONDecoder().decode(Object.self, from: data)
} catch {
    await TelemetryDeck.errorOccurred(
        identifiableError: error.with(id: "ImportObject.jsonDecode")
    )

    // Or with explicit parameters:
    await TelemetryDeck.errorOccurred(
        id: "ImportObject.jsonDecode",
        message: error.localizedDescription
    )
}
```

### Custom error types

Conform your own error types to `IdentifiableError`:

```swift
enum MyError: String, IdentifiableError {
    case fileMissing
    case invalidFormat

    var id: String { self.rawValue }
}

await TelemetryDeck.errorOccurred(identifiableError: myError)
```

### Error categories

Three built-in categories for organization:

```swift
// Thrown exceptions — parsing errors, I/O errors, permission errors
await TelemetryDeck.errorOccurred(
    id: "FileNotFound",
    category: .thrownException,
    message: error.localizedDescription
)

// User input errors — invalid format, invalid range
await TelemetryDeck.errorOccurred(
    id: "ProjectForm.hourlyRateConversionFailed",
    category: .userInput,
    message: "Text could not be converted to Int"
)

// App state errors — inconsistent navigation, invalid combinations
await TelemetryDeck.errorOccurred(
    id: "NavigationState.invalidTransition",
    category: .appState,
    message: "Cannot navigate from login to dashboard without authentication"
)
```

!!! note

    When using `errorOccurred(identifiableError:)`, the category defaults to `.thrownException`.

The `errorOccurred` function accepts the same optional arguments as `event` (`parameters`, `floatValue`, `customUserID`).

## Manual signal construction for other platforms

If you're not using the Swift SDK, construct the error signal manually.

**Event name**: `TelemetryDeck.Error.occurred`

**Required parameter**:

- `TelemetryDeck.Error.id`: A consistent identifier for grouping similar errors

**Optional parameters**:

- `TelemetryDeck.Error.message`: The full error message
- `TelemetryDeck.Error.category`: One of `thrown-exception`, `user-input`, or `app-state`

## Built-in error categories

| Category | Use when |
|---|---|
| `thrown-exception` | In `try-catch` blocks or when handling `nil` returns from operations that might fail |
| `user-input` | Validating or converting user input with fallback behavior |
| `app-state` | Assertion failures or unexpected application states |

## Privacy considerations

If you send dynamic values like `error.localizedDescription` or user-generated content in parameters, some user data reaches TelemetryDeck. Adjust your App Tracking Transparency disclosure accordingly.

TelemetryDeck does not link collected data to user identity or use it for tracking. Don't send data that could identify your users.
