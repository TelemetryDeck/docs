---
title: Context
tags:
- app analytics
- web analytics
---

## Introduction

Context specifies how a query is calculated and cached in the TelemetryDeck Query Engine.

## Specifics & Examples

Following you can find information regarding different Context elements available and an example of their application.

**Name**: Context Options

**Explanation**: There are four parameters usable via context.

If you specify a query context with your query, you can specify for how long it is cached, and how its calculation is prioritized for example.
**Example**:

```
{
    "context": {
      "priority": -1,
      "grandTotal": true,
      "cacheValidityDuration": 1440
    }
}
```

**Property Reference**

**Property**: `timeout`</br>
**Description**: query timeout in millis, beyond which unfinished queries will be cancelled.</br>
**Required**: false

**Property**: `priority`</br>
**Description**: the Query Priority. Queries with higher priority get precedence for in the query queue. Possible values are ‘-1’, ‘0’, ‘1’. Defaults to ‘0’.</br>
**Required**: false

**Property**: `grandTotal`</br>
**Description**: defines whether to include a grand total as the last row in query results. Defaults to ‘false’.</br>
**Required**: false

**Property**: `cacheValidityDuration`</br>
**Description**: defines how long the results of a query are cached. This is used to determine whether to use cached results or to re-run the query. Value is in minutes, default is 10.</br>
**Required**: false