---
title: TQL Query Reference
tags: overview
description: TelemetryDeck Query Language is the advanced query language for TelemetryDeck. This page describes the query object.
lead: TelemetryDeck Query Language is the advanced query language for TelemetryDeck. You don't need to write all your queries by hand, but if you do, here's how.
order: 0
headerImage: /img/tql-header.png
---

Most queries for TelemetryDeck can be constructed using the regular Insight Editor. However, if you need to construct a query that's not supported by the Insight Editor, or your query is more complicated and deeper than what the Insight Editor supports, you can use the TelemetryDeck Query Language (TQL) to construct your query.

You can use the TQL Query Builder to construct your query, or you can write it by hand. The minimum required properties are `granularity`, `dataSource` and `queryType`. The following sections describe the properties of the query object.

{% noteinfo "This looks curiously familiar" %}

If you've ever worked with [Apache Druid](https://druid.apache.org), you'll notice a lot of similarities between TQL and Druid's native query language. This is because TQL is a superset of Druid's native query language, and TQL queries are compiled down into Druid queries before they're executed.

Druid queries can do various things that TQL queries can't do for security and privacy reasons, and Druid queries are also more verbose. To get into the fine details of Druid's query language, please check the [Apache Druid Documentation](https://druid.apache.org/docs/latest/querying/querying.html).

{% endnoteinfo %}

This example timeseries query returns the number of users per week:

```json
{
  "queryType": "timeseries",
  "dataSource": "telemetry-signals",
  "granularity": "week",
  "aggregations": [
    {
      "fieldName": "clientUser",
      "name": "count",
      "type": "thetaSketch"
    }
  ]
}
```

This example groupBy query groups signals by the `majorSystemVersion` dimension and aggregates them by the `count` metric, resulting in the number of operating system versions:

```json
{
  "queryType": "groupBy",
  "dataSource": "telemetry-signals",
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
      "fieldName": "count",
      "name": "Number of Signals",
      "type": "longSum"
    }
  ]
}
```

## Common Properties

The following properties are common to all query types. See pages for each query type for additional properties only for those query types.

| Property                                                  | Description                                                                                                                                              |
| --------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [queryType](/docs/tql/queryType/)                         | The type of query, for example [timeseries](/docs/tql/timeseries/), [topN](/docs/tql/topN/), [groupBy](/docs/tql/groupBy/), [funnel](/docs/tql/funnel/). |
| [granularity](/docs/tql/granularity/)                     | The granularity of the query.                                                                                                                            |
| [relativeIntervals](/docs/tql/time-intervals/) (optional) | The time intervals to query, specified as relative to time of query.                                                                                     |
| [intervals](/docs/tql/time-intervals/) (optional)         | The time intervals to query, specified as absolute time intervals.                                                                                       |
| [baseFilters](/docs/tql/baseFilters/) (optional)          | A list of filters that are applied to all queries.                                                                                                       |
| [filter](/docs/tql/filters/) (optional)                   | A filter that's applied to the query.                                                                                                                    |
| [dataSource](/docs/tql/datasource/) (optional)            | The data source to query. Must be `"telemetry-signals"`. Defaults to "telemetry-signals".                                                                |
| **testMode** (optional, Bool)                             | Wether to show test test data (`True`) or live data (`False`). Defaults to `False`. [More on Test Mode](/docs/articles/test-mode/)                       |
| **appID** (optional)                                      | If [baseFilters](/docs/tql/basefilters/) is set to `thisApp`, the id for the app in question.                                                            |
| **limit** (optional)                                      | The maximum number of results to return. Defaults to unlimited                                                                                           |
| **sampleFactor** (optional)                               | Include only every n-th signal in query. Possible values are `1`, `10`, `100` or `1000`. Defaults to `1`                                                 |
| **aggregations** (optional)                               | A list of [Aggregators](/docs/tql/aggregators/) to apply to the query.                                                                                   |
| **postAggregations** (optional)                           | A list of [Post-Aggregators](/docs/tql/post-aggregators/) to apply to the query.                                                                         |

## Additional Properties for [Timeseries](/docs/tql/timeseries/) Queries

| Property                                       | Description                                      |
| ---------------------------------------------- | ------------------------------------------------ |
| [descending](/docs/tql/descending/) (optional) | Whether to sort the results in descending order. |

## Additional Properties for [Top N](/docs/tql/topN/) Queries

| Property                              | Description                                                                        |
| ------------------------------------- | ---------------------------------------------------------------------------------- |
| [dimension](/docs/tql/dimensionSpec/) | A DimensionSpec defining the dimension that you want the top taken for.            |
| [metric](/docs/tql/topNMetricSpec/)   | A TopNMetricSpec object specifying the metric to sort by for the top list.         |
| **threshold** (optional)              | An integer defining the N in the topN (how many results you want in the top list). |

## Additional Properties for [Group By](/docs/tql/groupBy/) Queries

| Property                               | Description                                             |
| -------------------------------------- | ------------------------------------------------------- |
| [dimensions](/docs/tql/dimensionSpec/) | A list of DimensionSpec objects to do the groupBy over. |

## Additional Properties for [Funnel](/docs/tql/funnel/) Queries

| Property                                  | Description                                         |
| ----------------------------------------- | --------------------------------------------------- |
| [steps](/docs/tql/funnel/)                | A list of filters that form the steps of the funnel |
| [stepNames](/docs/tql/funnel/) (optional) | An optional List of names for the funnel steps      |
