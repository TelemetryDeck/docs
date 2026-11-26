---
title: Dimension Spec
tags:
- app analytics
- web analytics
---

## Introduction

DimensionSpecs define how dimension values get transformed prior to aggregation. An option to specify the output type of a column’s values is provided. This is necessary as it is possible for a column with given name to have different value types in different segments. Results will be converted to the type specified by outputType before merging.

## Specifics & Examples

Following you can find information regarding different Dimension Specs available and examples of their application.

**Name**: `Default DimensionSpec`

**Explanation**: The default DimensionSpec returns dimension values as is and optionally renames the dimension.

**Example**:

```
{
    "dimension": {
      "type": "default",
      "dimension": "example_dimension",
      "outputName": "output_name",
      "outputType": "STRING"
    }
}
```

**Property Reference**

**Property**: `dimension`</br>
**Description**: name of input column as is from dataset or virtual column name.</br>
**Required**: true

**Property**: `outputName`</br>
**Description**: the output name to be used for the dimension.</br>
**Required**: true

**Property**: `type`</br>
**Description**: must be ‘default’.</br>
**Required**: true

**Property**: `outputType`

**Description**: can be ‘STRING’, ‘LONG’ or ‘FLOAT’. Defaults to ‘STRING’ if not specified, so depending on the case you might have to include the type of the column when specifiying a DimensionSpec on a numeric column.

**Required**: false

---

**Name**: `Extraction DimensionSpec`

**Explanation**: If an extraction function is set, it returns dimension values transformed using the given extraction function.

In the example the values 1-12 of the parameter ‘TelemetryDeck.Calendar.monthOfYear’ are mapped on the respective month.

**Example**:

```
{
    "dimension": {
      "dimension": "TelemetryDeck.Calendar.monthOfYear",
      "extractionFn": {
        "injective": true,
        "lookup": {
          "map": {
            "1": "January",
            "2": "February",
            "3": "March",
            "4": "April",
            "5": "May",
            "6": "June",
            "7": "July",
            "8": "August",
            "9": "September",
            "10": "October",
            "11": "November",
            "12": "December"
          },
          "type": "map"
        },
        "retainMissingValue": true,
        "type": "lookup"
      },
      "outputName": "Month of Year",
      "outputType": "STRING",
      "type": "extraction"
    }
}
```

**Property Reference**

**Property**: `dimension`</br>
**Description**: name of input column as is from dataset or virtual column name.</br>
**Required**: true

**Property**: `outputName`</br>
**Description**: the output name to be used for the dimension.</br>
**Required**: true

**Property**: `type`</br>
**Description**: must be ‘extraction’.</br>
**Required**: true

**Property**: `outputType`</br>
**Description**: can be ‘STRING’, ‘LONG’ or ‘FLOAT’. Defaults to ‘STRING’ if not specified, so depending on the case you might have to include the type of the column when specifiying a DimensionSpec on a numeric column.</br>
**Required**: false

**Property**: `extractionFn`</br>
**Description**: specification of the Extraction Function to be applied.</br>
**Required**: true