---
title: topN
tags:
- app analytics
- web analytics
---

## Introduction

A TopN Query allows to list the top N values of a dimension, ordered by a metric. This type is thus a proper option for questions regarding the most frequent occurences of a certain criterion. By applying filters subgroups of the dataset can be investigated as well.

## Core Concepts & Examples

Following you can find additional information and practical examples.

**Use Case**: App versions - granularity all

**Explanation**: Lists the top 20 versions of an app by number of events. default-Dimension and the count-metric are used, which are common for this query type.

Regarding the graphical display of returned data the following option is recommended for topN-Queries with granularity all:

- donut chart: by clicking on the respective donut-chart-symbol data can be displayed as Donut Chart**Example**:

```
{
  "aggregations": [
    {
      "fieldName": "count",
      "name": "count",
      "type": "longSum"
    }
  ],
  "dimension": {
    "dimension": "TelemetryDeck.AppInfo.version",
    "outputName": "appVersion",
    "type": "default"
  },
  "granularity": "all",
  "metric": {
    "metric": "count",
    "type": "numeric"
  },
  "queryType": "topN",
  "threshold": 20
}
```

---

**Use Case**: App versions - granularity not all

**Explanation**: Like the previous examples lists the top 20 versions of an app by number of events. Only the granularity is changed and not 'all'.
Regarding the graphical display of returned data the following options are available for topN-Queries with granularity not all:

- normalized bars: by clicking on the respective donut-chart-symbol data can be displayed as bars with sum per granularity scaled to 100%, i.e. all bars have the same height
- bars of different heights: by clicking on the respective bar-chart-symbol data can be displayed as bars with different heights according to totals per granularity, i.e. height of bars depends on totals in respective time periods
**Example**:

```
{
  "aggregations": [
    {
      "fieldName": "count",
      "name": "count",
      "type": "longSum"
    }
  ],
  "dimension": {
    "dimension": "TelemetryDeck.AppInfo.version",
    "outputName": "appVersion",
    "type": "default"
  },
  "granularity": "week",
  "metric": {
    "metric": "count",
    "type": "numeric"
  },
  "queryType": "topN",
  "threshold": 20
}
```

---

**Use Case**: TopNMetricSpec - numeric

**Explanation**: TopNMetricSpec specify how TopN values are sorted. 'numeric' is one possible TopNMetricSpec type for defining how TopN results are sorted.

By using this type you can define the metric to sort topN results by, e.g. 'count' in this example. This is assuming that in the query a metric named 'count' is defined, for example in an aggregator.

**Example**:

```
{
    "metric": {
        "type": "numeric",
        "metric": "count"
    }
}
```

---

**Use Case**: TopNMetricSpec - dimension

**Explanation**: TopNMetricSpec specify how TopN values are sorted. One possible sorting order is the type 'dimension'.

By using this type results are sorted by dimension value itself rather than by an aggregated metric. The following options are available:
- 'lexicographic': Sorts values by converting Strings to their UTF-8 byte array representations and comparing lexicographically, byte-by-byte.

- 'alphanumeric': Suitable for strings with both numeric and non-numeric content. file12 sorts after file2.

- 'numeric': Sorts values as numbers.

- ‘strlen': Sorts values by their string lengths. When there is a tie, this comparator falls back to using the String compareTo method.
- ‘version': Sorts values as versions. 10.0 sorts after 9.0, 1.0.0-SNAPSHOT sorts after 1.0.0.

An additional option is to use ‘previousStop', which is an optional string and the starting point of the sort. For example, if a previousStop value is b, all values before b are discarded. This field can be used to paginate through all the dimension values.

**Example**:

```
{
    "metric": {
        "type": "dimension",
        "ordering": "lexicographic",
        "previousStop": "previousStop_value"
    }
}
```

---

**Use Case**: TopNMetricSpec - inverted

**Explanation**: TopNMetricSpec specifies how TopN values are sorted. Complementary to the previous two examples, 'inverted' is another TopNMetricSpec type.

By applying this type, the ordering defined by a delegate metric spec is reversed.

**Example**:

```
{
    "metric": {
        "type": "inverted",
        "metric": {
          "metric": "count",
          "type": "numeric"
        }
    }
}
```

### Property Reference

Here is a detailed overview of all available properties for TopN Queries.

**Property**: `queryType`</br>
**Description**: for this type has to be 'topN'</br>
**Required**: true

**Property**: `dataSource`</br>
**Description**: defaults to namespace, should usually not be changed</br>
**Required**: false

**Property**: `relativeIntervals`</br>
**Description**: see also respective section; the time intervals to query, specified as relative to time of query 
(if neither relativeIntervals nor intervals are set, the time period of the date picker in the dashboard is applied)</br>
**Required**: false

**Property**: `intervals`</br>
**Description**: a JSON Object representing ISO-8601 Intervals. This defines the time ranges to run the query over, 
specified as absolute time intervals (if neither relativeIntervals nor intervals are set, the time period of the 
date picker in the dashboard is applied)</br>
**Required**: false

**Property**: `granularity`</br>
**Description**: see also respective section; defines the granularity of the query. Potential values are 'hour', 
'day', 'week', 'month', 'quarter', 'year' and 'all'.</br>
**Required**: true

**Property**: `filter`</br>
**Description**: see also respective section; a filter that is applied to the query.</br>
**Required**: false

**Property**: `virtualColumns`</br>
**Description**: see also respective section; if created a JSON list of virtualColumns can be referenced in 
aggregations or postAggregations</br>
**Required**: false


**Property**: `aggregations`</br>
**Description**: see also respective section; a list of Aggregators to apply to the query, provides the option 
to aggregate data</br>
**Required**: false

**Property**: `postAggregations`</br>
**Description**: see also respective section; a list of Post-Aggregators to apply to the query, which provides 
the option for further actions on aggregated data.
**Required**: false

**Property**: `dimension`</br>
**Description**: a String or JSON object defining the dimension that you want the top taken for. 
If the values need to be returned as they are the 'type': 'default' with the fields 'dimension' and 
'outputName' should be selected. For more info and possibilities, see also section [DimensionSpecs](../query-elements/dimension-spec.md). </br>
**Required**: true

**Property**: `metric`.</br>
**Description**: a String or JSON object specifying the metric to sort by for the top list. 
For more info, see remarks to TopNMetricSpec in the Use Cases above</br>
**Required**: true

**Property**: `threshold`</br>
**Description**: an integer defining the N in the topN, i.e. how many results are wanted in the top list.</br>
**Required**: true

**Property**: `context`</br>
**Description**: see also respective section; a QueryContext object that specifies how the query is calculated and cached.</br>
**Required**: false