---
icon: lucide/plug
tags:
    - Get started
    - Setup
---

!!! warning

    This is a test for a new documentation system. Trust nothing and no one. The original TelemetryDeck 
    documentation still lives at https://telemetrydeck.com/docs/ for now.


---

# Get Started

TelemetryDeck helps you understand how users interact with your application through privacy-focused analytics. With just an SDK integration, you'll get valuable insights automatically – no complex configuration required.

_You can find all our supported SDKs [here](guides/sdk-setup/index.md)._

## Installation

TelemetryDeck is a SaaS solution for privacy-focused analytics. We provide you with out-of-the-box charts and insights, while maintaining your users privacy at all times.

!!! note "Prerequisites"
    Create an account with TelemetryDeck [here](https://dashboard.telemetrydeck.com/login).

!!! tip "How we handle user data with double hashing"
    Our SDKs accept a custom user identifier – like an email or an internal identifier – which we double hash, once on the user's device and once on our servers. Read more [here](articles/anonymization-how-it-works.md).
    

### Install an SDK in 2 steps


1. **Choose and install** the SDK for your platform.
2. **Deploy your app** to start collecting data

Once your updated app is in users' hands, TelemetryDeck will begin collecting data. It may take some time before you see meaningful insights, depending on your app's usage.

### What's next after setup?

After setting up the SDK and deploying your app, your most important next step is to learn how to use the dashboard to analyze your data:

<div class="grid cards" markdown>

-   :material-chart-bar:{ .lg .middle } __Analytics Walkthrough__

    ---

    Learn how to navigate TelemetryDeck, interpret `insights`,
    and use analytics to make `data-driven decisions` that improve your app
    and grow your user base.

    [:octicons-arrow-right-24: Getting started](/basics)

-   :material-test-tube:{ .lg .middle } __Testmode__

    ---

    Test Mode helps you make sure that TelemetryDeck is set up `correctly` in your app
    and allows you to set up your `insights even during development`.

    [:octicons-arrow-right-24: Getting started](/articles/test-mode.md)
</div>


### Documentation Feedback

If you find an error or feel like the documentation could be improved somewhat, we'd love 
to hear from you! Either directly submit a change request with the buttons on each page, 
or open an issue in our <a href="https://github.com/TelemetryDeck/docs">Docs GitHub Repository</a>.

The [documentation guide](/articles/documentation) explains all markdown and 
additional features you can use while writing documentation for TelemetryDeck.