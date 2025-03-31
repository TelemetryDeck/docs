---
title: The Pirate Metrics Framework
tags:
  - basics
  - analytics
  - pirate-metrics
basics: true
description: Learn how the AARRR framework provides a powerful lens for understanding your app's growth and how TelemetryDeck makes it accessible.
lead: The Pirate Metrics framework (AARRR) gives you a structured approach to understanding your app's full user journey. TelemetryDeck automatically organizes your analytics around these principles, making data-driven growth decisions simpler.
searchEngineTitle: Pirate Metrics (AARRR) Framework for App Analytics | TelemetryDeck
searchEngineDescription: Learn how TelemetryDeck implements the Pirate Metrics (AARRR) framework to provide actionable insights for your app with minimal configuration.
order: 100
---

## What are Pirate Metrics?

Pirate Metrics, also known as the AARRR framework, was created by venture capitalist Dave McClure to provide a simple, actionable way to think about product growth. The name "Pirate Metrics" comes from the sound pirates make: "AARRR!"

This framework breaks down the complete user journey into five key stages that form a natural progression:

![AARRR Framework Chart](/docs/images/aarrr-framework.png)

1. **Acquisition**: How users discover and install your app
2. **Activation**: How users experience your app for the first time
3. **Retention**: How users become regular, engaged users
4. **Referral**: How existing users invite new users
5. **Revenue**: How your app generates sustainable income

## Why we use Pirate Metrics at TelemetryDeck

We've adopted the Pirate Metrics framework for TelemetryDeck's analytics because:

1. **It's comprehensive**: The framework covers the entire user lifecycle from first discovery to becoming a paying, loyal advocate
2. **It's focused**: Each stage has clear metrics that matter, helping you avoid "data overload"
3. **It's actionable**: The framework naturally leads to specific strategies for improvement at each stage
4. **It's universal**: These concepts apply to virtually any app or digital product regardless of category

Most importantly, organizing analytics this way helps you identify your biggest growth opportunities. For example, if you have excellent acquisition but poor activation, you know exactly where to focus your efforts.

## How TelemetryDeck implements Pirate Metrics

The great news? **TelemetryDeck has done all the hard work for you**. 

Rather than requiring you to:
- Research which metrics matter for each stage
- Create custom tracking for each metric
- Build visualizations and dashboards
- Understand the intricacies of the framework

TelemetryDeck automatically organizes analytics around the Pirate Metrics framework with built-in insights that require minimal setup. Just update to our latest SDK, and the built-in metrics start working immediately.

## Built-in insights for each stage

Here's what TelemetryDeck automatically tracks for each stage of the Pirate Metrics framework:

### Acquisition insights

TelemetryDeck automatically tracks:
- Daily, weekly, and monthly new user counts
- Device and platform distribution (which devices are your new users using?)
- Geographic distribution (where are your new users located?)
- Acquisition time patterns (when do users typically discover your app?)

All of these insights help you understand where your users come from and optimize your marketing efforts.

### Activation insights (Coming Soon)

Our upcoming activation dashboard will automatically track:
- Daily, weekly, and monthly active user counts
- Average session length distribution
- Average sessions per active user
- Usage patterns by time of day and day of week
- First-time user experiences

These insights help you understand if users are successfully getting started with your app.

### Retention insights (Coming Soon)

Our retention dashboard will automatically track:
- Distinct days used distribution (how often users return)
- Engaged users metrics (session length > 2 minutes, 5+ days used per month)
- Power users metrics (session length > 5 minutes, 12+ days used per month)
- Long-term usage trends

These insights help you identify if users are finding ongoing value in your app.

### Referral insights (Coming Soon)

Our referral dashboard will track:
- Referral tracking metrics
- Channel effectiveness comparison
- Social sharing activity

These insights help you understand how effectively your app generates word-of-mouth growth.

### Revenue insights (Coming Soon)

Our revenue dashboard will track:
- Purchase counts (trials and non-trials)
- Free trial metrics
- Trial conversion rates
- Revenue trends over time

These insights help you understand your app's financial performance and optimize monetization.

## Minimal configuration required

The beauty of TelemetryDeck's implementation is that **most of these insights work with zero additional code** beyond basic SDK integration. Our SDKs automatically collect the necessary data to power these dashboards.

For some advanced metrics (particularly in the Referral and Revenue categories), you may need to add a few simple signals to your app. We provide simple, copy-paste examples for all major platforms that make this process quick and easy.

## Growth without the complexity

By implementing Pirate Metrics as built-in dashboards, TelemetryDeck gives you the benefits of sophisticated growth analytics without requiring you to:

- Become an expert in analytics theory
- Build complex custom dashboards
- Spend time deciphering what metrics matter
- Manually track dozens of different events

Instead, you get clear, actionable insights organized in a way that naturally guides you toward your biggest growth opportunities.

## Getting started with Pirate Metrics

To access these powerful dashboards:

1. **Update your SDK** to the latest version (SwiftSDK 2.8.0+, KotlinSDK 6.0.0+, FlutterSDK 2.3.0+)
2. **Navigate to the Customers tab** in your TelemetryDeck dashboard
3. **Explore each section** of the Pirate Metrics framework

As you navigate through these sections, you'll develop a comprehensive understanding of your app's performance throughout the entire user journey—from discovery to monetization—all with minimal setup on your part.

To dive deeper into specific parts of the framework, check out our dedicated guides:

<div class="not-prose">
  <div class="my-6 grid grid-cols-1 gap-6">
    <div class="group relative rounded-xl border bg-white border-slate-200 flex">
      <div class="absolute -inset-px rounded-xl border-2 border-transparent opacity-0 [background:linear-gradient(var(--quick-links-hover-bg,theme(colors.mars.50)),var(--quick-links-hover-bg,theme(colors.mars.100)))_padding-box,linear-gradient(to_top,theme(colors.mars.400),theme(colors.mars.500))_border-box] group-hover:opacity-100"></div>
      <div class="shadow relative overflow-hidden rounded-xl p-6 h-full">
        <h2 class="font-semibold text-base text-mars-500">
          <a href="/docs/basics/acquisition">
            <span class="absolute -inset-px rounded-xl"></span>Acquisition Analytics Guide</a>
        </h2>
        <p class="mt-1 text-sm text-slate-700">Learn how to interpret and act on acquisition metrics to optimize how users discover your app.</p>
      </div>
    </div>
  </div>
</div>
