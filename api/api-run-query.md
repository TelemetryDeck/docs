---
title: Run Query
tags: Advanced
testedOn: API v3 (beta)
description: Using the TelemetryDeck API, you can run a query and retrieve its results
lead: Using the TelemetryDeck API, you can run a query and retrieve its results
---

{% notewarning "Heads up!" %}

We're still working a lot on the API, so we'll be adding new features and improvements as we go. This also means that sometimes things might break, although we're doing our best to prevent that. Let us know if you see any issues.

Officially, we only allow API access for users in our Tier 2 Pricing tier and above. However, this is currently not enforced by the API, and there will be a grace period before it is. Feel free to try things out and let us know what you think! <3

{% endnotewarning %}

## Authorization

You need a Bearer Token to authenticate against the TelemetryDeck API. Our article [Getting an API Token](api-token.html) explains how to get a Bearer Token.

## TelemetryDeck Query Language

TelemetryDeck Query Language (TQL) is a JSON-based language for querying time-series data stored in TelemetryDeck. You can either write a query by hand, or [generate a query from an insight](api-get-the-query-for-an-insight.html).

## It's all async!

The query API is asynchronous. When you post a query to the API, it returns a task ID. You can then use the task ID to check the status of the query, and once it is succeeded, retrieve the last successful results.

## Step 1: Run the query

To submit your query to the API, POST it to the `/api/v3/query/calculate-async/` endpoint. As a return, you'll receive a task ID. Hold on to that.

Request:

```
POST /api/v3/query/calculate-async/ HTTP/1.1
Authorization: Bearer 🐻🐻🐻🐻🐻🐻🐻🐻🐻🐻🐻🐻🐻
Content-Type: application/json
Host: api.telemetrydeck.com

{
  "aggregations": [
    {
      "fieldName": "count",
      "name": "count",
      "type": "longSum"
    }
  ],
  "dataSource": "telemetry-signals",
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

Result:

```json
{
  "queryTaskID": "55b3487da8018369"
}
```

<small>Psst! There is a synchronous API for this too, but it's not recommended. To try it, leave out the "-async" part of the URL. Note that longer-running queries will be terminated by this API, and we're not yet sure if we're going to support this API at all in the future.</small>

## Step 2: Check the status of the query

This API endpoint will tell you if your query is finished or still running. It will return a JSON object with a "status" field, which will be one of these values:

- `running` - The query is still executing. Check again in a second or so.
- `successful` - The query has finished successfully. You can now retrieve the results.
- `failed` - The query has failed. There will be a second key, `error` which will contain a description of the error.

```

GET /api/v3/task/<task-id>/status/ HTTP/1.1
Authorization: Bearer 🐻🐻🐻🐻🐻🐻🐻🐻🐻🐻🐻🐻🐻
Host: api.telemetrydeck.com

```

Response:

```json
{
  "status": "successful"
}
```

## Step 3: Retrieve the results

Once your query task status is `successful`, you can retrieve the results.

```
GET /api/v3/task/55b3487da8018369/value/ HTTP/1.1
Authorization: Bearer 🐻🐻🐻🐻🐻🐻🐻🐻🐻🐻🐻🐻🐻
Host: api.telemetrydeck.com

```

Response:

```json
{
  "calculationDuration": 0.21845901012420654,
  "calculationFinishedAt": "2022-07-11T14:00:44+0000",
  "result": {
    "rows": [
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
    ],
    "type": "topNResult"
  }
}
```
