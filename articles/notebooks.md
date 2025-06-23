---
title: A Practical Guide to Notebooks
tags:
  - notebooks
  - insights
  - how-to
  - features
description: Learn how to effectively use Notebooks to combine live charts and markdown text for better analytics insights and documentation.
lead: Notebooks combine live charts with your analytical thinking, helping you preserve context and momentum in your investigations. This guide shows you how to use them effectively, from basic setup to advanced techniques.
searchEngineTitle: How to Use TelemetryDeck Notebooks - A Practical Guide
searchEngineDescription: Learn how to effectively use TelemetryDeck Notebooks to combine live charts and markdown text for better analytics insights and documentation.
---

## Getting Started with Notebooks

Notebooks are your analytics lab notebook – a place where you can document your findings, share insights with your team, and maintain context throughout your investigations. Let's explore how to use them effectively.

### Creating Your First Notebook

1. Open the Notebooks tab in your TelemetryDeck dashboard
2. Click "Create New"
3. Give it a clear, descriptive title
4. Start writing your analysis using markdown

{% noteinfo "Start with a clear question" %}
Starting with a clear question or hypothesis helps focus your analysis and makes it easier to structure your notebook. It also makes it easier to share your findings with others later.
{% endnoteinfo %}

![A screenshot of the Notebooks overview tab, showing a list of notebooks](/docs/images/Notebooks-Overview.png)

### Adding Charts to Your Notebook

The easiest way to add charts is using the "Copy TQL" button:

1. Create your chart in the TelemetryDeck Dashboard
2. Click the "Actions" menu
3. Select "Copy TQL"
4. In your notebook, create a code block marked as `tql` and paste the query:

```markdown
```tql
{
  // Your chart's TQL query will be here
}
`` `
```

{% noteinfo "Live TQL Editing" %}
You can modify a query right in your notebook – it will update live. This makes it easy to experiment with different visualizations and parameters.
{% endnoteinfo %}

You can customize how your data is displayed using the `displayMode` value in your TQL:
- `lineChart` - Perfect for trends over time
- `barChart` - Great for categorical comparisons
- `pieChart` - Best for proportional data
- `table` - Ideal for detailed breakdowns
- `funnel` - Essential for conversion analysis

![A screenshot showing the markdown editor with TQL code, and the live chart preview in a notebook](/docs/images/Notebooks-TQL-Live-Preview.png)

### Using Markdown Effectively

Notebooks support all standard markdown features:

