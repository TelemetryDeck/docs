---
title: Guideline for using TQL
tags: overview
description: TelemetryDeck Query Language is the advanced query language for TelemetryDeck. This page provides an overview of the main components and its overall structure.
lead: TelemetryDeck Query Language is the advanced query language for TelemetryDeck. You don't need to write all your queries by hand, but if you do, here are some guidelines how to get started.
order: 0
---

You are new to TQL? Here is an overview of the languages' main components and their purpose.
This page is intended to be short and easy to digest. Please follow the links at the specific sections to dig into details.

## Mandatory elements for every query

- `query type`
- `granularity`
- Everything else is either mandatory for a certain query or serves a specific purpose as indicated [here](https://telemetrydeck.com/docs/tql/query/).

## Query Type

- Especially in the beginning we recommend to use the **Visual Query Editor** to set up queries with all elements required for that query type. Once the general structure is set you can change the query type to **Advanced Query** and from there work on details in the JSON format if necessary / more convenient.
- Find an overview of the different query types and its characteristics [here](https://telemetrydeck.com/docs/tql/queryType/).

## Granularity

- It is usually chosen for the whole query.
- It defines how fine-grained a query shall be, i.e. you can for example return active users per day, per week, per month etc.
- It is also relevant for calculations potentially done within the query. If you choose granularity `day` for example you should probably only seek calculations within each day. To divide a certain value of one day by the sum of the values of multiple days when granularity day is chosen will likely not work as you expect.
- There is a workaround for cases like that though as you can define specific time intervals within queries in the **aggregations** by using type `filtered`. Granularity of the query should be set to `all` and now you can store results for time intervals of your choice through the filter. We come back to that example in the **filters** section.

## Aggregations

- There are different types of aggregators by which you can define the way data shall be returned
- The basic fields are:
  - `fieldName`: column you want to access
  - `name`: you can define the output name of your choice. One tip: if you use an aggregator only for calculation purposes you can hide the aggregated value by starting the name with an underscore (`"name": "_hiddenAggregatorXY"`). The elements returned through the aggregation are then not shown, but can be used in post-aggregations.
  - `type`: type of aggregation
- An overview of different aggregators can be found [here](https://telemetrydeck.com/docs/tql/aggregators/).

## Post-Aggregations

- Here you can execute further calculations on the values created in the aggregations. This is optional.
- The syntax of post-aggregations has some complexity to it, so we recommend to look up the syntax of a specific post-aggregator when you may need it until you are familiar with it.
- Information regarding post-aggregators can be found [here](https://telemetrydeck.com/docs/tql/post-aggregators/). Post-aggregators are in general applicable as stated on the [Apache Druid Homepage](https://druid.apache.org/docs/latest/querying/post-aggregations) (exception: JavaScript post-aggregator).

## Filters

- Filters can be used for a whole query when listed as a separate object in the JSON.
- As stated above filters can be used in the respective aggregator as well. This enables the creation of more complex insights as by using that you can create multiple differently filtered buckets in the aggregators section. The syntax for it is:

```json
  {
	  "type": "filtered",
	  "filter": {
		  <insert the filter of choice (`interval` if you want to access only certain days for example or `range` if only certain values shall be considered)>
	  },
	  "aggregator": {
		  <insert the aggregator of choice (oftentimes: `userCount` to get the different active users / `eventCount` to count certain signals / `doubleSum`/`longSum` for calculations)>
	  }
  }
```

Afterwards, if you want you can compare the different buckets aggregated with e.g. the `intersect` function in the post-aggregations as shown with an example [here](https://telemetrydeck.com/docs/tql/post-aggregators/#theta-sketch-estimate-post-aggregator).

- An overview of different filters can be found [here](https://telemetrydeck.com/docs/tql/filters/).
