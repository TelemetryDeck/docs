---
title: TelemetryDeck's Grand Rename
tags: setup
description: To avoid ambiguity and clean up things for the long term, we have decided to rename quite a few things in all the TelemetryDeck SDKs. We have laid out a migration path, here's all you need to know about it.
lead: To avoid ambiguity and clean up things for the long term, we have decided to rename quite a few things in all the TelemetryDeck SDKs. We have laid out a migration path, here's all you need to know about it.
---

## Motivation

When we started TelemetryDeck, it was clearly scoped to the iOS platform and we naturally started with a Swift client first. To get to speed quickly like one does, we decided to send a defualt signal & a bunch of parameters automatically. To keep things simple, we named the signal `newSessionBegan` the parameters `appVersion` and `locale`, for example.

But over time, we added more and more SDKs and now we have 5, but only 4 of them are also called "SDK": The initial Swift client was simply called "SwiftClient". We used the platform-specific terminology for things, leading to different names in some places. And we also learned the power of grouping signal names and event parameters as documented in our [naming guideline](https://telemetrydeck.com/docs/articles/signal-type-naming/). Because we sort everything alphabetically in our UI, it's a natural help in finding things more quickly if related things have the same prefix. Also, users could accidentally use the same signal or parameter name and override ours, causing confusion in the insight data.

After more than 3 years working on TelemetryDeck, we think it's about time to streamline things for a more clear long-term future.

## Consistency, Longevity, and Clarity

Our main goals with our new naming scheme were to be internally consistent, but at the same time make sure the names are abstract enough to work flexibly for changes to come in the foreseeable future. Too abstract names can be confusing and cumbersome, so we additionally strived for clarity.

The most obvious change was to rename our Swift repository from "SwiftClient" to "SwiftSDK". Thanks to GitHub redirections, this change should have no effect on our existing customers, but long term, it should make things more consistent. 🎉

For our signals & parameters, we decided the prefix them with `TelemetryDeck` to make the source clear and avoid amgiguity. Additionally, we analyzed all the signals and parameters we currently send and future ones we have in our roadmap and grouped them as follows:

### Signals

-

### Parameters

-

{% noteinfo "No action needed" %}
To make sure these changes don't affect existing customers with existing insights anytime soon, we decided to keep sending the old names for a transition period of at least 1 year while also sending the new ones. We have also auto-migrated any insights that were using the old names in their filters to work with the new system. This was safely achieved by replacing filters like "platform == iOS" with something like "platform == iOS OR TelemetryDeck.SystemInfo.platform == iOS" accepting both styles, ensuring you will continue to see historic data from before the transition, during the transition, and after the transition.
{% endnoteinfo %}

<!-- Discussion: What about Top-N insights that use a parameter like "appVersion" which got renamed to "TelemetryDeck.SystemInfo.appVersion"? -->

## Filling the Gaps

While doing the rename, we also noticed some missing variants of parameters that could be useful. So we added the following variants:

-

These could be useful to create even more accurate charts to make better informed decisions.

## Full Migration Table

Here's a full overview of all the changes we have done:


| Old Name                   | New Name                                                |
|----------------------------|---------------------------------------------------------|
| X                          | Y                                                       |
| X                          | Y                                                       |
| X                          | Y                                                       |
| X                          | Y                                                       |
| X                          | Y                                                       |
| X                          | Y                                                       |
| X                          | Y                                                       |
| X                          | Y                                                       |
| X                          | Y                                                       |
| X                          | Y                                                       |
| X                          | Y                                                       |
| X                          | Y                                                       |
| X                          | Y                                                       |
| X                          | Y                                                       |
| X                          | Y                                                       |
| X                          | Y                                                       |
| X                          | Y                                                       |
| X                          | Y                                                       |
| X                          | Y                                                       |
| X                          | Y                                                       |
| X                          | Y                                                       |
| X                          | Y                                                       |
| X                          | Y                                                       |
| X                          | Y                                                       |
| X                          | Y                                                       |
| X                          | Y                                                       |
| X                          | Y                                                       |
| X                          | Y                                                       |
| X                          | Y                                                       |
| X                          | Y                                                       |
| X                          | Y                                                       |
| X                          | Y                                                       |
| X                          | Y                                                       |


We hope you like these changes as much as we do!
While we did our best to not affect any data, we might have missed something, so please contact us if you run into any issues.
