---
title: Running SQL Queries
tags: Advanced
description: Using the TelemetryDeck API, you can run an SQL query and retrieve its results
---

??? warning "Paid plans only"

    API access — including running queries — is available on TelemetryDeck's paid plans. If your organization is on the free plan, upgrade your plan first and you'll be able to generate a personal access token and run queries.

??? note "Authorization"

    You need a personal access token to authenticate against the TelemetryDeck API. Our article [Getting a Personal Access Token](api-token.md) explains how to generate one from your dashboard.

## Running the query

POST your query to the `/api/v4/query/sql` endpoint. The endpoint runs the query and returns the results in the same response. Please allow up to 2 minutes query execution time for very complicated requests.

=== "Request"

    ```json
    POST /api/v4/query/sql HTTP/1.1
    Authorization: Bearer tdpat_…
    Content-Type: application/json
    Host: api.telemetrydeckapi.com

    {
      "query": "SELECT \"type\", SUM(\"count\") AS events FROM \"com.example\" WHERE __time >= CURRENT_TIMESTAMP - INTERVAL '\''7'\'' DAY GROUP BY 1 ORDER BY 2 DESC LIMIT 10",
      "context": {}
    }
    ```

=== "Response"

    ```json
    [
      ["type", "events"],
      ["STRING", "LONG"],
      ["VARCHAR", "BIGINT"],
      ["TelemetryDeck.Navigation.pathChanged", 158207],
      ["TelemetryDeck.AuditLog.httpRequest", 27962],
      ["pageview", 17714],
      ["TelemetryDeck.Web.pageLeave", 7348],
      ["plans.view", 918],
      ["signupCaptchaSuccess", 584],
      ["organizationCreated", 530],
      ["appCreated", 505],
      ["signupCompleted", 418],
      ["conversionAction", 126]
    ]
    ```

The response body's exact shape depends on the query type.
