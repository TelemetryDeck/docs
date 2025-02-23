---
title: Group By Query
description: Groups a set of events by a set of dimensions and aggregates them by a set of metrics in the TelemetryDeck Query Language.
lead: Groups a set of events by a set of dimensions and aggregates them by a set of metrics.
order: 40
---

A group by query can group arbitrary values using aggregations and post-aggregations. This is slightly more complicated than the Top N query, but allows you more flexibility and more complex queries.

## Example

```json
{
  "aggregations": [
    {
      "name": "Number of Signals",
      "type": "eventCount"
    }
  ],
  "dataSource": "telemetry-signals",
  "dimensions": [
    {
      "dimension": "majorSystemVersion",
      "outputName": "Major System Version",
      "outputType": "STRING",
      "type": "default"
    }
  ],
  "filter": {
    "dimension": "appID",
    "type": "selector",
    "value": "AAABBBCCC"
  },
  "granularity": "all",
  "queryType": "groupBy"
}
```

## Properties

All [default properties](/docs/tql/query/) and the following properties are supported:

| Property                               | Description                                             |
| -------------------------------------- | ------------------------------------------------------- |
| [dimensions](/docs/tql/dimensionSpec/) | A list of DimensionSpec objects to do the groupBy over. |
