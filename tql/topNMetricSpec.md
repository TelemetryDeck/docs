---
title: TopNMetricSpec
description: Specifies how topN values should be sorted in the TelemetryDeck Query Language.
lead: Specifies how topN values should be sorted.
order: 230
---

## Numeric TopNMetricSpec

Indicates the metric to sort topN results by, e.g. "count" in this example:

```json
"metric": {
  "type": "numeric",
  "metric": "count"
}
```

## Dimension TopNMetricSpec

This metric specification sorts TopN results by dimension value.

```json
"metric": {
  "type": "dimension",
  "ordering": "lexicographic",
  "previousStop": "<previousStop_value>"
}
```

Possible sorting orders are:

| Ordering        | Description                                                                                                                   |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| `lexicographic` | Sorts values by converting Strings to their UTF-8 byte array representations and comparing lexicographically, byte-by-byte.   |
| `alphanumeric`  | Suitable for strings with both numeric and non-numeric content. `file12` sorts after `file2`.                                 |
| `numeric`       | Sorts values as numbers.                                                                                                      |
| `strlen`        | Sorts values by their string lengths. When there is a tie, this comparator falls back to using the String `compareTo` method. |
| `version`       | Sorts values as versions. `10.0` sorts after `9.0`, `1.0.0-SNAPSHOT` sorts after `1.0.0`.                                     |

## Inverted TopNMetricSpec

Inverts the order of the delegate metric spec and sorts dimension values in inverted order. It can be used to sort the values in ascending order.

```json
"metric": {
    "type": "inverted",
    "metric": <delegate_top_n_metric_spec>
}
```
