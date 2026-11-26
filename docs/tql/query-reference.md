---
title: TQL Query Reference
tags: overview
description: TelemetryDeck Query Language is the advanced query language for TelemetryDeck. This page describes the query object.
lead: TelemetryDeck Query Language is the advanced query language for TelemetryDeck. You don't need to write all your queries by hand, but if you do, here's how.
order: 5
headerImage: /img/tql-header.png
---

Most queries for TelemetryDeck can be constructed using the regular Insight Editor. However, if you need to construct a query that's not supported by the Insight Editor, or your query is more complicated and deeper than what the Insight Editor supports, you can use the TelemetryDeck Query Language (TQL) to construct your query.

You can use the TQL Query Builder to construct your query, or you can write it by hand. The minimum required properties are `granularity`, `dataSource` and `queryType`. The following sections describe the properties of the query object.

!!! warning "This looks curiously familiar"

    If you've ever worked with [Apache Druid](https://druid.apache.org), you'll notice a lot of similarities between TQL and Druid's native query language. This is because TQL is a superset of Druid's native query language, and TQL queries are compiled down into Druid queries before they're executed.

    Druid queries can do various things that TQL queries can't do for security and privacy reasons, and Druid queries are also more verbose. To get into the fine details of Druid's query language, please check the [Apache Druid Documentation](https://druid.apache.org/docs/latest/querying/).

This example timeseries query returns the number of users per week:

```json
{
  "queryType": "timeseries",
  "granularity": "week",
  "aggregations": [
    {
      "name": "count",
      "type": "userCount"
    }
  ]
}
```

This example groupBy query groups signals by the `majorSystemVersion` dimension and aggregates them by the `count` metric, resulting in the number of operating system versions:

```json
{
  "queryType": "groupBy",
  "granularity": "all",
  "dimensions": [
    {
      "dimension": "majorSystemVersion",
      "outputName": "Major System Version",
      "outputType": "STRING",
      "type": "default"
    }
  ],
  "aggregations": [
    {
      "name": "Number of Signals",
      "type": "eventCount"
    }
  ]
}
```

## Common Properties

The following properties are common to all query types. See pages for each query type for additional properties only for those query types.

| Property                                                  | Description                                                                                                                                                                                               |
| --------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [queryType](query-reference.md)                         | The type of query, for example [timeseries](query-types/timeseries.md), [topN](query-types/topN.md), [groupBy](query-types/groupBy.md), [funnel](query-types/funnel.md), [retention](recipes/retention.md), [scan](query-types/scan.md). |
| [granularity](query-elements/granularity.md)                     | The granularity of the query.                                                                                                                                                     |
| [relativeIntervals](query-elements/time-intervals.md) (optional) | The time intervals to query, specified as relative to time of query.                                                                                                              |
| [intervals](query-elements/time-intervals.md) (optional)         | The time intervals to query, specified as absolute time intervals.                                                                                                                |
| [baseFilters](query-elements/base-filters.md) (optional)          | A list of filters that are applied to all queries.                                                                                                                                |
| [filter](query-elements/filters.md) (optional)                   | A filter that's applied to the query.                                                                                                                                             |
| **dataSource** (optional)            | The data source to query. Must be your namespace. Defaults to your namespace.                                                                                        |
| **testMode** (optional, Bool)                             | Wether to show test data (`True`) or live data (`False`). Defaults to `False`. [More on Test Mode](../articles/test-mode.md)                                                     |
| **appID** (optional)                                      | If [baseFilters](query-elements/base-filters.md) is set to `thisApp`, the id for the app in question.                                                                                     |
| **limit** (optional)                                      | The maximum number of results to return. Defaults to unlimited                                                                                                                    |
| **sampleFactor** (optional)                               | Include only every n-th signal in query. Possible values are `1`, `10`, `100` or `1000`. Defaults to `1`                                                                          |
| **aggregations** (optional)                               | A list of [Aggregators](query-elements/aggregators.md) to apply to the query.                                                                                                            |
| **postAggregations** (optional)                           | A list of [Post-Aggregators](query-elements/post-aggregators.md) to apply to the query.                                                                                                  |
| [valueFormatter](query-elements/value-formatter.md) (optional)    | A [ValueFormatter](query-elements/value-formatter.md) object that specifies how query values are displayed.                                                                               |
| [context](query-elements/query-context.md) (optional)             | A [QueryContext](query-elements/query-context.md) object that specifies how the query is calculated and cached.                                                                           |

## Additional Properties for [Timeseries](query-types/timeseries.md) Queries

| Property                                       | Description                                      |
| ---------------------------------------------- | ------------------------------------------------ |
| [descending](query-types/timeseries.md) (optional) | Whether to sort the results in descending order. |

## Additional Properties for [Top N](query-types/topN.md) Queries

| Property                              | Description                                                                        |
| ------------------------------------- | ---------------------------------------------------------------------------------- |
| [dimension](query-elements/dimension-spec.md) | A DimensionSpec defining the dimension that you want the top taken for.            |
| [metric](query-types/topN.md)   | A TopNMetricSpec object specifying the metric to sort by for the top list.         |
| **threshold** (optional)              | An integer defining the N in the topN (how many results you want in the top list). |

## Additional Properties for [Group By](query-types/groupBy.md) Queries

| Property                               | Description                                             |
| -------------------------------------- | ------------------------------------------------------- |
| [dimensions](query-elements/dimension-spec.md) | A list of DimensionSpec objects to do the groupBy over. |

## Additional Properties for [Funnel](query-types/funnel.md) Queries

| Property                                  | Description                                         |
| ----------------------------------------- | --------------------------------------------------- |
| [steps](query-types/funnel.md)                | A list of filters that form the steps of the funnel |
| [stepNames](query-types/funnel.md) (optional) | An optional List of names for the funnel steps      |

## Additional Properties for [Retention](recipes/retention.md) Queries

| Property                                | Description                                                                                      |
| --------------------------------------- | ------------------------------------------------------------------------------------------------ |
| [granularity](query-elements/granularity.md)  | Defines the retention period granularity (day, week, month, quarter, or year). Defaults to month. |
| **intervals** or **relativeIntervals** | The time period to analyze for retention (required).                                             |
