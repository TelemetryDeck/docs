---
title: (Deprecated) Funnels
tags:
  - setup
  - intermediate
  - funnels
  - insights
testedOn: TelemetryDeck API v3
description: How to create funnels, or click-stream funnels, using the TelemetryDeck Query Language.
lead: This is a quick overview on how to create funnels, or click-stream funnels, using the TelemetryDeck Query Language.
searchEngineTitle: How to extract funnels from your analytics data
searchEngineDescription: This is a quick overview on how to create funnels, or click-stream funnels, using the TelemetryDeck Query Language.
order: 1000
---

{% notewarning "Deprecated" %}

The content below is deprecated and will be removed in the future. Please refer to the [new documentation](/docs/tql/funnel/) instead.

{% endnotewarning %}

This article explains the thought process on how to create funnel-type queries; scroll to the bottom for a complete example.

## Think about your funnel stages

Before you begin, think about how to express each of the steps of your funnel as a filter. For example, you can use different signal types such as `appLaunchedByNotification` and `dataEntered`:

```json
{ "type": "selector", "dimension": "type", "value": "appLaunchedByNotification" },
```

```json
{ "type": "selector", "dimension": "type", "value": "dataEntered" }
```

Alternatively, you can have more vague signal types such as `view` and `event` and express those in a more complex filter. Here is an example of how to express a stage where a specific `watchNow` event has been triggered.

```json
{
  "type": "and",
  "fields": [
    { "type": "selector", "dimension": "type", "value": "event" },
    { "type": "selector", "dimension": "action_id", "value": "watchNow" }
  ]
}
```

This is all up to you and how you set up your signals in the first place–it might require some experimentation with queries until you settle for good ones. For the rest of this example, we will use our two steps of `appLaunchedByNotification` and `dataEntered` as examples.

Once you have an idea how to express the stages of your funnel, we can write the individual aspects of our query:

## Metadata

We need a `groupBy` query with no explicit dimensions and we'll just chuck in our default relative time intervals in there for good measure. We'll set the `granularity` to `all`, although setting that to various values could yield interesting results.

```json
{
  "queryType": "groupBy",
  "dataSource": "telemetry-signals",
  "granularity": "all",
  "dimensions": [],
  // ...
  "relativeIntervals": [
    {
      "beginningDate": {
        "component": "month",
        "offset": -1,
        "position": "beginning"
      },
      "endDate": {
        "component": "month",
        "offset": 0,
        "position": "end"
      }
    }
  ]
}
```

## Filters

For our filters, we want to grab all signals that might be relevant for the funnel. This means filtering for the app ID, for test mode, and all the signals that are interesting for the different stages of the funnel. In our example, we can use an outer `and` filter to select `appID` and `isTestMode` and our inner `or` filter.

```json
{
  "fields": [
    {
      "dimension": "appID",
      "type": "selector",
      "value": "B97579B6-FFB8-4AC5-AAA7-DA5796CC5DCE"
    },
    {
      "dimension": "isTestMode",
      "type": "selector",
      "value": "false"
    },
    {
      "type": "or",
      "fields": [
        {
          "type": "selector",
          "dimension": "type",
          "value": "appLaunchedByNotification"
        },
        { "type": "selector", "dimension": "type", "value": "dataEntered" }
      ]
    }
  ],
  "type": "and"
}
```

## Aggregations

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

## Post aggregation

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

## The final query

Here's the final funnel query in all it's glory:

```json
{
  "queryType": "groupBy",
  "dataSource": "telemetry-signals",
  "granularity": "all",
  "dimensions": [],
  "filter": {
    "fields": [
      {
        "dimension": "appID",
        "type": "selector",
        "value": "YOUR-APP-ID"
      },
      {
        "dimension": "isTestMode",
        "type": "selector",
        "value": "false"
      },
      {
        "type": "or",
        "fields": [
          {
            "type": "selector",
            "dimension": "type",
            "value": "appLaunchedByNotification"
          },
          { "type": "selector", "dimension": "type", "value": "dataEntered" }
        ]
      }
    ],
    "type": "and"
  },
  "aggregations": [
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
  ],
  "postAggregations": [
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
  ],
  "relativeIntervals": [
    {
      "beginningDate": {
        "component": "month",
        "offset": -1,
        "position": "beginning"
      },
      "endDate": {
        "component": "month",
        "offset": 0,
        "position": "end"
      }
    }
  ]
}
```
