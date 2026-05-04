---
title: Web Setup Guide
tags:
  - Setup
  - JavaScript
  - Websites
featured: true
description: How to include the TelemetryDeck SDK in your website or blog
lead: You have an account, and you have an app ID. Now let's include the TelemetryDeck Package in your website
order: 250
---

## Prerequisites

<!-- vale proselint.Cliches = NO -->

- You'll need access to your website's code to install this package. If you're using a CMS like WordPress, you'll need to be able to edit the theme files.
- You'll need a TelemetryDeck account. [Sign up for free](https://dashboard.telemetrydeck.com/register?source=websdk) if you don't have one yet.
- You'll need a TelemetryDeck App ID. [Create a new app](https://dashboard.telemetrydeck.com/apps/create) if you don't have one yet.

<!-- vale proselint.Cliches = YES -->

## Installation

Once you have your App ID, edit the source code of your website and add the following code snippet to the `<head>` section of every page, making sure to replace `<YOUR APP ID>` with your actual App ID:

```html
<script async
  src="https://cdn.telemetrydeck.com/websdk/telemetrydeck.min.js"
  data-app-id="<YOUR APP ID>"
></script>
```

💡 If you use Google Tag Manager, please see our separate guide on [how to include TelemetryDeck in your website using Google Tag Manager](/docs/integrations/web-setup-google-tag-manager/).

## Usage

You don't need to write any code to use TelemetryDeck. Once you've installed the package, TelemetryDeck will automatically send `pageView` events for every page load.

## Updating the Dashboard

