---
title: Retention Query
description: Analyzes user retention across multiple time periods in the TelemetryDeck Query Language.
lead: Analyzes user retention across multiple time periods to understand how many users return to your app over time.
order: 70
testedOn: TelemetryDeck API v3
tags:
  - setup
  - intermediate
  - retention
  - insights
searchEngineTitle: How to analyze user retention from your analytics data
searchEngineDescription: This is a quick overview on how to create retention analysis using the TelemetryDeck Query Language.
---

A retention query analyzes how many users from an initial cohort return to use your app in subsequent time periods. It's compiled at runtime into a [groupBy](/docs/tql/groupBy/) query with sophisticated aggregations to track user cohorts over time.

## Example

This example analyzes monthly retention over a 3-month period:

```json
{
  "queryType": "retention",
  "dataSource": "telemetry-signals",
  "granularity": "month",
  "intervals": [
    {
      "beginningDate": "2024-01-01T00:00:00.000Z",
      "endDate": "2024-03-31T23:59:59.999Z"
    }
  ]
}
```

For daily retention analysis over a week:

```json
{
  "queryType": "retention",
  "dataSource": "telemetry-signals",
  "granularity": "day",
  "intervals": [
    {
      "beginningDate": "2024-01-01T00:00:00.000Z",
      "endDate": "2024-01-07T23:59:59.999Z"
    }
  ]
}
```

## Properties

All [default properties](/docs/tql/query/) and the following properties are supported:

**intervals** or **relativeIntervals** (required)
: The time period to analyze for retention. The query will split this period into smaller intervals based on the granularity setting.

**granularity** (required for retention period definition)
: Determines the retention period granularity. Supported values are:

- `day` - Daily retention analysis
- `week` - Weekly retention analysis
- `month` - Monthly retention analysis (default)
- `quarter` - Quarterly retention analysis
- `year` - Yearly retention analysis

Note: After compilation, the query's granularity is set to `all` for the actual Druid execution.

[filter](/docs/tql/filters/) (optional)
: A [Filter](/docs/tql/filters/) to apply to the data to be queried. The default is no filter apart from the [base filters](/docs/tql/baseFilters/).

## Output

The output of a retention query includes aggregations and post-aggregations that show:

1. **User cohorts per period**: Each time period (day/week/month/etc.) gets an aggregation showing unique users in that period
2. **Retention intersections**: Post-aggregations showing users who appeared in both the initial period and subsequent periods

Example output structure for a 3-month retention:

```json
{
  "timestamp": "2024-01-01T00:00:00.000Z",
  "_2024-01-01_2024-01-31": 5000,
  "_2024-02-01_2024-02-28": 4200,
  "_2024-03-01_2024-03-31": 3800,
  "retention_2024-01-01_2024-01-31_2024-01-01_2024-01-31": 5000,
  "retention_2024-01-01_2024-01-31_2024-02-01_2024-02-28": 2100,
  "retention_2024-01-01_2024-01-31_2024-03-01_2024-03-31": 1520
}
```

The retention values show:

- Initial cohort size (January): 5000 users
- Users from January who returned in February: 2100 (42% retention)
- Users from January who returned in March: 1520 (30.4% retention)

## Minimum Interval Requirements

Each granularity has a minimum interval requirement:

- **day**: At least 1 day between start and end dates
- **week**: At least 1 week between start and end dates
- **month**: At least 1 month between start and end dates
- **quarter**: At least 1 quarter between start and end dates
- **year**: At least 1 year between start and end dates

## Use Cases

Retention queries are ideal for:

- Understanding user engagement patterns over time
- Measuring the effectiveness of app updates or marketing campaigns
- Identifying when users tend to stop using your app
- Comparing retention rates across different user segments (using filters)
- Tracking long-term user loyalty
