---
title: How to name your signal types
tags: best-practices
description: Should you give your signal types a simple name, or use a more complex naming scheme? We'll help you decide.
lead: Should you give your signal types a simple name, or use a more complex naming scheme? We'll help you decide.
---

When you send a signal, you'll always have to tell TelemetryDeck what **type** of signal you want to send. Type is just a
String, so in theory you could add anything in there. Your type could be `asfdgllahsavhaligha`, or `This sentence no verb` or even `🤖`.

But we recommend a different style to keep things clear and easy to find.

## Single word types

If you're just hacking with TelemetryDeck, consider using a single word for your type. It's easy to type, and as long as your app is not too big, it's easy to find the signal type you're looking for.

Examples are:

- `AppLaunchedByNotification`
- `ShareButtonAppeared`
- `SavePreferences`

## Paths in Dot Notation

What many of our customers do (and we ourselves internally as well) is using a dot notation that represents the path of an action or event inside the app.

Here are some examples:

- `InsightEditor.MetaEditor.saveInsight`
- `Main.appLaunched`
- `Preferences.ErrorModal.shown`

We recommend you don’t make the paths too specific or deeper than, say, 3 levels. Otherwise, you’ll run into annoying mismatches when you move a feature around but can’t really rename the insight type to match.

We prefer to use UpperCamelCase for the prefix components but lowerCamelCase for the last component because that matches how calls are made in most programming languages, inluding Swift and Kotlin. The convention there is that type names are uppercased but functions and parameters are lowercased. We feel this style looks more natural alongside other code, but you can of course use a different style, just be consistent with it!

## Distinguishing between views, actions and events

If you want to distinguish between views, actions and events, or just views and actions, you can add that to the type, such as `InsightEditor.MetaEditor.Actions.saveInsight`. However, we don’t get much value from that. Instead, we usually annotate types implicitly using grammar:

1. Present tense compound verbs are actions:

- `InsightEditor.MetaEditor.saveInsight`
- `Preferences.syncNow`

2. Anything in past tense is a view or an event:

- `InsightEditor.appeared`
- `Main.appLaunched`
- `Preferences.ErrorModal.shown`

Don’t be afraid to play around a bit and find out what works best for you!
