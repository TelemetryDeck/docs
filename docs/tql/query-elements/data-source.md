---
title: Data Source
tags:
- app analytics
- web analytics
---

## Introduction

The data source to query. It is not required to set a dataSource in the UI. By default the namespace is used, which always works. However, you may come accros a couple of other values for dataSource, which are explained below.

## Specifics & Examples

Following you can find information regarding the different Data Sources available and examples of their application.

**Name**: Namespaces and `com.telemetrydeck.all`

**Explanation**: There are potentially three different values for dataSource in a query:

- namespaces: after a migration period by now all clients have a so-called namespace set. This should be used as dataSource. The name of the namespace is individually chosen.
- com.telemetrydeck.all: you may find the dataSource ‘com.telemetrydeck.all’ when copying TQL queries from default dashboards for example. This dataSource is similar in performance to namespaces, however only default events and parameters are available via this dataSource.
- telemetry-signals: you may find (customized) queries with dataSource ‘telemetry-signals’. With the implementation of namespaces this dataSource is deprecated and does not work anynmore.

**Example**:

```
{
  "dataSource": "<customized-namespace>"
}
```

**Property Reference**

**Property**: `dataSource`</br>
**Description**: in the UI the dataSource always defaults to the respective namespace at query time, which always works. Only when using the Query API (vai terminal or MCP) a dataSource has to be defined - your namespace should be applied in that case.</br>
**Required**: false