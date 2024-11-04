---
title: Filters - How to use the Filter Editor
tags:
  - setup
  - quickstart
  - intermediate
  - how-to
description: Sometimes, generic insights aren’t enough. With TelemetryDeck filters you can further specify what you’re really interested in your signals!
searchEngineTitle: Refine your query, gain insights - the power of filters
---

Filters are tools that allow you to segment and manipulate your analytics data in various ways. They help you exclude or include specific data sets and user groups based on parameters such as location, device, user behavior, and more.
With filters, you can create custom views of your insights and organize the information in a meaningful way to help you make better data-driven decisions. The key feature of filters is extracting a subset of all the data for you to analyse. This functionality is critical for identifying trends, patterns, and anomalies! Here’s how you can utilize filters in the TelemetryDeck dashboard.

## The filter editor

Navigate to the [dashboard](https://dashboard.telemetrydeck.com), and select your app. You can find the filter editor in your insight group, while editing an insight. Either create a new insight or edit an existing one to see the editor just below the chart itself.

![Screenshot of the filter location in the dashboard](/docs/images/filter_location.png)

In your insight group, you can add filters to any insight you want. With advanced filter options available, you can add multiple filters to obtain the desired query results. Nesting filters and combining them with boolean operations can help you refine your query and achieve even more accurate insights.

## Filter conditions

You can use analytics filters to refine your data and obtain precise insights. Want to dive deeper into filter conditions? Take a look at our [filter conditions](/docs/tql/filters/) documentation!

- These filters include the **Signal Type** filter, which allows you to filter data by signal type, such as page views, clicks, or conversions. Having Signal Type as a filter condition makes it easier to combine multiple signal types using the _boolean operations_. Nest your insights with `AND`, `OR`, and `NOTs`!
- The **Selector** filter lets you compare any _payload key_ (also known as a dimension) to a value. For instance, if you send a `shouldUseHealthKit` parameter as part of your payload in signals, you can filter for `shouldUseHealthKit = “true”`.
- Additionally, you can use **Regular Expressions** (RegEx) to filter data based on _complex patterns or strings of text_. Sometimes it is not possible to match a value exactly, and in such cases, regular expressions can be incredibly useful to obtain more accurate and specific insights into user behavior. A good example for using RegEx is filtering by device type, locale, or anything else you would like a more precise view on!

![Screenshot of how adding a condition changes the output. Adding that only iOS versions should be shown, and then wrapping the condition inside a NOT so that everything but iOS versions is shown.](/docs/images/filter_example.png)

## Query construction

Filters are part of the **TelemetryDeck Query Language** (TQL), which means you don’t have to write them by hand. Instead you can just use them as described above! In case you want to customize your queries even more than the filter feature allows you to do, check out our TQL documentation! There you can further learn how to get the most out of your insights.

<a href=“/docs/tql/query/“ class="btn btn-secondary btn-large">Next Up: Spice up your queries with TQL →</a>
