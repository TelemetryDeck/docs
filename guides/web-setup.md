---
title: Web Setup Guide
tags:
  - Setup
  - JavaScript
  - Websites
featured: true
description: How to include the TelemetryDeck SDK in your website or blog
lead: You have an account, and you have an app ID. Now let's include the TelemetryClient Package in your website
order: 250
---

## Prerequisites

- You'll need access to your website's code to install this package. If you're using a CMS like WordPress, you'll need to be able to edit the theme files.
- You'll need a TelemetryDeck account. [Sign up for free](https://dashboard.telemetrydeck.com/registration/organization?source=websdk) if you don't have one yet.
- You'll need a TelemetryDeck App ID. [Create a new app](https://dashboard.telemetrydeck.com/apps/create) if you don't have one yet.

## Installation

Once you have your App ID, edit the source code of your website and add the following code snippet to the `<head>` section of every page, making sure to replace `<YOUR APP ID>` with your actual App ID:

```html
<script
  src="https://cdn.telemetrydeck.com/websdk/telemetrydeck.min.js"
  data-app-id="<YOUR APP ID>"
></script>
```

## Usage

You don't need to write any code to use TelemetryDeck. Once you've installed the package, TelemetryDeck will automatically send `pageView` events for every page load.

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
