---
title: Granularity
tags:
- app analytics
- web analytics
---

## Introduction

This section contains an overview of all graphical display methods and charts available in TelemetryDeck plus respective remarks.

## Specifics & Examples

Following you can find information regarding the different options to graphically display returned data and examples of their application.

**Name**: Table

**Explanation**: This is the default mode for graphical display and can be used with all query types. Returned data is shown in table form. This is in most cases not a good way to present data in a way easy to digest and to identify outliers, trends etc. though.

**Example**:

```
{
  "aggregations": [
    {
      "type": "userCount"
    }
  ],
  "dimensions": [
    {
      "dimension": "TelemetryDeck.Device.systemVersion",
      "outputName": "TelemetryDeck.Device.systemVersion",
      "outputType": "STRING",
      "type": "default"
    },
    {
      "dimension": "TelemetryDeck.UserPreference.language",
      "outputName": "TelemetryDeck.UserPreference.language",
      "outputType": "STRING",
      "type": "default"
    }
  ],
  "granularity": "all",
  "queryType": "groupBy"
}
```

---

**Name**: Line Chart

**Explanation**: A Line Chart is the usual way to display data of timeseries queries. The y-axis indicates the values and the x-axis the timeline.

Issues and workaround: There are problems with displaying both data of aggregations and post-aggregations in a Line Chart as well as aggregators of type ‘filtered’. A workaround for that issue is hiding an aggregator by starting the name with an underscore and in the post-aggregations multiply the hidden aggregator with 1 so that only post-aggregations are displayed. In that case it is necessary to add the element “name”: “_none” in the aggregator to completely hide it (if only the ‘name’ in the thetaSketch starts with an underscore an empty value is added in the Line Chart, which is bothering). This functions to hide aggregators applies to all query types, but is usually most useful for timeseries-queries.

Following an example for a hidden aggregator for users with preferred language English, which is then accessed in the post-aggregations.

**Example**:

```
{
  "aggregations": [
    {
      "aggregator": {
        "fieldName": "clientUser",
        "name": "_Bucket_English",
        "type": "thetaSketch"
      },
      "filter": {
        "dimension": "TelemetryDeck.UserPreference.language",
        "type": "selector",
        "value": "en"
      },
      "name": "_none",
      "type": "filtered"
    }
  ],

  "postAggregations": [
    {
      "fields": [
        {
          "fieldName": "_Bucket_English",
          "type": "finalizingFieldAccess"
        },
        {
          "name": "const",
          "type": "constant",
          "value": 1
        }
      ],
      "fn": "*",
      "name": "Users with preferred language English",
      "type": "arithmetic"
    }
  ],

  "granularity": "day",
  "queryType": "timeseries"
}
```

---

**Name**: Bar Chart

**Explanation**: Bar Charts are an alternative way to display timeseries queries. For example, it can be very useful when granularity is all and total values for multiple (post-)aggregators are to be displayed or only one (post-)aggregator is to be displayed independent of the granularity. With multiple (post-)aggregators and granularity not all it tends to become hard to digest the visualization. Following an example of an aggregator to display bar(s) of events per user independent of the desired granularity.

It is sometimes more robust to create aggregators and post-aggregators as constructed in the example Line Chart, i.e. with thetaSketch in the aggregator. For this case however the used version works as well.

Hidding x-axis: When granularity is all and a Bar Chart shall be used the x-axis should be hidden as the values for the timeline would not be correct. This can be done by adding the ‘chart configuration’ as showed in the query.

**Example**:

```
{
  "aggregations": [
    {
      "name": "Users",
      "type": "userCount"
    },
    {
      "name": "_Events",
      "type": "eventCount"
    }
  ],
  "chartConfiguration": {
    "options": {
      "xAxis": {
        "show": false,
        "type": "time"
      }
    }
  },
  "granularity": "all",
  "postAggregations": [
    {
      "fields": [
        {
          "fieldName": "_Events",
          "name": "Events",
          "type": "finalizingFieldAccess"
        },
        {
          "fieldName": "Users",
          "name": "Users",
          "type": "finalizingFieldAccess"
        }
      ],
      "fn": "/",
      "name": "Average Events per User",
      "type": "arithmetic"
    }
  ],
  "queryType": "timeseries"
}
```

---

**Name**: Experiment

**Explanation**: The display type ‘Experiment’ is specifically implemented to display experiment-queries and is thus the recommended display type for this query type. It can only be used when granularity is all.

