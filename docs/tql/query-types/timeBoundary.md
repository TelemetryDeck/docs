---
title: timeBoundary
tags:
- app analytics
- web analytics
---

## Introduction

Time Boundary Queries return the time of the earliest and latest data points of a data set. This is the proper type if you want to check the time of the first and last occurence of an event.

## Core Concepts & Examples

Following you can find additional information and a practical example.

**Use Case**: Time range of App Version

**Explanation**: Query with a filter for (the randomly selected) app version 1.2. to detect the timestamp of first and last event when this app version was used.
**Example**:

```
{
  "queryType": "timeBoundary",
  "filter": {
    "dimension": "TelemetryDeck.AppInfo.version",
    "type": "selector",
    "value": "1.2."
  },
  "granularity": "all"
}
```

### Property Reference

Here is a detailed overview of all available properties for TimeBoundary Queries.

**Property**: `queryType`</br>
**Description**: for this type has to be 'timeBoundary'.</br>
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

**Property**: `context`</br>
**Description**: see also respective section; a QueryContext object that specifies how the query is calculated and cached.</br>
**Required**: false