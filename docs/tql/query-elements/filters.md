---
title: Filters
tags:
- app analytics
- web analytics
---

## Introduction

A filter indicates which rows of data should be included in the computation for a query. It is essentially the equivalent of the WHERE clause in SQL. Filters can be chained and combined with the 'and', 'or' and 'not' operators into a tree of filters with one root filter.

By using filters in the filtered-aggregator cohorts of the complete data can be created and used in post-aggregations.

## Specifics & Examples

Following you can find information regarding the different filters available and examples of their application.

**Name**: Selector - filter

**Explanation**: The selector filter matches rows where the value of a dimension is exactly equal to the specified value.

**Example**:

```
{
    "filter": {
      "type": "selector",
      "dimension": "type",
      "value": "TelemetryDeck.Session.started"
    }
}
```

**Property Reference**

**Property**: `dimension`</br>
**Description**: input column or virtual column name to filter on. To filter for a specific event the dimension is 'type' and the event-name to be used in the value-property. To filter for a specific parameter-value the parameter's name is to be used as dimension and the desired value in the value-property.</br>
**Required**: true

**Property**: `value`</br>
**Description**: string value to match (not required; if not specified the filter matches NULL values).</br>
**Required**: false

**Property**: `type`</br>
**Description**: must be 'selector'.</br>
**Required**: true

---

**Name**: Column Comparison - filter

**Explanation**: The column comparison filter compares dimensions to each other. Note that the column comparison filter converts all values to strings prior to comparison. This allows differently-typed input columns to match without a cast operation.

**Example**:

```
{
    "filter": {
      "type": "columnComparison",
      "dimensions": "<dimension_a>, <dimension_b>"
    }
}
```

**Property Reference**

**Property**: `dimensions`</br>
**Description**: list of DimensionSpec to compare; makes it possible to apply an extraction function if needed.</br>
**Required**: true

**Property**: `type`</br>
**Description**: must be 'columnComparison'.</br>
**Required**: true

---

**Name**: Logical Expression and - filter

**Explanation**: The and-filter combines multiple filters into a single filter that only matches rows that match all sub-filters.

**Example**:

```
{
  "filter": {
    "type": "and",
    "fields": [
        {
          "type": "selector",
          "dimension": "type",
          "value": "TelemetryDeck.Session.started"
        },
        {
          "type": "selector",
          "dimension": "TelemetryDeck.AppInfo.version",
          "value": "3.1.0"
        }
    ]
  }
}
```

**Property Reference**

**Property**: `fields`</br>
**Description**: a list of filter JSON objects.</br>
**Required**: true

**Property**: `type`</br>
**Description**: must be 'and'.</br>
**Required**: true

---

**Name**: Logical Expression or - filter

**Explanation**: The or-filter combines multiple filters into a single filter that matches rows that match any sub-filter.

**Example**:

```
{
  "filter": {
    "type": "or",
    "fields": [
        {
          "type": "selector",
          "dimension": "TelemetryDeck.AppInfo.version",
          "value": "2.1.0"
        },
        {
          "type": "selector",
          "dimension": "TelemetryDeck.AppInfo.version",
          "value": "3.1.0"
        }
    ]
  }
}
```

**Property Reference**

**Property**: `fields`</br>
**Description**: a list of filter JSON objects.</br>
**Required**: true

**Property**: `type`</br>
**Description**: must be 'or'.</br>
**Required**: true

**Name**: Logical Expression not - filter</br>
**Explanation**: The not-filter negates a filter i.e. events are returned that do not meet the criteria of the filter defined in the property 'field' of the not-filter. This enables to filter out rows with no value by negating a selector-filter with an empty value-property.</br>
**Example**:

```
{
  "filter": {
    "type": "not",
    "field": {
          "type": "selector",
          "dimension": "TelemetryDeck.AppInfo.version",
          "value": "2.1.0"
      }
  }
}
```

**Property Reference**

**Property**: `field`</br>
**Description**: a filter JSON object.</br>
**Required**: true

**Property**: `type`</br>
**Description**: must be 'not'.</br>
**Requied**: true

---

**Name**: Range - filter