**Example**:

```
{
  "aggregations": [
    {
      "fieldName": "clientUser",
      "name": "count",
      "type": "thetaSketch"
    }
  ],
  "granularity": "all",
  "queryType": "experiment",
  "sample1": {
    "filter": {
      "dimension": "type",
      "type": "selector",
      "value": "trialScreenViewed.Paywall_1"
    },
    "name": "Paywall 1"
  },
  "sample2": {
    "filter": {
      "dimension": "type",
      "type": "selector",
      "value": "trialScreenViewed.Paywall_2"
    },
    "name": "Paywall 2"
  },
  "successCriterion": {
    "filter": {
      "dimension": "type",
      "type": "selector",
      "value": "convertedFromTrial"
    },
    "name": "Converted from Trial"
  }
}
```

---

**Name**: Funnel Chart

**Explanation**: The display type ‘Funnel Chart’ is specifically implemented to display funnel-queries and is thus the recommended display type for this query type. It can only be used when granularity is all.

**Example**:

```
{
  "aggregations": [
    {
      "fieldName": "clientUser",
      "name": "count",
      "type": "thetaSketch"
    }
  ],
  "granularity": "all",
  "queryType": "funnel",
  "steps": [
    {
      "filter": {
        "dimension": "type",
        "type": "selector",
        "value": "paidSubscription"
      },
      "name": "Converted to Paid Subscription"
    },
    {
      "filter": {
        "dimension": "type",
        "type": "selector",
        "value": "paidSubscription_renewed"
      },
      "name": "Paid Subscripction renewed"
    }
  ]
}
```

---

**Name**: Donut Chart

**Explanation**: The display type ‘Donut Chart’ is specifically implemented to display topN-queries and is thus the recommended display type for this query type.

Depending on the granularity this display type has the following effects:

- Granularity all: When granularity is all the results are displayed as a donut chart.
- Granularity not all, display type donut: When granularity is not all the results are displayed in normalized bars, i.e. when granularity is day for each day there is a bar of the same height. The share of the different values determines how much of the bar is shown with the colour for that value.
- Addtional remark when granularity is not all and display type is Bar Chart: for topN-queries also the display type Bar Chart can be used. Then the data is visualized with bars with the total values, i.e. when granularity is day each bar can be of different height. Again, the share of the different values causes how much of the bar is shown with the colour for that value.
The following example would return an actual Donut Chart, when the respective display type is selected.**Example**:

```
{
  "aggregations": [
    {
      "name": "count",
      "type": "userCount"
    }
  ],
  "dimension": {
    "dimension": "TelemetryDeck.Device.modelName",
    "extractionFn": {
      "lookup": "deviceType",
      "retainMissingValue": true,
      "type": "registeredLookup"
    },
    "outputName": "TelemetryDeck.Device.modelName",
    "type": "extraction"
  },
  "granularity": "all",
  "metric": {
    "metric": "count",
    "type": "numeric"
  },
  "queryType": "topN",
  "threshold": 50
}
```

---

**Name**: Sankey Chart

**Explanation**: This is a display type still being tested. It shall be used to display navigational analytics eventually, but is currently still not a recommended type.

**Example**:

```
{
  "aggregations": [
    {
      "fieldName": "count",
      "name": "count",
      "type": "longSum"
    }
  ],
  "dimension": {
    "dimension": "TelemetryDeck.Navigation.identifier",
    "outputName": "TelemetryDeck.Navigation.identifier",
    "type": "default"
  },
  "filter": {
    "fields": [
      {
        "field": {
          "dimension": "TelemetryDeck.Navigation.identifier",
          "type": "selector",
          "value": ""
        },
        "type": "not"
      },
      {
        "dimension": "TelemetryDeck.Navigation.identifier",
        "pattern": "-> https://telemetrydeck.com/docs/guides/swift-setup/(.*)",
        "type": "regex"
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
  "threshold": 10
}
```

---

**Name**: Explanations

**Explanation**: It is possible to add an explanation field to the graphical display of queries. This is implemented as the element ‘explanation’ to the ‘chartConfiguration’ issued in the display type ‘Bar Chart’.

Following an example to hide the x-axis and also add an explanation (it is also possible to just add a comment and not hide the x-axis).

**Example**:

```
{
    "chartConfiguration": {
      "explanation": "This chart shows amount of users and events per user.",
      "options": {
        "xAxis": {
          "show": false,
          "type": "time"
        }
      }
    }
}
```