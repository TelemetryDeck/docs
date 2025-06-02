---
title: Metrics Analytics
tags:
  - setup
  - basics
  - technical-metrics
  - analytics
basics: true
description: Learn how to interpret and act on TelemetryDeck's technical metrics to optimize your app's performance and compatibility.
lead: Metrics Analytics provides critical technical insights about how your app performs across different devices, platforms, and configurations. TelemetryDeck automatically collects these details to help you make informed decisions about development priorities, OS support, and accessibility needs.
searchEngineTitle: App Technical Metrics & Analytics | TelemetryDeck
searchEngineDescription: Learn how to interpret technical metrics data for your app with TelemetryDeck's automatic device, version, and error analytics.
order: 70
---

## What are Technical Metrics?

Technical metrics represent the operational aspects of your app – how it performs across devices, versions, languages, and accessibility settings. These metrics help you understand your app's compatibility landscape, identify technical issues, and prioritize development efforts.

With TelemetryDeck's Metrics dashboard, these insights are automatically collected and visualized with no additional code required beyond the basic SDK integration.

## Device & platform distribution

**Questions you can answer:**
- What devices are my users using to access my app?
- Which platforms should I prioritize for development and testing?
- When can I safely drop support for older devices?

![Device and Platform Distribution](/docs/images/metrics-devices.png)

**How to interpret the charts:**
- **Models**: Shows specific device models being used, helping prioritize testing
- **Types**: Reveals device categories for understanding user hardware preferences
- **Platforms**: Displays the OS platform breakdown (iOS, macOS, visionOS)
- **Platform distribution changes**: Identifies shifts in platform usage over time

**Action example:** Looking at the Models chart, we can see MacBook Air (M1 and M2) models account for 17% of devices, while new Apple Vision Pro (RealityDevice) users represent 7%. iPhone models collectively account for a significant portion of usage. With iOS accounting for 62.05% of platform usage and macOS at 34.55%, you should prioritize iOS testing while maintaining solid macOS support. The emergence of visionOS at 3.40% shows early adoption of this platform that may warrant attention for future development.

## Version analytics

**Questions you can answer:**
- How quickly are users adopting my latest app version?
- When do users typically update after a new release?
- Are there patterns in build adoption?
- Which SDK versions are in use across your user base?

![Version Analytics](/docs/images/metrics-versions.png)

**How to interpret the charts:**
- **App Versions**: Tracks adoption of your app releases over time
- **Build Numbers**: Provides more granular insight into specific build adoption
- **SDK Versions**: Reveals which versions of your SDK are in use

**Action example:** The App Versions chart shows a clear transition starting in early March, with users moving from the previous version (green) to the latest release (blue). This transition happened relatively quickly, suggesting users are responsive to updates. The Build Numbers chart shows a similar pattern, with a diverse range of builds in use before March consolidating to newer versions. The SDK Versions chart reveals an interesting transition from version 2.2.3 (yellow) to 2.2.4 (light green) and SwiftClient 1.5.1 (green) in March, suggesting your SDK updates are being adopted alongside app updates. This data indicates that you can likely count on most users updating within 2-3 weeks of a release.

## Error monitoring

**Questions you can answer:**
- What are the most common errors occurring in my app?
- When did error rates spike or change?
- Which errors should I prioritize fixing?
- Are errors occurring on specific devices or platforms?

![Error Monitoring](/docs/images/metrics-errors.png)

**How to interpret the charts:**
- **Most Frequent Errors**: Ranks issues by occurrence count and percentage
- **Error History**: Shows error frequency over time, highlighting spikes
- **Thrown Exception Errors**: Details specific exception types
- **Error distribution**: Helps correlate errors with platforms or versions

**Action example:** The "Most Frequent Errors" chart identifies "ProjectDetails.loadAppInfo" as your most common error (29% of total errors), followed by "AITranslation.loadAvailability" (25%). These two issues account for more than half of all errors, making them high-priority fixes. The error history graph shows a significant spike in mid-March, which may correlate with a specific release or backend change. Focusing on resolving these top issues first will have the largest impact on improving app stability for your users.

{% noteinfo "Action Required" %}
TelemetryDeck offers built-in presets for error tracking that require some configuration in your app code. With a few simple implementation steps, you can collect and categorize errors to identify patterns and prioritize fixes.
{% endnoteinfo %}

<div class="not-prose">
  <div class="my-6 grid grid-cols-1 gap-6">
    <div class="group relative rounded-xl border bg-white border-slate-200 flex">
      <div class="absolute -inset-px rounded-xl border-2 border-transparent opacity-0 [background:linear-gradient(var(--quick-links-hover-bg,theme(colors.mars.50)),var(--quick-links-hover-bg,theme(colors.mars.100)))_padding-box,linear-gradient(to_top,theme(colors.mars.400),theme(colors.mars.500))_border-box] group-hover:opacity-100"></div>
      <div class="shadow relative overflow-hidden rounded-xl p-6 h-full">
        <h2 class="font-semibold text-base text-mars-500">
          <a href="/docs/articles/preset-errors">
            <span class="absolute -inset-px rounded-xl"></span>Implementing Error Tracking</a>
        </h2>
        <p class="mt-1 text-sm text-slate-700">Learn how to set up TelemetryDeck's error reporting system in your app code to capture and analyze runtime issues.</p>
      </div>
    </div>
  </div>
