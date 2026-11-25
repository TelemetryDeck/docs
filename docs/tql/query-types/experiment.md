---
title: Experiment
tags:
- app analytics
- web analytics
- A/B-testing
---

## Introduction

An Experiment Query compares two sets of users to find out which of them is reaching a given success criterion more often. It is a way of generating an A/B testing experiment. This is the proper query type if you want to compare two cohorts with regard to reaching a defined success criterion.

## Core Concepts & Examples

Following you can find additional information and a practical example.

**Use Case**: Payscreen Experiment

**Explanation**: Compares Payscreen A and Payscreen B, which will return metrics to judge which is more successful (assuming the respective events are implemented).

There is an implementation to display experiment queries graphically. This can be applied by clicking on the respective experiment-symbol, but works only when granularity is 'all'. With other granularities the returned data can only be displayed in table format.

The output of an experiment query is a list of objects with the following properties:

- `timestamp`: The timestamp of the interval (or none if granularity all is used).
- `cohort_1`: The number of users in the first sample.
- `cohort_2`: The number of users in the second sample.
- `success`: The number of users in any sample that reached the success criterion.
- `cohort_1_success`: The number of users in the first sample that reached the success criterion.
- `cohort_2_success`: The number of users in the second sample that reached the success criterion.
- `zscore`: The z-score of the experiment.
- `pvalue`: The p-value of the experiment.

**Example**:

```
{
  "granularity": "all",
  "queryType": "experiment",
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

### Property Reference

Here is a detailed overview of all available properties for Experiment Queries.

**Property**: `queryType`</br>
**Description**: for this type has to be 'experiment'.</br>
**Required**: true

**Property**: `dataSource`</br>
**Description**: defaults to namespace, should usually not be changed.</br>
**Required**: false

**Property**: `relativeIntervals`</br>
**Description**: see also respective section; the time intervals to query, specified as relative to time of query (if neither relativeIntervals nor intervals are set, the time period of the date picker in the dashboard is applied).</br>
**Required**: false

**Property**: `intervals`</br>
**Description**: a JSON Object representing ISO-8601 Intervals. This defines the time ranges to run the query over, specified as absolute time intervals (if neither relativeIntervals nor intervals are set, the time period of the date picker in the dashboard is applied).</br>
**Required**: false

**Property**: `granularity`</br>
**Description**: see also respective section; defines the granularity of the query. Potential values are 'hour', 'day', 'week', 'month', 'quarter', 'year' and 'all'.</br>
**Required**: true

**Property**: `filter`</br>
**Description**: see also respective section; a filter that is applied to the query.</br>
**Required**: false

**Property**: `sample1`</br>
**Description**: the first sample to compare, i.e. the control group in the experiment. It must have a name and a filter property. The filter property is used to select signals of all users that are part of the sample.</br>
**Required**: true

**Property**: `sample2`</br>
**Description**: the second sample to compare, i.e. the test group in the experiment. It must have a name and a filter property. The filter property is used to select signals of all users that are part of the sample.</br>
**Required**: true

**Property**: `successCriterion`</br>
**Description**: the success criterion to use for the experiment. It must have a name and a filter property. The filter property is used to select signals of all users that are part of the sample.</br>
**Required**: true

**Property**: `context`</br>
**Description**: see also respective section; a QueryContext object that specifies how the query is calculated and cached.</br>
**Required**: false