**Explanation**: The range-filter can be used for comparison filtering like greater than, less than, greater than or equal to, less than or equal to, and 'between'.

Following are three examples (the purpose of this is to present three examples together - it is not a valid syntax to have three 'filter'-fields in a query):

- filter 1: 21 < age < 31
- filter 2: age < 31
- filter 3: 'foo' <= name <= 'hoo', using STRING comparison**Example**:

```
{
    "filter": {
        "type": "range",
        "column": "age",
        "matchValueType": "DOUBLE",
        "lower": "21",
        "lowerOpen": true,
        "upper": "31",
        "upperOpen": true
    },

    "filter": {
        "type": "range",
        "column": "age",
        "matchValueType": "DOUBLE",
        "upper": "31",
        "upperOpen": true
    },

    "filter": {
        "type": "range",
        "column": "name",
        "matchValueType": "STRING",
        "lower": "foo",
        "upper": "hoo"
    }
}
```

**Property Reference**

**Property**: `column`</br>
**Description**: input column or virtual column name to filter on.</br>
**Required**: true

**Property**: `matchValueType`</br>
**Description**: specifies the type of bounds to match. It determines how TelemetryDeck interprets the matchValue to assist in converting to the type of the matched column and also defines the type of comparison used when matching values. Valid values are STRING and DOUBLE.</br>
**Required**: true

**Property**: `lower`</br>
**Description**: lower bound of the range (optional, but at least one of lower or upper must not be null).</br>
**Required**: false

**Property**: `lowerOpen`</br>
**Description**: if true, the lower bound is exclusive.</br>
**Required**: false

**Property**: `upper`</br>
**Description**: upper bound of the range (optional, but at least one of lower or upper must not be null).</br>
**Required**: false

**Property**: `upperOpen`</br>
**Description**: if true, the upper bound is exclusive.</br>
**Required**: false

**Property**: `type`</br>
**Description**: must be 'range'.</br>
**Required**: true

---

**Name**: Regular Expression - filter

**Explanation**: The regex-filter is similar to the selector filter, but using regular expressions. It matches the specified dimension with the given pattern. The example is for values matching the criterion that they start with '50.'

**Example**:

```
{
    "filter": {
        "type": "regex",
        "dimension": "floatValue",
        "pattern": "^50.*"
    }
}
```

**Property Reference**

**Property**: `column`</br>
**Description**: input column or virtual column name to filter on.</br>
**Required**: true

**Property**: `pattern`</br>
**Description**: string pattern to match - any standard Java regular expression.</br>
**Required**: true

**Property**: `extractionFn`</br>
**Description**: extraction function to apply to dimension prior to value matching.</br>
**Required**: false

**Property**: `type`</br>
**Description**: must be 'regex'.</br>
**Required**: true

---

**Name**: Interval - filter

**Explanation**: The interval filter enables range filtering on columns that contain long millisecond values, with the boundaries specified as ISO 8601 time intervals. Intervals can be relative or absolute. Absolute intervals are specified as a string in the format start/end, where start and end are ISO 8601 timestamps.

Following are two examples (the purpose of this is to present two examples together - it is not a valid syntax to have two 'filter'-fields in a query):

- absolute interval: two specified time ranges in October and November 2024
- relative interval: 30 days ago until today**Example**:

```
{
    "filter": {
        "type": "interval",
        "dimension": "__time",
        "intervals": [
          "2024-10-01T00:00:00.000Z/2024-10-07T00:00:00.000Z",
          "2024-11-15T00:00:00.000Z/2024-11-16T00:00:00.000Z"
        ]
      },

    "filter": {
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

}
```

**Property Reference**

**Property**: `dimension`</br>
**Description**: input column or virtual column name to filter on, usually '__time'.</br>
**Required**: true

**Property**: `intervals`</br>
**Description**: in case of absolute intervals a JSON array containing ISO-8601 interval strings that defines the time ranges to filter on.</br>
**Required**: true

**Property**: `extractionFn`</br>
**Description**: extraction function to apply to dimension prior to value matching. An extraction function should output values that are parseable as long milliseconds.</br>
**Required**: false

**Property**: `type`</br>
**Description**: must be 'interval'.</br>
**Required**: true