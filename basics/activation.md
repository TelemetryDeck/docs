---
title: Activation Analytics
tags:
  - setup
  - basics
  - pirate-metrics
  - activation
basics: true
description: Learn how to interpret and act on TelemetryDeck's activation metrics to optimize your app's first-time user experience.
lead: Activation is the second stage of the Pirate Metrics framework, focusing on when users experience your app's core value for the first time. TelemetryDeck automatically tracks these patterns to help you optimize the crucial first sessions that turn new users into engaged users.
searchEngineTitle: App User Activation Analytics & Metrics | TelemetryDeck
searchEngineDescription: Learn how to interpret user activation data for your mobile app with TelemetryDeck's automatic activation analytics.
order: 21
---

## What is User Activation?

User activation represents the critical moment when users first experience your app's core value – the "aha moment" that transforms them from curious installers into engaged users. These metrics help you understand how well your Onboarding works, identify friction points, and optimize the first-time experience.

With TelemetryDeck's Activation dashboard, these insights are automatically collected and visualized with no additional code required beyond updating to SwiftSDK 2.8.0 / KotlinSDK 6.0.0 or later.

{% noteinfo "How TelemetryDeck Detects Activated Users" %}
Activated users are those with at least 5 minutes accumulated total usage time within their 5 sessions.
{% endnoteinfo %}

## Activated user growth trends

**Questions you can answer:**
- How many users are experiencing my app's core value?
- Are my activation rates improving over time?
- How effective is my Onboarding experience?
- What are the immediate activation patterns in the last 24 hours?

![Hourly, Daily, Weekly, and Monthly Activated Users](/docs/images/activation-activated-users.png)

**How to interpret the charts:**
- **Hourly (last 24h)**: Shows recent activation activity and immediate trends – useful for spotting issues or validating recent changes
- **Daily patterns**: Consistent upward trend indicates your Onboarding is working well; sudden spikes may correlate with improvements or campaigns
- **Weekly/Monthly trends**: Reveal longer-term activation health and seasonal patterns
- **Declining trends**: May indicate Onboarding friction, confusing first experiences, or performance issues

**How to read your data:** In this example dashboard, the monthly chart shows activation building from earlier months to peak around March-April (~50+ users), demonstrating successful activation strategies reaching strong performance levels. The weekly data shows more stable patterns (12-15 user range) compared to daily fluctuations (1-8 users with occasional spikes), which suggests normal variation rather than systemic issues. Use the hourly chart to immediately validate Onboarding changes – if activation drops after deploying improvements, investigate quickly.

## Activation time patterns

**Questions you can answer:**
- When during the day do users typically get activated?
- Which days of the week see the most successful first experiences?
- Do weekdays or weekends provide better conditions for user activation?
- Are recent activation patterns consistent with long-term trends?

![Activation Time Patterns](/docs/images/activation-by-time.png)

**How to interpret the charts:**
- **Hour of day patterns**: Show when users have time to properly explore your app (user-local timezone)
- **Day patterns (past 4 weeks)**: Reveal specific days with exceptional activation performance
- **Weekend vs. weekday balance**: Indicates whether activation requires focused time or fits into busy schedules
- **Recent trends**: Help identify if timing patterns are changing over time

**How to read your data:** In this example, the Hour of Day chart shows peak activations around 12-1 p.m. and 5-6 p.m., which would suggest users activate during lunch breaks and after work hours when they have focused time to explore the app. The Day of Week chart shows Friday with the strongest activation performance (34 users) and Sunday with the lowest (21 users), indicating a weekday preference for activation. If you see similar patterns in your data, it would suggest users are more likely to experience your app's core value during structured time periods. You could then time your Onboarding prompts and feature introductions for weekday lunch periods and early evenings when users are most engaged.

## Activation by device & platform

**Questions you can answer:**
- Which devices provide the best activation experience?
- Should I optimize my Onboarding for specific hardware or screen sizes?
- Are there platform-specific activation barriers?

![Activated Users by Device Type](/docs/images/activation-device-distribution.png)

**How to interpret the chart:**
- **Top-performing devices**: These provide the best activation experience – understand why
- **Low activation devices**: May have UI issues, performance problems, or usability challenges
- **Platform differences**: iOS vs. Android vs. other platforms may have different activation patterns

**How to read your data:** In this example, iOS users represent 60% of activated users while macOS represents 40%. Among individual devices, iPhone 15 Pro Max leads at 8.57%, with several models each representing around 5.71% of activations. When you see relatively even distribution across device types like this, it suggests the Onboarding experience works consistently well across platforms. A strong secondary platform presence (like the 40% macOS here) would indicate successful cross-platform activation. If you see similar patterns, focus your testing efforts on the leading device models while maintaining cross-platform activation quality.

## Activation by geography & language

**Questions you can answer:**
- Where are users most successfully experiencing my app's value?
- What languages correlate with higher activation rates?
- Which markets provide the strongest foundation for growth?

![Activated Users by Country and Language](/docs/images/activation-geographic-distribution.png)

**How to interpret the charts:**
- **Strong activation regions**: Countries where users consistently experience your app's value
- **Emerging markets**: Regions with growing activation that may warrant localization investment
- **Language correlation**: Languages that correlate with successful activation experiences

**How to read your data:** In this example dashboard, Germany (37.14%) shows as the strongest activation market, followed by Italy (14.29%) and the United States (8.57%). The language distribution shows German (48.57%) and English (28.57%) users with the strongest activation patterns, plus Italian (17.14%) showing significant engagement. When you see patterns like this in your own data, it would suggest your Onboarding experience works particularly well for certain language groups. You could then prioritize localization efforts for your top-performing regions to maximize activation in those markets.


## Making data-driven activation decisions

As you analyze your activation metrics, consider these key questions:

1. **Onboarding Optimization**
   - What time investment does successful activation require, and how can you set proper expectations?
   - Which devices or platforms struggle with activation, and what specific improvements are needed?
   - When do users have the focus and motivation needed for successful activation experiences?

2. **Experience design priorities**
   - Are there geographic or language patterns that suggest localization opportunities?
   - How can you design activation experiences that work within users' natural usage patterns?
   - What can you learn from your highest-performing activation time windows?

3. **Growth opportunities**
   - Which user segments show strong activation rates that you can focus acquisition efforts on?
   - Are there activation patterns that suggest your app fits specific use cases or lifestyles better than others?
   - How can you help the users who are active but not yet activated discover your app's core value?

Remember that successful activation is the foundation for retention. Users who experience your app's core value in their first sessions are much more likely to become long-term, engaged users who drive sustainable growth.
