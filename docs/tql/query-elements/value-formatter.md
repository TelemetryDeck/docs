---
title: Value Formatter
tags:
- app analytics
- web analytics
---

## Introduction

The Value Formatter specifies how query values are displayed in the TelemetryDeck UI. Using a valueFormatter, you can round values, specify a suffix, or format values as percentages.

## Specifics & Examples

Following you can find information regarding the different options available in the Value Formatter and examples of their application.

**Name**: Style Options

**Explanation**: There are two higher level properties: 'options' and 'locale':

- options: via key-value-pairs the desired format can be selected. No particular key is necessary, but some key has to be defined.
- locale: active setting of locales can be used to format values according to the desired output format. Defaults to locale of the user's browser.
Within the property 'options' different style options can be defined. In the example the locale is set to 'en-US', i.e. the results are displayed in English. Via the options it is defined that results shall be returned as units.

**Example**:

```
{
  "valueFormatter": {
    "options": {
      "style": "unit",
      "unit": "user",
      "unitDisplay": "long"
    },
    "locale": "en-US"
  }
}
```

**Property Reference**

**Property**: `style`</br>
**Description**: Sets the style of the value, 'decimal' (default), 'currency', 'percent', or 'unit'.</br>
**Required**: false

**Property**: `currency`</br>
**Description**: The currency to use in currency formatting. Possible values are the ISO 4217 currency codes, such as 'USD' for the US dollar, 'EUR' for the euro, or 'CNY' for the Chinese RMB.</br>
**Required**: false

**Property**: `currencyDisplay`</br>
**Description**: Defines how to display the currency in currency formatting. Options are 'code', 'symbol', 'narrowSymbol', and 'name'.</br>
**Required**: false

**Property**: `currencySign`</br>
**Description**: In many locales, accounting format means to wrap the number with parentheses instead of appending a minus sign. Possible values are 'standard' and 'accounting'; the default is 'standard'.</br>
**Required**: false

**Property**: `unit`</br>
**Description**: The unit to use in unit formatting. Possible values are 'acre', 'bit', 'byte', 'celsius', 'centimeter', 'day', 'degree', 'fahrenheit', 'fluid-ounce', 'foot', 'gallon', 'gigabit', 'gigabyte', 'gram', 'hectare', 'hour', 'inch', 'kilobit', 'kilobyte', 'kilogram', 'kilometer', 'liter', 'megabit', 'megabyte', 'meter', 'microsecond', 'mile', 'mile-scandinavian', 'milliliter', 'millimeter', 'millisecond', 'minute', 'month', 'nanosecond', 'ounce', 'percent', 'petabyte', 'pound', 'second', 'stone', 'terabit', 'terabyte', 'week', 'yard', and 'year'.</br>
**Required**: false

**Property**: `unitDisplay`</br>
**Description**: Defines how to display the unit in unit formatting. Options are 'short', 'narrow', and 'long'.</br>
**Required**: false

---

**Name**: Digit options

**Explanation**: Digit options allow to define different characteristics like rounding or the maximum and minimum number of digits to be used.

In the example the data is returned in currency US Dollar with two digits.
**Example**:

```
{
    "valueFormatter": {
      "options": {
        "style": "currency",
        "currency": "USD",
        "minimumFractionDigits": 2,
        "maximumFractionDigits": 2
      },
      "locale": "en-US"
    }
}
```

**Property Reference**

**Property**: `minimumFractionDigits`</br>
**Description**: Sets the minimum number of digits after the decimal point.</br>
**Required**: false

**Property**: `minimumIntegerDigits`</br>
**Description**: The minimum number of integer digits to use. A value with a smaller number of integer digits than this number will be left-padded with zeros (to the specified length) when formatted. Possible values are from 1 to 21; the default is 1.</br>
**Required**: false

**Property**: `maximumFractionDigits`</br>
**Description**: Sets the maximum number of digits after the decimal point..</br>
**Required**: false

**Property**: `minimumSignificantDigits`</br>
**Description**: The minimum number of significant digits to use.</br>
**Required**: false

**Property**: `maximumSignificantDigits`</br>
**Description**: The maximum number of significant digits to use.</br>
**Required**: false

**Property**: `roundingPriority`</br>
**Description**: The rounding priority to use. Options are 'morePrecision', 'lessPrecision', and 'auto'.</br>
**Required**: false

**Property**: `roundingIncrement`</br>
**Description**: Indicates the increment at which rounding should take place relative to the calculated rounding magnitude. Possible values are 1, 2, 5, 10, 20, 25, 50, 100, 200, 250, 500, 1000, 2000, 2500, and 5000; the default is 1. It cannot be mixed with significant-digits rounding or any setting of roundingPriority other than auto.</br>
**Required**: false

**Property**: `roundingMode`</br>
**Description**: The rounding mode to use. Options are 'ceil', 'floor', 'expand', 'trunc', 'halfCeil', 'halfFloor', 'halfExpand', 'halfTrunc', and 'halfEven'.</br>
**Required**: false

**Property**: `trailingZeroDisplay`</br>
**Description**: Whether to display trailing zeros. Options are 'auto', 'stripIfInteger', and 'stripIfNotInteger'.</br>
**Required**: false

---

**Name**: Other options

**Explanation**: There are some additional options to define the format the data is displayed in.
**Example**:

```
{
    "valueFormatter": {
    "options": {
      "notation": "compact"
    }
  }
}
```

**Property Reference**

**Property**: `notation`</br>
**Description**: The formatting that should be displayed for the number. Possible values are 'standard', 'scientific', 'engineering', and 'compact'.</br>
**Required**: false

**Property**: `compactDisplay`</br>
**Description**: Defines whether to display compact notation. Options are 'short', and 'long', default is 'short'.</br>
**Required**: false

**Property**: `useGrouping`</br>
**Description**: Defines whether to use grouping separators, such as thousands separators or thousand/lakh/crore separators. Options are 'auto', 'always', and 'min2' to only use grouping for numbers with at least two digits.</br>
**Required**: false

**Property**: `signDisplay`</br>
**Description**: Defines whether to display the sign. Options are 'auto', 'always', 'never', 'negative', and 'exceptZero'..</br>
**Required**: false