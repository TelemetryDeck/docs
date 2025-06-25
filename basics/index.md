---
title: Analytics Overview
tags:
  - setup
  - basics
  - analytics
basics: true
description: Learn how to navigate TelemetryDeck's dashboard to find the insights you need about your app's performance.
lead: TelemetryDeck's dashboard is organized into intuitive sections that help you understand how users interact with your app. This guide walks you through each part of the interface.
searchEngineTitle: TelemetryDeck Dashboard Guide | App Analytics
searchEngineDescription: Learn how to navigate the TelemetryDeck dashboard to get the most out of your app analytics data.
order: 10
---

## Dashboard navigation

After integrating the TelemetryDeck SDK into your app, your data will start appearing in the TelemetryDeck dashboard. The main navigation tabs help you find different types of insights:

![TelemetryDeck Main Navigation](/docs/images/dashboard-main-nav.png)

Let's explore what you'll find in each section:

## Overview

The Overview tab provides a high-level summary of your app's performance, showing key metrics like daily active users, total users, user retention, app version distribution, and system version distribution:

![Overview Dashboard](/docs/images/dashboard-overview.png)

This view gives you immediate answers to: "How is my app performing right now?" and "Are my users upgrading to new versions?"

## Customers (User Analytics)

The Customers section organizes your user data according to the journey users take with your app, from discovery to monetization:

![Acquisition Dashboard](/docs/images/dashboard-acquisition.png)

Each tab focuses on a different stage of the user journey:

**Acquisition** tracks how users find and install your app, with metrics for new user counts, device distribution, geographic insights, and typical discovery patterns.

**Activation** (Coming Soon) monitors initial engagement with metrics like active user counts, session length distribution, and usage patterns by time of day and day of week.

**Retention** (Coming Soon) measures how effectively your app keeps users coming back, tracking distinct days used, engaged user metrics, and power user identification.

**Referral** (Coming Soon) helps understand how users share your app with others.

**Revenue** (Coming Soon) tracks your app's financial performance metrics.

<div class="not-prose">
  <div class="my-6 grid grid-cols-1 gap-6 sm:grid-cols-2">
    <div class="group relative rounded-xl border bg-white border-slate-200 flex">
      <div class="absolute -inset-px rounded-xl border-2 border-transparent opacity-0 [background:linear-gradient(var(--quick-links-hover-bg,theme(colors.mars.50)),var(--quick-links-hover-bg,theme(colors.mars.100)))_padding-box,linear-gradient(to_top,theme(colors.mars.400),theme(colors.mars.500))_border-box] group-hover:opacity-100"></div>
      <div class="shadow relative overflow-hidden rounded-xl p-6 h-full">
        <h2 class="font-semibold text-base text-mars-500">
          <a href="/docs/basics/acquisition">
            <span class="absolute -inset-px rounded-xl"></span>Acquisition Analytics</a>
        </h2>
        <p class="mt-1 text-sm text-slate-700">Learn how to interpret and act on acquisition metrics to optimize how users discover your app.</p>
      </div>
    </div>
    <div class="group relative rounded-xl border bg-white border-slate-200 flex">
      <div class="absolute -inset-px rounded-xl border-2 border-transparent opacity-0 [background:linear-gradient(var(--quick-links-hover-bg,theme(colors.mars.50)),var(--quick-links-hover-bg,theme(colors.mars.100)))_padding-box,linear-gradient(to_top,theme(colors.mars.400),theme(colors.mars.500))_border-box] group-hover:opacity-100"></div>
      <div class="shadow relative overflow-hidden rounded-xl p-6 h-full">
        <h2 class="font-semibold text-base text-mars-500">
          <a href="/docs/basics/pirate-metrics">
            <span class="absolute -inset-px rounded-xl"></span>Understanding Pirate Metrics Framework</a>
        </h2>
        <p class="mt-1 text-sm text-slate-700">Learn about the AARRR framework that organizes analytics by acquisition, activation, retention, referral, and revenue.</p>
      </div>
    </div>
  </div>
</div>

TelemetryDeck also provides built-in presets for tracking purchases and revenue that require minimal additional configuration in your app:

