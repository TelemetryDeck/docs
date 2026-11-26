---
title: Virtual Columns
tags:
- app analytics
- web analytics
---

## Introduction

Virtual columns are queryable column 'views' created from a set of columns during a query. A virtual column can potentially draw from multiple underlying columns, although a virtual column always presents itself as a single column. Virtual columns can be referenced by their output names to be used as dimensions or as inputs to filters and aggregators. Each Apache Druid query can accept a list of virtual columns as a parameter.

## Specifics & Examples

Following you can find further information regarding Virtual Columns and an example of their application.

**Name**: Expression Virtual Column

**Explanation**: In this example for a virtual column using expression the accumulated activity duration of users is calculated.

The totalSessionsCount of the respective default parameter includes the current session, whereas the averageSessionSeconds-parameter does not. Thus the session count is lowered by 1 and then multiplied by the average session seconds so that the virtual column returns the total duration per user before the current session.

**Example**:

```
{
  "virtualColumns": [
    {
      "expression": "(cast(\"TelemetryDeck.Retention.totalSessionsCount\", 'DOUBLE')-1) * cast(\"TelemetryDeck.Retention.averageSessionSeconds\", 'DOUBLE')",
      "name": "virtualColumn_accumulatedActivityDuration",
      "outputType": "DOUBLE",
      "type": "expression"
    }
  ]
}
```

**Property Reference**

**Property**: `name`</br>
**Description**: name of the virtual column by which it can be referenced as dimension or as input to filters and (post-)aggregators.</br>
**Required**: true

**Property**: `expression`</br>
**Description**: an expression that takes a row as input and outputs a value for the virtual column, see respective section.</br>
**Required**: true

**Property**: `outputType`</br>
**Description**: expression's output will be coerced to this type. Can be LONG, FLOAT, DOUBLE, STRING, ARRAY types, or COMPLEX types (default is FLOAT).</br>
**Required**: false

**Property**: `type`</br>
**Description**: must be 'expression'.</br>
**Required**: true