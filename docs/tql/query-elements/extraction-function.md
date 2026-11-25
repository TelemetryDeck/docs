---
title: Extraction Function
tags:
- app analytics
- web analytics
---

## Introduction

Extraction functions define the transformation applied to each dimension value. Transformations can be applied to both regular (string) dimensions, as well as the special __time dimension, which represents the current time bucket according to the query aggregation granularity.

## Specifics & Examples

Following you can find information regarding different Extraction Functions available and examples of their application.

**Name**: Regular Expression Extraction Function

**Explanation**: Returns the first matching group for the given regular expression. If there is no match or specification, it returns the dimension value as is.

The example would delete 'UTC' if applied to the property `TelemetryDeck.Device.timeZone`.

Another small example: using `expr: (\w\w\w).*` will transform 'Monday', 'Tuesday', 'Wednesday' into 'Mon', 'Tue', 'Wed'.

**Example**:

```
{
    "type": "regex",
    "expr": "UTC(.+)",
    "index": 1,
    "replaceMissingValue": true,
    "replaceMissingValueWith": "unknown"
}
```

**Property Reference**

**Property**: `expr`</br>
**Description**: a regular expression.</br>
**Required**: true

**Property**: `index`</br>
**Description**: if 'index' is set, it will control which group from the match to extract. Index zero extracts the string matching the entire pattern.</br>
**Required**: false

**Property**: `replaceMissingValue`</br>
**Description**: if the 'replaceMissingValue' property is 'true', the extraction function will transform dimension values that do not match the regex pattern to a user-specified String. Default value is 'false'. The replaceMissingValueWith property sets the String that unmatched dimension values will be replaced with, if replaceMissingValue is true.</br>
**Required**: false

**Property**: `replaceMissingValueWith`</br>
**Description**: if 'replaceMissingValueWith' is not specified, unmatched dimension values will be replaced with nulls.</br>
**Required**: false

**Property**: `type`</br>
**Description**: must be 'regex'.</br>
**Required**: true

---

**Name**: Registered Lookup Extraction Function

**Explanation**: The TelemetryDeck servers have lookup tables that can be used to translate extracted values into human readable names. The registeredLookup extraction function lets you refer to a lookup table that has been prepared by us. For example, the appleModelNames lookup table can be used to translate the model name of an Apple device into a human readable name.

Available lookup tables are:

- `appleModelNames`: Translates Apple device model names into human readable names.
- `deviceType`: Translates device model names into a type such as 'Desktop', 'Phone', 'Tablet', etc.
- `processorFamily`: Translates a device model name into a processor family such as 'A12 Bionic'.
- `processorType`: Translates a device model name into a processor type such as 'Apple Silicon' or 'Intel'.**Example**:

```
{
    "dimension": {
      "dimension": "modelName",
      "extractionFn": {
        "type": "registeredLookup",
        "lookup": "appleModelNames",
        "retainMissingValue": true
      },
      "outputName": "modelName",
      "type": "extraction"
    }
}
```

**Property Reference**

**Property**: `lookup`</br>
**Description**: most common one is 'appleModelNames' for Apple devices.</br>
**Required**: true

**Property**: `retainMissingValue`</br>
**Description**: setting 'retainMissingValue' to true will use the dimension's original value if it is not found in the lookup. Default value is retainMissingValue = false. It is illegal to set retainMissingValue = true and also specify a replaceMissingValueWith.</br>
**Required**: false

**Property**: `replaceMissingValueWith`</br>
**Description**: Setting replaceMissingValueWith to “” has the same effect as setting it to null or omitting the property. Default value is replaceMissingValueWith = null. It is illegal to set retainMissingValue = true and also specify a replaceMissingValueWith.</br>
**Required**: false

**Property**: `injective`</br>
**Description**: can be set to 'true' to indicate that the lookup is injective. This means that each key maps to a single value. If the lookup is not injective, then the first value found will be used. The default value is 'false'.</br>
**Required**: false

**Property**: `type`</br>
**Description**: must be 'registeredLookup'.</br>
**Required**: true

---

**Name**: Inline Lookup Extraction Function

**Explanation**: The inlineLookup extraction function lets you specify a lookup table inline in the TQL query. This is useful if you want to use a lookup table that is not available as a registered lookup table.

The following example shows how to map numbers in dimension `TelemetryDeck.Calendar.dayOfWeek` to the respective days.

**Example**:

```
{
    "injective": true,
    "lookup": {
      "map": {
        "1": "Monday",
        "2": "Tuesday",
        "3": "Wednesday",
        "4": "Thursday",
        "5": "Friday",
        "6": "Saturday",
        "7": "Sunday"
      },
      "type": "map"
    },
    "retainMissingValue": true,
    "type": "lookup"
}
```

**Property Reference**

**Property**: `map`</br>
**Description**: key-value-pairs defining the desired mapping.</br>
**Required**: true

**Property**: `retainMissingValue`</br>
**Description**: setting 'retainMissingValue' to true will use the dimension's original value if it is not found in the lookup. Default value is retainMissingValue = false. It is illegal to set retainMissingValue = true and also specify a replaceMissingValueWith.</br>
**Required**: false

**Property**: `replaceMissingValueWith`</br>
**Description**: Setting replaceMissingValueWith to “” has the same effect as setting it to null or omitting the property. Default value is replaceMissingValueWith = null. It is illegal to set retainMissingValue = true and also specify a replaceMissingValueWith.</br>
**Required**: false

**Property**: `injective`</br>
**Description**: can be set to 'true' to indicate that the lookup is injective. This means that each key maps to a single value. If the lookup is not injective, then the first value found will be used. The default value is 'false'.</br>
**Required**: false

**Property**: `type`</br>
**Description**: must be 'map'.</br>
**Required**: true