---
title: Setting Up the 'Purchases' Preset to Get Live Purchase Data
tags:
  - setup
  - beginner
  - insights
  - presets
lead: TelemetryDeck ships with a set of insights that can be useful to track your revenue within the last few hours with live purchase data. Here's how to set them up.
---

## Why Track Purchases?

If you are offering In-App Purchases in your app, you might have noticed some delay in officially reported purchase stats. For example, App Store Connect charts do not offer any purchase data for the last 3 hours. Such a delay can be very annoying sometimes such as at the day of your app launch or a specific live event related to your app. On top of that, App Store Connect in particular signs you out of your account very regularly, making it annoying to quickly look up purchase statistics.

That's why you might want to set up a signal in your application to track purchases in your app through TelemetryDeck with just a couple of seconds delay, providing you with the live data you want.

{% notewarning "Live Data vs. Correct Data" %}
We do not offer any intelligence to correct once reported purchases, such as when users make refunds, or to detect subscription renewals. Therefore, our insights focus on more recent data. For longer-term or 100% correct data, refer to official sources.
{% endnotewarning %}


## Sending the Signal

To report purchases to TelemetryDeck, send the event name `TelemetryDeck.Purchase.completed` with the `floatValue` parameter set to the USD amount the user purchased. For example, using the Swift SDK you can get the price from `StoreKit.Transaction` like so:

```swift
let priceValue = NSDecimalNumber(decimal: transaction.price ?? Decimal()).doubleValue

TelemetryDeck.signal("TelemetryDeck.Purchase.completed", floatValue: priceValue)
```

{% notewarning "Converting Currencies" %}
Make sure to convert any currencies to USD before sending them as signals. You can use [an API like this](https://www.exchangerate-api.com/docs/standard-requests) which offers 1,500 requests per month for free to get current exchange rates if needed. You could also fetch & hard-code them to your app for a rough estimate if you expect more than 1,500 purchases per month.
{% endnotewarning %}

The Swift SDK ships with a more convenient API that handles reading the price from the StoreKit transaction and converting to USD (with hard-coded non-live currency conversion) for you like so:

```swift
TelemetryDeck.purchaseCompleted(transaction: transaction)
```

{% noteinfo "Built-In Automatics" %}
The `purchaseCompleted` convenience function in the Swift SDK also automates the extraction of the values explained in the next section. Optionally, it accepts the same arguments as the `signal` function (namely `parameters` and `customUserID`) in case you want to provide additional context info. The function is only available on iOS 15 or higher.
{% endnoteinfo %}

{% noteinfo "RevenueCat" %}
If you use RevenueCat and followed their [setup guide](https://www.revenuecat.com/docs/getting-started/making-purchases), you will have a `Purchases.shared.purchase(package:)` call somewhere in your code. The closure of this function gets a RevenueCat-specific `transaction` [wrapper](https://github.com/RevenueCat/purchases-ios/blob/11f3962192271cdbbb70096ff5a693b8a0e48f49/Sources/Purchasing/StoreKitAbstractions/StoreTransaction.swift) as its first parameter. You can either access fields directly from that or get the native `StoreKit.Transaction` type by calling `transaction.sk2Transaction`. If you use RevenueCats built-in paywalls, they currently don't provide access to `transaction`, which we reported in [this issue](https://github.com/RevenueCat/purchases-ios/issues/4007).
{% endnoteinfo %}

## Attaching the Payload

Optionally (but recommended), there are two additional payload keys that will give you additional insights:

* `TelemetryDeck.Purchase.type`: Pass either `subscription` or `one-time-purchase` to see the type distribution.
* `TelemetryDeck.Purchase.countryCode`: Pass the country code of the storefront to see the country distribution.
* `TelemetryDeck.Purchase.currencyCode`: Pass the currency code of the storefront to see currency distribution.

In Swift getting all values and sending them looks like this:

```swift
TelemetryDeck.signal(
  "TelemetryDeck.Purchase.completed",
  parameters: [
    "TelemetryDeck.Purchase.type": transaction.subscriptionGroupID != nil ? "subscription" : "one-time-purchase",
    "TelemetryDeck.Purchase.countryCode": transaction.storefrontCountryCode,
    "TelemetryDeck.Purchase.currencyCode": transaction.currencyCode ?? "???"
  ],
  floatValue: NSDecimalNumber(decimal: transaction.price ?? Decimal()).doubleValue
)
```


## Effect on Privacy & App Tracking Transparency

If you are using a 3rd-party service like RevenueCat, you don't need to change your privacy labels at all because you're sending way less data to TelemetryDeck than you are already to those services. So if you've followed their guides, you should be good.

If you aren't using a 3rd-party library, you are now sending purchase history data to TelemetryDeck. So make sure to mark the checkbox for "Analytics" in the "Purchase History" entry in your App Privacy page.

You can answer all subsequent questions with "No" because we neither link collected data to the users identity, nor do we use them for tracking purposes.

When all is configured your "Purchases" entry in your App Privacy page should end up looking like this:

![Purchases entry with only 'Used for Analytics' in the box](/docs/images/purchases-privacy-box.png)
