---
title: Timeseries Query
description: Groups a set of events by time and aggregates them by the chosen granularity in the TelemetryDeck Query Language.
lead: Groups a set of events by time and aggregates them by the chosen granularity.
order: 20
---

The timeseries query groups a set of events by time and aggregates them by the chosen granularity. for example "How many users used my app per day in the last 30 days?"

## Examples

This query returns the number of signals per day.

It uses the `timeseries` query type, and the `day` granularity. It also aggregates using the `longSum` aggregator, which sums up the values of the `count` field. This is because TelemetryDeck stores multiple identical signals as one signal with a `count` field that contains the number of identical signals.

No time interval is given, so it will use the default time interval supplied by the query runner or the UI.

```json
{
  "aggregations": [
    {
      "fieldName": "count",
      "name": "count",
      "type": "longSum"
    }
  ],
  "dataSource": "telemetry-signals",
  "granularity": "day",
  "queryType": "timeseries"
}
```

This query returns the number of users per week:

```json
{
  "aggregations": [
    {
      "fieldName": "clientUser",
      "name": "count",
      "type": "thetaSketch"
    }
  ],
  "dataSource": "telemetry-signals",
  "granularity": "week",
  "queryType": "timeseries"
}
```

## Properties

All [default properties](/docs/tql/query/) and the following properties are supported:

[descending](/docs/tql/descending/) (optional)
: Whether to sort the results in descending order. The default is false.
