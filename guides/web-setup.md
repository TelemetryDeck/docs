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
<script
  src="https://cdn.telemetrydeck.com/websdk/telemetrydeck.min.js"
  data-app-id="<YOUR APP ID>"
></script>
```

💡 If you use Google Tag Manager, please see our separate guide on [how to include TelemetryDeck in your website using Google Tag Manager](/docs/integrations/web-setup-google-tag-manager/).

## Usage

You don't need to write any code to use TelemetryDeck. Once you've installed the package, TelemetryDeck will automatically send `pageView` events for every page load.

## Updating the Dashboard

If you like, you can switch your [TelemetryDeck Dashboard](https://dashboard.telemetrydeck.com/) to Website mode. To do that, navigate to the relevant app in the Dashboard, click **App Settings** in the sidebar, and change the **Overview Layout** to **Show Data for a blog or static website**.

## Test Mode

By default, all signals sent from `localhost` or an IP address in the [private IP address ranges](https://en.wikipedia.org/wiki/Private_network#Private_IPv4_address_spaces) are automatically marked as test signals. This is to prevent test signals from polluting your data.

It is also possible to mark all signals as test signals by setting the dataset attribute `data-is-test-mode` to `true`.

```html
<script
  src="https://cdn.telemetrydeck.com/websdk/telemetrydeck.min.js"
  data-app-id="<YOUR APP ID>"
  data-is-test-mode="true"
></script>
```

To see test signals, you can enable **Test Mode** in the Dashboard.

## Privacy Policy and Opt-Out

You don't need to update your privacy policy, [but we recommend you do it anyway](/docs/guides/privacy-faq/#do-i-need-to-add-telemetrydeck-to-my-privacy-policy%3F).

## What data is collected?

Signals automatically contain the following data, although various data points may be missing depending on the user's browser, privacy settings or network connection, or they might be not applicable.

### URL Data

- `url`: The URL of the page that was loaded
- `referrer`: The URL of the page that referred the user to this page
- `type`: The type of event. This is always `pageView` for page views.

### Origin and Country Data

- `locale`: The locale of the user, e.g. `en-US` or `de-DE`
- `country.isoCode`: The ISO code of the country the user is in, e.g. `US` or `DE`
- `country.isInEuropeanUnion`: Whether the user is in the European Union
- `continent.code`: The code of the continent the user is in, e.g. `EU` or `NA`

### Campaign and Referrer Data

- `utm_campaign`: The UTM campaign of the page, if any
- `utm_source`: The UTM source of the page, if any
- `utm_medium`: The UTM medium of the page, if any
- `utm_term`: The UTM term of the page, if any
- `utm_content`: The UTM content of the page, if any
- `source`: The source parameter of the page, if any
- `ref`: The ref parameter of the page, if any

### Browser and System Data

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

## User Identifiers

Our user identifiers are designed to be as privacy-friendly as possible. We do not use cookies or fingerprinting to track users. Instead, combine the IP Address, the App ID, and the User Agent string, and a daily-changing salt to create a unique identifier for each user. This identifier is then hashed using SHA-256 to protect the user's privacy.

This means that the Web SDK will recognize recurring users on the same day on the same website. However, it cannot recognize recurring users across different websites, or across different days. This is by design, to protect the user's privacy.

## If you're a developer

{% noteinfo "There are multiple ways of adding TelemetryDeck to a web site" %}

There are different tutorials you should read depending on your use case.

- If you are building a **JavaScript application or PWA using node package manager**, you should read the [Node Package Setup Guide](/docs/guides/javascript-setup).
- If you are building a **website or blog**, and want to include TelemetryDeck with a simple script tag similar to Google Analytics or Plausible Analytics, you should read this guide.

{% endnoteinfo %}

## Your Next Essential Step

Now that you've integrated TelemetryDeck, the most important thing to do is learn how to use the dashboard to gain valuable insights about your users:

<div class="not-prose ">
  <div class="my-10 grid grid-cols-1 gap-6">
    <div class="group relative rounded-xl border-2 border-mars-300 bg-white flex">
      <div class="absolute -inset-px rounded-xl border-2 border-transparent opacity-0 [background:linear-gradient(var(--quick-links-hover-bg,theme(colors.mars.50)),var(--quick-links-hover-bg,theme(colors.mars.100)))_padding-box,linear-gradient(to_top,theme(colors.mars.400),theme(colors.mars.500))_border-box] group-hover:opacity-100"></div>
      <div class="shadow relative overflow-hidden rounded-xl p-6 h-full">
        <h2 class="font-semibold text-lg text-mars-500">
          <a href="/docs/basics/index">
            <span class="absolute -inset-px rounded-xl"></span>📊 Complete Dashboard Guide</a>
        </h2>
        <p class="mt-2 text-sm text-slate-700">This essential guide walks you through the TelemetryDeck dashboard, showing you how to interpret your automatic insights, create custom analytics, track important user behavior, and make data-driven decisions to improve your app.</p>
        <p class="mt-4 text-sm text-mars-500 font-semibold flex justify-between">
          <span>Start here to get real value from your analytics</span>
          <span>→</span>
        </p>
      </div>
    </div>
  </div>
</div>