If you like, you can switch your [TelemetryDeck Dashboard](https://dashboard.telemetrydeck.com/) to Website mode. To do that, navigate to the relevant app in the Dashboard, click **App Settings** in the sidebar, and change the **Overview Layout** to **Show Data for a blog or static website**.

## Options and parameters

### App ID `data-app-id` (Required)

### Test Mode `data-is-test-mode` (Optional)

By default, all events sent from `localhost` or an IP address in the [private IP address ranges](https://en.wikipedia.org/wiki/Private_network#Private_IPv4_address_spaces) are automatically marked as test events. This is to prevent test events from polluting your data.

It is also possible to mark all events as test events by setting the dataset attribute `data-is-test-mode` to `true`.

```html
<script async
  src="https://cdn.telemetrydeck.com/websdk/telemetrydeck.min.js"
  data-app-id="<YOUR APP ID>"
  data-is-test-mode="true"
></script>
```
To see test events, you can enable **Test Mode** in the Dashboard.

### Disable Engagement `data-page-engagement` (Optional)

If you don't want to collect `TelemetryDeck.Web.pageLeave` events and their metrics, you can disable them by passing `data-page-engagement="false"`:


```html
<script async
  src="https://cdn.telemetrydeck.com/websdk/telemetrydeck.min.js"
  data-app-id="<YOUR APP ID>"
  data-page-engagement="false"
></script>
```

### Custom Ingest Endpoint `data-api` (Optional)

Use the `data-api` parameter to point the Web SDK to a custom TelemetryDeck v3 ingest endpoint.

## Privacy Policy and Opt-Out

You don't need to update your privacy policy, [but we recommend you do it anyway](/docs/guides/privacy-faq/#do-i-need-to-add-telemetrydeck-to-my-privacy-policy%3F).

## What data is collected?

The TelemetryDeck Web SDK automatically sends two events per page per user to TelemetryDeck: `pageview` and `TelemetryDeck.Web.pageLeave`. 

### `pageview`

`pageview` events are fired when a page first loads and automatically contain the following data, although various data points may be missing depending on the user's browser, privacy settings or network connection, or they might be not applicable.

#### URL Data

- `url`: The URL of the page that was loaded
- `path`: The relative path of the page, i.e. the URL minus host and protocol
- `referrer`: The URL of the page that referred the user to this page
- `type`: The type of event. This is always `pageview` for page views.

#### Origin and Country Data

- `locale`: The locale of the user, e.g. `en-US` or `de-DE`
- `country.isoCode`: The ISO code of the country the user is in, e.g. `US` or `DE`
- `country.isInEuropeanUnion`: Whether the user is in the European Union
- `continent.code`: The code of the continent the user is in, e.g. `EU` or `NA`

#### Campaign and Referrer Data

- `utm_campaign`: The UTM campaign of the page, if any
- `utm_source`: The UTM source of the page, if any
- `utm_medium`: The UTM medium of the page, if any
- `utm_term`: The UTM term of the page, if any
- `utm_content`: The UTM content of the page, if any
- `source`: The source parameter of the page, if any
- `ref`: The ref parameter of the page, if any

#### Browser and System Data

- `systemVersion`: The version of the operating system the user is using
- `platform`: The platform the user is using, e.g. a Mac or an iPhone or an Android Phone
- `modelName`: The model name of the device the user is using, e.g. iPhone 12 Pro Max
- `browser`: The browser the user is using, e.g. Chrome or Safari
- `browserVersion`: The version of the browser the user is using
- `isMobile`: Whether the user is using a mobile device
- `isTablet`: Whether the user is using a tablet
- `isDesktop`: Whether the user is using a desktop computer
- `isTouchCapable`: Whether the user's device supports touch input
- `isBot`: Whether the user is a bot

### `TelemetryDeck.Web.pageLeave`

`TelemetryDeck.Web.pageLeave` events are fired the first time the page is hidden or unloaded: tab switch, tab close, navigation away, app switch on mobile. They do not fire again if the visitor returns to the tab. These events contain information about how much the visitor engaged with the page in question:

#### URL Data

- `url`: The URL of the page that was loaded
- `path`: The relative path of the page, i.e. the URL minus host and protocol
- `referrer`: The URL of the page that referred the user to this page
- `type`: The type of event, i.e. `TelemetryDeck.Web.pageLeave`

#### Engagement Data

- `TelemetryDeck.PageEngagement.scrollDepth`: A number between 0 and 100. The deepest point of the page that has been in the viewport, as a percentage of total page height. A page that fits in the viewport reports 100 without any scrolling.
- `TelemetryDeck.PageEngagement.scrollDepthMilestone`: String, one of "0", "25", "50", "75", "100": A quantified version of scroll depth for better clustering
- `TelemetryDeck.PageEngagement.engagedSeconds`: Number, whole seconds the page was visible in the foreground (i.e. only while the tab is visible, background time is excluded)

## User Identifiers

Our user identifiers are designed to be as privacy-friendly as possible. We do not use cookies or fingerprinting to track users. Instead, combine the IP Address, the App ID, and the User Agent string, and a daily-changing salt to create a unique identifier for each user. This identifier is then hashed using SHA-256 to protect the user's privacy.

This means that the Web SDK will recognize recurring users on the same day on the same website. However, it cannot recognize recurring users across different websites, or across different days. This is by design, to protect the user's privacy.

## If you're a developer

{% noteinfo "There are multiple ways of adding TelemetryDeck to a web site" %}

There are different tutorials you should read depending on your use case.

- If you are building a **JavaScript application or PWA using node package manager**, you should read the [Node Package Setup Guide](/docs/guides/javascript-setup).
- If you are building a **website or blog**, and want to include TelemetryDeck with a simple script tag similar to Google Analytics or Plausible Analytics, you should read this guide.

{% endnoteinfo %}

## What's new in 3.0

Web SDK 3.0, released on September 23, 2026, introduced these changes. If you use the Web SDK without pointing it at a custom API, none of these should be breaking changes:

- We updated the format that web events are sent to a more simplified format
- We are sending these new events to the new Web v3 API
- Events no longer contain the `telemetryClientVersion` property. Instead, the property is now named `TelemetryDeck.SDK.nameAndVersion`

## What to do next

Now that you've integrated TelemetryDeck, learn how to use the analytics platform to gain valuable insights about your users:

<div class="not-prose ">
  <div class="my-10 grid grid-cols-1 gap-6">
    <div class="group relative rounded-xl border-2 border-mars-300 bg-white flex">
      <div class="absolute -inset-px rounded-xl border-2 border-transparent opacity-0 [background:linear-gradient(var(--quick-links-hover-bg,theme(colors.mars.50)),var(--quick-links-hover-bg,theme(colors.mars.100)))_padding-box,linear-gradient(to_top,theme(colors.mars.400),theme(colors.mars.500))_border-box] group-hover:opacity-100"></div>
      <div class="shadow relative overflow-hidden rounded-xl p-6 h-full">
        <h2 class="font-semibold text-lg text-mars-500">
          <a href="/docs/basics/index">
            <span class="absolute -inset-px rounded-xl"></span>📊 Analytics Walkthrough</a>
        </h2>
        <p class="mt-2 text-sm text-slate-700">Learn how to navigate TelemetryDeck, interpret insights, and use analytics to make data-driven decisions that improve your app and grow your user base.</p>
        <p class="mt-4 text-sm text-mars-500 font-semibold flex justify-between">
          <span>Start here to get real value from your analytics</span>
          <span>→</span>
        </p>
      </div>
    </div>
  </div>
</div>
