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

The TelemetryDeck SDK was developed from the ground up with privacy in mind. An important principle of TelemetryDeck is to store only the minimum amount of data necessary to identify specific user behaviors.

The TelemetryDeck SDK code is completely open source, allowing users and app publishers to see for themselves what data the TelemetryDeck SDK stores. TelemetryDeck has never integrated software or equipment for law enforcement agencies into its network.

## What is TelemetryDeck?

TelemetryDeck is a privacy friendly analytics platform for mobile, desktop and web application. It helps you understand how your users are using your app, and how you can improve it. TelemetryDeck is privacy friendly and will never collect personally identifiable information.

TelemetryDeck collects only the data that you explicitly send to it. It does not collect any data automatically. Any user identifiers are thoroughly anonymized before they are sent to TelemetryDeck – and the word "anonymized" is used here as defined by the GDPR, meaning that TelemetryDeck only ever collects data that is not personally identifiable and does not strictly fall under the GDPR or other privacy laws.

## What data is collected by TelemetryDeck SDK for apps?

The data collected on our analytics servers includes the following:

1. An anonymized user ID. This ID is constant for each app installation but cannot be traced back to personal information.
2. An action performed, such as "App launched" or "Settings opened." These actions are defined by the app publisher.
3. A timestamp rounded to the nearest hour when the action was performed.
4. Device metadata, such as system version, app version, build number, whether the build was downloaded from the App Store or TestFlight, and device type (e.g., iPhone X, iPad Air, or iPhone 12). A complete list is available here: https://telemetrydeck.com/docs/ingest/default-parameters/
5. Additional metadata as defined by the app publisher, e.g., "Number of items in the database" or "TelemetryDeck setting is enabled."

IP addresses are never stored on the TelemetryDeck server, neither in the database nor in log files or anywhere else.

For a full list of default paremeters, refer to [our list of default parameters](/docs/ingest/default-parameters/).

Developers can optionally send additional metadata with each signal.

## What data is collected by TelemetryDeck for Web?

The data collectd on our analytics servers includes the following:

1. An anonymized user ID. For Web SDK API requests, we look at the first three triplets of incoming IP addresses to determine the possible country of origin of the request.
2. A timestamp rounded to the nearest hour when the action was performed.
3. Device metadata, such as system version, browser version, whether it is a bot or a visitor, and device type (e.g., iPhone X, iPad Air , or iPhone 12). A complete list is available here: https://telemetrydeck.com/docs/ingest/default-parameters/#web-analytics

IP addresses are never stored on the TelemetryDeck server, neither in the database nor in log files or anywhere else.

## Definitions

- App Publisher: A natural or legal person who creates, publishes, or maintains an app or website that includes the TelemetryDeck SDK. You are responsible for ensuring that only anonymized data is passed to the TelemetryDeck SDK.
- TelemetryDeck SDK: The code that collects data and transmits it to the TelemetryDeck server. It can be viewed in its entirety on GitHub: https://github.com/TelemetryDeck
- Signal/Event: An instance of data sent by the app to the TelemetryDeck server via the TelemetryDeck SDK.

## Where is TelemetryDeck's Privacy Policy?

Our [Privacy Policy](/privacy) covers both our customers and their users. It is written in plain English and is easy to understand.

## Do I need to add TelemetryDeck to my privacy policy?

No. TelemetryDeck does not collect any data governed by privacy laws such as GDPR or CCPA so you do not need to add TelemetryDeck to your privacy policy.

However, we think it's a good idea to mention TelemetryDeck in your privacy policy anyway. It's a good way to show your users that you care about their privacy and that you are transparent about the data you collect.

Here are snippets you can use in your privacy policy:

- [Privacy Policy Snippet in English](https://telemetrydeck.com/privacy-policy-snippet/en)
- [Textbaustein für Datenschutzerklärung in Deutsch](https://telemetrydeck.com/privacy-policy-snippet/de)

## Where is TelemetryDeck hosted?

We distribute our servers between Microsoft Azure, Amazon AWS, and Hetzner GmbH. Azure services are hosted in Amsterdam, the Netherlands,

AWS Services are hosted in Frankfurt, Germany, and Hetzner Services are hosted in Falkenstein, Germany and Nürnberg, Germany.

## Do I need to fill out Apple's app privacy details?

Yes, every app needs to fill out this form, even those that do not track any data. But our Swift SDK includes a privacy manifest which should list all the right things in your [generated privacy report](https://developer.apple.com/documentation/bundleresources/describing-data-use-in-privacy-manifests#Create-your-apps-privacy-report). Alternatively, see our [App Privacy Guide](/docs/articles/apple-app-privacy/) for detailed instructions.

## Do I need to offer an opt-out from TelemetryDeck?

Legally, no. TelemetryDeck does not collect any data that is governed by privacy laws such as GDPR or CCPA so you do not need to offer an opt-out from TelemetryDeck.

In many cases, users will find being asked about their privacy preferences annoying when done in the wrong way. You've already chosen the privacy-preserving alternative, so why not revel in that fact. If you do offer an opt-out, we recommend showing this in a non-blocking dialog or in a settings screen.

## Do I need to show a cookie banner for TelemetryDeck?

No. TelemetryDeck does not use cookies.

## How does TelemetryDeck anonymize user identifiers?

See our article [How TelemetryDeck anonymizes user identifiers](/docs/articles/anonymization-how-it-works/)
