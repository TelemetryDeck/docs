---
title: Namespaces
tags:
  - setup
  - advanced
lead: Namespaces isolate your organization's data, boost query performance, and unlock advanced features like Sync Queries for faster analytics.
---

All events (previously known as signals) in TelemetryDeck belong to a namespace. If we were using a relational database for events data (which we don't), we would call these database tables, similar to when you run `SELECT * FROM your_namespace`.

Namespaces ensure that each customer's data remains completely separated from other customers' data. They significantly improve query performance and, being human-readable, make debugging and maintenance more straightforward behind the scenes.

## Why use namespaces?

- **Performance**: Dedicated data storage significantly speeds up queries
- **Privacy**: Complete data isolation between organizations
- **Organization**: Clear separation makes data management more reliable

## Naming your namespace

Namespaces follow reverse DNS notation, matching your organization's domain. For example, if your domain is `telemetrydeck.com`, your namespace should be `com.telemetrydeck`. This follows the same convention as iOS app identifiers like `com.telemetrydeck.viewer`, creating consistency across your organization's identifiers.

## Enabling namespaces

To enable namespaces for your organization:

1. Navigate to https://dashboard.telemetrydeck.com/namespace
2. Enter your namespace name following the reverse DNS notation
3. The system will begin converting your existing data automatically

The conversion process copies data in 30-day chunks, working backwards from today. Each 30-day period typically takes 1-2 hours to process, though this varies based on your data volume.

You can start using your namespace immediately while conversion continues in the background. Recent data will be available right away, with older data becoming accessible as the conversion progresses.

To activate the namespace before conversion completes, enable it manually at https://dashboard.telemetrydeck.com/namespace. Otherwise, it will activate automatically once all data has been converted.

## Enhanced features with namespaces

Namespaces unlock additional capabilities, including **Sync Queries**.

Traditionally, TelemetryDeck processes queries asynchronously: they enter a queue, execute in the background, and the frontend periodically checks for completion. While this approach works for all organizations, it can introduce noticeable delays.

With namespaces enabled, Sync Queries use the improved performance and caching to return results within the same HTTP request. This eliminates the wait-and-check cycle, delivering noticeably faster query responses.

Enable Sync Queries at https://dashboard.telemetrydeck.com/namespace to experience the performance improvement. (And let us know if something doesn't work for you with this beta feature!)
