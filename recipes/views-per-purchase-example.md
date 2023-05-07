---
title: Calculating the average number of views per purchase
tags:
  - examples
  - advanced
lead: An example of how to think with TQL. You can take these queries and modify them to fit your needs.
description: An example of how to think with TQL. You can take these queries and modify them to fit your needs.
testedOn: TelemetryDeck v2023-3
order: 60
---

Imagine we're sending two types of signals.

1. `upgradeDetailViewDidLoad` - when a user opens the upgrade detail screen
2. `purchaseSuccessful` - when a user completes a purchase

We want to know how many times a user opens the upgrade detail screen before completing a purchase. This is a really good candiate for a `groupBy` query!

## Our objective

At a very high level, we want to do these three things:

1. **Only consider signals of type `upgradeDetailViewDidLoad` and `purchaseSuccessful` in our query.** We can achieve that with an `and` filter.
2. Count the number of occurrences of each signal. We'll use [filtered aggregators](/docs/tql/aggregators/#filtered) for that.
3. Calculate the average number of views per purchase. We'll use the [arithmetic post-aggregator](/docs/tql/post-aggregators/#arithmetic-post-aggregator) for that.

Let's look at the various parts of our query in detail. If you just want the finished query, you can find it at the bottom of this article.

If you're new to TQL, you can read more about [queries](/docs/tql/query/) and [filters](/docs/tql/filters/) in the documentation.

## Boilerplate

We'll start with the boilerplate of our query. We'll use the `groupBy` query type, and we're setting the granularity to `all` so that we get a single result.

```json
{
  "queryType": "groupBy",
  "dataSource": "telemetry-signals",
  "granularity": "all",
  "filter": null, // will be set later
  "aggregations": null, // will be set later
  "postAggregations": null, // will be set later
  "dimensions": null // will be set later
}
```

## Filtering

We only want to consider the signals of type `upgradeDetailViewDidLoad` and `purchaseSuccessful`. We can achieve that with an `or` filter.

```json
"filter": {
  "type": "or",
  "fields": [
    {
      "type": "selector",
      "dimension": "type",
      "value": "upgradeDetailViewDidLoad"
    },
    {
      "type": "selector",
      "dimension": "type",
      "value": "purchaseSuccessful"
    }
  ]
}
```

## Aggregation

We want to count the number of occurrences of each signal. We'll use [filtered aggregators](/docs/tql/aggregators/#filtered) for that.

```json
"aggregations": [
  {
    "type": "filtered",
    "filter": {
      "type": "selector",
      "dimension": "type",
      "value": "purchaseSuccessful"
    },
    "aggregator": {
      "type": "doubleSum",
      "name": "_purchase_successful_count",
      "fieldName": "count"
    }
  },
  {
    "type": "filtered",
    "filter": {
      "type": "selector",
      "dimension": "type",
      "value": "upgradeDetailViewDidLoad"
    },
    "aggregator": {
      "type": "doubleSum",
      "name": "_views_count",
      "fieldName": "count"
    }
  }
]
```

{% noteinfo "Why does this use the `doubleSum` aggregator?" %}
When almost-identical TelemetryDeck signals are sent, they are merged into a single database entry. This is why signals have a `count` field, which will increase with each merge. We're using `doubleSum` here to make sure that we're counting the number of signals, not the number of database entries.
{% endnoteinfo %}

We're prepending our field names with underscores. This is because they are intermediary steps that we don't want to display in the results. Any field name that starts with an underscore will be hidden in TelemetryDeck insight UI.

## Post-Aggregation

We now have the number of views and the number of purchases. To get the average number of views per purchase, we'll use the [arithmetic post-aggregator](/docs/tql/post-aggregators/#arithmetic-post-aggregator) to divide the number of views by the number of purchases, resulting in the average number of views per purchase.

```json
"postAggregations": [
  {
    "type": "arithmetic",
    "name": "Average Views per Purchase",
    "fn": "/",
    "fields": [
      { "type": "fieldAccess", "fieldName": "_views_count" },
      {
        "type": "fieldAccess",
        "fieldName": "_purchase_successful_count"
      }
    ]
  }
]
```

## Optional: Grouping

If we want to group the results by a dimension, we can specify a [dimension](/docs/tql/dimensionSpec/) in our query. This can help us track improvements in the numbers made over time, or compare the numbers between differentv versions of our app.

For example, if we want to group the results by `appVersion`, we can add the following to our query:

```json
"dimensions": [
  {
    "dimension": "appVersion",
    "outputName": "App Version",
    "outputType": "STRING",
    "type": "default"
  }
]
```

This will give us the average number of views per purchase, seperately for each version of our app.

{% noteinfo "Grouping by time" %}
If we instead want to group by date, we don't even need to specify a dimension. We set the granularity to `day`, `week`, `month`, or `year` and we'll get the results grouped by that time period.
{% endnoteinfo %}

## Putting it all together

Here's our finished query in all its glory:

```json
{
  "queryType": "groupBy",
  "dataSource": "telemetry-signals",
  "granularity": "all",
  "filter": {
    "type": "or",
    "fields": [
      {
        "type": "selector",
        "dimension": "type",
        "value": "upgradeDetailViewDidLoad"
      },
      {
        "type": "selector",
        "dimension": "type",
        "value": "purchaseSuccessful"
      }
    ]
  },
  "aggregations": [
    {
      "type": "filtered",
      "filter": {
        "type": "selector",
        "dimension": "type",
        "value": "purchaseSuccessful"
      },
      "aggregator": {
        "type": "doubleSum",
        "name": "_purchase_successful_count",
        "fieldName": "count"
      }
    },
    {
      "type": "filtered",
      "filter": {
        "type": "selector",
        "dimension": "type",
        "value": "upgradeDetailViewDidLoad"
      },
      "aggregator": {
        "type": "doubleSum",
        "name": "_views_count",
        "fieldName": "count"
      }
    }
  ],
  "postAggregations": [
    {
      "type": "arithmetic",
      "name": "Average Views per Purchase",
      "fn": "/",
      "fields": [
        { "type": "fieldAccess", "fieldName": "_views_count" },
        {
          "type": "fieldAccess",
          "fieldName": "_purchase_successful_count"
        }
      ]
    }
  ],
  "dimensions": [
    {
      "dimension": "appVersion",
      "outputName": "App Version",
      "outputType": "STRING",
      "type": "default"
    }
  ]
}
```
