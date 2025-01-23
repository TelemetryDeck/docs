---
title: Showing a list of events
description: Sometimes you don't want to aggregate your data, but instead show a list of events, like a list of error messages.
lead: Sometimes you don't want to aggregate your data, but instead show a list of events, like a list of error messages.
order: 2
testedOn: TelemetryDeck API v3
searchEngineTitle: How to show a list of events in TelemetryDeck
searchEngineDescription: This is a quick overview on how to show a list of events in TelemetryDeck. This can be useful for showing a list of error messages, or other events that you want to look at individually.
---

TelemetryDeck has a `scan` query type that allows you to show a list of events. This is useful for when you don't want to aggregate your data, but instead show a list of events ordered by time. You could compare them to an SQL SELECT statement.

In this example we'll show a list of 200 most recent error messages. Since scan queries allow filters, just like other queries, we'll use a filter to only show error messages from a specific app version.

```json
{
  "queryType": "scan",
  "limit": 200,
  "columns": ["__time", "appVersion", "error"],
  "filter": {
    "type": "and",
    "fields": [
      {
        "type": "selector",
        "dimension": "type",
        "value": "calculation-error"
      },
      {
        "type": "selector",
        "dimension": "appVersion",
        "value": "1.2.3"
      }
    ]
  }
}
```

Replace `1.2.3` with your app version and `calculation-error` with your signal type. For more information, read the docs on [scan queries](/docs/tql/scan/).

## How it works

### Columns

Scan queries have a `columns` property that allows you to specify the columns to return. In this example we're returning the `__time`, `appVersion`, and `error` columns.

### Limit

The `limit` property is used to specify the maximum number of events to return. In this example we're returning 200 events.

### Filter

The filter is used to filter the data by app id and signal type. You can also add more filters here, for example to filter by a specific version of your app.

[Read more on filters in TQL](/docs/tql/filters/).
