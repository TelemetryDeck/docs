---
title: Aggregators
tags:
- app analytics
- web analytics
---

## Introduction

Aggregations can be used at query time to aggregate data by criteria defined through the respective aggregator.

Aggregators might only be created for further calculations and in that case can be hidden from returned data when their name-property starts with an underscore.

## Specifics & Examples

Following you can find information regarding the different aggregators available and examples of their application.

### Analytics aggregations

**Name**: `longSum` / `eventCount` - aggregator (long version)

**Explanation**: The longSum-aggregator takes the values of the specified field and calculates the sum of the values for the returned events. When used on fieldName 'count' this aggregator computes the number of TelemetryDeck events in the query.

**Example**:

```
{
  "type": "longSum",
  "fieldName": "count",
  "name": "Events"
}
```

**Property Reference**

**Property**: `name`</br>
**Description**: the output name for the respective aggregator.</br>
**Required**: true

**Property**: `fieldName`</br>
**Description**: the name of the metric column used for the respective aggregator. Must be a field containing numeric values. To count events must be 'count'.</br>
**Required**: true

**Property**: `type`</br>
**Description**: must be 'longSum'.</br>
**Required**: true

---

**Name**: `eventCount` - aggregator (short version)

**Explanation**: The aggregator of type 'eventCount' was implemented as a convenient syntax in TQL and is identical to the Apache Druid type longSum on the dimension count. So this is the short version of an aggregator that computes the number of TelemetryDeck events in the query.

**Example**:

```
{
  "type": "eventCount",
  "name": "<output_name, defaults to 'Events'>"
}
```

**Property Reference**

**Property**: `name`</br>
**Description**: the output name for the respective aggregator, which can be defined. Defaults to 'Events'.</br>
**Required**: false

**Property**: `type`</br>
**Description**: must be 'eventCount'.</br>
**Required**: true

---

**Name**: `thetaSketch` / `userCount` - aggregator (long version)

**Explanation**: The thetaSketch-aggregator computes the number of unique values in the specified field for the returned events. When used on fieldName 'clientUser' this aggregator returns the number of different users.

**Example**:

```
{
  "type": "thetaSketch",
  "fieldName": "clientUser",
  "name": "Users"
}
```

**Property Reference**

**Property**: `name`</br>
**Description**: the output name for the respective aggregator.</br>
**Required**: true

**Property**: `fieldName`</br>
**Description**: the name of the metric column used for the respective aggregator. Must be a field containing numeric values. To count events must be 'clientUser'.</br>
**Required**: true

**Property**: `type`</br>
**Description**: must be 'thetaSketch'.</br>
**Required**: true

---

**Name**: `userCount` - aggregator (short version)

**Explanation**: The aggreagator of type 'userCount' was implemented as a convenient syntax in TQL and is identical to the Apache Druid type thetaSketch on the dimension clientUser. So this is the short version of an aggregator that computes the number of unique users in the query.

**Example**:

```
{
  "type": "userCount",
  "name": "<output_name, defaults to 'Users'>"
}
```

**Property Reference**

**Property**: `name`</br>
**Description**: the output name for the respective aggregator, which can be defined. Defaults to 'Users'.</br>
**Required**: false

**Property**: `type`</br>
**Description**: must be 'userCount'.</br>
**Required**: true

### Exact aggregations

**Name**: `count` - aggregator

**Explanation**: The count aggregator computes the count of rows that match the filters i.e. this gives the number of rows returned.

**Example**:

```
{
  "type": "count",
  "name": "count_returnedRows"
}
```

**Property Reference**

**Property**: `name`</br>
**Description**: the output name for the respective aggregator.</br>
**Required**: true

**Property**: `type`</br>
**Description**: must be 'count'.</br>
**Required**: true

---

**Name**: `doubleSum` - aggregator

**Explanation**: The doubleSum aggregator takes the values of the specified field and calculates the sum of the values for the returned events. This aggregator computes and stores the sum of values as a 64-bit floating point value (longSum and floatSum instead of doubleSum work as well).

**Example**:

```
{
  "type": "doubleSum",
  "name": "sum_floatValues",
  "fieldName": "floatValue"
}
```

**Property Reference**

**Property**: `name`</br>
**Description**: the output name for the respective aggregator.</br>
**Required**: true

**Property**: `fieldName`</br>
**Description**: the name of the metric column used for the respective aggregator. Must be a field containing numeric values.</br>
**Required**: true

**Property**: `type`</br>
**Description**: must be 'doubleSum'.</br>
**Required**: true

---

**Name**: `doubleMin` - aggregator

**Explanation**: The doubleMin aggregator computes the minimum of all metric values and Double.POSITIVE_INFINITY (floatMin and longMin instead of doubleMin work as well). So this returns the minimum value of the specified field for returned events.

**Example**:

```
{
  "type": "doubleMin",
  "name": "minimumValue",
  "fieldName": "floatValue"
}
```

