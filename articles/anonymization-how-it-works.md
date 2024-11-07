---
title: Anonymization of user data
tags:
  - setup
  - how-to
  - privacy
description: TelemetryDeck anonymizes user data, by double salting and hashing IDs, to ensure anonymity and protect user privacy while still providing valuable insights.
lead: We take user privacy seriously. To ensure the privacy of our users, we use various techniques to anonymize user data. One of the ways we do this is by using a double hashing technique to anonymize user identifiers.
searchEngineTitle: How TelemetryDeck anonymizes user data privacy-friendly
searchEngineDescription: TelemetryDeck anonymizes user data, by double hashing and salting IDs, to ensure anonymity and protect user privacy while still providing valuable insights.
headerImage: /docs/images/anonymization-display-image.jpg
---

## Methodology

Anonymizing data involves transforming it to prevent direct linkage to a person. However, if the original data can be recreated with additional information, the transformation only qualifies as pseudonymization. **GDPR considers data truly anonymized** only if the original data can’t be recreated, even with additional information.

At TelemetryDeck, we even go a step further: the “identification date” is no longer available; “re-identification” is thus ruled out and cannot be performed. Therefore, anonymized data is not personal data anymore. [You can check out our code](https://github.com/TelemetryDeck/SwiftSDK/blob/main/Sources/TelemetryDeck/Signals/SignalManager.swift#L135) to confirm the statement for yourself!

## User identifiers

Our SDKs accept a **custom user identifier**, such as an email address or an internal identifier, to help you identify your users. If you don’t supply an identifier, we generate a random one for you. On some platforms, we may ask the operating system for one, such as the iOS `identifierForVendor`.

## Salting and hashing

We salt and hash the identifier **on the user’s device**. If you have a custom salt string, you can provide it using the configuration object. When a signal arrives on our server, **we add our own salt to the user identifier and hash it again**. This ensures that neither TelemetryDeck nor you can reconstruct the original identifier, protecting the user’s privacy.

## Recognizing users

If you use the same (custom) salt and provide the same original identifier, you can recognize the same user across different platforms. For example, if a user logs in to your website using their email address on one device and then switches to your app another device where they are logged in with the same email address, they can still be recognized if the same salt and original identifier are used.

## Conclusion

We hope that this information provides you with a better understanding of how TelemetryDeck anonymizes user data and that we are committed to protecting user privacy! With the above techniques, TelemetryDeck makes sure that user data cannot be traced back to an individual. If you still have any questions or concerns about how TelemetryDeck anonymizes user data, please feel free to contact us!
