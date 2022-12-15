---
title: How app tracking transparency affects app developers
tags:
  - privacy
  - ATT
description: How iOS 14.5 is changing the playing field for App Developers and how it affects you.
lead: With iOS 14.5, Apple is introducing App Tracking Transparency, a new feature to make sure apps and services are not tracking users between apps. Here's how that affects app developers
searchEngineTitle: App tracking transparency and the impact on developers
searchEngineDescription: How iOS 14.5 App Tracking Transparency (ATT) is changing the rule book for App Developers and how it affects you.
---

As Apple is introducing this newest privacy feature, app developers will have to inform themselves whether the change
applies to them. We all want what's best for our users, and we want to be honest with them. At the same time, we would
like our apps' user experience to be as smooth as possible, and displaying a scary dialog will likely diminish that.

## What this is

App Tracking Transparency (ATT) is an iOS 14.5 feature that requires apps to be more transparent about how they track
their users. For example, Twitter can still track how users use its app and website, but couldn't then track their
usage of other companies’ apps without now getting permission first.

According to Apple in [User Privacy and Data Use](https://developer.apple.com/app-store/user-privacy-and-data-use/):

> Tracking refers to the act of linking user or device data collected from your app with user or device data collected from other companies’ apps, websites, or offline properties for targeted advertising or advertising measurement purposes. Tracking also refers to sharing user or device data with data brokers.

What this means is that the **Tracking** part of App Tracking Transparency refers explicitly to **tracking users across
apps**. Here are some more examples of tracking from the [User Privacy and Data Use page](https://developer.apple.com/app-store/user-privacy-and-data-use/):

- Displaying targeted advertisements in your app based on user data collected from apps and websites owned by other
  companies.
- Sharing device location data or email lists with a data broker.
- Sharing a list of emails, advertising IDs, or other IDs with a third-party advertising network that uses that
  information to retarget those users in other developers’ apps or to find similar users.
- Placing a third-party SDK in your app that combines user data from your app with user data from other developers’ apps
  to target advertising or measure advertising efficiency, even if you don’t use the SDK for these purposes. For
  example, using an analytics SDK that repurposes the data it collects from your app to enable targeted advertising in
  other developers’ apps.

## What this is not

It is important that Apple makes it very clear what falls under ATT and what does not. Specifically, that your own
analytics does not fall under ATT, because it does not need to use the _Advertising Identifier_ (IDFA) and the data is
not being linked to data from other sources.

Another thing that is very clearly not related to ATT is the collection of anonymous usage data.

A third thing that does not fall under ATT is the collection of user data that is relevant to your app and does not
leave the app to be sold to some data brokers. For example, if your app is a shopping list, you are very clearly
allowed to save the user's shopping list items on a server in order to sync them.

## What does that mean for us indie developers?

It is very likely that indie devs will only be affected by this if they are either

1. using an external advertising SDK like Facebook Ads or Google Ads, or
2. using a very intrusive analytics tool.

The first case, external advertising SDKs, is pretty definitive: Those will extremely likely have to use the advertising
identifier (IDFA), and therefore trigger the App Tracking Transparency dialog. Can't be helped. In this case, Apple has
decided that your users' right to privacy trumps your ad service's right to their data.

The second case is not as clear-cut. Many large, free analytics tools like Firebase and Google Analytics are using the
IDFA because it helps them follow users across apps and websites more easily, allowing them to gather more data. This
can help you as a developer in order to understand your users better, but it also helps these companies directly,
because they can use the data you collect for them for other purposes.

In this case, you might have to either accept you're going to disrupt your users' days a bit with the sudden appearance
of an ATT dialog, or you might have to switch away to a different analytics tool.

## Alternatives to Firebase and Google Analytics

Here are some directions you could go if you decide to part ways with analytics tools that are too data-hungry:

### No Analytics

A drastic measure would be to just go without and hope your users are tweeting at you every now and then and telling you
how they use your app. This is entirely possible, especially for smaller apps or developers who have impeccable taste.
But I wouldn't recommend it.

### Apple's App Store Analytics

Apple's own analytics are enabled by default, are very good for user privacy, and definitely won't trigger the ATT
dialog. The only problem is, I wouldn't really call them analytics: The information you get is important, like how
many downloads and app launches you got last week, but it is neither immediate nor very deep. You won't get live data
and there is practically no information on _how_ users use your app. It's a good start, but for many, it won't be
enough.

### TelemetryDeck

I might be biased (spoiler: I am very biased in this regard), but I think TelemetryDeck is an amazing alternative here:
TelemetryDeck gives you completely anonymized usage data of how users use your app. This means you'll get a deep dive
into usage patterns, flows, and configuration, without compromising your users' privacy.

Your users will have the comfort of knowing their data is not being shared with other third parties, and they won't have
to think about App Tracking Transparency dialogs. Meanwhile, you as the developer will be able to get all the
information you need to improve, enhance and boost your app!

Why not [try it out now](https://dashboard.telemetrydeck.com/registration/organization)? It's free and easy to start, and your users' privacy will thank you! 😊

<a class="nav-btn btn btn-gradient text-white" href="https://dashboard.telemetrydeck.com/registration/organization">Download the TelemetryDeck Beta Now</a>
