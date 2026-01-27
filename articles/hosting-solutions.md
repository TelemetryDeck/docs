---
title: Hosting Solutions at TelemetryDeck
tags:
  - setup
  - hosting
  - privacy
lead: Since we started with our public beta in 2021, we have been hosting TelemetryDeck, its customers, and data in the cloud. We currently don’t offer on-premise hosting or self-hosted solutions.
---

One reason is our [Double-Hashing anonymization method](https://telemetrydeck.com/docs/articles/anonymization-how-it-works/). It requires two distinct parties to use their own private keys to make sure neither can retrieve any personally identifiable information. When an event arrives on the server, we add our own salt to the user identifier and hash it again. This ensures that neither TelemetryDeck nor you can reconstruct the original identifier, protecting the user’s privacy.

Another reason is how we think about data protection. We handle data with one of [the strongest data protection laws in mind](https://telemetrydeck.com/blog/privacy-by-design-vs-privacy-by-paperwork/) - and this way we can always make sure our customers use TelemetryDeck with strong data protection regulations.

TelemetryDeck is always hosted in the cloud. Additionally, we save our customers tons of infrastructure cost and work by taking care of all hosting, bandwidth, and security, all hosted within the EU.

{% callToAction "Try TelemetryDeck today" "Track user engagement with the fastest privacy friendly setup you can find" %}
