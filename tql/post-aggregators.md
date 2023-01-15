---
title: Post Aggregators
description: Post-aggregations are specifications of processing that should happen on aggregated values as they come out of the timeseries DB in the TelemetryDeck Query Language.
lead: Post-aggregations are specifications of processing that should happen on aggregated values as they come out of the timeseries DB.
order: 170
---

## Field accessor post-aggregator

These post-aggregators return the value produced by the specified aggregator. Use type "field
object, or use type "finalizingFieldAccess" to return a finalized value, such as an estimated cardinality.

```json
{ "type": "fieldAccess", "name": "tot", "fieldName": "tot" }
```

## Constant post-aggregator

The constant post-aggregator always returns the specified value.

```json
{ "type": "constant", "name": "const", "value": 100 }
```

## Arithmetic post-aggregator

The arithmetic post-aggregator applies the provided function to the given fields from left to right. The
Supported functions are `+`, `-`, `*`, `/`, and `quotient`.

Note:

- / division always returns 0 if dividing by 0, regardless of the numerator.
- quotient division behaves like regular floating point division
- Arithmetic post-aggregators always use floating point arithmetic.
- Arithmetic post-aggregators may also specify an ordering, which defines the order of resulting values when sorting.
- If no ordering (or null) is specified, the default floating point ordering is used.
- numericFirst ordering always returns finite values first, followed by NaN, and infinite values last.

```json
{
  "type": "arithmetic",
  "name": "part_percentage",
  "fn": "*",
  "fields": [
    {
      "type": "arithmetic",
      "name": "ratio",
      "fn": "/",
      "fields": [
        { "type": "fieldAccess", "name": "part", "fieldName": "part" },
        { "type": "fieldAccess", "name": "tot", "fieldName": "tot" }
      ]
    },
    { "type": "constant", "name": "const", "value": 100 }
  ]
}
```

## Expression post-aggregator

The expression post-aggregator is defined using a Druid expression.

```json
{
  "type": "expression",
  "name": "part_percentage",
  "expression": "100 * (part / tot)"
}
```

## HyperUnique Cardinality post-aggregator

The hyperUniqueCardinality post aggregator is used to wrap a hyperUnique object such that it can be used in post aggregations.

```json
{
  "type": "arithmetic",
  "name": "average_users_per_row",
  "fn": "/",
  "fields": [
    { "type": "hyperUniqueCardinality", "fieldName": "unique_users" },
    { "type": "fieldAccess", "name": "rows", "fieldName": "rows" }
  ]
}
```

## Theta Sketch Estimate post-aggregator

The thetaSketchEstimate post aggregator is used to wrap a theta sketch object such that it can be used in post aggregations.

This is used in the following example to compute the number of users who launched the app and then entered data.

```json
{
  "type": "thetaSketchEstimate",
  "name": "app_launched_and_data_entered_count",
  "field": {
    "type": "thetaSketchSetOp",
    "name": "app_launched_and_data_entered_count",
    "func": "INTERSECT",
    "fields": [
      {
        "type": "fieldAccess",
        "fieldName": "appLaunchedByNotification_count"
      },
      {
        "type": "fieldAccess",
        "fieldName": "dataEntered_count"
      }
    ]
  }
}
```

## Theta Sketch Set Operation post-aggregator

The thetaSketchSetOp post aggregator is used to wrap a theta sketch object such that it can be used in post aggregations.

This is used in the following example to compute the number of users who launched the app and then entered data.

```json
{
  "type": "thetaSketchEstimate",
  "name": "app_launched_and_data_entered_count",
  "field": {
    "type": "thetaSketchSetOp",
    "name": "app_launched_and_data_entered_count",
    "func": "INTERSECT",
    "fields": [
      {
        "type": "fieldAccess",
        "fieldName": "appLaunchedByNotification_count"
      },
      {
        "type": "fieldAccess",
        "fieldName": "dataEntered_count"
      }
    ]
  }
}
```

## Greatest / Least post-aggregators

`doubleGreatest` computes the maximum of all fields and `Double.NEGATIVE_INFINITY`. `doubleLeast` computes the minimum of all fields and `Double.POSITIVE_INFINITY.`

The difference between the doubleMax aggregator and the doubleGreatest post-aggregator is that doubleMax returns the highest value of all rows for one specific column while doubleGreatest returns the highest value of multiple columns in one row. These are similar to the SQL MAX and GREATEST functions.

Example:

```json
{
"type" : "doubleGreatest",
"name" : <output_name>,
"fields": [<post_aggregator>, <post_aggregator>, ...]
}
```