<div class="not-prose">
  <div class="my-6 grid grid-cols-1 gap-6">
    <div class="group relative rounded-xl border bg-white border-slate-200 flex">
      <div class="absolute -inset-px rounded-xl border-2 border-transparent opacity-0 [background:linear-gradient(var(--quick-links-hover-bg,theme(colors.mars.50)),var(--quick-links-hover-bg,theme(colors.mars.100)))_padding-box,linear-gradient(to_top,theme(colors.mars.400),theme(colors.mars.500))_border-box] group-hover:opacity-100"></div>
      <div class="shadow relative overflow-hidden rounded-xl p-6 h-full">
        <h2 class="font-semibold text-base text-mars-500">
          <a href="/docs/articles/preset-purchases">
            <span class="absolute -inset-px rounded-xl"></span>Purchase Tracking with Built-in Presets</a>
        </h2>
        <p class="mt-1 text-sm text-slate-700">Learn how to track in-app purchases with TelemetryDeck's built-in purchase tracking system and dashboards.</p>
      </div>
    </div>
  </div>
</div>

## Metrics (Technical Analytics)

The Metrics section provides essential technical insights about your app across different devices and platforms:

![Metrics Dashboard - Devices](/docs/images/metrics-devices.png)

**Key metrics include:**

- **Devices**: Hardware models, screen resolutions, and platform distributions
- **Versions**: App and SDK version adoption rates
- **Errors**: Issue monitoring by frequency and type
- **Localization**: Language and regional settings insights
- **Accessibility**: Usage of accessibility features

<div class="not-prose">
  <div class="my-6 grid grid-cols-1 gap-6">
    <div class="group relative rounded-xl border bg-white border-slate-200 flex">
      <div class="absolute -inset-px rounded-xl border-2 border-transparent opacity-0 [background:linear-gradient(var(--quick-links-hover-bg,theme(colors.mars.50)),var(--quick-links-hover-bg,theme(colors.mars.100)))_padding-box,linear-gradient(to_top,theme(colors.mars.400),theme(colors.mars.500))_border-box] group-hover:opacity-100"></div>
      <div class="shadow relative overflow-hidden rounded-xl p-6 h-full">
        <h2 class="font-semibold text-base text-mars-500">
          <a href="/docs/basics/metrics">
            <span class="absolute -inset-px rounded-xl"></span>Complete Metrics Analytics Guide</a>
        </h2>
        <p class="mt-1 text-sm text-slate-700">Explore our comprehensive guide to technical analytics, including detailed information on device types, app versions, error tracking, localization insights, and accessibility usage.</p>
      </div>
    </div>
  </div>
</div>

## Explore (Signal Analytics)

The Explore section gives you direct access to your raw event data through multiple views:

![Explore Dashboard - Signal Types](/docs/images/dashboard-signal-types.png)

Here you can examine all signal types your app has sent, explore parameters attached to your events, view recent events chronologically, and use the query playground to experiment with data analysis. This section is particularly useful for debugging, understanding user behavior sequences, and diving deeper into specific user actions.

<div class="not-prose">
  <div class="my-6 grid grid-cols-1 gap-6">
    <div class="group relative rounded-xl border bg-white border-slate-200 flex">
      <div class="absolute -inset-px rounded-xl border-2 border-transparent opacity-0 [background:linear-gradient(var(--quick-links-hover-bg,theme(colors.mars.50)),var(--quick-links-hover-bg,theme(colors.mars.100)))_padding-box,linear-gradient(to_top,theme(colors.mars.400),theme(colors.mars.500))_border-box] group-hover:opacity-100"></div>
      <div class="shadow relative overflow-hidden rounded-xl p-6 h-full">
        <h2 class="font-semibold text-base text-mars-500">
          <a href="/docs/articles/signal-type-naming">
            <span class="absolute -inset-px rounded-xl"></span>Event Naming Best Practices</a>
        </h2>
        <p class="mt-1 text-sm text-slate-700">Learn how to name your signal types effectively for better organization and analysis.</p>
      </div>
    </div>
  </div>
</div>

## Dashboards (Custom Insights)

The Dashboards section allows you to create and organize custom visualizations:

![Custom Dashboards](/docs/images/dashboard-custom.png)

You can build insights using either the visual editor (for simple queries) or TelemetryDeck Query Language (TQL) for more complex analysis. Common dashboard setups include:

- **Feature usage dashboards** that track adoption of specific features
- **Conversion funnels** showing how users progress through multi-step processes
- **User segment comparisons** between different types of users
- **Error monitoring dashboards** focused on app stability

Each insight can be organized into groups (displayed in the sidebar) to keep related metrics together, such as "Onboarding Experience", "Premium Features", or "App Performance".

