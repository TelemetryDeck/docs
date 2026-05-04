---
title: Using Google Tag Manager to include TelemetryDeck in your website
tags:
  - JavaScript
  - Websites
  - Google Tag Manager
description: Learn how to include TelemetryDeck in your website using Google Tag Manager. This is a slightly different process than using the regular JavaScript snippet, so here's how to do it.
lead: You can use Google Tag Manager to include the TelemetryDeck Analytics tracking code in your website.
order: 250
searchEngineDescription: Learn how to include TelemetryDeck in your website using the Google Tag Manager (compared to the regular JavaScript snippet).
---

1. Navigate to "Add a new tag" in your Google Tag Manager account
2. Select "Choose a tag type to begin setup"
3. Select "Custom HTML" as the tag type
4. Paste the following code snippet into the HTML field, replacing `<YOUR APP ID>` with your actual App ID:

```html
<script>
  var script = document.createElement('script');
  script.defer = true;
  script.dataset.appId = "YOUR_APP_ID";
  script.src = "https://cdn.telemetrydeck.com/websdk/telemetrydeck.min.js";
  document.getElementsByTagName('head')[0].appendChild(script);
</script>
```
