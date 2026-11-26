---
title: Get the query for an Insight
tags: Advanced
testedOn: API v3 (beta)
description: Using the TelemetryDeck API, you can retrieve the query that is used in an insight
lead: Using the TelemetryDeck API, you can retrieve the query that is used in an insight
---

!!! warning "Paid plans only"

    API access — including retrieving an insight's query — is available on TelemetryDeck's paid plans. If your organization is on the free plan, upgrade your plan first and you'll be able to generate a personal access token and use the API.

## Authorization

You need a personal access token to authenticate against the TelemetryDeck API. Our article [Getting a Personal Access Token](/docs/api/api-token/) explains how to generate one from your dashboard.

## TelemetryDeck Query Language

TelemetryDeck Query Language (TQL) is a JSON-based language for querying time-series data stored in TelemetryDeck. To get the data for an insight, we have to get its query first. You can then [execute the query](/docs/api/api-run-query/) and get the results.

## Time intervals and relative time intervals

A TelemetryDeck query only always needs a specified time interval. You can either specify a specific time interval (such as "June 1st, 2022 to June 31st, 2022"), or you can use a relative time interval (such as "the last 30 days").

In this example, we're going to use relative time intervals. Here's an example relative interval for the last 30 days.

```json
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
```

The `beginningDate` is the start of the interval, and the `endDate` is the end of the interval. The `component` is the time unit, and the `offset` is the number of units. The `position` is either "beginning" or "end", and determines whether the point in time is at the `beginning` or the `end` of the component – usually, you'll want `beginning` for the `beginningDate` and `end` for the `endDate`.

## Getting the query for an insight

To generate the query that is behind an insight, you need its ID. You can get the ID by looking at the URL of the insight in the Dashboard.

Then use that ID to generate an HTTP POST to the API. The POST body needs to be a JSON object with the `relativeInterval` field, which should contain a relative time interval as described in the previous section.

Here's an example query:

```text
POST /api/v3/insights/<insight-id>/query/ HTTP/1.1
Authorization: Bearer tdpat_…
Content-Type: application/json
Host: api.telemetrydeckapi.com

{
  "relativeInterval": {
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
}
```

This will generate and return a complete query for the insight you specified:

```json
{
  "aggregations": [
    {
      "type": "eventCount"
    }
  ],
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

You can [execute the query](/docs/api/api-run-query/) to get its results.
