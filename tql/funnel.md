---
title: Funnel Query
description: Groups a set of events by a set of steps and aggregates them by a set of metrics in the TelemetryDeck Query Language.
lead: Groups a set of events by a set of steps and aggregates them by a set of metrics.
order: 50
---

A funnel query is a way of generating a funnel chart. It's compiled at runtime into a [groupBy](/docs/tql/groupBy/) query, but has a vastly simpler syntax.

## Example

This query returns the number of users that went through the funnel steps `Login` -> `View Product` -> `Purchase`:

```json
{
  "dataSource": "telemetry-signals",
  "queryType": "funnel",
  "granularity": "all",
  "steps": [
    {
      "type": "selector",
      "dimension": "event",
      "value": "Login"
    },
    {
      "type": "selector",
      "dimension": "event",
      "value": "View Product"
    },
    {
      "type": "selector",
      "dimension": "event",
      "value": "Purchase"
    }
  ],
  "stepNames": ["Login", "View Product", "Purchase"]
}
```

## Properties

All [default properties](/docs/tql/query/) and the following properties are supported:

**steps** (required)
: The steps of the funnel, expressed as a list of [Filters](/docs/tql/filters/). Each step is a filter that's applied to the data. The first step is applied to all data, the second step is applied to the data that passed the first step, and the third step is applied to the data that passed the first two steps.

stepNames (optional, Array of Strings)
: The names of the steps. If not given, the steps will be named `Step 0`, `Step 0`, etc.

[filter](/docs/tql/filters/) (optional)
: A [Filter](/docs/tql/filters/) to apply to the data to be queried. The default is no filter apart from the [base filters](/docs/tql/baseFilters/).

[granularity](/docs/tql/granularity/) (optional)
: The granularity of the results. The default is `all`.