**Property Reference**

**Property**: `name`</br>
**Description**: the output name for the respective aggregator.</br>
**Required**: true

**Property**: `fieldName`</br>
**Description**: the name of the metric column used for the respective aggregator. Must be a field containing numeric values.</br>
**Required**: true

**Property**: `type`</br>
**Description**: must be 'doubleMin'.</br>
**Required**: true

---

**Name**: `doubleMax` - aggregator

**Explanation**: The doubleMax aggregator computes the maximum of all metric values and Double.NEGATIVE_INFINITY (floatMax and longMax instead of doubleMax work as well). So this returns the maximum value of the specified field for returned events.

**Example**:

```
{
  "type": "doubleMax",
  "name": "maximumValue",
  "fieldName": "floatValue"
}
```

**Property Reference**

**Property**: `name`</br>
**Description**: the output name for the respective aggregator.</br>
**Required**: true

**Property**: `fieldName`</br>
**Description**: the name of the metric column used for the respective aggregator. Must be a field containing numeric values.</br>
**Required**: true

**Property**: `type`</br>
**Description**: must be 'doubleMax'.</br>
**Required**: true

---

**Name**: `doubleMean` - aggregator

**Explanation**: The doubleMean aggregator computes and returns the arithmetic mean of a column's values as a 64-bit floating point value. So this takes all values of the specified field for returned events and calculates the arithmetic mean.

**Example**:

```
{
  "type": "doubleMean",
  "name": "meanValue",
  "fieldName": "floatValue"
}
```

**Property Reference**

**Property**: `name`</br>
**Description**: the output name for the respective aggregator.</br>
**Required**: true

**Property**: `fieldName`</br>
**Description**: the name of the metric column used for the respective aggregator. Must be a field containing numeric values.</br>
**Required**: true

**Property**: `type`</br>
**Description**: must be 'doubleMean'.</br>
**Required**: true

---

**Name**: `doubleFirst` - aggregator

**Explanation**: The doubleFirst aggregator computes the first value of all numerical metric values (floatFirst and longFirst instead of doubleFirst work as well), i.e. can be used when the first value of a specified field is needed for the returned events.

**Example**:

```
{
  "type": "doubleFirst",
  "name": "firstValue",
  "fieldName": "floatValue"
}
```

**Property Reference**

**Property**: `name`</br>
**Description**: the output name for the respective aggregator.</br>
**Required**: true

**Property**: `fieldName`</br>
**Description**: the name of the metric column used for the respective aggregator. Must be a field containing numeric values.</br>
**Required**: true

**Property**: `type`</br>
**Description**: must be 'doubleFirst'.</br>
**Required**: true

---

**Name**: `doubleLast` - aggregator

**Explanation**: The doubleLast aggregator computes the last value of all numerical metric values (floatLast and longLast instead of doubleLast work as well), i.e. can be used when the last value of a specified field is needed for the returned events.

**Example**:

```
{
  "type": "doubleLast",
  "name": "lastValue",
  "fieldName": "floatValue"
}
```

**Property Reference**

**Property**: `name`</br>
**Description**: the output name for the respective aggregator.</br>
**Required**: true

**Property**: `fieldName`</br>
**Description**: the name of the metric column used for the respective aggregator. Must be a field containing numeric values.</br>
**Required**: true

**Property**: `type`</br>
**Description**: must be 'doubleLast'.</br>
**Required**: true

---

**Name**: `stringFirst` - aggregator

**Explanation**: The stringFirst aggregator computes the first string value of all metric values, i.e. can be used when the first value of a specified field is needed for the returned events.

**Example**:

```
{
  "type": "stringFirst",
  "name": "firstValue",
  "fieldName": "sessionID"
}
```

**Property Reference**

**Property**: `name`</br>
**Description**: the output name for the respective aggregator.</br>
**Required**: true

**Property**: `fieldName`</br>
**Description**: the name of the metric column used for the respective aggregator. Must be a field containing string values.</br>
**Required**: true

**Property**: `type`</br>
**Description**: must be 'stringFirst'.</br>
**Required**: true

---

**Name**: `stringLast` - aggregator

**Explanation**: The stringLast aggregator computes the last value of all metric values, i.e. can be used when the last value of a specified field is needed for the returned events.

**Example**:

```
{
  "type": "stringLast",
  "name": "lastValue",
  "fieldName": "sessionID"
}
```

**Property Reference**

**Property**: `name`</br>
**Description**: the output name for the respective aggregator.</br>
**Required**: true

**Property**: `fieldName`</br>
**Description**: the name of the metric column used for the respective aggregator. Must be a field containing string values.</br>
**Required**: true

**Property**: `type`</br>
**Description**: must be 'stringLast'.</br>
**Required**: true

---

**Name**: `doubleAny` - aggregator