- **Headings** (`#`, `##`, etc.) – Structure your analysis into clear sections
- **Lists** (`-` or `1.`) – Break down steps, findings, or requirements
- **Code blocks** (```) – Share TQL queries or technical details
- **Images** (`![Alt text](image-url)`) – Add screenshots or diagrams
- **Blockquotes** (`>`) – Highlight important insights or tips
- **Tables** – Compare data or list requirements

{% noteinfo "Adding Images to Notebooks" %}
For images, upload them to a service like Imgur or imgbb and use standard markdown image syntax. This is great for adding screenshots, diagrams, or any visual aids to your analysis.
{% endnoteinfo %}

## Putting It All Together: A Real-World Example

Now that we've covered the basics, let's see how notebooks work in practice. We'll walk through an example of analyzing an app's onboarding flow, showing how notebooks help maintain context long-term.

### Setting Up the Analysis

1. **Define the Question**
   ```markdown
   # Onboarding Flow Analysis
   Question: How well does our app convert installations into paying customers?
   Hypothesis: The welcome window might be causing issues due to its similarity to Xcode's welcome screen.
   ```

2. **Create the Funnel Chart**
   - Use the dashboard to create a funnel chart
   - Click "Copy TQL" to get the query
   - Add it to your notebook with context:

   ```markdown
   ## User Journey Analysis
   Let's track the complete user journey from installation to first successful value delivery:
   
   <paste TQL here>
   ```

3. **Document Findings**
   ```markdown
   ## Initial Results
   - 80% of users proceed past welcome screen
   - 55% complete setup step ⚠️
   - 80% convert after setup
   
   Key Insight: Welcome window isn't the problem. The real bottleneck is the setup step.
   ```

4. **Plan Next Steps**
   ```markdown
   ## Next Investigation
   To understand why users drop off during setup, we need to track:
   - [ ] `Onboarding.SetupStep.started` - When users begin the setup process
   - [ ] `Onboarding.SetupStep.completed` - When users finish setup
   - [ ] `Onboarding.SetupStep.abandoned` - When users leave without completing
   - [ ] `Onboarding.SetupStep.duration` - How long users spend in setup
   ```

{% noteinfo "Preparing for Future Data" %}
You can already create insights using these parameters and copy their TQL into your notebook. When the tracking is implemented and data starts flowing, your charts will automatically update, letting you dive deeper immediately.
{% endnoteinfo %}

### Maintaining Context Over Time

The real power of notebooks becomes apparent during long-running investigations. As you wait for new data, your notebook serves as a living document that:

1. **Preserves Your Thinking** – Document your hypotheses/assumptions
2. **Tracks Progress** – Note what data you're waiting for and why
3. **Prepares for Analysis** – Set up charts that will show data when it arrives
4. **Shares Knowledge** – Help team members understand the context

This approach ensures you can pick up right where you left off when new data arrives, rather than starting from scratch.

## Common Use Cases

Notebooks excel in several scenarios:

**Performance Investigation**:
When tracking down issues, combine error logs with performance metrics in one place. Document your hypotheses, track implementation progress, and update findings as new data arrives.

**Team Communication**:
Create weekly product health reports or onboard new team members by showing your notebooks. The combination of live charts and explanatory text makes it easy to convey complex insights.

**Feature Analysis**:
Compare user behavior across versions or track feature adoption over time. Notebooks help you maintain context throughout the analysis, from initial hypothesis to final implementation.

**Long-Running Investigations**:
Perhaps most importantly, notebooks help you maintain momentum during investigations that span weeks or months. Document what you're waiting for, prepare your analysis structure, and dive back in as soon as new data arrives.

Ready to level up your analytics workflow? Open the Notebooks tab and start exploring your data in a more structured, insightful way now!

## Related Resources

<div class="not-prose">
  <div class="my-6 grid grid-cols-1 gap-6 sm:grid-cols-2">
    <div class="group relative rounded-xl border bg-white border-slate-200 flex">
      <div class="absolute -inset-px rounded-xl border-2 border-transparent opacity-0 [background:linear-gradient(var(--quick-links-hover-bg,theme(colors.mars.50)),var(--quick-links-hover-bg,theme(colors.mars.100)))_padding-box,linear-gradient(to_top,theme(colors.mars.400),theme(colors.mars.500))_border-box] group-hover:opacity-100"></div>
      <div class="shadow relative overflow-hidden rounded-xl p-6 h-full">
        <h2 class="font-semibold text-base text-mars-500">
          <a href="/docs/articles/insights">
            <span class="absolute -inset-px rounded-xl"></span>Understanding Insights</a>
        </h2>
        <p class="mt-1 text-sm text-slate-700">Learn how insights work and how to create effective visualizations for your notebooks.</p>
      </div>
    </div>
    <div class="group relative rounded-xl border bg-white border-slate-200 flex">
      <div class="absolute -inset-px rounded-xl border-2 border-transparent opacity-0 [background:linear-gradient(var(--quick-links-hover-bg,theme(colors.mars.50)),var(--quick-links-hover-bg,theme(colors.mars.100)))_padding-box,linear-gradient(to_top,theme(colors.mars.400),theme(colors.mars.500))_border-box] group-hover:opacity-100"></div>
      <div class="shadow relative overflow-hidden rounded-xl p-6 h-full">
        <h2 class="font-semibold text-base text-mars-500">
          <a href="/docs/tql/firstGuideline">
            <span class="absolute -inset-px rounded-xl"></span>TQL Query Language</a>
        </h2>
        <p class="mt-1 text-sm text-slate-700">Master the query language that powers notebook charts and enables advanced analytics.</p>
      </div>
    </div>
    <div class="group relative rounded-xl border bg-white border-slate-200 flex">
      <div class="absolute -inset-px rounded-xl border-2 border-transparent opacity-0 [background:linear-gradient(var(--quick-links-hover-bg,theme(colors.mars.50)),var(--quick-links-hover-bg,theme(colors.mars.100)))_padding-box,linear-gradient(to_top,theme(colors.mars.400),theme(colors.mars.500))_border-box] group-hover:opacity-100"></div>
      <div class="shadow relative overflow-hidden rounded-xl p-6 h-full">
        <h2 class="font-semibold text-base text-mars-500">
          <a href="/docs/articles/how-to-funnel-insights">
            <span class="absolute -inset-px rounded-xl"></span>Creating Funnel Charts</a>
        </h2>
        <p class="mt-1 text-sm text-slate-700">Learn how to track user conversion through multi-step processes – a key technique for notebook analyses.</p>
      </div>
    </div>
    <div class="group relative rounded-xl border bg-white border-slate-200 flex">
      <div class="absolute -inset-px rounded-xl border-2 border-transparent opacity-0 [background:linear-gradient(var(--quick-links-hover-bg,theme(colors.mars.50)),var(--quick-links-hover-bg,theme(colors.mars.100)))_padding-box,linear-gradient(to_top,theme(colors.mars.400),theme(colors.mars.500))_border-box] group-hover:opacity-100"></div>
      <div class="shadow relative overflow-hidden rounded-xl p-6 h-full">
        <h2 class="font-semibold text-base text-mars-500">
          <a href="/docs/guides/privacy-faq">
            <span class="absolute -inset-px rounded-xl"></span>Privacy FAQ</a>
        </h2>
        <p class="mt-1 text-sm text-slate-700">Understand how TelemetryDeck's privacy-first approach aligns with the data minimization strategy notebooks encourage.</p>
      </div>
    </div>
  </div>
</div>