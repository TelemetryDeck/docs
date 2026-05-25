---
title: QueryContext
description: Specifies how a query is calculated and cached in the TelemetryDeck Query Engine.
lead: Specifies how a query is calculated and cached.
order: 240
---

If you specify a query context with your query, you can specify how long it is cached, and how its calculation is prioritized.

```json
"context": {
  "priority": -1,
  "grandTotal": true,
  "cacheValidityDuration": 1440
}
```

## Options

| Option                  | Description                                                                                                                                                          |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `timeout`               | Query timeout in millis, beyond which unfinished queries will be cancelled.                                                                                          |
| `priority`              | Query Priority. Queries with higher priority get precedence for in the query queue. Possible values are `-1`, `0`, `1`. Default: `0`                                 |
| `grandTotal`            | Whether to include a grand total as the last row in query results. Default: `false`                                                                                  |
| `cacheValidityDuration` | How long are the results of this query valid for? This is used to determine whether to use cached results or to re-run the query. Value is in minutes. Default: `10` |
