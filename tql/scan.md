---
title: Scan Query
description: The Scan query returns raw data rows.
lead: The Scan query returns raw data rows.
order: 40
---

A scan query will return events as they are received, similar to `SELECT * FROM telemetry-signals` SQL command would.

## Example

```json
{
  "queryType": "scan",
  "dataSource": "telemetry-signals",
  "columns": ["__time", "appID", "type"],
  "intervals": ["2024-01-01/2024-01-02"],
  "limit": 3,
  "order": "descending"
}
```

## Properties

All [default properties](/docs/tql/query/) and the following properties are supported:

| Property | Description                                                                                                               |
| -------- | ------------------------------------------------------------------------------------------------------------------------- |
| columns  | A list of columns to return.                                                                                              |
| limit    | The maximum number of rows to return.                                                                                     |
| order    | The ordering of returned rows based on timestamp. Make sure to include the timestamp column `__time` in the columns list. |