</div>

## Localization insights

**Questions you can answer:**
- What languages do my users speak?
- Which regions show significant app usage?
- Should I invest in additional localizations?
- Are users using my app in the same language as their device?

![Localization Insights](/docs/images/metrics-localization.png)

**How to interpret the charts:**
- **Preferred Language**: Shows user device language settings
- **App Language**: Indicates which language the system (or user) has selected for your app
- **Region**: Displays geographical distribution of your users
- **Layout Direction**: Shows text direction preferences (LTR vs RTL)

**Action example:** The data shows a diverse user base with English (45.52% preferred/51.87% app) and German (30.94% preferred/31.12% app) leading language usage. Germany (25.49%), US (20.60%), and UK (13.29%) are your top markets. The strong German presence in both language and regional data suggests significant opportunity for enhanced German-language support and targeted marketing in German-speaking countries.

## Accessibility usage

**Questions you can answer:**
- How many of my users utilize accessibility features?
- Which accessibility settings are most common?
- Does my app need better accessibility support?
- How would design changes impact users with accessibility needs?

![Accessibility Usage](/docs/images/metrics-accessibility.png)

**How to interpret the charts:**
- **Preferred Content Size**: Shows text size preferences (88.43% use default size "L")
- **Bold Text Usage**: Indicates users who need stronger text contrast (3.31%)
- **Reduce Motion**: Shows users sensitive to animations (0% in this sample)
- **Reduce Transparency**: Reveals users who need less UI transparency (4.13%)

**Action example:** While most users (88.43%) use the default content size "L", a significant portion (6.61%) use the larger "XXXL" setting, indicating they need much larger text for readability. Additionally, 4.13% of users have enabled the Reduce Transparency setting. These metrics suggest you should test your app thoroughly with larger text settings and ensure it remains functional and attractive for users who need these accessibility features. The complete absence of "Reduce Motion" usage in your current user base doesn't mean you can ignore motion considerations – it may simply reflect that users who need this setting aren't using your app yet.

## Making data-driven decisions with Metrics

Your technical metrics provide critical insights for development decisions. Consider these key questions as you analyze the data:

1. **Platform strategy**
   - Which device models and OS versions represent your core users?
   - When can you adopt new platform features or drop legacy support?
   - Does your user base justify expanding to emerging platforms?

2. **Technical improvements**
   - Which errors have the highest impact on your user experience?
   - Are specific devices or configurations experiencing more issues?
   - How quickly are users adopting your latest app version?

3. **Localization priorities**
   - Which languages and regions show significant adoption?
   - Are users using your app in their preferred language?
   - Would accessibility improvements benefit a meaningful portion of users?

Remember that technical metrics complement your user behavior analytics. By combining device insights with acquisition and engagement data, you'll build a complete picture of how technical decisions impact real-world user experience.

## Related guides

<div class="not-prose">
  <div class="my-6 grid grid-cols-1 gap-6 sm:grid-cols-2">
    <div class="group relative rounded-xl border bg-white border-slate-200 flex">
      <div class="absolute -inset-px rounded-xl border-2 border-transparent opacity-0 [background:linear-gradient(var(--quick-links-hover-bg,theme(colors.mars.50)),var(--quick-links-hover-bg,theme(colors.mars.100)))_padding-box,linear-gradient(to_top,theme(colors.mars.400),theme(colors.mars.500))_border-box] group-hover:opacity-100"></div>
      <div class="shadow relative overflow-hidden rounded-xl p-6 h-full">
        <h2 class="font-semibold text-base text-mars-500">
          <a href="/docs/articles/decide-to-drop-ios-version">
            <span class="absolute -inset-px rounded-xl"></span>Strategic OS Support Planning</a>
        </h2>
        <p class="mt-1 text-sm text-slate-700">Learn the practical framework for balancing backward compatibility with development resources using metrics data.</p>
      </div>
    </div>
    <div class="group relative rounded-xl border bg-white border-slate-200 flex">
      <div class="absolute -inset-px rounded-xl border-2 border-transparent opacity-0 [background:linear-gradient(var(--quick-links-hover-bg,theme(colors.mars.50)),var(--quick-links-hover-bg,theme(colors.mars.100)))_padding-box,linear-gradient(to_top,theme(colors.mars.400),theme(colors.mars.500))_border-box] group-hover:opacity-100"></div>
      <div class="shadow relative overflow-hidden rounded-xl p-6 h-full">
        <h2 class="font-semibold text-base text-mars-500">
          <a href="/docs/articles/check-if-users-upgrade-to-latest-app-version">
            <span class="absolute -inset-px rounded-xl"></span>Version Migration Insights</a>
        </h2>
        <p class="mt-1 text-sm text-slate-700">Discover patterns in how quickly users update and what this means for your release strategy.</p>
      </div>
    </div>
  </div>
</div>