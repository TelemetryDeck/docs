---
title: Run Query
tags: Advanced
testedOn: Query API v4
description: Using the TelemetryDeck API, you can run a query and retrieve its results
lead: Using the TelemetryDeck API, you can run a query and retrieve its results
order: 2
---

!!! warning "Paid plans only"

    API access — including running queries — is available on TelemetryDeck's paid plans. If your organization is on the free plan, upgrade your plan first and you'll be able to generate a personal access token and run queries.

## Authorization

You need a personal access token to authenticate against the TelemetryDeck API. Our article [Getting a Personal Access Token](/docs/api/api-token/) explains how to generate one from your dashboard.

## TelemetryDeck Query Language

TelemetryDeck Query Language (TQL) is a JSON-based language for querying time-series data stored in TelemetryDeck. You can either write a query by hand, or [generate a query from an insight](/docs/api/api-query-from-insight/).

## Running the query

POST your query to the `/api/v4/query/tql` endpoint. The endpoint runs the query and returns the results in the same response. Please allow up to 2 minutes query execution time for very complicated requests.

Request:

```json
POST /api/v4/query/tql HTTP/1.1
Authorization: Bearer tdpat_…
Content-Type: application/json
Host: api.telemetrydeckapi.com

{
  "aggregations": [
    {
      "type": "eventCount"
    }
  ],
  "dataSource": "com.yourorganization",
  "dimension": {
    "dimension": "modelName",
    "outputName": "modelName",
    "type": "default"
  },
  "filter": {
    "fields": [
      {
        "dimension": "appID",
        "type": "selector",
        "value": "B97579B6-FFB8-4AC5-AAA7-DA5796CC5DCE"
      },
      {
        "dimension": "isTestMode",
        "type": "selector",
        "value": "false"
      }
    ],
    "type": "and"
  },
  "granularity": "all",
  "metric": {
    "metric": "count",
    "type": "numeric"
  },
  "queryType": "topN",
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
  ],
  "threshold": 200
}
```

Response:

```json
[
  {
    "result": [
      {
        "count": 516,
        "modelName": "iPhone13,1"
      },

      // ...

      {
        "count": 2,
        "modelName": "iPad8,6"
      }
    ],
    "timestamp": "2022-06-11T00:00:00+0000"
  }
]
```

That's it — the response body is the raw query result. Its exact shape depends on the query type (for example, a `topN` query returns an array of timestamped result buckets as shown above, while a `timeseries` query returns one entry per time bucket).
