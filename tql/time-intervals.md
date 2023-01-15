---
title: Time intervals and relative time intervals
tags: intervals
description: How to to define absolute or relative time intervals for your queries
lead: A TelemetryDeck query always affects a certain time interval, which you can specify either in absolute terms, or relative to the query execution time.
order: 120
---

A TelemetryDeck query always needs at least one specified time interval to run against. You can either specify a specific time interval (such as "June 1st, 2022 to June 31st, 2022"), or you can use a relative time interval (such as "the last 30 days").

It is possible to specify multiple disjunct intervals for a query, for example to compare the current month with the same month last year.

A TelemetryDeck query can either have the `relativeIntervals` property set to an array of Relative Time Interval objects or have the `intervals` property set to an array of Absolute Time Interval strings.

## Relative Time Intervals

In the following example, we're going to use relative time intervals. Here's an example relative interval for the last 30 days.

```json
{
  "beginningDate": {
    "component": "day",
    "offset": -30,
    "position": "beginning"
  },
  "endDate": {
    "component": "day",
    "offset": 0,
    "position": "end"
  }
}
```

The `beginningDate` is the start of the interval, and the `endDate` is the end of the interval. The `component` is the time unit, and the `offset` is the number of units. The `position` is either "beginning" or "end", and determines whether the point in time is at the very `beginning` or the very `end` of the component – usually, you'll want `beginning` for the `beginningDate` and `end` for the `endDate`.

## Absolute Time Intervals

An absolute time interval object is a string containing two ISO-8601 timestamps separated by a `/` character:

```json
"2012-01-01T00:00:00.000/2012-01-03T00:00:00.000"
```