<div class="not-prose">
  <div class="my-6 grid grid-cols-1 gap-6 sm:grid-cols-2">
    <div class="group relative rounded-xl border bg-white border-slate-200 flex">
      <div class="absolute -inset-px rounded-xl border-2 border-transparent opacity-0 [background:linear-gradient(var(--quick-links-hover-bg,theme(colors.mars.50)),var(--quick-links-hover-bg,theme(colors.mars.100)))_padding-box,linear-gradient(to_top,theme(colors.mars.400),theme(colors.mars.500))_border-box] group-hover:opacity-100"></div>
      <div class="shadow relative overflow-hidden rounded-xl p-6 h-full">
        <h2 class="font-semibold text-base text-mars-500">
          <a href="/docs/articles/insights">
            <span class="absolute -inset-px rounded-xl"></span>Understanding Insights</a>
        </h2>
        <p class="mt-1 text-sm text-slate-700">Learn what insights are and how they help you understand your app's performance data.</p>
      </div>
    </div>
    <div class="group relative rounded-xl border bg-white border-slate-200 flex">
      <div class="absolute -inset-px rounded-xl border-2 border-transparent opacity-0 [background:linear-gradient(var(--quick-links-hover-bg,theme(colors.mars.50)),var(--quick-links-hover-bg,theme(colors.mars.100)))_padding-box,linear-gradient(to_top,theme(colors.mars.400),theme(colors.mars.500))_border-box] group-hover:opacity-100"></div>
      <div class="shadow relative overflow-hidden rounded-xl p-6 h-full">
        <h2 class="font-semibold text-base text-mars-500">
          <a href="/docs/articles/create-custom-dashboards">
            <span class="absolute -inset-px rounded-xl"></span>Creating Custom Dashboards</a>
        </h2>
        <p class="mt-1 text-sm text-slate-700">Learn how to organize your insights into custom dashboard groups for better organization.</p>
      </div>
    </div>
    <div class="group relative rounded-xl border bg-white border-slate-200 flex">
      <div class="absolute -inset-px rounded-xl border-2 border-transparent opacity-0 [background:linear-gradient(var(--quick-links-hover-bg,theme(colors.mars.50)),var(--quick-links-hover-bg,theme(colors.mars.100)))_padding-box,linear-gradient(to_top,theme(colors.mars.400),theme(colors.mars.500))_border-box] group-hover:opacity-100"></div>
      <div class="shadow relative overflow-hidden rounded-xl p-6 h-full">
        <h2 class="font-semibold text-base text-mars-500">
          <a href="/docs/articles/set-up-filters-insights">
            <span class="absolute -inset-px rounded-xl"></span>Setting Up Filters</a>
        </h2>
        <p class="mt-1 text-sm text-slate-700">Learn how to use the filter editor to refine your insights and focus on specific data.</p>
      </div>
    </div>
    <div class="group relative rounded-xl border bg-white border-slate-200 flex">
      <div class="absolute -inset-px rounded-xl border-2 border-transparent opacity-0 [background:linear-gradient(var(--quick-links-hover-bg,theme(colors.mars.50)),var(--quick-links-hover-bg,theme(colors.mars.100)))_padding-box,linear-gradient(to_top,theme(colors.mars.400),theme(colors.mars.500))_border-box] group-hover:opacity-100"></div>
      <div class="shadow relative overflow-hidden rounded-xl p-6 h-full">
        <h2 class="font-semibold text-base text-mars-500">
          <a href="/docs/articles/how-to-funnel-insights">
            <span class="absolute -inset-px rounded-xl"></span>Creating Funnel Charts</a>
        </h2>
        <p class="mt-1 text-sm text-slate-700">Learn how to track user conversion through multi-step processes with funnel charts.</p>
      </div>
    </div>
  </div>
</div>

## Notebooks (Analysis Documentation)

The Notebooks tab lets you combine live charts and markdown text in a single place, so you can document your questions, structure your investigations, and share insights with your team. Perfect for keeping context during long-running analyses, preparing presentations, or leaving notes for your future self.

For example, here's an excerpt of a notebook:
![Sample Notebook investigating Onboarding issues with Explanations](/docs/images/dashboard-notebooks.png)

You can use Notebooks to:
- Document your hypotheses and findings alongside live data
- Track what data you're waiting for and plan next steps
- Share structured analyses with your team or stakeholders

<div class="not-prose">
  <div class="my-6 grid grid-cols-1 gap-6">
    <div class="group relative rounded-xl border bg-white border-slate-200 flex">
      <div class="absolute -inset-px rounded-xl border-2 border-transparent opacity-0 [background:linear-gradient(var(--quick-links-hover-bg,theme(colors.mars.50)),var(--quick-links-hover-bg,theme(colors.mars.100)))_padding-box,linear-gradient(to_top,theme(colors.mars.400),theme(colors.mars.500))_border-box] group-hover:opacity-100"></div>
      <div class="shadow relative overflow-hidden rounded-xl p-6 h-full">
        <h2 class="font-semibold text-base text-mars-500">
          <a href="/docs/articles/notebooks">
            <span class="absolute -inset-px rounded-xl"></span>A Practical Guide to Notebooks</a>
        </h2>
        <p class="mt-1 text-sm text-slate-700">Learn how to effectively use Notebooks to combine live charts and markdown text for better analytics insights and documentation.</p>
      </div>
    </div>
  </div>
