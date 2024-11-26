---
title: topN Query for the referrers of your website
tags:
  - intermediate
  - how-to
  - insights
  - visual-editor
  - Websites
testedOn:
featured:
description: A guide on how to create an insight that displays your users´ referrers before accessing your website.
lead: Are there patterns which websites your users visit before using your homepage? Here is our guide for getting a handy insight into just that.
searchEngineTitle: Get an insight into your users behavior before entering your homepage.
searchEngineDescription: Follow our handy guide to get insights into referrers of your website and improve your understandings of your users.
order:
---

To begin with, add a new insight in the dashboard of your choice and select **Advanced Query** so that you can proceed using the **Visual Editor**.
![Create a new advanced query](/docs/images/Referrers_1.png)

1. In the first section of the Visual Editor, **Metadata**, choose a `topN query` - we propose granularity `all` so that you can display the information in a donut chart in the end.
  ![Metadata](/docs/images/Referrers_2.png)

2. In the next step you can choose which **Data to Include**. To get started, add `thisApp` as well as the respective App ID. Additionally, it is recommended to add a filter to **avoid that parts of your own website are returned by the query**.
  To acchieve that add a `regex` filter with dimension `referrer` and domain as well as top-level-domain of your website separated by a `\`: `referrer~yourDomain\.com`.
  Please be aware that this is a rather basic regex filter as the purpose here is to show the creation of the query. More elements can be added to the filter of course.
  Once you have entered the information for the filter click on the field again and select `Negate (Wrap in "not" condition)`
  ![Data to Include_1](/docs/images/Referrers_3a.png)
  When you are finished, the final **Data to Include** section should look as follows:
  ![Data to Include_2](/docs/images/Referrers_3b.png)
  Additionally, feel free to add further `regex` filters in case you want to exclude search engines as referrers for example. To use multiple (regex) filters use an `and` filter where you had just selected `Negate (Wrap in "not" condition)`.
 
4. The following section are **topN Options**. In the first part regarding the dimension, select type `default` and type in `referrer` two times. Furthermore, choose a `numeric` metric and add `count`. To wrap this section up choose the number of topN results to be returned, i.e. the threshold.
  ![topN Options](/docs/images/Referrers_4.png)

5. Finally, add a `longSum`-aggregator for the **Aggregations** and type in `count` in the two respective fields.
  ![Aggregations](/docs/images/Referrers_5.png)

To wrap the creation of the insight up we recommend using a `Donut Chart` to display topN of the query results.
