---
title: Understanding User Acquisition
tags:
  - setup
  - basics
  - pirate-metrics
  - acquisition
basics: true
description: Learn how to interpret and act on TelemetryDeck's acquisition metrics to optimize how users discover your app.
lead: Acquisition is the first stage of the Pirate Metrics framework, focusing on how users find and install your app. TelemetryDeck automatically tracks these patterns to help you make data-driven decisions about marketing, platform support, and regional strategy.
searchEngineTitle: App User Acquisition Analytics & Metrics | TelemetryDeck
searchEngineDescription: Learn how to interpret user acquisition data for your mobile app with TelemetryDeck's automatic acquisition analytics.
order: 20
---

## What is User Acquisition?

User acquisition represents the entry point of your app's growth funnel – how users discover and install your app. Understanding acquisition patterns helps you answer critical questions about your marketing effectiveness, target audience, and growth opportunities.

With TelemetryDeck's Acquisition dashboard, these insights are automatically collected and visualized with no additional code required beyond updating to SwiftSDK 2.8.0+ or KotlinSDK 6.0.0+.

## Is Your App Growing?

**Key Question:** Is my user base expanding, and at what rate?

The Daily, Weekly, and Monthly New Users charts help you track growth trends over different time periods:

![New Users Charts](/docs/images/acquisition-new-users.png)

**How to use these insights:**
- **Identify growth trends**: Are new user numbers increasing, stable, or declining?
- **Measure marketing impact**: Do spikes in new users correlate with marketing campaigns?
- **Detect seasonality**: Are there predictable patterns in user acquisition by month or quarter?
- **Set realistic goals**: Use historical data to establish benchmark growth rates

**Action opportunities:**
- If you notice acquisition slowing, consider refreshing your App Store listing or increasing marketing efforts
- Use peak acquisition periods to schedule major feature announcements
- If you see consistent growth, investigate which channels are driving it and double down

## Who Are Your New Users?

**Key Question:** What proportion of your active users are discovering your app for the first time?

The Active vs. New Users charts reveal the balance between growth and retention:

![Active vs New Users Charts](/docs/images/acquisition-active-vs-new.png)

**How to interpret the ratio:**
- **High ratio (>0.5)**: Your app is growing rapidly with many new users, but may need to focus on retention
- **Decreasing ratio**: Your user base is stabilizing with more returning users than new ones
- **Fluctuating ratio**: May indicate seasonal interest or inconsistent marketing

**Action opportunities:**
- After major updates, watch for returning users (indicated by a lower ratio)
- If the ratio stays consistently high, investigate potential retention issues
- Use the ratio to determine when to shift focus from acquisition to retention efforts

## When Do Users Discover Your App?

**Key Question:** What temporal patterns exist in how users find your app?

The Acquisition Time Patterns section reveals exactly when users typically install your app:

![Acquisition Time Patterns](/docs/images/acquisition-time-patterns.png)

**What to look for:**
- **Hour of day peaks**: When during the day do most installations occur?
- **Day of week patterns**: Which days consistently bring the most new users?
- **Weekend vs. weekday balance**: Is your app primarily discovered during work hours or leisure time?

**Action opportunities:**
- Schedule social media posts or App Store ads to coincide with peak acquisition hours
- Time your marketing campaigns around your strongest acquisition days
- If you see strong weekday acquisition, emphasize productivity use cases in your marketing
- For weekend-dominant acquisition, highlight leisure or entertainment aspects

**Pro tip:** Compare when users *find* your app (acquisition time) with when they *use* your app (activation time) to understand the gap between discovery and engagement.

## What Devices Are Your New Users Using?

**Key Question:** Which hardware and platforms should you prioritize for development?

The Device & Platform Distribution charts show exactly what your new users are using:

![Device Distribution](/docs/images/acquisition-device-distribution.png)

**How to use these insights:**
- **Device prioritization**: Which specific device models represent the majority of your new users?
- **Platform strategy**: How is your audience distributed across operating systems?
- **Version support decisions**: Which OS versions are still relevant for your user base?

**Action opportunities:**
- Prioritize testing on the top 3-5 device types in your acquisition data
- Make informed decisions about dropping support for older OS versions
- Align your feature development with the capabilities of your users' actual devices
- If you see unexpected device types gaining traction, investigate potential new market opportunities

## Where Are Your New Users Located?

**Key Question:** In which regions is your app finding success, and where are the opportunities?

The Geographic & Language Distribution charts reveal the global footprint of your app:

![Geographic Distribution](/docs/images/acquisition-geographic-distribution.png)

**What to analyze:**
- **Regional strengths**: Which countries show the strongest adoption?
- **Untapped markets**: Are there regions with minimal presence but high potential?
- **Language preferences**: Do users' language settings suggest localization opportunities?

**Action opportunities:**
- Consider localization for languages that represent >5% of your user base
- Develop region-specific marketing strategies for high-performing areas
- Investigate regulatory or cultural factors in regions with lower-than-expected adoption
- Use regional insights to inform pricing strategy and payment method support

## Putting It All Together: Acquisition Strategy

Your acquisition metrics tell a story about who your users are, where they come from, and when they discover your app. Use these automated insights to:

1. **Optimize marketing timing** based on when users typically find your app
2. **Make informed platform decisions** based on actual user device distribution
3. **Target geographic expansion** with data on regional adoption patterns
4. **Allocate development resources** to support the devices your users actually use
5. **Measure the effectiveness** of marketing campaigns and App Store optimization efforts

Remember that acquisition is just the first step in the Pirate Metrics framework. Once you've optimized how users find your app, the next challenge is ensuring they have a great first experience – which is where [Activation metrics](/docs/pirate-metrics/activation.md) come into play.

## Questions to Ask About Your Acquisition Data

As you explore your acquisition dashboard, consider these strategic questions:

- Is my acquisition growth keeping pace with my marketing investment?
- Are there untapped geographic markets where my app is gaining organic traction?
- Does my app architecture and feature roadmap align with the devices my users actually have?
- Are my marketing activities synchronized with when users typically discover my app?
- Is my app store presence optimized for the regions showing the strongest growth?

By regularly reviewing your acquisition metrics and asking these questions, you'll develop a more strategic approach to growing your app's user base.
