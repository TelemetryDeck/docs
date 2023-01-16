---
title: Dimension Spec
description: DimensionSpecs define how dimension values get transformed prior to aggregation in the TelemetryDeck Query Language.
lead: DimensionSpecs define how dimension values get transformed prior to aggregation.
order: 200
---

The default DimensionSpec returns dimension values as is and optionally renames the dimension.

If an etraction function is set, it returns dimension values transformed using the given extraction function.

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