</div>

## Common Dashboard tasks

### Filtering data

At the top of most dashboard pages, you'll find time filters that let you focus on specific periods:

![Filtering Data](/docs/images/dashboard-filtering-data.png)

- **Last 30 Days** (default) – Shows data from the past month
- **Test Mode** – Toggle to see data from development builds (when your app is run directly from your IDE)

<div class="not-prose">
  <div class="my-6 grid grid-cols-1 gap-6">
    <div class="group relative rounded-xl border bg-white border-slate-200 flex">
      <div class="absolute -inset-px rounded-xl border-2 border-transparent opacity-0 [background:linear-gradient(var(--quick-links-hover-bg,theme(colors.mars.50)),var(--quick-links-hover-bg,theme(colors.mars.100)))_padding-box,linear-gradient(to_top,theme(colors.mars.400),theme(colors.mars.500))_border-box] group-hover:opacity-100"></div>
      <div class="shadow relative overflow-hidden rounded-xl p-6 h-full">
        <h2 class="font-semibold text-base text-mars-500">
          <a href="/docs/articles/test-mode">
            <span class="absolute -inset-px rounded-xl"></span>Using Test Mode</a>
        </h2>
        <p class="mt-1 text-sm text-slate-700">Understand how to use Test Mode to separate development events from production data.</p>
      </div>
    </div>
  </div>
</div>

### Exploring details

Many visualizations have interactive elements:

![Exploring Details](/docs/images/dashboard-exploring-details.png)

- Hover over chart elements to see detailed values and source info
- Use the "..." menu in the top right of cards for additional options


## Collaboration

<div class="not-prose">
  <div class="my-6 grid grid-cols-1 gap-6">
    <div class="group relative rounded-xl border bg-white border-slate-200 flex">
      <div class="absolute -inset-px rounded-xl border-2 border-transparent opacity-0 [background:linear-gradient(var(--quick-links-hover-bg,theme(colors.mars.50)),var(--quick-links-hover-bg,theme(colors.mars.100)))_padding-box,linear-gradient(to_top,theme(colors.mars.400),theme(colors.mars.500))_border-box] group-hover:opacity-100"></div>
      <div class="shadow relative overflow-hidden rounded-xl p-6 h-full">
        <h2 class="font-semibold text-base text-mars-500">
          <a href="/docs/articles/invite-members-to-organization">
            <span class="absolute -inset-px rounded-xl"></span>Inviting Team Members</a>
        </h2>
        <p class="mt-1 text-sm text-slate-700">Learn how to invite colleagues to your TelemetryDeck organization and collaborate on analytics.</p>
      </div>
    </div>
  </div>
</div>

## Advanced features

<div class="not-prose">
  <div class="my-6 grid grid-cols-1 gap-6 sm:grid-cols-2">
    <div class="group relative rounded-xl border bg-white border-slate-200 flex">
      <div class="absolute -inset-px rounded-xl border-2 border-transparent opacity-0 [background:linear-gradient(var(--quick-links-hover-bg,theme(colors.mars.50)),var(--quick-links-hover-bg,theme(colors.mars.100)))_padding-box,linear-gradient(to_top,theme(colors.mars.400),theme(colors.mars.500))_border-box] group-hover:opacity-100"></div>
      <div class="shadow relative overflow-hidden rounded-xl p-6 h-full">
        <h2 class="font-semibold text-base text-mars-500">
          <a href="/docs/tql/firstGuideline">
            <span class="absolute -inset-px rounded-xl"></span>Using TQL for Advanced Queries</a>
        </h2>
        <p class="mt-1 text-sm text-slate-700">Learn about TelemetryDeck Query Language for creating complex custom insights.</p>
      </div>
    </div>
    <div class="group relative rounded-xl border bg-white border-slate-200 flex">
      <div class="absolute -inset-px rounded-xl border-2 border-transparent opacity-0 [background:linear-gradient(var(--quick-links-hover-bg,theme(colors.mars.50)),var(--quick-links-hover-bg,theme(colors.mars.100)))_padding-box,linear-gradient(to_top,theme(colors.mars.400),theme(colors.mars.500))_border-box] group-hover:opacity-100"></div>
      <div class="shadow relative overflow-hidden rounded-xl p-6 h-full">
        <h2 class="font-semibold text-base text-mars-500">
          <a href="/docs/articles/insights-about-referrers">
            <span class="absolute -inset-px rounded-xl"></span>Website Traffic Source Analysis</a>
        </h2>
        <p class="mt-1 text-sm text-slate-700">For web apps, learn how to track where your users are coming from before visiting your site.</p>
      </div>
    </div>
  </div>
