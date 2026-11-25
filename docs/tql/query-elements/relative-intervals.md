---
title: Relative Intervals
tags:
- app analytics
- web analytics
---

## Introduction

An Apache Druid query always needs at least one specified time interval to run against. In TelemetryDeck this can be a specific time interval (such as 'June 1st, 2022 to June 31st, 2022') or a relative time interval (such as 'the last 30 days'). In case none of the two is specified in the query, the time interval selected for the dashboard is applied. In all cases the respective time is parsed into specific time intervals when a query is executed.

## Specifics & Examples

Following you can find an example of the application of Relative Intervals.

**Name**: Example Relative Interval

**Explanation**: This example sets the relative interval to start 30 days in the past and the end to 0, i.e. the current day, which is the default value of the date picker in the UI.

**Example**:

```
{
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

**Property Reference**

**Property**: `beginningDate`</br>
**Description**: The start of the interval is defined in this part.</br>
**Required**: true

**Property**: `endDate`</br>
**Description**: The end of the interval is defined in this part.</br>
**Required**: true

**Property**: `component`</br>
**Description**: The time unit, can be 'hour', 'day', 'week', 'month', 'quarter' and 'year'.</br>
**Required**: true

**Property**: `offset`</br>
**Description**: The number of units. '-30' equals 30 units in the past for example and '0' equals the current unit.</br>
**Required**: true

**Property**: position</br>
**Description**: In case of the defintion of the beginningDate has to be 'beginning'. In case of the definition of endDate has to be 'end'.</br>
**Required**: true