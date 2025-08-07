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

## Getting started with Notebooks

Notebooks are your analytics lab notebook – a place where you can document your findings, share insights with your team, and maintain context throughout your investigations. Let's explore how to use them effectively.

{% noteinfo "See Notebooks in action" %}
[![Notebooks Feature Demo - Learn how to combine live charts with markdown text for better analytics insights](/docs/images/notebooks-video-thumbnail.png)](https://www.youtube.com/watch?v=WAa2BRIaVGE)

*Watch the [Notebooks Walkthrough](https://www.youtube.com/watch?v=WAa2BRIaVGE) on our YouTube channel*
{% endnoteinfo %}

### Creating your first notebook

1. Open the Notebooks tab in your TelemetryDeck dashboard
2. Click "Create New"
3. Give it a clear, descriptive title
4. Start writing your analysis using markdown

{% noteinfo "Start with a clear question" %}
Starting with a clear question or hypothesis helps focus your analysis and makes it easier to structure your notebook. It also makes it easier to share your findings with others later.
{% endnoteinfo %}

![A screenshot of the Notebooks overview tab, showing a list of notebooks](/docs/images/Notebooks-Overview.png)

### Adding charts to your notebook

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

### Using Markdown effectively

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

## Sharing your findings: Public Snapshots

Notebooks can be published as public snapshots – shareable reference documents that preserve your findings exactly as they were when you published them.

### How it works

When you publish a notebook, TelemetryDeck creates a **snapshot** that freezes your data at that moment:

1. Click "Publish Snapshot" to make your notebook publicly accessible
2. All TQL queries are processed and results saved into the snapshot
3. Data is frozen – charts show exactly what you saw at publish time
4. You get a unique, private URL that only people with the link can access

{% noteinfo "Private by design" %}
Published snapshots use UUIDs in their URLs and aren't indexed by search engines. Only people you share the link with can access your notebook.
{% endnoteinfo %}

### Publishing workflow

- **First publish**: Click "Publish Snapshot" to create your public version
- **Updates**: Button changes to "Update Snapshot" – creates fresh data and replaces the old snapshot
- **Managing**: Use the link icon to visit your public page, "Copy Public Link" to share, or "Unpublish" to remove access
- **Mulitple versions**: Simply "Duplicate" your notebook if to keep the old published analysis and publish the new one when it's ready

### Why snapshots matter

Freezing data ensures your written insights stay meaningful over time. When you reference specific numbers in your analysis, they'll always match the charts – perfect for:

- **Team documentation** that won't become outdated
- **Task requirements** and project briefs with reliable data context
- **Client reports** with consistent, reliable data  
- **Reference materials** for future investigations
- **Articles or presentations** where data accuracy matters

{% noteinfo "Live vs. Snapshot Data" %}
Your private notebook editor always shows live, real-time data for ongoing analysis. The public snapshot preserves a point-in-time view for sharing. This gives you both current data for investigation and stable data for communication.
{% endnoteinfo %}

## Putting it all together: a real-world example

Now that we've covered the basics, let's see how notebooks work in practice. We'll walk through an example of analyzing an app's Onboarding flow, showing how notebooks help maintain context long-term.

### Setting up the analysis

1. **Define the Question**
   ```markdown
   # Onboarding flow analysis
   Question: How well does our app convert installations into paying customers?
   Hypothesis: The welcome window might be causing issues due to its similarity to Xcode's welcome screen.
   ```

2. **Create the Funnel Chart**
   - Use the dashboard to create a funnel chart
   - Click "Copy TQL" to get the query
   - Add it to your notebook with context:

   ```markdown
   ## User journey analysis
   Let's track the complete user journey from installation to first successful value delivery:
   
   <paste TQL here>
   ```

3. **Document Findings**
   ```markdown
   ## Initial results
   - 80% of users proceed past welcome screen
   - 55% complete setup step ⚠️
   - 80% convert after setup
   
   Key Insight: Welcome window isn't the problem. The real bottleneck is the setup step.
   ```

4. **Plan Next Steps**
   ```markdown
   ## Next investigation
   To understand why users drop off during setup, we need to track:
   - [ ] `Onboarding.SetupStep.started` - When users begin the setup process
   - [ ] `Onboarding.SetupStep.completed` - When users finish setup
   - [ ] `Onboarding.SetupStep.abandoned` - When users leave without completing
   - [ ] `Onboarding.SetupStep.duration` - How long users spend in setup
   ```

{% noteinfo "Preparing for Future Data" %}
You can already create insights using these parameters and copy their TQL into your notebook. When the tracking is implemented and data starts flowing, your charts will automatically update, letting you dive deeper immediately.
{% endnoteinfo %}

### Maintaining context over time

The real power of notebooks becomes apparent during long-running investigations. As you wait for new data, your notebook serves as a living document that:

1. **Preserves Your Thinking** – Document your hypotheses/assumptions
2. **Tracks Progress** – Note what data you're waiting for and why
3. **Prepares for Analysis** – Set up charts that will show data when it arrives
4. **Shares Knowledge** – Help team members understand the context

This approach ensures you can pick up right where you left off when new data arrives, rather than starting from scratch.

## Common use cases

Notebooks excel in several scenarios:

**Performance Investigation**:
When tracking down issues, combine error logs with performance metrics in one place. Document your hypotheses, track implementation progress, and update findings as new data arrives.

**Team Communication**:
Create weekly product health reports or onboard new team members by showing your notebooks. The combination of live charts and explanatory text makes it easy to convey complex insights.

**Feature Analysis**:
Compare user behavior across versions or track feature adoption over time. Notebooks help you maintain context throughout the analysis, from initial hypothesis to final implementation.

**Long-Running Investigations**:
Perhaps most importantly, notebooks help you maintain momentum during investigations that span weeks or months. Document what you're waiting for, prepare your analysis structure, and dive back in as soon as new data arrives.

Ready to level up your analytics workflow? Open the Notebooks tab and start exploring your data in a more structured, insightful way – and share your discoveries with confidence!

## Related resources

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