---
title: Tracking Purchases
tags:
  - setup
  - beginner
  - insights
  - presets
lead: Track in-app purchases through TelemetryDeck for near-realtime revenue data — no waiting hours for App Store Connect to update.
searchEngineDescription: Track your app's in-app purchases through TelemetryDeck with just a couple of seconds delay, providing live revenue data.
testedOn: SwiftSDK 3.0.0
---

## Why track purchases?

App Store Connect purchase data lags by several hours and requires frequent re-authentication. TelemetryDeck gives you purchase data within seconds.

You can track purchases through:

- The TelemetryDeck Swift SDK directly
- RevenueCat integration
- FreemiumKit integration

!!! warning "Live data vs. correct data"

    TelemetryDeck does not handle refunds or detect subscription renewals. For long-term or 100% correct revenue data, use official sources like App Store Connect.

## Using the TelemetryDeck Swift SDK

Pass a StoreKit transaction to the convenience method:

```swift
await TelemetryDeck.purchaseCompleted(transaction: transaction)
```

This automatically:

- Extracts the price from the transaction
- Converts the currency to USD (using built-in exchange rates)
- Determines if it's a subscription or one-time purchase
- Detects free trial starts vs. paid conversions
- Includes the storefront country and currency codes

!!! note "Requirements"

    Requires iOS 15+. Accepts optional `parameters` and `customUserID` for additional context.

### Automatic trial conversion detection

The SDK includes a `TrialConversionProcessor` that monitors StoreKit `Transaction.updates` in the background. When a user transitions from a free trial to a paid subscription, it automatically fires `TelemetryDeck.Purchase.convertedFromTrial`. No additional code needed.

## Using TelemetryDeck with RevenueCat

See our [RevenueCat Setup Guide](/integrations/revenuecat/).

## Using FreemiumKit

Add FreemiumKit's `.onPurchaseCompleted` view modifier to your main view — it passes the `transaction` parameter directly to `TelemetryDeck.purchaseCompleted(transaction:)`. See their [setup guide](https://freemiumkit.app/documentation/freemiumkit/setupguide#Direct-Access-to-StoreKit-Transactions).

## Manual signal construction for other platforms

!!! warning

    Only needed if you are NOT using the TelemetryDeck Swift SDK.

### Required fields

- **Event name**: `TelemetryDeck.Purchase.completed`
- **`floatValue`**: The purchase amount in USD

!!! warning "Currency conversion"

    You must convert the transaction value to USD before sending. Use [an exchange rate API](https://www.exchangerate-api.com/docs/standard-requests) (1,500 free requests/month) or hard-code approximate rates.

### Optional parameters

- `TelemetryDeck.Purchase.type`: `subscription` or `one-time-purchase`
- `TelemetryDeck.Purchase.countryCode`: Storefront country code
- `TelemetryDeck.Purchase.currencyCode`: Storefront currency code

### Example

```swift
let priceInUSD = convertToUSD(transaction.price, from: transaction.currencyCode)

await TelemetryDeck.event(
    "TelemetryDeck.Purchase.completed",
    parameters: [
        "TelemetryDeck.Purchase.type": transaction.subscriptionGroupID != nil
            ? "subscription" : "one-time-purchase",
        "TelemetryDeck.Purchase.countryCode": transaction.storefrontCountryCode,
        "TelemetryDeck.Purchase.currencyCode": transaction.currencyCode ?? "???"
    ],
    floatValue: priceInUSD
)
```

## Privacy

If you already use RevenueCat or a similar service, you're already sending more data to them than TelemetryDeck collects. No privacy label changes needed.

If tracking purchases directly, mark "Analytics" under "Purchase History" in your App Privacy page. Answer all subsequent questions with "No".

![Purchases entry with only 'Used for Analytics' in the box](/assets/purchases-privacy-box.png)
