---
title: How to Detect if Users Update to the Latest App Version
tags:
  - setup
  - beginner
  - filter
  - user-cohorts
  - insights
description: From your vision into the app - Let's find out if your users update to the newest version and make those changes worth it.
lead: Do users like the newest features? What services can be shut down? And do people install security updates? - Whatever the occasion, getting insights into the update behavior of your users is a helpful and a compelling way to ensure you hit your user's needs.
searchEngineTitle:
searchEngineDescription: Are your users updating to the newest app version? Let's find out the reason behind it and ways to improve upgrade behavior.
---

## Use Our App Overview

We provide a helpful chart out of the box for a quick and informative first look. Choose your app from the drop-down menu at the top. After choosing an app, you should automatically be on the app overview page, but you can also navigate to the overview category by yourself.

On the left sidebar, the topmost category is the app overview. Here you will find a general summary of the received signals, sessions, users, and of course, the used app versions.

The bar chart displays the distribution of your app's versions by day. Are you interested in the usage of your builds? Just toggle between Versions and Builds on the top right side of the bar chart.

## Create a Custom Insight

A general summary often does not fit your individual needs. That is where custom insights come to play! You can show the distribution of all used app versions with custom insights. First, we must navigate to a group or create a new one.

To create a group in the dashboard, look at the left sidebar. Here you can find the `GROUPS` category. Click `+ New Group`, give your group a name and then click `Create`. You now have a new group in your sidebar!

### Configuring Your Insight

While in your group, create a new insight field. Choose `App Versions` from our templates. Now you can get started.
We recommend using the donut chart or the table view. Make sure the following settings are selected and filled:

**Signal**

- Signal Type: `All Signals`
- Granularity: any of the given options

**Query Type**

- Query Type: `Top N`

**Top N Configuration**

- Breakdown Key: `appVersion`

**Filters**

- You can customize your filter depending on your needs. Make sure the **field is not empty**, and it contains at least an empty dictionary `{}`.

## The Importance of User Upgrade Behavior

As mentioned in the beginning, there are different reasons why you would want to have insights into the update behavior of your users. Understanding how your users update and also recognizing what causes the behavior will help you create better products in the long term. The good thing with TelemetryDeck is you can get a ton of information about your users by their update activity without collecting sensitive data about them! Here are some points to why those insights can be helpful to you:

### My Users Are Updating - Great! But What Does It Mean?

With your new insights, you now know your users are frequently updating and in mass. But why is that so? It might say something about how willing your users are to use new features or install essential security updates. Not only will you understand what features your users like and dislike, but you will also be able to have a better look and understanding of who your user base is.
On the other hand, if they tend not to upgrade, you might want to make it a priority to get them to update - especially with security updates on the line.
With API-driven apps, it is also exciting to see what endpoints get used the most and which might even be deprecated.

If a small user group is stuck on an older version, consider investigating what keeps them from upgrading. These insights also help you further improve your update process, allowing you to see which method works best and which does not.