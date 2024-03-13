---
title: Privacy FAQ
tags:
  - Setup
  - Privacy
featured: true
description: Frequently asked questions about TelemetryDeck's Privacy Policy
lead: This FAQ answers the most common questions about our Privacy Policy and how to answer your users' questions.
order: 10000
headerImage: /docs/images/faq.jpg
---

## What is TelemetryDeck?

TelemetryDeck is a privacy friendly analytics platform for mobile, desktop and web application. It helps you understand how your users are using your app, and how you can improve it. TelemetryDeck is privacy friendly and will never collect personally identifiable information.

## What data does TelemetryDeck collect?

TelemetryDeck collects only the data that you explicitly send to it. It does not collect any data automatically. Any user identifiers are thoroughly anonymized before they are sent to TelemetryDeck – and the word "anonymized" is used here as defined by the GDPR, meaning that TelemetryDeck only ever collects data that is not personally identifiable and does not strictly fall under the GDPR or other privacy laws.

## Where is TelemetryDeck's Privacy Policy?

Our [Privacy Policy](/privacy) covers both our customers and their users. It is written in plain English and is easy to understand.

## Where is TelemetryDeck hosted?

We host our servers in Amsterdam, The Netherlands. We use [Microsoft Azure](https://azure.microsoft.com) as our hosting provider.

## Do I need to add TelemetryDeck to my privacy policy?

No. TelemetryDeck does not collect any data governed by privacy laws such as GDPR or CCPA so you do not need to add TelemetryDeck to your privacy policy.

However, we think it's a good idea to mention TelemetryDeck in your privacy policy anyway. It's a good way to show your users that you care about their privacy and that you are transparent about the data you collect.

Here's an example of how you could mention TelemetryDeck in your privacy policy:

> We use TelemetryDeck to collect anonymized usage data. This helps us understand how our users are using our app and how we can improve it. TelemetryDeck does not collect any personally identifiable information. You can read more about TelemetryDeck's privacy policy at https://telemetrydeck.com/privacy

## Do I need to fill out Apple's app privacy details?

By default, the privacy manifest metadata included in the TelemetryDeck Swift SDK should already fill out Apple App Privacy Details information for you. See our [App Privacy Guide](/docs/articles/apple-app-privacy/) for more information.

## Do I need to offer an opt-out from TelemetryDeck?

Legally, no. TelemetryDeck does not collect any data that is governed by privacy laws such as GDPR or CCPA so you do not need to offer an opt-out from TelemetryDeck.

In many cases, users will find being asked about their privacy preferences annoying when done in the wrong way. You've already chosen the privacy-preserving alternative, so why not revel in that fact. If you offer an opt-out, we recommend not showing this at startup but rather in a settings screen.

## Do I need to show a cookie banner for TelemetryDeck?

No. TelemetryDeck does not use cookies.

## How does TelemetryDeck anonymize user identifiers?

See our article [How TelemetryDeck anonymizes user identifiers](/docs/articles/anonymization-how-it-works/)

## What data does TelemetryDeck collect from my app users?

By default, TelemetryDeck collects the following metadata from app users:

- clientUser: The anonymized user identifier that you can use to identify a user
- type: The type of the signal, e.g. "event" or "error"
- time: The timestamp of the signal, rounded down to the hour
- App Information: appVersion, buildNumber, App Store vs TestFlight and appID
- Device Information: architecture, locale, operating system version, device model, platform
- The SDK Version

Developers can optionally send additional metadata with each signal.

### What data does TelemetryDeck collect from my website visitors?

See the [Web Setup Guide](/docs/guides/web-setup/#what-data-is-collected%3F) for a list of data that TelemetryDeck collects from websites.
