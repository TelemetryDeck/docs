---
title: Top N Query
description: Groups a set of events by a dimension and aggregates them by a metric in the TelemetryDeck Query Language.
lead: Groups a set of events by a dimension and aggregates them by a metric.
order: 30
---

A Top N query allows you to list the top N values of a dimension, ordered by a metric. For example, you can list the top 10 versions of your app by number of users.

## Example

```json
{
  "aggregations": [{ "name": "count", "type": "count" }],
  "dataSource": "telemetry-signals",
  "dimension": {
    "dimension": "appVersion",
    "outputName": "appVersion",
    "type": "default"
  },
  "granularity": "all",
  "metric": {
    "ordering": "version",
    "type": "dimension"
  },
  "filter": {
    "dimension": "appID",
    "type": "selector",
    "value": "AAABBBCCC"
  },
  "queryType": "topN",
  "threshold": 10
}
```

## Properties

All [default properties](/docs/tql/query/) and the following properties are supported:

| Property                              | Description                                                                        |
| ------------------------------------- | ---------------------------------------------------------------------------------- |
| [dimension](/docs/tql/dimensionSpec/) | A single DimensionSpec defining the dimension that you want the top taken for.     |
| [metric](/docs/tql/topNMetricSpec/)   | A TopNMetricSpec object specifying the metric to sort by for the top list.         |
| **threshold**                         | An integer defining the N in the topN (how many results you want in the top list). |
