---
title: groupBy
tags:
- app analytics
- web analytics
---

## Introduction

A GroupBy Query groups a set of events by a set of dimensions and aggregates them by a set of metrics. It is slightly more complicated than the Top N query, but allows more flexibility and more complex queries. This is the proper query type if you want to group your data by multiple criteria.

## Core Concepts & Examples

Following you can find additional information and a practical example.

**Use Case**: System Versions and Model Names

**Explanation**: A query to group events TelemetryDeck.Session.started regarding the dimensions for System Major Version and Model Name. The dimensions are unchanged and thus the type default used.

Currently, the data returned with this query type can only be displayed in table format.
**Example**:

```
{
    "aggregations": [
        {
          "name": "Number of Events",
          "type": "eventCount"
        }
    ],
    "dimensions": [
        {
          "dimension": "TelemetryDeck.Device.systemMajorVersion",
          "outputName": "Major System Version",
          "outputType": "STRING",
          "type": "default"
        },
        {
          "dimension": "TelemetryDeck.Device.modelName",
          "outputName": "Model Name",
          "outputType": "STRING",
          "type": "default"
        }
    ],
    "filter": {
      "dimension": "type",
      "type": "selector",
      "value": "TelemetryDeck.Session.started"
    },
    "granularity": "all",
    "queryType": "groupBy"
}
```

### Property Reference

Here is a detailed overview of all available properties for GroupBy Queries.

**Property**: `queryType`</br>
**Description**: for this type has to be 'groupBy'.</br>
**Required**: true

**Property**: `dataSource`</br>
**Description**: defaults to namespace, should usually not be changed.</br>
**Required**: false

**Property**: `relativeIntervals`</br>
**Description**: see also respective section; the time intervals to query, specified as relative to time of query (if neither relativeIntervals nor intervals are set, the time period of the date picker in the dashboard is applied).</br>
**Required**: false

**Property**: `intervals`</br>
**Description**: a JSON Object representing ISO-8601 Intervals. This defines the time ranges to run the query over, specified as absolute time intervals (if neither relativeIntervals nor intervals are set, the time period of the date picker in the dashboard is applied).</br>
**Required**: false

**Property**: `granularity`</br>
**Description**: see also respective section; defines the granularity of the query. Potential values are 'hour', 'day', 'week', 'month', 'quarter', 'year' and 'all'.</br>
**Required**: true

**Property**: `filter`</br>
**Description**: see also respective section; a filter that is applied to the query.</br>
**Required**: false

**Property**: `virtualColumns`</br>
**Description**: see also respective section; if created a JSON list of virtualColumns can be referenced in aggregations or postAggregations.</br>
**Required**: false

**Property**: `aggregations`</br>
**Description**: see also respective section; a list of Aggregators to apply to the query, provides the option to aggregate data.</br>
**Required**: false

**Property**: `postAggregations`</br>
**Description**: see also respective section; a list of Post-Aggregators to apply to the query, which provides the option for further actions on aggregated data.</br>
**Required**: false

**Property**: `dimensions`</br>
**Description**: a JSON list of dimensions to do the groupBy over. For more info and possibilities, see also section DimensionSpecs.</br>
**Required**: true

**Property**: context</br>
**Description**: see also respective section; a QueryContext object that specifies how the query is calculated and cached.</br>
**Required**: false