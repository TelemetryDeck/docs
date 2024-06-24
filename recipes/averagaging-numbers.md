---
title: Calculating Averages, Sums, Minimums and Maximums
description: A snippet for when you want the aggregate floatValues by sum, average, minimum or maximum in TelemetryDeck.
lead: A snippet for when you want the aggregate floatValues by sum, average, minimum or maximum.
order: 1
testedOn: TelemetryDeck API v3
searchEngineTitle: How to aggregate floatValues by sum, average, minimum or maximum
searchEngineDescription: This is a quick overview on how to aggregate floatValues by sum, average, minimum or maximum using the TelemetryDeck Query Language.
---

When you're sending numerical values to TelemetryDeck's `floatValue` signal property, you usually want to aggregate them somehow. This is how to get the average value of a `floatValue` metric for a specific signal type:

```json
{
  "granularity": "day",
  "queryType": "timeseries",
  "filter": {
    "dimension": "type",
    "type": "selector",
    "value": "YOUR_SIGNAL_TYPE"
  },
  "baseFilters": "thisApp",
  "appID": "YOUR_APP_ID",
  "aggregations": [
    {
      "fieldName": "floatValue",
      "name": "Mean",

      // "doubleSum", "doubleMin", "doubleMax" also work here
      "type": "doubleMean"
    }
  ]
}
```

Replace `YOUR_APP_ID` with your app id and `YOUR_SIGNAL_TYPE` with your signal type.

## How it works

### Granularity

The granularity is set to `day` in this example. This means that the data will be aggregated by day. You can also use `hour` or `month` as a granularity to get averages for months or hours. Use granularity `all` to produce one single number for the whole displayed time range. (The displayed time range is usually set in the UI).

### Filter

The filter is used to filter the data by app id and signal type. You can also add more filters here, for example to filter by a specific version of your app.

### Aggregations

The aggregation is set to `doubleMean` in this example. This means that the average value of the `floatValue` metric will be calculated. You can also use `doubleSum` to get the sum of all values or `doubleMin` and `doubleMax` to get the minimum or maximum value.

[Read more on aggregators in TQL](/docs/tql/aggregators/).