</div>

## Integrations

<div class="not-prose">
  <div class="my-6 grid grid-cols-1 gap-6 sm:grid-cols-2">
    <div class="group relative rounded-xl border bg-white border-slate-200 flex">
      <div class="absolute -inset-px rounded-xl border-2 border-transparent opacity-0 [background:linear-gradient(var(--quick-links-hover-bg,theme(colors.mars.50)),var(--quick-links-hover-bg,theme(colors.mars.100)))_padding-box,linear-gradient(to_top,theme(colors.mars.400),theme(colors.mars.500))_border-box] group-hover:opacity-100"></div>
      <div class="shadow relative overflow-hidden rounded-xl p-6 h-full">
        <h2 class="font-semibold text-base text-mars-500">
          <a href="/docs/integrations/revenuecat">
            <span class="absolute -inset-px rounded-xl"></span>RevenueCat Integration</a>
        </h2>
        <p class="mt-1 text-sm text-slate-700">Learn how to integrate TelemetryDeck with RevenueCat to combine usage data with purchase data.</p>
      </div>
    </div>
    <div class="group relative rounded-xl border bg-white border-slate-200 flex">
      <div class="absolute -inset-px rounded-xl border-2 border-transparent opacity-0 [background:linear-gradient(var(--quick-links-hover-bg,theme(colors.mars.50)),var(--quick-links-hover-bg,theme(colors.mars.100)))_padding-box,linear-gradient(to_top,theme(colors.mars.400),theme(colors.mars.500))_border-box] group-hover:opacity-100"></div>
      <div class="shadow relative overflow-hidden rounded-xl p-6 h-full">
        <h2 class="font-semibold text-base text-mars-500">
          <a href="/docs/integrations/superwall">
            <span class="absolute -inset-px rounded-xl"></span>Superwall Integration</a>
        </h2>
        <p class="mt-1 text-sm text-slate-700">Learn how to integrate TelemetryDeck with Superwall to get insights into your paywalls.</p>
      </div>
    </div>
  </div>
</div>

## Privacy & Security

<div class="not-prose">
  <div class="my-6 grid grid-cols-1 gap-6 sm:grid-cols-2">
    <div class="group relative rounded-xl border bg-white border-slate-200 flex">
      <div class="absolute -inset-px rounded-xl border-2 border-transparent opacity-0 [background:linear-gradient(var(--quick-links-hover-bg,theme(colors.mars.50)),var(--quick-links-hover-bg,theme(colors.mars.100)))_padding-box,linear-gradient(to_top,theme(colors.mars.400),theme(colors.mars.500))_border-box] group-hover:opacity-100"></div>
      <div class="shadow relative overflow-hidden rounded-xl p-6 h-full">
        <h2 class="font-semibold text-base text-mars-500">
          <a href="/docs/articles/anonymization-how-it-works">
            <span class="absolute -inset-px rounded-xl"></span>How User Data Anonymization Works</a>
        </h2>
        <p class="mt-1 text-sm text-slate-700">Learn how TelemetryDeck protects user privacy while still providing valuable analytics.</p>
      </div>
    </div>
    <div class="group relative rounded-xl border bg-white border-slate-200 flex">
      <div class="absolute -inset-px rounded-xl border-2 border-transparent opacity-0 [background:linear-gradient(var(--quick-links-hover-bg,theme(colors.mars.50)),var(--quick-links-hover-bg,theme(colors.mars.100)))_padding-box,linear-gradient(to_top,theme(colors.mars.400),theme(colors.mars.500))_border-box] group-hover:opacity-100"></div>
      <div class="shadow relative overflow-hidden rounded-xl p-6 h-full">
        <h2 class="font-semibold text-base text-mars-500">
          <a href="/docs/guides/privacy-faq">
            <span class="absolute -inset-px rounded-xl"></span>Privacy FAQ</a>
        </h2>
        <p class="mt-1 text-sm text-slate-700">Find answers to common questions about TelemetryDeck's privacy features and policies.</p>
      </div>
    </div>
  </div>
</div>