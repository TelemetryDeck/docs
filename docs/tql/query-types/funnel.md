---
title: Funnel
tags:
- app analytics
- web analytics
---

## Introduction

A Funnel Query groups a set of events by a set of steps and aggregates them by a set of metrics. A funnel query is a way of generating a funnel chart and thus the proper type if you want to find out how many users went through multiple defined steps.

## Core Concepts & Examples

Following you can find additional information and a practical example.

**Use Case**: Purchase Funnel

**Explanation**: A query that returns the number of users that went through the funnel steps ‘Login’ -> ‘View Product’ -> ‘Purchase’ (assuming the respective events are implemented).

There is an implementation to display funnel queries graphically. This can be applied by clicking on the respective funnel-symbol, but works only when granularity is ‘all’. With other granularities the returned data can only be displayed in table format.

**Example**:

```
{
  "queryType": "funnel",
  "granularity": "all",
  "steps": [
    {
      "name": "Login",
      "filter": {
        "type": "selector",
        "dimension": "type",
        "value": "Login"
      }
    },
    {
      "name": "View Product",
      "filter": {
        "type": "selector",
        "dimension": "type",
        "value": "View Product"
      }
    },
    {
      "name": "Purchase",
      "filter": {
        "type": "selector",
        "dimension": "type",
        "value": "Purchase"
      }
    }
  ]
}
```

## Property Reference

Here is a detailed overview of all available properties for Funnel Queries.

**Property**: `queryType`</br>
**Description**: for this type has to be ‘funnel’.</br>
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
**Description**: see also respective section; defines the granularity of the query. Potential values are ‘hour’, ‘day’, ‘week’, ‘month’, ‘quarter’, ‘year’ and ‘all’.</br>
**Required**: true

**Property**: `filter`</br>
**Description**: see also respective section; a filter that is applied to the query.</br>
**Required**: false

**Property**: `steps`</br>
**Description**: a list of JSON files where each file indicates one funnel step. Each step has a property ‘name’ to label the step and a filter applied to the data defining criteria for the step.</br>
**Required**: true

**Property**: `context`</br>
**Description**: see also respective section; a QueryContext object that specifies how the query is calculated and cached.</br>
**Required**: false