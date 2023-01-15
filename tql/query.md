---
title: TQL Query Reference
tags: overview
description: TelemetryDeck Query Language is the advanced query language for TelemetryDeck. This page describes the query object.
lead: TelemetryDeck Query Language is the advanced query language for TelemetryDeck. You don't need to write all your queries by hand, but if you do, here's how.
order: 0
---

Most queries for TelemetryDeck can be constructed using the regular Insight Editor. However, if you need to construct a query that is not supported by the Insight Editor, or your query is more complicated and deeper than what the Insight Editor supports, you can use the TelemetryDeck Query Language (TQL) to construct your query.

You can use the TQL Query Builder to construct your query, or you can write it by hand. The minumum required properties are `granularity`, `dataSource` and `queryType`. The following sections describe the properties of the query object.

{% noteinfo "This looks curiously familiar" %}

If you've ever worked with [Apache Druid](https://druid.apache.org), you'll notice a lot of similarities between TQL and Druid's native query language. This is because TQL is a superset of Druid's native query language, and TQL queries are compiled down into Druid queries before they are executed.

Druid queries can do various things that TQL queries cannot do for security and privacy reasons, and Druid queries are also more verbose. To get into the fine details of Druid's query language, please check the [Apache Druid Documentation](https://druid.apache.org/docs/latest/querying/querying.html).

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
      "dimension": "",
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

| Property                                                  | Description                                                                                                                                        |
| --------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| [queryType](/docs/tql/querytype/)                         | The type of query, e.g. [timeseries](/docs/tql/timeseries/), [topN](/docs/tql/topN/), [groupBy](/docs/tql/groupBy/), [funnel](/docs/tql/funnels/). |
| [dataSource](/docs/tql/datasource/)                       | The data source to query. Must be `"telemetry-signals"`.                                                                                           |
| [granularity](/docs/tql/granularity/)                     | The granularity of the query.                                                                                                                      |
| [relativeIntervals](/docs/tql/time-intervals/) (optional) | The time intervals to query, specified as relative to time of query.                                                                               |
| [intervals](/docs/tql/time-intervals/) (optional)         | The time intervals to query, specified as absolute time intervals.                                                                                 |
| [baseFilters](/docs/tql/basefilters/) (optional)          | A list of filters that are applied to all queries.                                                                                                 |
| [filter](/docs/tql/filter/) (optional)                    | A filter that is applied to the query.                                                                                                             |
| [limit](/docs/tql/limit/) (optional)                      | The maximum number of results to return.                                                                                                           |
| aggregations (optional)                                   | A list of [Aggregators](/docs/tql/aggregators/) to apply to the query.                                                                             |
| postAggregations (optional)                               | A list of [Post-Aggregators](/docs/tql/post-aggregators/) to apply to the query.                                                                   |

## Additional Properties for Timeseries Queries

| Property                                       | Description                                      |
| ---------------------------------------------- | ------------------------------------------------ |
| [descending](/docs/tql/descending/) (optional) | Whether to sort the results in descending order. |

## Additional Properties for Top N Queries

| Property                                     | Description                                                                             |
| -------------------------------------------- | --------------------------------------------------------------------------------------- |
| [dimension](/docs/tql/dimension/)            | A DimensionSpec defining the dimension that you want the top taken for.                 |
| [metric](/docs/tql/metric/)                  | Specifying the metric to sort by for the top list.                                      |
| [threshold](/docs/tql/threshold/) (optional) | An integer defining the N in the topN (i.e. how many results you want in the top list). |

## Additional Properties for Group By Queries

| Property                            | Description                                  |
| ----------------------------------- | -------------------------------------------- |
| [dimensions](/docs/tql/dimensions/) | A list of dimensions to do the groupBy over. |

## Additional Properties for Funnel Queries

| Property                                     | Description                                         |
| -------------------------------------------- | --------------------------------------------------- |
| [steps](/docs/tql/steps/)                    | A list of filters that form the steps of the funnel |
| [stepNames](/docs/tql/stepnames/) (optional) | An optional List of names for the funnel steps      |
