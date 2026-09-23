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

- If you're already using RevenueCat, you can use the RevenueCat Integration
- If you're using FreemiumKit, you can connect that to TelemetryDeck

See the sections below for a detailed description.

{% notewarning "Live Data vs. Correct Data" %}
We do not offer any intelligence to correct once reported purchases, such as when users make refunds, or to detect subscription renewals. Therefore, our insights focus on more recent data. For longer-term or 100% correct data, refer to official sources.
{% endnotewarning %}

{% notewarning "EOL for TelemetryDeck Purchase Events" %}
For new apps, we're no longer showing the option to fill the Purchase Tab with data collected directly with the TelemetryDeck SDK. This option was not reliable enough, so we have sunset it. Apps that had it enabled already can keep it.
{% endnotewarning %}

## Using TelemetryDeck with RevenueCat

If you use [RevenueCat](https://revenuecat.com), you can use our [RevenueCat Setup Guide](/docs/integrations/revenuecat/).

## Using FreemiumKit

If you use [FreemiumKit](https://freemiumkit.app), just add their SDKs `.onPurchaseCompleted` view modifier to your main view. It passes the `transaction` parameter to the closure, which you can directly pass to `TelemetryDeck.purchaseCompleted(transaction: transaction)`. Read the related section in their [setup guide](https://freemiumkit.app/documentation/freemiumkit/setupguide#Direct-Access-to-StoreKit-Transactions) to learn more.


## Effect on Privacy & App Tracking Transparency

If you are using a 3rd-party service like RevenueCat, you don't need to change your privacy labels at all because you're sending way less data to TelemetryDeck than you are already to those services. So if you've followed their guides, you should be good.

If you aren't using a 3rd-party library, you are now sending purchase history data to TelemetryDeck. So make sure to mark the checkbox for "Analytics" in the "Purchase History" entry in your App Privacy page.

You can answer all subsequent questions with "No" because we neither link collected data to the users identity, nor do we use them for tracking purposes.

When all is configured your "Purchases" entry in your App Privacy page should end up looking like this:

![Purchases entry with only 'Used for Analytics' in the box](/docs/images/purchases-privacy-box.png)
