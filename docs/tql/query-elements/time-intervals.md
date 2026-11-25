---
title: Time Intervals
tags:
- web analytics
- user agent
---

## Introduction

An Apache Druid query always needs at least one specified time interval to run against. In TelemetryDeck this can be a specific time interval (such as 'June 1st, 2022 to June 31st, 2022') or a relative time interval (such as 'the last 30 days'). In case none of the two is specified in the query, the time interval selected for the dashboard is applied. In all cases the respective time is parsed into specific time intervals when a query is executed.

## Specifics & Examples

Following you can find an example of the application of Absolute and Relative Intervals.

**Name**: Example Absolute Interval

**Explanation**: This example defines two absolute time intervals: January 1, 2012, to January 3, 2012, and February 1, 2012, to February 3, 2012. Each interval is specified as a string containing two ISO 8601 timestamps separated by a / character.

**Example**:

```
"intervals": [
   "2012-01-01T00:00:00.000/2012-01-03T00:00:00.000",
   "2012-02-01T00:00:00.000/2012-02-03T00:00:00.000"
]
```

**Property Reference**

**Property**: intervals</br>
**Description**: A list of strings defining the start and end of one or more time intervals. The start of each interval is inclusive, while the end is exclusive. Therefore, in this example, the dates January 3, 2012, and February 3, 2012, are not included in their respective intervals.</br>
**Required**: true

---

**Name**: Example Relative Interval

**Explanation**: This example defines a relative time interval starting at the beginning of the day 30 days ago and ending at the end of the current day. The offset of 0 represents the current day. This corresponds to the default date picker selection in the UI.

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

**Property**: `relativeIntervals`</br>
**Description**: A list defining one or more relative time intervals. Each interval contains a beginning date and an end date, which are specified using a time component, an offset, and a position.</br>
**Required**: true

**Property**: `beginningDate`</br>
**Description**: Defines the start of the relative time interval.</br>
**Required**: true

**Property**: `endDate`</br>
**Description**: Defines the end of the relative time interval.</br>
**Required**: true

**Property**: `component`
**Description**: The time unit, can be 'hour', 'day', 'week', 'month', 'quarter' and 'year'.</br>
**Required**: true

**Property**: `offset`</br>
**Description**: The number of time units relative to the current date or time. Negative values represent units in the past, while 0 represents the current time unit. For example, -30 represents 30 units in the past.</br>
**Required**: true

**Property**: `position`</br>
**Description**: Defines the position within the specified time unit. For beginningDate, the value must be beginning. For endDate, the value must be end.</br>
**Required**: true