---
title: Filters
description: Filters in the TelemetryDeck Query Language.
lead: A filter indicates which rows of data should be included in the computation for a query.
order: 150
---

A filter is essentially the equivalent of the WHERE clause in SQL.

Filters can be chained and combined with the `and` and `or` and `not` operators into a tree of filters with one root filter.

## Logical Expression Filters

### and

The `and` operator combines multiple filters into a single filter that only matches rows that match all sub-filters.

```json
"filter": { "type": "and", "fields": [<filter>, <filter>, ...] }
```

### or

The `or` operator combines multiple filters into a single filter that matches rows that match any sub-filter.

```json
"filter": { "type": "or", "fields": [<filter>, <filter>, ...] }
```

### not

The `not` operator negates a filter.

```json
"filter": { "type": "not", "field": <filter> }
```

## Value Filters

### selector

The `selector` filter matches rows where the value of a dimension is equal to the specified value.

```json
"filter": { "type": "selector", "dimension": "appID", "value": "AABBCC" }
```

### Column Comparison

The `columnComparison` filter is similar to the selector filter, but instead compares dimensions to each other.

```json
"filter": { "type": "columnComparison", "dimensions": [<dimension_a>, <dimension_b>] }
```

### Range

The `range` filter can be used for comparison filtering like greater than, less than, greater than or equal to, less than or equal to, and "between".

| Property         | Description                                                                                                                                                                                                                                                                      |
| ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `column`         | Input column or virtual column name to filter on. (Required)                                                                                                                                                                                                                     |
| `matchValueType` | Specifies the type of bounds to match. It determines how TelemetryDeck interprets the matchValue to assist in converting to the type of the matched column and also defines the type of comparison used when matching values. Valid values are `STRING` and `DOUBLE`. (Required) |
| `lower`          | Lower bound of the range. (Optional, but at least one of lower or upper must not be null)                                                                                                                                                                                        |
| `lowerOpen`      | If true, the lower bound is exclusive. (Optional)                                                                                                                                                                                                                                |
| `upper`          | Upper bound of the range. (Optional, but at least one of lower or upper must not be null)                                                                                                                                                                                        |
| `upperOpen`      | If true, the upper bound is exclusive. (Optional)                                                                                                                                                                                                                                |

#### Example: equivalent to `WHERE 21 ﹤ age ﹤ 31`

```json
"filter": {
  "type": "range",
  "column": "age",
  "matchValueType": "DOUBLE",
  "lower": "21",
  "lowerOpen": true,
  "upper": "31",
  "upperOpen": true
}
```

#### Example: equivalent to `WHERE age ﹤ 31`

```json
"filter": {
  "type": "range",
  "column": "age",
  "matchValueType": "DOUBLE",
  "upper": "31",
  "upperOpen": true
}
```

#### Example: equivalent to `WHERE age ﹥﹦ 18`

```json
"filter": {
  "type": "range",
  "column": "age",
  "matchValueType": "DOUBLE",
  "lower": "18"
}
```

#### Example: equivalent to `WHERE 'foo' ﹤﹦ name ﹤﹦ 'hoo'`, using STRING comparison

```json
"filter": {
  "type": "range",
  "column": "name",
  "matchValueType": "STRING",
  "lower": "foo",
  "upper": "hoo"
}
```

### Regular Expression

The `regex` filter is similar to the selector filter, but using regular expressions. It matches the specified dimension with the given pattern.

```json
"filter": { "type": "regex", "dimension": <dimension_string>, "pattern": <pattern_string> }
```

### Interval

The **interval** filter enables range filtering on columns that contain long millisecond values, with the boundaries specified as ISO 8601 time intervals. This is mainly used for Theta Sketch operations.

Intervals can be relative or absolute. Absolute intervals are specified as a string in the format `start/end`, where `start` and `end` are ISO 8601 timestamps. Relative intervals are specified as an array of [relative time interval](/docs/tql/time-intervals/) objects.

````json
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
````

```json
{
  "type": "interval",
  "dimension": "__time",
  "intervals": [
    "2021-10-01T00:00:00.000Z/2021-10-07T00:00:00.000Z",
    "2021-11-15T00:00:00.000Z/2021-11-16T00:00:00.000Z"
  ]
}
```
