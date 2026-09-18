---
icon: fontawesome/brands/vuejs
title: Vue.js Setup Guide
tags:
  - setup
  - javascript
  - node
  - npm
  - typescript
  - vue
  - vuejs
---

## Prerequisites

<!-- vale proselint.Cliches = NO -->

- You'll need a TelemetryDeck account. [Sign up for free](https://dashboard.telemetrydeck.com/register?source=websdk) if you don't have one yet.
- You'll need a TelemetryDeck App ID. [Create a new app](https://dashboard.telemetrydeck.com/apps/create) if you don't have one yet.
<!-- vale proselint.Cliches = YES -->

## Installation

```shell
npm i @peerigon/telemetrydeck-vue --save
```

## Setup

Set up the plugin in your application setup:

```javascript
import TelemetryDeckPlugin from "@peerigon/telemetrydeck-vue";

const app = createApp(App);
app.use(TelemetryDeckPlugin, {
  appID: "{your telemetrydeck appID}",
  testMode: true, // optional - defaults to false
  clientUser: "Guest", // optional - defaults to 'Guest'
});

app.mount("#app");
```

## Basic usage

```ts
<script setup lang="ts">
import { useTelemetryDeck } from "@peerigon/telemetrydeck-vue";
const { signal, queue, setClientUser } = useTelemetryDeck();

const changeClientUserClick = () => {
  setClientUser("user" + Math.floor(Math.random() * 1000));
};

const buttonSignalClick = () => {
  signal("example_signal_event_name", {
    custom_data: "other_data", // any custom data as required
  });
};

const buttonQueueClick = () => {
  queue("example_queue_event_name", {
    custom_data: "other_data", // any custom data as required
  });
};

const buttonSignalClickWithOptions = () => {
  signal(
    "example_signal_event_name_with_options",
    {
      custom_data: "other_data", // any custom data as required
    },
    {
      testMode: true,
      clientUser: "other_user",
      appID: "other_app_id",
    },
  ); // telemetryDeck options (optional)
};

const buttonQueueClickWithOptions = () => {
  queue(
    "example_queue_event_name_with_options",
    {
      custom_data: "other_data", // any custom data as required
    },
    {
      testMode: true,
      clientUser: "other_user",
      appID: "other_app_id",
    },
  ); // telemetryDeck options (optional)
};
</script>

<template>
  <div>
    <div>
      <button id="btnSignalClick" @click="buttonSignalClick">
        Log a click with signal
      </button>
      <button id="btnQueueClick" @click="buttonQueueClick">
        Log a click with queue
      </button>
      <button id="btnSetClient" @click="changeClientUserClick">
        Change user
      </button>
    </div>
    <div>
      <button
        id="btnSignalClickWithOptions"
        @click="buttonSignalClickWithOptions"
      >
        Log a click with signal with Options
      </button>
      <button
        id="btnQueueClickWithOptions"
        @click="buttonQueueClickWithOptions"
      >
        Log a click with queue with Options
      </button>
    </div>
  </div>
</template>
```

## What to do next

Now that you've integrated TelemetryDeck, learn how to use the analytics platform to gain valuable insights about your users:

<div class="grid cards" markdown>

-   **📊 Analytics Walkthrough**

    Learn how to navigate TelemetryDeck, interpret insights, and use analytics to make data-driven decisions that improve your app and grow your user base.

    [:fontawesome-solid-right-long: Start here to get real value from your analytics](../basics/index.md)
</div>

## Sponsors

[<img src="/assets/Peerigon_Logo_RGB_no_padding.svg" width=300 class="p-3 bg-white" />](https://www.peerigon.com)

The development of the TelemetryDeck Vue SDK was graciously provided by our friends at Augsburg-based bespoke software development company [Peerigon](https://www.peerigon.com). Thanks a lot, and check them out for your application development needs. 🧡

[Follow the development on GitHub](https://github.com/peerigon/telemetrydeck-vue)
