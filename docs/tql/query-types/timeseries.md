---
title: Timeseries
tags:
- app analytics
- web analytics
---

## Introduction

A Timeseries Query displays returned values for defined cohorts and provides the option to compare the values over time. With this query type you can get the number of hourly, daily, weekly, monthly or all users, events or sessions for example. By creating cohorts in (post-)aggregations different subgroups can be compared.

## Core Concepts & Examples

Following you can find additional information and practical examples.

**Use Case**: Number of signals per day (long version)

**Explanation**: It uses the timeseries query type, and the day granularity. It aggregates using the longSum aggregator, which sums up the values of the count field. This is because TelemetryDeck stores multiple identical events as one event with a count field that contains the number of identical events. No time interval is given, so it will use the default time interval in the UI.

**Example**:

```
{
  "aggregations": [
    {
      "type": "longSum",
      "fieldName": "count",
      "name": "count"
    }
  ],
  "granularity": "day",
  "queryType": "timeseries"
}
```

---

**Use Case**: Number of signals per day (short version)

**Explanation**: To make the query syntax more convenient an aggregator counting events was implemented in TQL. So this query returns identical data as the previous 'Number of signals per day (long version)'.

**Example**:

```
{
  "aggregations": [
    {
      "type": "eventCount"
    }
  ],
  "granularity": "day",
  "queryType": "timeseries"
}
```

---

**Use Case**: Number of users per week (long version)

**Explanation**: It uses the timeseries query type, and the week granularity. It aggregates using the thetaSketch aggregator, which counts different users by counting different values in “fieldName”: “clientUser” in this case. No time interval is given, so it will use the default time interval supplied by the query runner or the UI.

**Example**:

```
{
  "aggregations": [
    {
      "fieldName": "clientUser",
      "name": "count",
      "type": "thetaSketch"
    }
  ],
  "granularity": "week",
  "queryType": "timeseries"
}
```

---

**Use Case**: Number of users per week (short version)

**Explanation**: To make the query syntax more convenient an aggregator counting users was implemented in TQL. So this query returns identical data as the previous 'Number of users per week (long version)'.
**Example**:

```
{
  "aggregations": [
    {
      "name": "Count of Users",
      "type": "userCount"
    }
  ],
  "granularity": "week",
  "queryType": "timeseries"
}
```

### Property Reference

Here is a detailed overview of all available properties for Timeseries Queries.

**Property**: `queryType`</br>
**Description**: for this type has to be 'timeseries'.</br>
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

**Property**: `descending`</br>
**Description**: whether to make descending ordered result. Default is false(ascending).</br>
**Required**: false

**Property**: `context`</br>
**Description**: see also respective section; a QueryContext object that specifies how the query is calculated and cached.</br>
**Required**: false