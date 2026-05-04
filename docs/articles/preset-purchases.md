---
title: Setting Up the 'Purchases' Preset to Get Live Purchase Data
tags:
  - setup
  - beginner
  - insights
  - presets
lead: TelemetryDeck ships with a set of insights that can be useful to track your revenue within the last few hours with live purchase data. Here's how to set them up.
searchEngineDescription: TelemetryDeck ships with a set of insights that can be useful to track your revenue within the last few hours with live purchase data. Learn how to set them up.
---

## Why Track Purchases?

If you are offering In-App Purchases in your app, you might have noticed some delay in officially reported purchase stats. For example, App Store Connect charts do not offer any purchase data for the last 3 hours. Such a delay can be annoying sometimes such as at the day of your app launch or a specific live event related to your app. On top of that, App Store Connect in particular signs you out of your account regularly, making it annoying to quickly look up purchase statistics.

That's why you might want to set up a signal in your application to track purchases in your app through TelemetryDeck with just a couple of seconds delay, providing you with the live data you want.

You can use these methods to include your purchase data in TelemetryDeck:

- Use the TelemetryDeck Swift SDK directly
- If you're already using RevenueCat, you can use the RevenueCat Integration
- If you're using FreemiumKit, you can connect that to TelemetryDeck

See the sections below for a detailed description.

{% notewarning "Live Data vs. Correct Data" %}
We do not offer any intelligence to correct once reported purchases, such as when users make refunds, or to detect subscription renewals. Therefore, our insights focus on more recent data. For longer-term or 100% correct data, refer to official sources.
{% endnotewarning %}

## Using the TelemetryDeck Swift SDK

If you're using the TelemetryDeck Swift SDK, tracking purchases is incredibly simple. Just call the convenience method when you receive a StoreKit transaction:

```swift
TelemetryDeck.purchaseCompleted(transaction: transaction)
```

That's it! This method automatically:

- Extracts the price from the transaction
- Converts the currency to USD (using hard-coded exchange rates)
- Determines if it's a subscription or one-time purchase
- Includes the storefront country and currency codes
- Sends the properly formatted signal to TelemetryDeck

{% noteinfo "Requirements" %}
The `purchaseCompleted` convenience function is only available on iOS 15 or higher. It accepts the same optional arguments as the `signal` function (namely `parameters` and `customUserID`) in case you want to provide additional context info.
{% endnoteinfo %}

## Using TelemetryDeck with RevenueCat

If you use [RevenueCat](https://revenuecat.com), you can use our [RevenueCat Setup Guide](/docs/integrations/revenuecat/).

## Using FreemiumKit

If you use [FreemiumKit](https://freemiumkit.app), just add their SDKs `.onPurchaseCompleted` view modifier to your main view. It passes the `transaction` parameter to the closure, which you can directly pass to `TelemetryDeck.purchaseCompleted(transaction: transaction)`. Read the related section in their [setup guide](https://freemiumkit.app/documentation/freemiumkit/setupguide#Direct-Access-to-StoreKit-Transactions) to learn more.

## Manual Signal Structure for Other Platforms

{% notewarning "Only Needed for Non-Swift Platforms" %}
The following section describes the manual signal structure only necessary if you are NOT using the TelemetryDeck Swift SDK. Swift developers should use the `purchaseCompleted` convenience method described above.
{% endnotewarning %}

If you're reporting purchases from other platforms (Android, Web, etc.), you'll need to manually construct and send the purchase signal with the following structure:

### Required Fields

- **Event name**: Must be `TelemetryDeck.Purchase.completed`
- **`floatValue`**: The purchase amount in USD

{% notewarning "Manual Currency Conversion Required" %}
When sending purchase signals manually, you MUST convert the transaction value to USD yourself before sending. You can use [an API like this](https://www.exchangerate-api.com/docs/standard-requests) which offers 1,500 requests per month free of charge to get current exchange rates. Alternatively, you could fetch & hard-code exchange rates in your app for a rough estimate if you expect more than 1,500 purchases per month.
{% endnotewarning %}

### Optional but Recommended Payload Keys

To get more detailed insights, include these additional parameters:

- `TelemetryDeck.Purchase.type`: Either `subscription` or `one-time-purchase`
- `TelemetryDeck.Purchase.countryCode`: The country code of the storefront
- `TelemetryDeck.Purchase.currencyCode`: The currency code of the storefront

### Example Manual Implementation (Swift)

Here's what the manual implementation looks like if you need to customize it or understand what the convenience method does internally:

```swift
// Convert price to USD first (you need to handle currency conversion)
let priceInUSD = convertToUSD(transaction.price, from: transaction.currencyCode)

TelemetryDeck.signal(
  "TelemetryDeck.Purchase.completed",
  parameters: [
    "TelemetryDeck.Purchase.type": transaction.subscriptionGroupID != nil ? "subscription" : "one-time-purchase",
    "TelemetryDeck.Purchase.countryCode": transaction.storefrontCountryCode,
    "TelemetryDeck.Purchase.currencyCode": transaction.currencyCode ?? "???"
  ],
  floatValue: priceInUSD
)
```

## Effect on Privacy & App Tracking Transparency

If you are using a 3rd-party service like RevenueCat, you don't need to change your privacy labels at all because you're sending way less data to TelemetryDeck than you are already to those services. So if you've followed their guides, you should be good.

If you aren't using a 3rd-party library, you are now sending purchase history data to TelemetryDeck. So make sure to mark the checkbox for "Analytics" in the "Purchase History" entry in your App Privacy page.

You can answer all subsequent questions with "No" because we neither link collected data to the users identity, nor do we use them for tracking purposes.

When all is configured your "Purchases" entry in your App Privacy page should end up looking like this:

![Purchases entry with only 'Used for Analytics' in the box](/docs/images/purchases-privacy-box.png)
