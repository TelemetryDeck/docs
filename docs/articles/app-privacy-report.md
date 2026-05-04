---
title: Why is Apple's app privacy report important to you as an app developer?
tags: privacy
description: We evaluate Apple's App Privacy Report from the perspective of app developers and explain common misconceptions.
lead: In this article, we'll take a look at the new privacy report that Apple is making available to iPhone users. We are particularly interested in. What are the implications of this feature for app developers?
searchEngineTitle: How to use Apple's app privacy report as a developer
searchEngineDescription: What is the iOS and iPadOS App Privacy Report? And how to use it as a privacy orientated app developer?
---

## What is the App Privacy Report?

Starting in iOS 15.2, the operating system collects all domains that are contacted by an app. The App Privacy Report provides users with a summary of this information. The list shows: Which app has contacted which domain and how often. Also interesting: The report shows how often an app has requested the microphone, camera, GPS locations, photos and contacts.

The purpose of the App Privacy Report is to make it easier for users to identify unfair app practices. For example, thanks to the new report, you can see if you have installed an app that constantly shares your location or if an app matches contacts from your address book.

## How to interpret the App Privacy Report correctly

The App Privacy Report is a powerful tool that you can have a lot of fun with (fun in the sense of spooky insights). Unfortunately, it also holds a lot of potential for misunderstanding.

If an app contacts a lot of domains, at first glance it might look like surveillance to inexperienced users. So you have to look closely at what the particular purpose of this app is and which domains are contacted. For example, an app that synchronizes files to different cloud storage providers logically needs to contact all these cloud storage providers as well. For a banking app, however, calling Facebook would be unusual.

You have to evaluate each app individually step by step and remind yourself what you actually use the app for in everyday life. Of course it looks strange when Instagram constantly accesses my microphone. But in fact, it's not because of a big bugging operation, but because I'm constantly making videos of myself.

To be able to interpret the list in the privacy report, users need some technical background knowledge. Not every connection is automatically evil. You should still be vigilant.

These contacted domains indicate that an app is intensively monitoring its users (and the data will most likely end up in an advertising network, which will then be used to play out personal ads):

- `admob`
- `doubleclick`
- `facebook`
- `adcolony`
- `fbcdn`
- `ga`
- and so on

## What entry do users see when an app uses TelemetryDeck?

Apps that have TelemetryDeck embedded contact the domain `nom.telemetrydeck.com`. And that is exactly what is seen in the App Privacy Report. "Nom" is the point where our server picks up the signals, that is, eats them. Nom Nom… you know what I mean? Maybe we should put a GIF of the Cookie Monster in there some time…

## Is the App Privacy Report good or ad for app developers?

Our conclusion: The App Privacy Report helps users who have some prior technical knowledge to form a judgment about individual apps. It is fun to search for trackers and then raise an eyebrow in disdain when you discover one.

An app with a particularly clean privacy report, on the other hand, will make you feel good - especially if it processes sensitive data.

Analytics is important and privacy is important. The app privacy report lets your users see what's going on at a glance. So choose your analytics software wisely.

---

Why not [try TelemetryDeck now](https://dashboard.telemetrydeck.com/register?source=doc_att)? It's quick, helpful, free, and your users' privacy will thank you! 😊