**Explanation**: The doubleAny aggregator returns any double metric value including null. It can simplify and optimize the performance by returning the first encountered value (floatAny and longAny instead of doubleAny work as well).

**Example**:

```
{
  "type": "doubleAny",
  "name": "any",
  "fieldName": "TelemetryDeck.Device.screenResolutionHeight"
}
```
**Property Reference**

**Property**: `name`</br>
**Description**: the output name for the respective aggregator.</br>
**Required**: true

**Property**: `fieldName`</br>
**Description**: the name of the metric column used for the respective aggregator. Must be a field containing numeric values.</br>
**Required**: true

**Property**: `type`</br>
**Description**: must be 'doubleAny'.</br>
**Required**: true

---

**Name**: `stringAny` - aggregator

**Explanation**: The stringAny aggregator returns any string metric value. It can simplify and optimize the performance by returning the first encountered value.

**Example**:

```
{
  "type": "stringAny",
  "name": "any",
  "fieldName": "TelemetryDeck.Device.operatingSystem"
}
```

**Property Reference**

**Property**:`name`</br>
**Description**: the output name for the respective aggregator.</br>
**Required**: true

</br>

**Property**: `fieldName`</br>
**Description**: the name of the metric column used for the respective aggregator. Must be a field containing string values.</br>
**Required**: true

**Property**: `type`</br>
**Description**: must be 'stringAny'.</br>
**Required**: true

### Approximate aggregations

**Name**: `thetaSketch` - aggregator

**Explanation**: The thetaSketch-aggregator computes the number of unique values in the specified field for the returned events. Theta sketches are a probabilistic data structure used for the count-distinct problem. They allow to quickly count elements in sets, such as the set of users or sessions in aggregation buckets.

**Example**:

```
{
  "type": "thetaSketch",
  "name": "countSessions",
  "fieldName": "sessionID"
}
```

**Property Reference**

**Property**: `name`</br>
**Description**: the output name for the respective aggregator.</br>
**Required**: true

**Property**: `fieldName`</br>
**Description**: the name of the metric column used for the respective aggregator.</br>
**Required**: true

**Property**: `type`</br>
**Description**: must be 'thetaSketch'.</br>
**Required**: true

---

**Name**: `histogram` - aggregator

**Explanation**: The histogram aggregator computes the histogram of a metric. By default, it computes the histogram of the field floatValue, because that is the only metric that is guaranteed to be a numerical value in TelemetryDeck events. This aggregator only works within queries of type timeseries with granularity all. Display mode should be bar chart.

**Example**:

```
{
  "type": "histogram",
  "fieldName": "<metric_name, defaults to 'floatValue'>",
  "name": "<output_name, defaults to 'Histogram'>",
  "numBuckets": "<number_of_buckets, defaults to 10>"
}
```

**Property Reference**

**Property**: name</br>
**Description**: the output name for the respective aggregator, which can be defined. Defaults to 'Histogram'.</br>
**Required**: false

**Property**: `fieldName`</br>
**Description**: the name of the metric column used for the respective aggregator. Must be a field containing numeric values. To count events must be 'clientUser'.</br>
**Required**: false

**Property**: `type`</br>
**Description**: must be 'histogram'.</br>
**Required**: true

**Property**: `numBuckets`</br>
**Description**: defines the number of bars in the histogram chart. Defaults to 10.</br>
**Required**: false

**Property**: `splitPoints`</br>
**Description**: a list with manually defined split points between cohorts of the histogram. If split points are defined the numBuckets property is not used anymore.</br>
**Required**: false

### Miscellaneous aggregations

**Name**: `filtered` - aggregator

**Explanation**: A filtered aggregator wraps any given aggregator, but only aggregates the values for which the given dimension filter matches. This makes it possible to compute the results of a filtered and an unfiltered aggregation and / or multiple differently filtered aggregations simultaneously, without having to issue multiple queries. Filtered aggregators also support relative time intervals as filters. Following an example for a cohort containing only yesterday's users.

**Example**:

```
{
  "aggregator": {
    "fieldName": "clientUser",
    "name": "Users_Day -1",
    "type": "thetaSketch"
  },
  "filter": {
    "dimension": "__time",
    "relativeIntervals": [
      {
        "beginningDate": {
          "component": "day",
          "offset": -1,
          "position": "beginning"
        },
        "endDate": {
          "component": "day",
          "offset": -1,
          "position": "end"
        }
      }
    ],
    "type": "interval"
  },
  "type": "filtered"
}
```

**Property Reference**

**Property**: `name`</br>
**Description**: the output name for the respective aggregator, which can be defined. Defaults to 'Histogram'.</br>
**Required**: true

**Property**: `filter`</br>
**Description**: specification of the cohort via any of the available filters..</br>
**Required**: true

**Property**: `aggregator`</br>
**Description**: specification of the aggregation via any of the available aggregators.</br>
**Required**: true

**Property**: `type`</br>
**Description**: must be 'filtered'.</br>
**Required**: true