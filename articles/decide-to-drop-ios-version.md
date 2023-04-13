---
title: Picking your minimum iOS or Android version
description: Which minimum iOS or Android version should I pick?
lead: New OS versions give us new features and new possibilities, but not everyone updates right away. When is the right time to upgrade your requirements?
searchEngineTitle:
searchEngineDescription: Choosing the minimum OS versions, both for iOS and Android, helps you understand how many versions you should support.
order: 30
---

New versions of the Operating System give us new features and new possibilities. They expose new APIs or update the capabilities of existing ones. However, you'll always lose a certain portion of your users because they are staying on the old version. Here are a few ways to help you decide:

## Always require the newest version

Always require the newest version of the Operating System as soon as it's released. This will give you all the cool new hotness, but it'll mean that a lot of users will be left behind. People who can't upgrade because their devices are too old. People who are rightfully skeptical of the new version and prefer to wait a bit. People who are not sure if they want to upgrade or not.

## Lag _n_ versions behind

This is a tactic that a lot of indie developers use. It's a good idea to require a version of the OS that's one version, two versions, three versions behind the latest version. This will give you new features later, but it will probably keep compatibility with a large chunk of your user base. You might even be able to use some of the new features already, if you can keep them behind some kind of compatibility gate. A bit more complex, but oftentimes worth it.

The downside is that you might wait too long, to implement new cool features that would drive adoption and growth of your app. While everyone on the internet is talking about the new stuff, your app might feel dusty and old.

## The compromise: Use a data-driven approach

Instead of using these absolute rules, consider using a data-based heuristic approach. This will give you a lot of flexibility, and it will also mean that you can predict in advance how many users you'll lose, should you drop an old version of the OS.

The TelemetryDeck SDK by default tries to collect data about the user's operating system version. You can then use this data to decide when to drop the OS version. Our recommendation is: drop a version when less than **10% of your users** are using it.

To find out which percentage of your users are using a certain OS version, use a **Breakdown Insight** (also known as a **Top N Insight**). Then you'll have multiple options for the breakdown key.

### Top N `systemVersion`

The most detailed breakdown key is the `systemVersion`. It's a string that represents the complete version of the OS, major, minor, and patch. For example, `iOS 15.1.1`. This is helpful if you want an idea whether a certain patch has been applied, a certain bug has been fixed in the OS, that kind of thing. However, it's not useful if you want to know how many users are using a certain _major_ version of the OS.

### Top N `majorMinorVersion`

The `majorMinorVersion` breakdown key is a string that represents the major and minor version of the OS. For example, `iOS 15.1`. This is more helpful, since most operating system vendors release these minor versions every few months. Using this data, you can decide when to maybe require iOS 15.1 instead of 15.0 for example.

### Top N `majorVersion`

The `majorVersion` breakdown key is a string that represents the major version of the OS. For example, `iOS 15`. This is what most of your decisions in this space should be based on, since most of the time you'll want to drop a _major_ version of the operating system. Most operating system vendors release these major versions every few years. Using this data, you can decide when to maybe require iOS 15 instead of 14 for example.

## That's it!

We hope this article gave you a little overview on what you can do to decide when to drop a previous version of the OS. If you have any questions, feel free to ask on [Twitter @Telemetry_Deck](https://twitter.com/telemetry_deck) and we'll be happy to talk.
