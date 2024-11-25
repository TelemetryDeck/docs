---
title: Quick set-up for your MAU insights
tags:
  - beginner
  - how-to
  - quickstart
  - user-cohorts
  - insights
testedOn:
featured:
description: A guide on how to create an insight that displays the number of monthly users
lead: As creators of apps, the feeling of knowing that your app gets used is amazing. Here is our guide for quickly getting a handy insight into your monthly active users' statistics!
searchEngineTitle: 4 steps to your monthly active users insights
searchEngineDescription: Follow our handy guide to get your MAU insights and start understanding your users.
order:
---

Follow these steps to get an insight of your monthly active users (MAU) within a couple of minutes:

1. Go to the dashboard and create a New Insight.
   ![Create a new insight](/docs/images/MAU_1.png)

2. In the next step select "I don’t know, show me some examples" and then choose "Monthly Users".

3. Now you are already getting results! Unfortunately, you probably still do not find the chart that helpful since only data of the last 30 days is included and that contradicts a chart with granularity set to "Month".
   ![Standard insight](/docs/images/MAU_2.png)
   **A quick fix** is changing the included data from "Last 30 Days" to "This Year" in the respective dropdown at the top of the page.
   ![Insight current year](/docs/images/MAU_3.png)

4. An issue is that you do not want to constantly change the time interval manually every time you use TelemetryDeck for this query to work. To resolve this:

- While editing the query click on the **Query Type** button and choose **Advanced Query**. This will cause that you stop editing the query, but once you click on "Edit" that same query again you can now use the Visual Editor.
- In the Metadata section add an item for Relative Intervals
- At beginningDate choose `month`, `-12` and `beginning` to start the time interval 12 months ago and for **endDate** choose `month`, `0` and `end` to end the time interval at the current time.
  ![Set relative interval](/docs/images/MAU_4.png)

The query is now working as required although the dropdown at the top is changed back to "Last 30 Days".
![Final insight](/docs/images/MAU_5.png)
