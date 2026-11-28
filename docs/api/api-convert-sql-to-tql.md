---
title: Converting SQL to TQL
tags: Advanced
description: Using the TelemetryDeck API, you can convert an SQL query to a TQL query
---

??? warning "Paid plans only"

    API access — including running queries — is available on TelemetryDeck's paid plans. If your organization is on the free plan, upgrade your plan first and you'll be able to generate a personal access token and run queries.

??? note "Authorization"

    You need a personal access token to authenticate against the TelemetryDeck API. Our article [Getting a Personal Access Token](api-token.md) explains how to generate one from your dashboard.

Sometimes you start with an SQL query, but want to later convert it to TQL to have a more structured query you can fine-tune.

## Running the query

POST your query to the `/api/v4/query/sql/convert` endpoint. The endpoint accepts SQL and returns an equivalent TQL query.

=== "Request"

    ```json
    POST /api/v4/query/sql/convert HTTP/1.1
    Authorization: Bearer tdpat_…
    Content-Type: application/json
    Host: api.telemetrydeckapi.com

    {
      "query": "SELECT \"type\", SUM(\"count\") AS events FROM {{events}} GROUP BY 1 ORDER BY 2 DESC LIMIT 10"
    }
    ```

=== "Response"

    ```json
    {
      "aggregations": [{ "fieldName": "count", "name": "a0", "type": "longSum" }],
      "dimension": {
        "dimension": "type",
        "outputName": "d0",
        "outputType": "STRING",
        "type": "default"
      },
      "granularity": { "type": "all" },
      "metric": { "metric": "a0", "type": "numeric" },
      "queryType": "topN",
      "threshold": 10
    }
    ```
