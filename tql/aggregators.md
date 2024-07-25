---
title: Aggregators
description: You can use aggregations at query time to summarize result data in the TelemetryDeck Query Language.
lead: You can use aggregations at query time to summarize result data.
order: 160
---

You can use aggregations at query time to summarize result data. The following aggregators are available:

## Numerical Aggregators

### Count

`count` computes the count of rows that match the filters.

```json
{ "type" : "count", "name" : <output_name> }
```

### DoubleSum

`doubleSum` computes and stores the sum of values as a 64-bit floating point value.

The doubleSum aggregator takes the following properties:

- `name`: Output name for the summed value
- `fieldName`: Name of the metric column to sum over

```json
{ "type" : "doubleSum", "name" : <output_name>, "fieldName" : <metric_name> }
```

### DoubleMin

`doubleMin` computes the minimum of all metric values and `Double.POSITIVE_INFINITY`.

```json
{ "type" : "doubleMin", "name" : <output_name>, "fieldName" : <metric_name> }
```

### DoubleMax

`doubleMax` computes the maximum of all metric values and `Double.NEGATIVE_INFINITY`.

```json
{ "type" : "doubleMax", "name" : <output_name>, "fieldName" : <metric_name> }
```

## Averaging Aggregators

### DoubleMean

`doubleMean` computes and returns the arithmetic mean of a column's values as a 64-bit floating point value.

Warning: this aggregator is mean 😡😡

```json
{ "type" : "doubleMean", "name" : <output_name>, "fieldName" : <metric_name> }
```

## Unique Aggregators

### ThetaSketch

Theta sketches are a probabilistic data structure used for the [count-distinct problem](https://en.wikipedia.org/wiki/Count-distinct_problem). They allow us to quickly count elements in sets, such as the set of users in the aggregation buckets

{% noteinfo "More on ThetaSketches" %}

A Theta sketch object can be thought of as a Set data structure. At query time, sketches are read and aggregated (set unioned) together. By default, you receive the estimate of the number of unique entries in the sketch object.

Also, you can use post aggregators to do union, intersection or difference on sketch columns in the same row. This means you can create distinct sets of users and compare them against each other. This is necessary for retention and funnel queries.

{% endnoteinfo %}

```json
{
  "fieldName": "clientUser",
  "name": "count",
  "type": "thetaSketch"
}
```

### Cardinality

`cardinality` computes the cardinality of a dimension.

{% notewarning "Deprecated" %}

This aggregator is deprecated. Use `thetaSketch` instead.

{% endnotewarning %}

```json
{
  "byRow": false,
  "fields": ["clientUser"],
  "name": "a0",
  "round": true,
  "type": "cardinality"
}
```

## First and Last Aggregators

### DoubleFirst

`doubleFirst` computes the first value of all metric values.

```json
{ "type" : "doubleFirst", "name" : <output_name>, "fieldName" : <metric_name> }
```

### DoubleLast

`doubleLast` computes the last value of all metric values.

```json
{ "type" : "doubleLast", "name" : <output_name>, "fieldName" : <metric_name> }
```

### StringFirst

`stringFirst` computes the first value of all metric values.

```json
{ "type" : "stringFirst", "name" : <output_name>, "fieldName" : <metric_name> }
```

### StringLast

`stringLast` computes the last value of all metric values.

```json
{ "type" : "stringLast", "name" : <output_name>, "fieldName" : <metric_name> }
```

## ANY Aggregators

### DoubleAny

Returns any value including null. This aggregator can simplify and optimize the performance by returning the first encountered value (including null).

doubleAny returns any double metric value.

```json
{ "type" : "doubleAny", "name" : <output_name>, "fieldName" : <metric_name> }
```

### StringAny

Returns any value including null. This aggregator can simplify and optimize the performance by returning the first encountered value (including null).

stringAny returns any string metric value.

```json
{ "type" : "stringAny", "name" : <output_name>, "fieldName" : <metric_name> }
```

## Misc

### Filtered

A filtered aggregator wraps any given aggregator, but only aggregates the values for which the given dimension filter matches.

This makes it possible to compute the results of a filtered and an unfiltered aggregation simultaneously, without having to issue multiple queries, and use both results as part of post-aggregations.

Note: If only the filtered results are required, consider putting the filter on the query itself, which will be much faster since it doesn't require scanning all the data.

Filtered aggregators also support [relative time intervals](/docs/tql/time-intervals/).

```json
{
  "type": "interval",
  "dimension": "__time",
  "relativeIntervals": [
    {
      "beginningDate": {
        "component": "day",
        "offset": -30,
        "position": "beginning"
      },
      "endDate": {
        "component": "day",
        "offset": 0,
        "position": "end"
      }
    }
  ]
}
```

```json
{
  "type": "filtered",
  "filter": {
    "type": "and",
    "fields": [
      {
        "type": "selector",
        "dimension": "type",
        "value": "InsightShown"
      }
    ]
  },
  "aggregator": {
    "type": "thetaSketch",
    "name": "InsightShown",
    "fieldName": "clientUser"
  }
}
```
