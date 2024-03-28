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

If you are offering In-App Purchases in your app, you might have noticed some delay in officially reported purchase stats. For example, App Store Connect charts do not offer any purchase data for the last 3 hours. Such a delay can be very annoying sometimes such as the day of your app launch or a specific live event related to your app. On top of that, App Store Connect in particular signs you out of your account very regularly, making it annoying to quickly look up purchase statistics.

That's why you might want to set up a signal in your application to track purchases in your app through TelemetryDeck within seconds, providing you with the live data you want.

{% notewarning "Live Data vs. Correct Data" %}
We do not offer any intelligence to correct once reported purchases, such as when users make refunds, or to detect subscription renewals. Therefore, our insights focus on more recent data. For longer-term or 100% correct data, refer to official sources.
{% endnotewarning %}


## Sending the Signal

To report purchases to TelemetryDeck, send the event name `TelemetryDeck.Purchase.completed` with the `floatValue` parameter set to the USD amount the user purchased. For example, using the Swift SDK you can get the price from `StoreKit` like so:

```swift
let priceValue = NSDecimalNumber(decimal: storeKitProduct.price).doubleValue

TelemetryManager.send("TelemetryDeck.Purchase.completed", floatValue: priceValue)
```

{% notewarning "Converting Currencies" %}
Make sure to convert any currencies to USD before sending them as signals. You can use [an API like this](https://www.exchangerate-api.com/docs/standard-requests) which offers 1,500 requests per month for free to get current exchange rates if needed. You could also fetch & hard-code them to your app for a rough estimate if you expect more than 1,500 purchases per month.
{% endnotewarning %}


## Attaching the Payload

Optionally (but recommended), there are two additional payload keys that will give you additional insights:

* `TelemetryDeck.Purchase.type`: Pass either `subscription` or `one-time-purchase` to see the type distribution.
* `TelemetryDeck.Purchase.countryCode`: Pass the country code of the storefront to see the country distribution.

In Swift getting all values and sending them looks like this:

```swift
let priceValue = NSDecimalNumber(decimal: storeKitProduct.price).doubleValue
let purchaseType = storeKitProduct.subscription != nil ? "subscription" : "one-time-purchase"
let countryCode = storeKitProduct.priceLocale.region?.identifier ?? "ZZ"

TelemetryManager.send(
  "TelemetryDeck.Purchase.completed",
  floatValue: priceValue,
  with: [
    "TelemetryDeck.Purchase.type": purchaseType,
    "TelemetryDeck.Purchase.countryCode": countryCode
  ]
)
```

{% noteinfo "3rd-Party Services" %}
> If you are using a third-party service like RevenueCat, you can access the `SKProduct` type on their own types. For example, for the `Package` type in RevenueCat, you would call `.storeProduct.skProduct`.
{% endnoteinfo %}


## Effect on Privacy & App Tracking Transparency

If you are using a 3rd-party service like RevenueCat, you don't need to change your privacy labels at all because you're sending way less data to TelemetryDeck than you are already to those services. So if you've followed their guides, you should be good.

If you aren't using a 3rd-party library, you are now sending purchase history data to TelemetryDeck. So make sure to mark the checkbox for "Analytics" in the "Purchase History" entry in your App Privacy page.

You can answer all subsequent questions with "No" because we neither link collected data to the users identity, nor do we use them for tracking purposes.

When all is configured your "Purchases" entry in your App Privacy page should end up looking like this:

![Purchases entry with only 'Used for Analytics' in the box](/docs/images/purchases-privacy-box.png)
