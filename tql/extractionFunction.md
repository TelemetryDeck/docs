---
title: Extraction Function
description: Extraction functions define the transformation applied to each dimension value in the TelemetryDeck Query Language.
lead: Extraction functions define the transformation applied to each dimension value.
order: 210
---

{% noteinfo "Only One?" %}

The Regular Expression Extraction Function is the only extraction function currently supported in TQL.

{% endnoteinfo %}

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
