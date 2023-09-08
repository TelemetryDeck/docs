---
title: Apple's app privacy details
tags: setup
description: Apple's App Store now requires developers to show a Privacy Details section. Here's how to fill out this section when you are using TelemetryDeck.
lead: Apple's App Store now requires developers to show a Privacy Details section. Here's how to fill out this section when you are using TelemetryDeck.
searchEngineTitle: How to set up Apple's app privacy details
searchEngineDescription: The App Store now displays an app's privacy practice as a measure to help users. Here's how you can set it up for your app.
---

Starting December 8, 2020, the Apple App Store will require developers to include a section on [App Privacy Details](https://developer.apple.com/app-store/app-privacy-details/) with their App Store listing.

Since TelemetryDeck's analytics are private by default, you can include this information easily: The only information TelemetryDeck collects is

- Identifiers (not personally identifiable information)
- and Usage Data (also not personally identifiable information)

This means your app will get an excellent privacy rating.

{% noteinfo "Automatic Setup" %}

With version 1.5.0 of the [TelemetryDeck Swfit SDK](https://github.com/TelemetryDeck/SwiftClient), you don't need to manually set up the App Store privacy details any more. Instead, the SDK includes a [Privacy Manifest](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files) that will automatically set up the correct labels for you.

If you're using 1.5.0 or above, you can safely ignore the rest of this document.

{% endnoteinfo %}

![A screenshot of Apple's Privacy Overview](/docs/images/privacy-overview.png)

## How do I start?

1. Go to [App Store Connect](https://appstoreconnect.apple.com), click on **My Apps**, and then on the app you want to set up with Privacy Details.
2. In the left sidebar, under the **General** heading, click on **App Privacy**.
3. At the bottom of screen screen, click **Get Started**

## Data Types

First Screen: TelemetryDeck does collect data, so answer **Yes, we collect data from this app** and click **Next**.

### Identifiers

In the second screen, scroll down until you see the **Identifiers** section.

In TelemetryDeck's **default mode**, with no user identifier specified, check the **Device ID** checkmark. This is what identifies individual users to TelemetryDeck.

{% noteinfo "Other Types of Identifiers" %}

In case you use TelemetryDeck in a more advanced way where you supply a custom user identifier, you'll need to think about this for a second:

- If you instead specify a User Identifier such as email address or username to TelemetryDeck, check instead the **User ID** checkmark. The identifier is only transmitted as a hash, but it still counts as a user identifier.
- If you instead are purposefully disabling user tracking by handing the same string to TelemetryDeck for each user, you don't need to check any of the checkboxes in the **Identifiers** section.

{% endnoteinfo %}

### Usage Data

Now scroll further down to the **Usage Data** section and check the **Product Interaction** checkbox, and you're done with the first part. Click Save and you'll be returned to the main screen, where it'll say _2 data types collected from this app: Device ID, Product Interaction_.

Next up, you'll need to give Apple more information about the Device ID and how the Product Interaction works.

## Device ID

In the newly appeared **Identifiers** section, click **Set Up Device ID**. In the dialog, check the checkbox next to **Analytics** and click **Next**.

The next question is **Are the device IDs collected from this app linked to the user’s identity?** Unless you are specifically adding user identifiable information to your Signal payloads, you can answer **No** to this question, and click **Next**.

The next screen defines various terms, such as _Tracking_ and _Third-Party Data_. After reading through it, click next, and next again until you reach the next question.

TelemetryDeck does not fall under the definition of tracking. Care is taken to dis-associate ID's in TelemetryDeck from any real world person. Unless you do other tracking unrelated to the Device ID, answer **No, we do not use device IDs for tracking purposes**.

Next, we are back at the main screen and need to set up Usage Data.

## Usage Data

To begin, click **Set Up Product Interaction**. We only use Usage Data for Analytics, so enable the checkbox next to **Analytics** and click **Next**.

Similar to the user identifier, we do not link this data to personally identifiable data. Select **No, product interaction data collected from this app is not linked to the user’s identity** and click next.

The next two screens are information screens. After reading them, click **Next** on each.

Finally, we are asked if product information is used for tracking purposes. That is not the case, so select **No, we do not use product interaction data for tracking purposes** and click **Save**.

## That's it!

And you're done! Your app now has a complete set of privacy details, and thanks to TelemetryDeck's privacy-first design, you'll still get all the value of analytics, while still giving your users excellent privacy!
