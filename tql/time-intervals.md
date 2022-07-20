---
title: Time intervals and relative time intervals
---

A TelemetryDeck query only always needs a specified time interval. You can either specify a specific time interval (such as "June 1st, 2022 to June 31st, 2022"), or you can use a relative time interval (such as "the last 30 days").

In this example, we're going to use relative time intervals. Here's an example relative interval for the last 30 days.

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
