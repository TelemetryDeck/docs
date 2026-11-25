---
title: Scan
tags:
- app analytics
- web analytics
---

## Introduction

The Scan Query returns raw data rows, it will return events as they are received. This is the proper type if you just want to look at a share of non-aggregated data.

## Core Concepts & Examples

Following you can find additional information and a practical example.

**Use Case**: Scan of Event Type and Device Model

**Explanation**: Query to display time, event type and device model name of events in January 2025, limited to 10 data rows.

**Example**:

```
{
  "queryType": "scan",
  "columns": [
    "__time",
    "type",
    "TelemetryDeck.Device.modelName"
  ],
  "intervals": [
    "2025-01-01/2025-01-02"
  ],
  "limit": 10,
  "order": "descending"
}
```

### Property Reference

Here is a detailed overview of all available properties for Scan Queries.

**Property**: `queryType`</br>
**Description**: for this type has to be 'scan'.</br>
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

**Property**: `columns`</br>
**Description**: a list of columns to return.</br>
**Required**: true

**Property**: `limit`</br>
**Description**: the maximum number of rows to return.</br>
**Required**: true

**Property**: `order`</br>
**Description**: the ordering of returned rows based on timestamp. The timestamp column __time is to be included in the columns list.</br>
**Required**: false

**Property**: `context`</br>
**Description**: see also respective section; a QueryContext object that specifies how the query is calculated and cached.</br>
**Required**: false