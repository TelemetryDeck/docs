---
title: Using TelemetryDeck with RevenueCat
tags:
  - how-to
  - iOS
testedOn: RevenueCat Swift SDK 5.2.3
description: Here's how to integrate TelemetryDeck with RevenueCat to combine usage data with purchase data.
lead: Here's how to integrate TelemetryDeck with RevenueCat to combine usage data with purchase data.
order: 90
---

[RevenueCat](https://www.revenuecat.com/) is a service that helps you process payments and in-app purchases on iOS, Android, and the web. It's a great way to add monetization to your app.

RevenueCat pairs excellently with TelemetryDeck – use TelemetryDeck to improve your users' flow through your application, and then present them with convenient In-App-Purchase offers.

With this integration, you can import your RevenueCat events into TelemetryDeck, and see everything on one dashboard. We'll be using RevenueCat's _Webhooks_ feature to pass on their data to TelemetryDeck.

{% noteinfo "Read the announcement" %}

Our [announcement blog post](https://telemetrydeck.com/blog/revenuecat-integration/) shows you what to expect, how to use the new revenue dashboard, and gives examples on what to do with your revenue data.

{% endnoteinfo %}

## Installing RevenueCat and TelemetryDeck

First, we have to integrate both TelemetryDeck and RevenueCat into your app. You can find guides for both here:

1. [Install and set up TelemetryDeck](/docs/guides/swift-setup/)
2. [Install and set up RevenueCat](https://www.revenuecat.com/docs/getting-started/installation)

## Configuring the RevenueCat SDK

RevenueCat has a concept of **user attributes**. Our goal is to set two new user attributes for our RevenueCat users that will make TelemetryDeck recognize them as the same users it is already managing.

- `$telemetryDeckAppId`: This attribute should be set to your TelemetryDeck App ID, the same one you pass into the TelemetryDeck SDK for initialization.
- `$telemetryDeckUserId`: This attribute needs to be the **already-hashed user identifier** that TelemetryDeck is using.

{% noteinfo "RevenueCat gets the hashed version of the TelemetryDeck User Identifier" %}

While the TelemetryDeck SDK usually takes care of hashing for you, you'll need to extract the identifier after it's been hashed and pass that on to RevenueCat. Only then will the final identifiers in your TelemetryDeck dashboard match up.

If your version of the TelemetryDeck SDK does not expose a function to vend the hashed user identifier, you can hash it yourself using something like `SHA256(user_id + salt)`.

{% endnoteinfo %}

### iOS

Here's how to set up TelemetryDeck and RevenueCat on iOS. The setup process is similar for other platforms.

```swift
// 1.
// Initialize TelemetryDeck with your app ID
let telemetrydeckAppID = "AAAAAAAA-BBBB-CCCC-DDDD"
let telemetryDeckConfig = TelemetryDeck.Config(
    appID: telemetrydeckAppID,
    salt: "MY_SECRET_SALT" // optional but recommended
)
TelemetryDeck.initialize(config: telemetryDeckConfig)

// 2.
// Manually set a default user for TelemetryDeck
// We're using IFV here, but you can also use
// e.g. an email address or any other identifying property
let myUserID = UIDevice.current
    .identifierForVendor?.uuidString
    ?? "unknown user"
TelemetryDeck.updateDefaultUserID(to: myUserID)

// 3.
// Set up RevenueCat with your TelemetryDeck App ID
// and the pre-hashed TelemetryDeck User ID
Purchases.configure(withAPIKey: "my_revenuecat_api_key")
Purchases.shared.attribution.setAttributes([
    "$telemetryDeckUserId": TelemetryManager.shared
        .hashedDefaultUser,
    "$telemetryDeckAppId": telemetrydeckAppID
])
```

Here's what's going on in the above example

1. First we set up TelemetryDeck as described in the setup guide. If you already have set up TelemetryDeck, you can leave your setup unchanged.
2. We then manually set a default user for TelemetryDeck. This allows us to later retrieve a hashed version of the user identifier.
3. Finally, we configure RevenueCat and set up the necessary user attributes.

{% notewarning "You need to keep user identifiers in sync" %}

Whenever you update your TelemetryDeck user identifier, you'll also need to update the user identifier in RevenueCat's `$telemetryDeckUserId` user attribute.

{% endnotewarning %}

## Setting up RevenueCat's TelemetryDeck Integration

Now we need to tell RevenueCat to send copies of all events over to TelemetryDeck. We're using a RevenueCat's **TelemetryDeckIntegration** to do this.

- Navigate to your RevenueCat Project
- In the left sidebar, click **Integrations**
- Select **TelemetryDeck**
- Click **Add Integration** to confirm

![A screenshot of RevenueCat's TelemetryDeck Integration](/docs/images/rc-td-1.png)
![A screenshot of RevenueCat's TelemetryDeck Integration](/docs/images/rc-td-2.png)

And you're done. RevenueCat events should now arrive and be mixed in with your TelemetryDeck signals 🥳
