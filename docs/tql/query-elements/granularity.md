---
title: Granularity
tags:
- app analytics
- web analytics
---

## Introduction

The granularity determines how fine-grained the query should be, for example per day, per hour, per minute, etc. 'all' is a special value that can be used to disable the granularity. Supported values are 'all', 'hour', 'day', 'week', 'month', 'quarter' and 'year'.

## Specifics & Examples

Following you can find further information regarding granularity and the effects of changing the value.

**Name**: Granularity

**Explanation**: By setting the granularity to 'all' and not defining a time period in the query the number of all active users in the time period defined via the date picker in the UI is returned.

By e.g. setting the granularity to 'week' the weekly active users would be returned. Have in mind that the total of returned users might be higher than in the example with granularity 'all' as a user can be counted for in multiple weeks.

You can imagine that granularity determines how data is bucketed across the dimension time.
**Example**:

```
{
  "aggregations": [
    {
      "type": "userCount"
    }
  ],
  "granularity": "all",
  "queryType": "timeseries"
}
```

**Property Reference**

**Property**: `granularity`</br>
**Description**: the property granularity always has to be defined in any query. Granularities smaller than 'hour' are not implemented in TQL, i.e. 'all', 'hour', 'day', 'week', 'month', 'quarter' and 'year' are available.</br>
**Required**: true