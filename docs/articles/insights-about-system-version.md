---
title: Find out which operating system your users are using
tags:
  - beginner
  - how-to
  - quickstart
  - user-cohorts
  - insights
testedOn:
featured:
description: A guide on how to create an insight that shows all operating systems used by users
lead: Insights around used operating systems help you with planning features, and to understand how technologically advanced your users are. This step-by-step guide explains how you can create and configure your insights
searchEngineTitle: Which operating systems are your users using?
searchEngineDescription: A guide on creating an insight that shows all used operating systems. See what OS your users are using the most - or least.
order: 20
---

## Step one: Navigate to your app

To create insights, you first need to create an app. If you have not created and linked your app yet, check out our guide [Making an Account](/docs/articles/making-account/) first.

In your browser, navigate to the [dashboard](https://dashboard.telemetrydeck.com). There you will find a drop-down menu on the top left side, next to the TelemetryDeck logo. Choose your app from here.

## Step two: Select or create a new group

Grouping your insights is a great way to give a better overview of related topics. For example, grouping operating systems with insights about device types and app versions. In case you have not already created a group where your new insight fits into [you can create a new one](/docs/articles/create-custom-dashboards/).

## Step three: Create a new insight

Getting insights on the operating system is essential. That is why we provide you with helpful templates to choose from, for example **System Versions**. This will give you insights on the operating systems your users are using. Let's have a look on how to create insights for **System Versions**.

While in your group, you will see a `Create new Insight` field. Depending on if there are already existing insights, you may have to scroll down to find them.
Click on _+ Create new Insight_ and give it a name. Now you can either build your own query by choosing a query type, or you can start right ahead by clicking on _I don’t know, show me some examples ->_. Now just pick _System Versions_ from the templates and you’re good to go!
You can directly see how many users are using your app from a specific operating system.
By default, the versions are grouped by minor versions (displayed as `15.x.x`).

![Donut chart example of system versions](/docs/images/system-versions-example.png)

## Step four: Configure your insights

In some cases, it is not necessary to know every minor version a user uses. In that case, we provide you with different breakdown keys to better filter your signals. When configuring an insight, the default key is `systemVersion`, displayed as `15.x.x`.
Change the breakdown key under _Top N Dimension_. Here you can switch to `majorMinorSystemVersion` to display the version as `15.x`, or `majorSystemVersion` to display it as `15`.

Under _Counting_ you can also change what your insight is based on: either it counts the system versions based on the signals itself, or based on unique users.
Counting them by user will show you how many of your users are using specific system versions, while counting them based on signals shows you which system version generates the most data and therefore is used more often.