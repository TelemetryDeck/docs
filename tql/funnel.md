---
title: Funnel Query
description: Groups a set of events by a set of steps and aggregates them by a set of metrics in the TelemetryDeck Query Language.
lead: Groups a set of events by a set of steps and aggregates them by a set of metrics.
order: 50
testedOn: TelemetryDeck API v3
tags:
  - setup
  - intermediate
  - funnels
  - insights
searchEngineTitle: How to extract funnels from your analytics data
searchEngineDescription: This is a quick overview on how to create funnels, or click-stream funnels, using the TelemetryDeck Query Language.
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
      "name": "Login",
      "filter": {
        "type": "selector",
        "dimension": "event",
        "value": "Login"
      }
    },
    {
      "name": "View Product",
      "filter": {
        "type": "selector",
        "dimension": "event",
        "value": "View Product"
      }
    },
    {
      "name": "Purchase",
      "filter": {
        "type": "selector",
        "dimension": "event",
        "value": "Purchase"
      }
    }
  ]
}
```

## Properties

All [default properties](/docs/tql/query/) and the following properties are supported:

**steps** (required)
: The steps of the funnel, expressed as a list of **FilterStep** objects. Each step contains a filter that's applied to the data. The first step is applied to all data, the second step is applied to the data that passed the first step, and the third step is applied to the data that passed the first two steps.

[filter](/docs/tql/filters/) (optional)
: A [Filter](/docs/tql/filters/) to apply to the data to be queried. The default is no filter apart from the [base filters](/docs/tql/baseFilters/).

[granularity](/docs/tql/granularity/) (optional)
: The granularity of the results. The default is `all`.

## FilterStep

A **FilterStep** is an object that contains a filter and a name. The filter is applied to the data, and the name is used to label the results.

**name** (required)
: The name of the step. This is used to label the results.

[filter](/docs/tql/filters/) (required)
: A [Filter](/docs/tql/filters/) to apply to the data to be queried.

## How Funnels work

Internally, a `funnel` query will be compiled down into a [groupBy](/docs/tql/groupBy/) query with a few extra aggregations and post-aggregations. This is how it works:

### Aggregations

We're going to use aggregations to split up (or aggregate) the signals into different buckets, and count them by `clientUser` which is the field for TelemetryDeck's user identifier. We're using Theta Sketches to count the number of different users for the funnel stage.

{% noteinfo "What's a theta sketch?" %}

A theta sketch is a probabilistic data structure used for the [count-distinct problem](https://en.wikipedia.org/wiki/Count-distinct_problem). It allows us to quickly count elements in sets, such as the set of users in the aggregation buckets.

{% endnoteinfo %}

```json
[
  {
    "type": "filtered",
    "filter": {
      "type": "selector",
      "dimension": "type",
      "value": "appLaunchedByNotification"
    },
    "aggregator": {
      "type": "thetaSketch",
      "name": "appLaunchedByNotification_count",
      "fieldName": "clientUser"
    }
  },
  {
    "type": "filtered",
    "filter": {
      "type": "selector",
      "dimension": "type",
      "value": "dataEntered"
    },
    "aggregator": {
      "type": "thetaSketch",
      "name": "dataEntered_count",
      "fieldName": "clientUser"
    }
  }
]
```

### Post aggregation

After the aggregation stage, we will have two sets of users: users who sent the `appLaunchedByNotification` signal at least once, and users who sent the `dataEntered` signal at least once.

This is enough for simpler use cases, but there is one more expectation for the funnel: we expect the second stage uniquely to consist of users who sent **both** analytics signals. For example, some users might not have come from the `appLaunchedByNotification` signal, but instead launched the app from the home screen, sending the `appLaunchedFromHomeScreen` signal instead. We don't want to count data entry for these users, so we'll have to discard them.

To do that, we're calculating the _intersection_ of the two aggregation buckets generated in the earlier step, discarding all users that aren't in both buckets.

```json
[
  {
    "type": "thetaSketchEstimate",
    "name": "app_launched_and_data_entered_count",
    "field": {
      "type": "thetaSketchSetOp",
      "name": "app_launched_and_data_entered_count",
      "func": "INTERSECT",
      "fields": [
        {
          "type": "fieldAccess",
          "fieldName": "appLaunchedByNotification_count"
        },
        {
          "type": "fieldAccess",
          "fieldName": "dataEntered_count"
        }
      ]
    }
  }
]
```
