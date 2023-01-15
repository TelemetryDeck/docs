---
title: Timeseries Query
description: Groups a set of events by time and aggregates them by the chosen granularity in the TelemetryDeck Query Language.
lead: Groups a set of events by time and aggregates them by the chosen granularity.
order: 20
---

The timeseries query groups a set of events by time and aggregates them by the chosen granularity. E.g. "How many users used my app per day in the last 30 days?"

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

[type](/docs/tql/querytype/)
: The type of query, in this case `"timeseries"`.

[dataSource](/docs/tql/datasource/)
: The data source to query. Must be `"telemetry-signals"`.

[granularity](/docs/tql/granularity/)
: The granularity of the query.

[relativeIntervals](/docs/tql/time-intervals/) (optional)
: The time intervals to query, specified as relative to time of query.

[intervals](/docs/tql/time-intervals/) (optional)
: The time intervals to query, specified as absolute time intervals.

[descending](/docs/tql/descending/) (optional)
: Whether to sort the results in descending order.

[baseFilters](/docs/tql/basefilters/) (optional)
: A list of filters that are applied to all queries.

[filter](/docs/tql/filter/) (optional)
: A filter that is applied to the query.

[aggregations](/docs/tql/aggregations/) (optional)
: A list of aggregations to apply to the query.

[postAggregations](/docs/tql/postaggregations/) (optional)
: A list of post aggregations to apply to the query.

[limit](/docs/tql/limit/) (optional)
: The maximum number of results to return.
