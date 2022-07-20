---
title: How To Find Out Which Operating System Your Users Are Using
tags: Beginner, How-to, User-cohorts, Insights, Quickstart, Docs
description: A guide on how to create an insight that shows all operating systems used by users
lead: Insights around used operating systems help you with planning features, and to understand how technologically advanced your users are. This step-by-step guide explains how you can create and configure your insights
---

## Step One: Navigate To Your App

To create insights, you first need to create an app. If you have not created and linked your app yet, check out our guide [Making an Account](/pages/making-an-account.html) first.

In your browser, navigate to the [dashboard](https://dashboard.telemetrydeck.com). There you will find a drop-down menu on the top left side, next to the TelemetryDeck logo. Choose your app from here.

---

## Step Two: Select Or Create A New Group

Grouping your insights is a great way to give a better overview of related topics. For example, grouping operating systems with insights about device types and app versions. In case you have not already created a group where your new insight fits into, here is a quick guide on how to create groups in the browser dashboard:

To create a group in the dashboard, have a look at the left sidebar. Here you can find the `GROUPS` category. Click on <kbd>+ New Group</kbd>, give your group a name, and then click on `Create`. You now have a new group in your sidebar!

---

## Step Three: Creating a New Insight

Getting insights on the operating system is essential. That is why we provide you with helpful templates to choose from, for example **System Versions**. This will give you insights on the operating systems your users are using. Let's have a look on how to create insights for **System Versions**.

While in your group, you will see a `Create new Insight` field. Depending on if there are already existing insights, you may have to scroll down to find them.
Click on <kbd>+ Create new Insight</kbd>. Here you will find `System Versions` on the bottom. After clicking on it, a new insight card will be created. You can hover over the pie chart to get information about how many users are using your app from a specific operating system. By default, the versions are grouped by minor versions (displayed as `15.x.x`).

---

## Step Four: Configure Your Insights

In some cases, it is not necessary to know every minor version a user uses. In that case, we provide you with different breakdown keys to better filter your signals. When configuring an insight, the default key is `systemVersion`, displayed as `15.x.x`. You can switch to `majorMinorSystemVersion` to display the version as `15.x`, or `majorSystemVersion` to display it as `15`.

While you are in the **insight group**, click on the name of the insight you want to edit. Scroll down to `Top N Configuration` and click on the drop-down to change the `Breakdown Key`. Here you can switch to `majorMinorSystemVersion`or `majorSystemVersion`.
