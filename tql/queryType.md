---
title: Query Type
description: The type of TelemetryDeck query, for example `timeseries`, `topN`, `groupBy`, `funnel`.
lead: The type of query, for example `timeseries`, `topN`, `groupBy`, `funnel`.
order: 10
---

The following query types are supported:

[timeseries](/docs/tql/timeseries/)
: Groups a set of events by time and aggregates them by the chosen granularity. for example "How many users used my app per day in the last 30 days?"

[topN](/docs/tql/topN/)
: Groups a set of events by a dimension and aggregates them by a metric. for example "What are the top 10 countries by number of users?"

[groupBy](/docs/tql/groupBy/)
: Groups a set of events by a set of dimensions and aggregates them by a set of metrics. for example "How many users are there per country and per device?"

[funnel](/docs/tql/funnels/)
: Groups a set of events by a set of steps and aggregates them by a set of metrics. for example "How many users went through the funnel steps 'Login' -> 'View Product' -> 'Purchase'?"
