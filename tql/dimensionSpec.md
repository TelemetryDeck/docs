---
title: Dimension Spec
description: DimensionSpecs define how dimension values get transformed prior to aggregation in the TelemetryDeck Query Language.
lead: DimensionSpecs define how dimension values get transformed prior to aggregation.
order: 200
---

The default DimensionSpec returns dimension values as is and optionally renames the dimension.

If an extraction function is set, it returns dimension values transformed using the given extraction function.

## Default DimensionSpec

Returns dimension values as is and optionally renames the dimension.

```json
{
  "type" : "default",
  "dimension" : <dimension>,
  "outputName": <output_name>,
  "outputType": <"STRING"|"LONG"|"FLOAT">
}
```

## Extraction DimensionSpec

Returns dimension values transformed using the given [extraction function](/docs/tql/extractionFunction/).

```json
{
  "type" : "extraction",
  "dimension" : <dimension>,
  "outputName" :  <output_name>,
  "outputType": <"STRING"|"LONG"|"FLOAT">,
  "extractionFn" : <extraction_function>
}
```

## Extraction Functions

Extraction functions define the transformation applied to each dimension value.

Transformations can be applied to both regular (string) dimensions, as well as the special `__time` dimension, which represents the current time bucket according to the query aggregation granularity.

Note: for functions taking string values (such as regular expressions), `__time` dimension values will be formatted in ISO-8601 format before getting passed to the extraction function.

### Regular Expression Extraction Function

Returns the first matching group for the given regular expression. If there is no match, it returns the dimension value as is.

```json
{
  "type" : "regex",
  "expr" : <regular_expression>,
  "index" : <group to extract, default 1>
  "replaceMissingValue" : true,
  "replaceMissingValueWith" : "foobar"
}
```

For example, using `"expr" : "(\\w\\w\\w).*"` will transform `'Monday'`, `'Tuesday'`, `'Wednesday'` into `'Mon`', `'Tue'`, `'Wed'`.

If `index` is set, it will control which group from the match to extract. Index zero extracts the string matching the entire pattern.

If the `replaceMissingValue` property is `true`, the extraction function will transform dimension values that do not match the regex pattern to a user-specified String. Default value is false.

The `replaceMissingValueWith` property sets the String that unmatched dimension values will be replaced with, if `replaceMissingValue` is `true`. If `replaceMissingValueWith` is not specified, unmatched dimension values will be replaced with nulls.

For example, if expr is `"(a\w+)"` in the example JSON above, a regex that matches words starting with the letter a, the extraction function will convert a dimension value like `banana` to `foobar`.

