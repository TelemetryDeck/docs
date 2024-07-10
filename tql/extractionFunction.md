---
title: Extraction Function
description: Extraction functions define the transformation applied to each dimension value in the TelemetryDeck Query Language.
lead: Extraction functions define the transformation applied to each dimension value.
order: 210
---

## Regular Expression Extraction Function

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

For example, using `"expr" : "(\\w\\w\\w).*"` will transform `'Monday'`, `'Tuesday'`, `'Wednesday'`into `'Mon'`, `'Tue'`, `'Wed'`.

If "index" is set, it will control which group from the match to extract. Index zero extracts the string matching the entire pattern.

If the `replaceMissingValue` property is true, the extraction function will transform dimension values that do not match the regex pattern to a user-specified String. Default value is `false`.

The `replaceMissingValueWith` property sets the String that unmatched dimension values will be replaced with, if `replaceMissingValue` is true. If `replaceMissingValueWith` is not specified, unmatched dimension values will be replaced with nulls.

For example, if `expr` is `"(a\w+)"` in the example JSON above, a regex that matches words starting with the letter `a`, the extraction function will convert a dimension value like `banana` to `foobar`.

## Registered lookup extraction function

The TelemetryDeck servers have various **lookup tables** that can be used to translate extracted values into human readable names. The `registeredLookup` extraction function lets you refer to a lookup table that has been prepared by us. For example, the
`appleModelNames` lookup table can be used to translate the model name of an Apple device into a human readable name.

The following lookup tables are available:

- `appleModelNames` - Translates Apple device model names into human readable names.
- `deviceType` - Translates device device model names into a type such as "Desktop", "Phone", "Tablet", etc.
- `processorFamily` - Translates a device model name into a processor family such as "A12 Bionic" (the bionic part is very important!)
- `processorType` - Translates a device model name into a processor type such as "Apple Silicon" or "Intel"

(See our public [appleModelNames](https://github.com/TelemetryDeck/AppleModelNames) repo for a list of values in these.

Here's an example TQL query that uses the registered lookup extraction function to translate a dimension value into a human readable name:

```json
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
  },
  // Other TQL query properties...
}
```

A property of `retainMissingValue` and `replaceMissingValueWith` can be specified at query time to hint how to handle missing values. Setting `replaceMissingValueWith` to `""` has the same effect as setting it to `null` or omitting the property. Setting `retainMissingValue` to `true` will use the dimension's original value if it is not found in the lookup. The default values are `replaceMissingValueWith = null` and `retainMissingValue = false` which causes missing values to be treated as missing.

It is illegal to set `retainMissingValue = true` and also specify a `replaceMissingValueWith`.

The `injective` property can be set to `true` to indicate that the lookup is injective. This means that each key maps to a single value. If the lookup is not injective, then the first value found will be used. The default value is `false`.

## Inline lookup extraction function

The `inlineLookup` extraction function lets you specify a lookup table inline in the TQL query. This is useful if you want to use a lookup table that is not available as a registered lookup table.

Here is an example TQL query that uses the inline lookup extraction function to translate a dimension value into a human readable name:

```json
{
  "dimension": {
    "dimension": "modelName",
    "extractionFn": {
          "type":"lookup",
          "lookup":{
            "type":"map",
            "map":{"foo":"bar", "baz":"bat"}
          },
          "retainMissingValue":false,
          "injective":false,
          "replaceMissingValueWith":"MISSING"
        },
    "outputName": "modelName",
    "type": "extraction"
  },
  // Other TQL query properties...
}
```

The inline lookup should be of type `map`.

The properties `retainMissingValue`, `replaceMissingValueWith`, and `injective` behave similarly to the registered lookup extraction function.
