---
title: Insights Reference
tags: Headlinedocs, Docs, Insights
testedOn: Xcode 12.3 & Swift 5.3
description: A reference of all things configurable in an Insight and what they mean
lead: An Insight is a configurable way of looking at your signal data. You can think of it as a pre-defined database query with filters and groupings. This query will be run on the set of signals received in the currently visible date range (which is displayed in the top toolbar) and displayed in a customizable way. This document gives you a reference to the various parts of the Insight configuration and what they mean.
---

Insights are incredibly versatile: They can count either Signals or Users (or, soon, sessions). They can be restricted
to specific signal _types_, such as "the app launched" or "the user did x". They can be filtered by their metadata, e.g.
only show signals from iOS, or a specific app version.

They can show a breakdown of all available values for a given metadata key; this makes it easy to e.g. show what
percentage of an app's users have a feature enabled or which platform the app is used on the most.

Time-wise, insights can group their signals by hour, day, week, or month, allowing for either a fine-grained view or a good
overview.

Finally, all insights can display their data as a table, bar, or line chart, or as a donut or pie chart. All this
configuration can be changed and experimented with on the fly and allows developers who use TelemetryDeck to deep dive
into their data quickly and easily.

## Insight Data

Each insight runs its filters, groupings, and breakdowns (see below for more on those) on all Signals that were received for the currently selected app in the currently selected date range.

Signals have a **type** which is the name of the signal such as `AppLaunchedViaNotification` or `SettingsShown`, a **user** which is a string representation of a hashed user identifier, plus a **payload** which consists of various metadata, such as `operatingSystem`, `platform`, or custom metadata you want to deliver with each signal.

Calculating an Insight's data will yield a number of, for lack of a better word, rows of data, with each line having a title (either a string or a date) and a result (either a string or a number).

Here are some examples of what a line of data could be:

- a time series with each line representing a date, and the number of active users on that date
- a breakdown of the usage of a feature, with one line "enabled" and the number of users who have that feature enabled, and one line called "disabled"
- a single line for the active users in the current month

---

## Title and Subtitle

### Title

The title that will be displayed on top of any visual display of the insight. Example: "Daily Active Users"

### Subtitle

An optional subtitle for the Insight. Currently this subtitle is not displayed except in the Insight Editor itself. You can use it to save a longer description of the Insight.

### Show Expanded

If "Show Expanded" is active, the Insight will be displayed in a larger frame, and before any non-expanded Insights. This allows you to see your most important Insights on top and with extra detail.

---

## Chart Type

Chart Type can be one of these options

### Raw

Will display the query result as a raw list of numbers. If the query results in a time series, this will give you a list of dates and the numbers associated with those dates. If the query is a breakdown, this will give you a key-value list, such as the number of users per device type.

If only one line of data is returned, that line will be displayed in large type. If exactly two rows of data are returned, the first one will be displayed in large type and the second one smaller below that, with the percentage difference between the two numbers. This allows you to have a "Active Users this Month" type of display, with a comparison to the previous month.

### Bar Chart

Will display the query result as a vertical bar chart, one bar per line of data. This works for both time series data and other types, such as breakdowns.

### Line Chart

Will display the query result as a line chart, one bar per line of data. This works best for time-series data, displaying other data doesn't make a lot of sense in this chart type.

### Donut Chart

A pie/donut type chart that will sort the rows of data by number, and visually show their percentage of the whole.

---

## Group Values By

Group signals by time interval. The more fine-grained the grouping, the more separate values you'll receive.

This will put your signals in datetime-based buckets, depending on the time they were received. The more fine-grained settings, like hour and day, are great for looking at individual days or weeks. Settings like week and month are great for month-over-month or year-over-year comparisons, and are especially important if your users don't use your app daily.

---

## Signal Type

Insights that don't have a signal type specified will take all signals for the current app that were received in the currently selected date range. If you do specify a signal type, only signals of that type will be included in the Insight's calculation.

**Hint:** Take care to spell the signal type correctly. Signal types are case-sensitive. If you are unsure of the correct spelling, a look into the **lexicon** or the **list of recent signals** might help.

### Unique by User

If **unique by user** is unchecked, an Insight will count all signals that it applies to. If **unique by user** is checked, each user will only be counted once. If the set of signals counted by the Insight will contain multiple signals from the same user, only the newest of those will be counted. This is great for counting users, e.g. "How many users are using feature x?"

---

## Breakdown

If you enter a breakdown key for an Insight, calculation will switch from time series mode to breakdown mode, and result in a breakdown of possible values for the specified metadata payload key. For example: All signals by default contain the system version of the sending app in their metadata. If you enter `systemVersion` as breakdown key, you'll receive rows specifying how many signals were received for each possible system version.

**Hints:**

1. Breakdowns pair well with the donut chart as a Chart Type.
2. If you're interested in the number of **users** per e.g. system version instead of the number of signals, enabled the _unique by user_ option in _Signal Type_.

---

## Filters

**Note:** Support for entering filters is currently poor in the TelemetryDeck Viewer app, but will improve in future releases. Sorry for that.

Filters consist of a **key** and a **value**. If any filters are entered for an Insight, the Insight will only count signals with that key-value-pair in their metadata payload. If multiple filters are entered, all filters must apply for a signal to be counted.

If, for example, you use the same code base for the iOS and macOS version of your app, but you want a breakdown of only iOS signals, add a filter of `platform: iOS` to your Insight.
