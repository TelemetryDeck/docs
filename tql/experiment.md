---
title: Experiment Query
description: Compares two sets of users to find out which of them is reaching a given success function more often in the TelemetryDeck Query Language.
lead: Compares two sets of users to find out which of them is reaching a given success function more often.
order: 60
testedOn: TelemetryDeck API v3
tags:
  - setup
  - intermediate
  - experiments
  - insights
searchEngineTitle: How to use A/B testing experiments from your analytics data
searchEngineDescription: This is a quick overview on how to create A/B testing experiments using the TelemetryDeck Query Language.
---

An experiment query is a way of generating an A/B testing experiment. It's compiled at runtime into a [groupBy](/docs/tql/groupBy/) query, but has a vastly simpler syntax.

## Example

This example compares **Payscreen A** and **Payscreen B** and will return metrics to judge which is more successful.

```json
{
  "dataSource": "telemetry-signals",
  "granularity": "all",
  "queryType": "experiment",
  "relativeIntervals": [
    {
      "beginningDate": {
        "component": "month",
        "offset": -1,
        "position": "beginning"
      },
      "endDate": {
        "component": "month", "
        offset": 0,
        "position": "end"
      }
    }
  ],
  "sample1": {
    "filter": {
      "dimension": "type",
      "type": "selector",
      "value": "payScreenALaunched"
    },
    "name": "Payscreen A"
  },
  "sample2": {
    "filter": {
      "dimension": "type",
      "type": "selector",
      "value": "payScreenBLaunched"
    },
    "name": "Payscreen B"
  },
  "successCriterion": {
    "filter": {
      "dimension": "type",
      "type": "selector",
      "value": "paymentSucceeded"
    },
    "name": "Payment Succeeded"
  }
}
```

## Properties

All [default properties](/docs/tql/query/) and the following properties are supported:

**sample1** (required)
: The first sample to compare, i.e. the control group in the experiment. It must have a `name` and a `filter` property.
The `filter` property is used to select signals of all users that are part of the sample.

**sample2** (required)
: The second sample to compare, i.e. the test group in the experiment. It must have a `name` and a `filter` property.
The `filter` property is used to select signals of all users that are part of the sample.

**successCriterion** (required)
: The success criterion to use for the experiment. It must have a `name` and a `filter` property.
The `filter` property is used to select signals of all users that are part of the sample.

[filter](/docs/tql/filters/) (optional)
: A [Filter](/docs/tql/filters/) to apply to the data to be queried. The default is no filter apart from the [base filters](/docs/tql/baseFilters/).

[granularity](/docs/tql/granularity/) (optional)
: The granularity of the results. The default is `all`.

## Output

```json
{
  "timestamp": "2023-01-01T00:00:00.000Z",
  "cohort_1": 181,
  "cohort_2": 616,
  "success": 53,
  "cohort_1_success": 20,
  "cohort_2_success": 53,
  "zscore": 0.9444253447373949,
  "pvalue": 0.34495233502890077
}
```

The output of an experiment query is a list of objects with the following properties:

**timestamp**
: The timestamp of the interval (or none if granularity `all` is used).

**cohort_1**
: The number of users in the first sample.

**cohort_2**
: The number of users in the second sample.

**success**
: The number of users in any sample that reached the success criterion.

**cohort_1_success**
: The number of users in the first sample that reached the success criterion.

**cohort_2_success**
: The number of users in the second sample that reached the success criterion.

**zscore**
: The [z-score](https://en.wikipedia.org/wiki/Standard_score) of the experiment.

**pvalue**
: The [p-value](https://en.wikipedia.org/wiki/P-value) of the experiment.
