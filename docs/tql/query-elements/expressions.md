---
title: Expressions
tags:
- app analytics
- web analytics
---

## Introduction

Expressions are used in various places in the native query language, including virtual columns for example.

## Specifics & Examples

Following you can find information regarding different Expressions available and examples of their application.

**Name**: Supported operators

**Explanation**: The example shows how the ratio of events per user can be caluclated.

The following operators are supported:

- Unary NOT and Minus: !, -
- Binary power op: `^`
- Binary multiplicative: `*, /, %`
- Binary additive: `+, -`
- Binary Comparison: `<, ≤, >, ≥, ==, !=`
- Binary Logical: `AND, OR: &&, ||`
 
**Example**:

```
{
    "expression": "(_eventCount / _userCount)"
}
```

---

**Name**: General functions

**Explanation**: The example of an expression shows how the accumulated activity duration of users is calculated.

The `totalSessionsCount` of the respective default parameter includes the current session, whereas the `averageSessionSeconds`-parameter does not. Thus the session count is lowered by 1 and then multiplied by the average session seconds so that the virtual column returns the total duration per user before the current session. `cast` is used to transform dimensions to the needed type.

Following an overview of General Functions:

- `cast`: cast(expr,LONG or DOUBLE or STRING or ARRAY, or ARRAY or ARRAY) returns expr with specified type. exception can be thrown. Scalar types may be cast to array types and will take the form of a single element list (null will still be null).
- `coalesce`: coalesce(exprs) returns the first non-null expression, or null if all expressions are null.
- `if`: if(predicate,then,else) returns 'then' if 'predicate' evaluates to a positive number, otherwise it returns 'else'.
- `nvl`: nvl(expr,expr-for-null) returns 'expr-for-null' if 'expr' is null.
- `like`: like(expr, pattern[, escape]) is equivalent to SQL expr LIKE pattern.
- `case_searched`: case_searched(expr1, result1, [[expr2, result2, …], else-result]) is similar to CASE WHEN expr1 THEN result1 [ELSE else_result] END in SQL.
- `case_simple`: case_simple(expr, value1, result1, [[value2, result2, …], else-result]) is similar to CASE expr WHEN value THEN result [ELSE else_result] END in SQL.
- `isnull`: isnull(expr) returns 1 if the value is null, else 0.
- `notnull`: notnull(expr) returns 1 if the value is not null, else 0.
- `bloom_filter_test`: bloom_filter_test(expr, filter) tests the value of 'expr' against 'filter', a bloom filter serialized as a base64 string. See bloom filter extension documentation for additional details.

**Example**:

```
{
    "expression": "(cast(\"TelemetryDeck.Retention.totalSessionsCount\", 'DOUBLE')-1) * cast(\"TelemetryDeck.Retention.averageSessionSeconds\", 'DOUBLE')"
}
```

---

**Name**: String Functions

**Explanation**: There are several String Functions which can be used in expressions. The example returns the length of inputs submitted via 'inputField'
Following an overview of String Functions:

- `concat`: concat(expr, expr…) concatenate a list of strings.
- `format`: format(pattern[, args…]) returns a string formatted in the manner of Java's String.format.
- `like`: like(expr, pattern[, escape]) is equivalent to SQL expr LIKE pattern.
- `lookup`: lookup(expr, lookup-name[,replaceMissingValueWith]) looks up expr in a registered,replaceMissingValueWith is an optional constant string query-time lookup.
- `parse_long`: parse_long(string[, radix]) parses a string as a long with the given radix, or 10 (decimal) if a radix is not provided.
- `regexp_extract`: regexp_extract(expr, pattern[, index]) applies a regular expression pattern and extracts a capture group index, or null if there is no match. If index is unspecified or zero, returns the substring that matched the pattern. The pattern may match anywhere inside expr; if you want to match the entire string instead, use the ^ and $ markers at the start and end of your pattern.
- `regexp_like`: regexp_like(expr, pattern) returns whether expr matches regular expression pattern. The pattern may match anywhere inside expr; if you want to match the entire string instead, use the ^ and $ markers at the start and end of your pattern.
- `regexp_replace`: regexp_replace(expr, pattern, replacement) replaces all instances of a regular expression pattern with a given replacement string. The pattern may match anywhere inside expr; if you want to match the entire string instead, use the ^ and $ markers at the start and end of your pattern.
- `contains_string`: contains_string(expr, string) returns whether expr contains string as a substring. This method is case-sensitive.
- `icontains_string`: contains_string(expr, string) returns whether expr contains string as a substring. This method is case-insensitive.
- `replace`: replace(expr, pattern, replacement) replaces pattern with replacement.
- `substring`: substring(expr, index, length) behaves like java.lang.String's substring.
- `right`: right(expr, length) returns the rightmost length characters from a string.
- `left`: left(expr, length) returns the leftmost length characters from a string.
- `strlen`: strlen(expr) returns length of a string in UTF-16 code units.
- `strops`: strpos(haystack, needle[, fromIndex]) returns the position of the needle within the haystack, with indexes starting from 0. The search will begin at fromIndex, or 0 if fromIndex is not specified. If the needle is not found then the function returns -1.
- `trim`: trim(expr[, chars]) remove leading and trailing characters from expr if they are present in chars. chars defaults to ' ' (space) if not provided.
- `ltrim`: ltrim(expr[, chars]) remove leading characters from expr if they are present in chars. chars defaults to ' ' (space) if not provided.
- `rtrim`: rtrim(expr[, chars]) remove trailing characters from expr if they are present in chars. chars defaults to ' ' (space) if not provided.
- `lower`: lower(expr) converts a string to lowercase.
- `upper`: upper(expr) converts a string to uppercase.
- `reverse`: reverse(expr) reverses a string.
- `repeat`: repeat(expr, N) repeats a string N times.
- `lpad`: lpad(expr, length, chars) returns a string of length from expr left-padded with chars. If length is shorter than the length of expr, the result is expr which is truncated to length. The result will be null if either expr or chars is null. If chars is an empty string, no padding is added, however expr may be trimmed if necessary.
- `rpad`: rpad(expr, length, chars) returns a string of length from expr right-padded with chars. If length is shorter than the length of expr, the result is expr which is truncated to length. The result will be null if either expr or chars is null. If chars is an empty string, no padding is added, however expr may be trimmed if necessary.
 
**Example**:

```
{
    "expression": "strlen(\"inputField\")"
}
```