---
title: Granularity
tags:
- app analytics
- web analytics
---

## Introduction

Post-aggregations are specifications of processing that should happen on aggregated values as they come out of the timeseries database. The properties vary between the post-aggregators.

Post-aggregators may only be created for further calculations and in that case can be hidden from returned data when their name-property starts with an underscore.

## Specifics & Examples

Following you can find information regarding the different post-aggregators available and examples of their application.

**Name**: Field accessor post-aggregator

**Explanation**: The field accessor post-aggregator returns the value produced by the specified aggregator. Use type 'finalizingFieldAccess' to return a finalized value, such as an estimated cardinality.

**Example**:

```
{
    "type": "fieldAccess",
    "name": "total",
    "fieldName": "aggregation_total"
}
```

**Property Reference**

**Property**: `name`</br>
**Description**: the output name for the respective post-aggregator.</br>
**Required**: true

**Property**: `fieldName`</br>
**Description**: the output name of the dimension or aggregator to reference.</br>
**Required**: true

**Property**: `type`</br>
**Description**: must be 'fieldAccess' or 'finalizingFieldAccess'. Use type 'fieldAccess' to return the raw aggregation object, or use type 'finalizingFieldAccess' to return a finalized value, such as an estimated cardinality.</br>
**Required**: true

---

**Name**: Constant post-aggregator

**Explanation**: This constant post-aggregator always returns the specified value. This aggregator is usually used in further calculations within the post-aggregations.

**Example**:

```
{
    "type": "constant",
    "name": "const",
    "value": 100
}
```

**Property Reference**

**Property**: `name`</br>
**Description**: the output name for the respective post-aggregator.</br>
**Required**: true

**Property**: `value`</br>
**Description**: the constant value.</br>
**Required**: true

**Property**: `type`</br>
**Description**: must be 'constant'.</br>
**Required**: true

---

**Name**: Arithmetic post-aggregator

**Explanation**: The arithmetic post-aggregator applies the provided function to the given fields from left to right. The supported functions are `+, –, *, /`, and quotient. Calculations using this post-aggregator can be nested.

Further remarks:

- / division always returns 0 if dividing by 0, regardless of the numerator.
- Quotient division behaves like regular floating point division.
- Arithmetic post-aggregators always use floating point arithmetic.
- Arithmetic post-aggregators may also specify an ordering, which defines the order of resulting values when sorting.
In the following example of a nested post-aggregator a cohort 'part' is divided by the total to calulate its 'ratio', which is then multiplied by 100 to get a percentage value.

**Example**:

```
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
          {
            "type": "fieldAccess",
            "name": "part",
            "fieldName": "part"
          },
          {
            "type": "fieldAccess",
            "name": "total",
            "fieldName": "aggregation_total"
          }
        ]
      },
      {
        "type": "constant",
        "name": "const",
        "value": 100
      }
    ]
}
```

**Property Reference**

**Property**: `name`</br>
**Description**: the output name for the respective post-aggregator.</br>
**Required**: true

**Property**: `fn`</br>
**Description**: one of the supported functions: `+, -, *, /`, and quotient.</br>
**Required**: true

**Property**: `type`</br>
**Description**: must be 'arithmetic'.</br>
**Required**: true

**Property**: `fields`</br>
**Description**: list of post-aggregator specs which define inputs to the fn.</br>
**Required**: true

**Property**: ordering</br>
**Description**: if no ordering (or null) is specified, the default floating point ordering is used. numericFirst ordering always returns finite values first, followed by NaN, and infinite values last.</br>
**Required**: false

---

**Name**: Expression post-aggregator

**Explanation**: The expression post-aggregator is defined using a Druid expression. For the example it is assumed that aggregators '_part' and '_tot' are defined within the query enabling the calculation '100 * (_part / _tot)'.

**Example**:

```
{
    "type": "expression",
    "name": "part_percentage",
    "expression": "100 * (_part / _tot)"
}
```

**Property Reference**

**Property**: `name`</br>
**Description**: the output name for the respective post-aggregator.</br>
**Required**: true

**Property**: `expression`</br>
**Description**: Native Druid expression to compute, may refer to any dimension or aggregator output names.</br>
**Required**: true

**Property**: `type`</br>
**Description**: must be 'expression'.</br>
**Required**: true

---

**Name**: Theta Sketch Estimate post-aggregator

**Explanation**: The theta sketch estimate post-aggregator is used to wrap a theta sketch object such that it can be used in post aggregations. It is mostly used in combination with the theta sketch set operation post-aggregator.

The example is for Theta Sketch Estimate post-aggregator and Theta Sketch Set Operation post-aggregator to compute the number of users who launched the app by notification and entered data.

**Example**:

```
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

**Property Reference**

**Property**: `name`</br>
**Description**: the output name for the respective post-aggregator.</br>
**Required**: true

**Property**: `field`</br>
**Description**: post aggregator of type fieldAccess that refers to a thetaSketch aggregator or that of type thetaSketchSetOp.</br>
**Required**: true

**Property**: `type`</br>
**Description**: must be 'thetaSketchEstimate'.</br>
**Required**: true

---

**Name**: Theta Sketch Set Operation post-aggregator

**Explanation**: The theta sketch set operation post-aggregator is used in combination with the theta sketch estimate post-aggregator to wrap a theta sketch object such that it can be used in post aggregations.

The example is for Theta Sketch Estimate post-aggregator and Theta Sketch Set Operation post-aggregator to compute the number of users who launched the app by notification and entered data.

**Example**:

```
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

**Property Reference**

**Property**: `name`</br>
**Description**: the output name for the respective post-aggregator.</br>
**Required**: true

**Property**: `fields`</br>
**Description**: array of fieldAccess type post aggregators to access the thetaSketch aggregators or thetaSketchSetOp type post aggregators to allow arbitrary combination of set operations.</br>
**Required**: true

**Property**: `func`</br>
**Description**: one out of 'UNION', 'INTERSECT', or 'NOT'.</br>
**Required**: true

**Property**: `type`</br>
**Description**: must be 'thetaSketchEstimate'.</br>
**Required**: true

---

**Name**: Greatest / Least post-aggregator

**Explanation**: The post-aggregator doubleGreatest computes the maximum of all fields and Double.NEGATIVE_INFINITY. doubleLeast computes the minimum of all fields and Double.POSITIVE_INFINITY. The difference between the doubleMax aggregator and the doubleGreatest post-aggregator is that doubleMax returns the highest value of all rows for one specific column while doubleGreatest returns the highest value of multiple columns in one row. These are similar to the SQL MAX and GREATEST functions.

**Example**:

```
{
    "type": "doubleGreatest",
    "name": "theGreatest",
    "fields": [
      {
        "type": "fieldAccess",
        "fieldName": "someAgg"
      },
      {
        "type": "fieldAccess",
        "fieldName": "someOtherAgg"
      }
    ]
}
```

**Property Reference**

**Property**: `name`</br>
**Description**: the output name for the respective post-aggregator.</br>
**Required**: true

**Property**: `fields`</br>
**Description**: list of post-aggregator specs which define inputs to the greatest or least function.</br>
**Required**: true

**Property**: `type`</br>
**Description**: must be 'doubleGreatest' or 'doubleLeast' (longGreatest and longLeast instead of doubleGreatest and doubleLeast work as well).</br>
**Required**: true