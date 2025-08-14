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

User activation represents the critical moment when users first experience your app's core value – the "aha moment" that transforms them from curious installers into engaged users. These metrics help you understand how well your onboarding works, identify friction points, and optimize the first-time experience.

With TelemetryDeck's Activation dashboard, these insights are automatically collected and visualized with no additional code required beyond updating to SwiftSDK 2.8.0 / KotlinSDK 6.0.0 or later.

{% noteinfo "How TelemetryDeck Detects Activated Users" %}
Activated users are those with at least 5 minutes total usage time while having either less than 15 minutes total usage (to exclude long-term users) or fewer than 5 sessions.
{% endnoteinfo %}

## Activated user growth trends

**Questions you can answer:**
- How many users are experiencing my app's core value?
- Are my activation rates improving over time?
- How effective is my onboarding experience?
- What are the immediate activation patterns in the last 24 hours?

![Hourly, Daily, Weekly, and Monthly Activated Users](/docs/images/activation-activated-users.png)

**How to interpret the charts:**
- **Hourly (last 24h)**: Shows recent activation activity and immediate trends – useful for spotting issues or validating recent changes
- **Daily patterns**: Consistent upward trend indicates your onboarding is working well; sudden spikes may correlate with improvements or campaigns
- **Weekly/Monthly trends**: Reveal longer-term activation health and seasonal patterns
- **Declining trends**: May indicate onboarding friction, confusing first experiences, or performance issues

**Action example:** If you see that your daily activated users consistently grow after implementing a new onboarding flow, you've successfully improved the first-time experience. The hourly chart helps you immediately validate changes – if you deploy an onboarding improvement and see activation drop in the next few hours, you can quickly investigate and respond.

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

**Action example:** The Hour of Day chart shows peak activations around 8pm-10pm, suggesting users activate when they have leisure time to properly explore your app. The past 4 weeks data reveals that Sunday evenings consistently show the strongest activation performance, while Wednesday afternoons have declined. The Weekend vs Weekday chart shows 45% of activations happen on weekends (above the statistical norm of 29%), indicating users need focused time to experience your app's value. Time your onboarding prompts and feature introductions for weekend evenings when users are most receptive.

## Activation by device & platform

**Questions you can answer:**
- Which devices provide the best activation experience?
- Should I optimize my onboarding for specific hardware or screen sizes?
- Are there platform-specific activation barriers?

![Activated Users by Device Type](/docs/images/activation-device-distribution.png)

**How to interpret the chart:**
- **Top-performing devices**: These provide the best activation experience – understand why
- **Low activation devices**: May have UI issues, performance problems, or usability challenges
- **Platform differences**: iOS vs. Android vs. other platforms may have different activation patterns

**Action example:** The chart shows iPhone users have strong activation rates across multiple models (iPhone 11, 15, 16 Pro each around 10%), while certain older models show lower activation rates. This suggests your onboarding experience works well on modern iPhones but may need optimization for older hardware. With macOS representing 35% of activated users, ensure your cross-platform experience maintains the same activation quality across both mobile and desktop environments.

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

**Action example:** Looking at the Activated Users by Country chart, you can see that the United States (45%) and Germany (20%) show the strongest activation rates, followed by the United Kingdom and France (each around 10%). The language distribution shows English (70%) and German (15%) users have particularly strong activation patterns. This suggests your onboarding and core experience work exceptionally well for English and German-speaking users. Consider investing in localization for other represented languages like French and Italian to improve activation rates in those markets.

## First session insights

**Questions you can answer:**
- How long do users need to experience your app's core value?
- What session patterns indicate successful activation?
- How can I optimize the critical first session experience?

![First Session Duration and Patterns](/docs/images/activation-first-session-insights.png)

**How to interpret the charts:**
- **Session length distribution**: Shows how much time users need for activation
- **Sessions per user**: Indicates whether activation happens immediately or requires multiple attempts
- **Usage patterns**: Reveals when during first sessions users typically activate

**Action example:** The session length distribution shows most activated users spend 8-12 minutes in their first meaningful session, with very few activating in under 5 minutes. This suggests your app's core value requires focused exploration rather than immediate discovery. The sessions per user chart indicates that 70% of activated users succeed within their first 2-3 sessions. Use this data to design onboarding that guides users toward 10+ minute exploration sessions and provides clear progress indicators to encourage completion.

## Making data-driven activation decisions

As you analyze your activation metrics, consider these key questions:

1. **Onboarding optimization**
   - What time investment does successful activation require, and how can you set proper expectations?
   - Which devices or platforms struggle with activation, and what specific improvements are needed?
   - When do users have the focus and motivation needed for successful activation experiences?

2. **Experience design priorities**
   - Are there geographic or language patterns that suggest localization opportunities?
   - How can you design first sessions that consistently lead to your 8-12 minute activation sweet spot?
   - What can you learn from your highest-performing activation time windows?

3. **Growth opportunities**
   - Which user segments show strong activation rates that you can focus acquisition efforts on?
   - Are there activation patterns that suggest your app fits specific use cases or lifestyles better than others?
   - How can you help the users who are active but not yet activated discover your app's core value?

Remember that successful activation is the foundation for retention. Users who experience your app's core value in their first sessions are much more likely to become long-term, engaged users who drive sustainable growth.

## What's Next?

Start by analyzing your activation timing patterns and first session insights. Focus on optimizing the experience during your peak activation windows and consider how to guide users toward the 8-12 minute exploration sessions that typically lead to activation.

## Related resources

<div class="not-prose">
  <div class="my-6 grid grid-cols-1 gap-6 sm:grid-cols-2">
    <div class="group relative rounded-xl border bg-white border-slate-200 flex">
      <div class="p-6">
        <h3 class="text-lg font-semibold text-slate-900 group-hover:text-blue-600">
          <a href="/docs/basics/acquisition" class="stretched-link">
            Acquisition Analytics
          </a>
        </h3>
        <p class="mt-2 text-sm text-slate-600">
          Understanding how users discover and install your app sets the foundation for activation success.
        </p>
      </div>
    </div>
    <div class="group relative rounded-xl border bg-white border-slate-200 flex">
      <div class="p-6">
        <h3 class="text-lg font-semibold text-slate-900 group-hover:text-blue-600">
          <a href="/docs/basics/retention" class="stretched-link">
            Retention Analytics
          </a>
        </h3>
        <p class="mt-2 text-sm text-slate-600">
          Once users are activated, retention analytics help you understand how to keep them engaged long-term.
        </p>
      </div>
    </div>
  </div>
</div>