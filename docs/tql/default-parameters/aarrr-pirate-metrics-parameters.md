---
title: AARRR Pirate Metrics Parameters
tags:
- app analytics
- activation
- acquisition
- retention
---

## Introduction

TelemetryDeck provides its customers with standard dashboards regarding activation, acquisition, retention and revenue - part of the so called AARRR pirate metrics. The respective parameters can be used for customized queries as well.

## Parameters

**Name**: `TelemetryDeck.Calendar.dayOfMonth`</br>
**Type**: String</br>
**Description**: The day-of-month (1…31) component of the date.

**Name**: `TelemetryDeck.Calendar.dayOfWeek`</br>
**Type**: String</br>
**Description**: The ISO 8601 number of the given day of the week. Monday is 1, Sunday is 7.

**Name**: `TelemetryDeck.Calendar.dayOfYear`</br>
**Type**: String</br>
**Description**: The 1-based day-of-year component of the date.

**Name**: `TelemetryDeck.Calendar.weekOfYear`</br>
**Type**: String</br>
**Description**: The week number within the current year as defined by getFirstDayOfWeek() and getMinimalDaysInFirstWeek().

**Name**: `TelemetryDeck.Calendar.isWeekend`</br>
**Type**: Bool</br>
**Description**: true if the day of the week is Saturday or Sunday, false otherwise.

**Name**: `TelemetryDeck.Calendar.monthOfYear`</br>
**Type**: String</br>
**Description**: The number-of-the-month (1…12) component of the date.

**Name**: `TelemetryDeck.Calendar.quarterOfYear`</br>
**Type**: String</br>
**Description**: The the quarter-of-year (1…4). For API 26 and earlier, it’s the number of the month divided by 3.

**Name**: `TelemetryDeck.Calendar.hourOfDay`</br>
**Type**: String</br>
**Description**: The hour-of-day (1…24) time component. 1 = 00:00-00:59, 10 = 09:00-09:59, 24 = 23:00-23:59.

**Name**: `TelemetryDeck.Acquisition.firstSessionDate`</br>
**Type**: String</br>
**Description**: The date of the first session e.g. 2025-02-22.

**Name**: `TelemetryDeck.Retention.averageSessionSeconds`</br>
**Type**: String</br>
**Description**: The average session duration in seconds of the respective user. Only past sessions are included, with the exception of the first session. During the first session the average is updated when an event is sent.

**Name**: `TelemetryDeck.Retention.distinctDaysUsed`</br>
**Type**: String</br>
**Description**: The number of distinct dates on which the app was used by the user.

**Name**: `TelemetryDeck.Retention.totalSessionsCount`</br>
**Type**: String</br>
**Description**: The total number of sessions of the respective user. The current session is already included in the count.

**Name**: `TelemetryDeck.Retention.previousSessionSeconds`</br>
**Type**: String</br>
**Description**: The duration of the previous session of the user in seconds.

**Name**: `TelemetryDeck.Retention.distinctDaysUsedLastMonth`</br>
**Type**: String</br>
**Description**: The number of distinct dates on which the app was used by the user in the last month.