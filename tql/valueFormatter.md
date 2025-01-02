---
title: ValueFormatter
description: Specifies how query values are displayed in the TelemetryDeck UI.
lead: Specifies how query values are displayed in the UI.
order: 230
---

Using a ValueFormatter, you can round values, specify a suffix, or format values as percentages.

## Rounding

Here's how to round values to the nearest integer:

```json
"valueFormatter": {
  "options": {
    "maximumFractionDigits": 0,
  }
}
```

## Currencies

Here's how to format values as dollars, with two decimal places:

```json
"valueFormatter": {
  "options": {
    "style": "currency",
    "currency": "USD",
    "minimumFractionDigits": 2,
  },
  "locale": "en-US"
}
```

## Percentages

Here's how to format values as percentages, with one decimal place:

```json
"valueFormatter": {
  "options": {
    "style": "percent",
    "minimumFractionDigits": 1,
  }
}
```

## Units

Here's how to format values with a unit, e.g. "100,000 users":

```json
"valueFormatter": {
  "options": {
    "style": "unit",
    "unit": "user",
    "unitDisplay": "long",
  }
}
```

## Locales

Locales are used to format values according to the locale of the user. For example, the locale `en-US` formats values as US dollars, while the locale `en-GB` formats values as British pounds. Leave the locale empty to use the default locale of the user's browser.

## Style Options

| Option            | Description                                                                                                                                                                                 |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `style`           | Sets the style of the value, "decimal" (default), "currency", "percent", or "unit".                                                                                                         |
| `currency`        | The currency to use in currency formatting. Possible values are the ISO 4217 currency codes, such as "USD" for the US dollar, "EUR" for the euro, or "CNY" for the Chinese RMB              |
| `currencyDisplay` | How to display the currency in currency formatting. Options are "code", "symbol", "narrowSymbol", and "name".                                                                               |
| `currencySign`    | In many locales, accounting format means to wrap the number with parentheses instead of appending a minus sign. Possible values are "standard" and "accounting"; the default is "standard". |
| `unit`            | The unit to use in unit formatting. Possible values are [here](https://tc39.es/ecma402/#table-sanctioned-single-unit-identifiers)                                                           |
| `unitDisplay`     | How to display the unit in unit formatting. Options are "short", "narrow", and "long".                                                                                                      |

## Digit Options

| Option                     | Description                                                                                                                                                                                                                                                                                                                       |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `minimumFractionDigits`    | Sets the minimum number of digits after the decimal point.                                                                                                                                                                                                                                                                        |
| `minimumIntegerDigits`     | The minimum number of integer digits to use. A value with a smaller number of integer digits than this number will be left-padded with zeros (to the specified length) when formatted. Possible values are from 1 to 21; the default is 1.                                                                                        |
| `maximumFractionDigits`    | Sets the maximum number of digits after the decimal point.                                                                                                                                                                                                                                                                        |
| `minimumSignificantDigits` | The minimum number of significant digits to use.                                                                                                                                                                                                                                                                                  |
| `maximumSignificantDigits` | The maximum number of significant digits to use.                                                                                                                                                                                                                                                                                  |
| `roundingPriority`         | The rounding priority to use. Options are "morePrecision", "lessPrecision", and "auto".                                                                                                                                                                                                                                           |
| `roundingIncrement`        | Indicates the increment at which rounding should take place relative to the calculated rounding magnitude. Possible values are 1, 2, 5, 10, 20, 25, 50, 100, 200, 250, 500, 1000, 2000, 2500, and 5000; the default is 1. It cannot be mixed with significant-digits rounding or any setting of roundingPriority other than auto. |
| `roundingMode`             | The rounding mode to use. Options are "ceil", "floor", "expand", "trunc", "halfCeil", "halfFloor", "halfExpand", "halfTrunc", and "halfEven".                                                                                                                                                                                     |
| `trailingZeroDisplay`      | Whether to display trailing zeros. Options are "auto", "stripIfInteger", and "stripIfNotInteger"                                                                                                                                                                                                                                  |

## Other Options

| Option           | Description                                                                                                                                                                                             |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `notation`       | The formatting that should be displayed for the number. Possible values are "standard", "scientific", "engineering", and "compact".                                                                     |
| `compactDisplay` | Whether to display compact notation. Options are "short", and "long", default is "short".                                                                                                               |
| `useGrouping`    | Whether to use grouping separators, such as thousands separators or thousand/lakh/crore separators. Options are "auto", "always", and "min2" to only use grouping for numbers with at least two digits. |
| `signDisplay`    | Whether to display the sign. Options are "auto", "always", "never", "negative", and "exceptZero".                                                                                                       |
