---
title: Funnels - How they work
tags:
  - setup
  - quickstart
  - beginner
  - how-to
description: Funnels are here to help you understand your users. Watch how they navigate and flow through your app and find out how to improve your in-App processes with funnels!
searchEngineTitle: Get your analytics flowing - the art of funneling your signals
searchEngineDescription: Watch how your users navigate and flow through your app and learn how to improve your in-App processes with funnels!
---

## The flow of your app
Whenever users use an app, they do so with intent. This can be a simple look if there is anything new in the social media app or ordering a product or service.
Sometimes they go directly to their goal, do not pass Go, and do not collect 200€ 😋. At other times, they wander off and get distracted before reaching their destination. And occasionally, they even find hurdles and cancel before finishing the process.

These goals are often your goals, too. As the app owner, you want them to spend time in your app, find the new feature, and order that new product.

![Screenshot of a funnel called "Log in Journey" with 4 decreasing steps, going from "user login", to "show group view", to "show insight", and finally to "widget setup"](/docs/images/funnels_example.png)

![Screenshot of the funnel steps with set filters for "Log in Journey"](/docs/images/funnels_set_filters.jpg)

Funnels are a great way to show this kind of behavior. What funnels do at heart is display **when** a user **ends the process**. For example, it is possible to showcase each page of an app - from opening the home page to the final checkout page. If you have 100 users going through that process, and all of them finish it, all steps should show 100 users.
If there happens to be some confusion during the process, and users cancel it before the checkout, you will see that the page causing that issue will leave a drop in users afterward. The checkout page will probably show fewer than 100 users at the end.

Let's have a look at how to use funnels in TelemetryDeck.

## How to use funnels
Imagine you want to track how many users turn into customers. You can use funnels to track this conversion process. Since a funnel filters your insights by conditions, you must set up filters in your TelemetryDeck dashboard with the **filter editor**. These filters help you track how many users complete each funnel step, leading to a great visualization of your app's conversion. To create a **funnel chart**, just set the chart type to funnel and the query type to **funnel query** - or use our handy template to create an empty funnel!

![Screenshot of the selected funnel query and chart type](/docs/images/funnel_type.PNG)

For example, let's say your funnel has three steps:

1. Visiting the product page in your app
2. Adding the product to the cart
3. Completing the checkout process

You can set up corresponding filters to track how many users complete each step of the funnel.

For the first step, you can filter the data to only show users who visited the product page. For the second step, you can filter the data to only show users who added the product to their cart after visiting the product page. For the third step, you can filter the data to only show users who completed the checkout process after adding the product to their cart, and so on. You don't need to repeat filter steps, since the previous condition always applies to the following ones, too.

Using filters to track each step of the funnel, you can see how many users make it through each step and where they drop off. This information can help you identify areas to **improve** your app to **increase conversions**!


{% callToAction "Check out funnels now!" "Go to your TelemetryDeck dashboard and start right away" %}

## Diving deeper into funnels
You can already start using funnels in TelemetryDeck right now! And with this next step, you can learn more about how to extract funnels from your analytics data by using the **TelemetryDeck Query Language (TQL)**! 

<a href="/docs/tql/funnel/" class="btn btn-secondary btn-large">Next Up: How to extract funnels from your analytics data →</a>