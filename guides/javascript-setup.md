---
title: JavaScript App Setup Guide
tags:
  - Setup
  - JavaScript
  - Node
  - NPM
  - TypeScript
featured: true
description: How to include the TelemetryDeck SDK in Your JavaScript Application or Web App
lead: You have an account, and you have an app ID. Now let's include the TelemetryClient Package in your JS application or web app
order: 300
---

The TelemetryDeck SDK has no dependencies and supports **modern evergreen browsers** and **modern versions of Node.js** with support for [cryptography](https://caniuse.com/cryptography).

{% noteinfo "There are multiple ways of adding TelemetryDeck to a web site" %}

There are different tutorials you should read depending on your use case.

- The [TelemetryDeck Web SDK](/docs/guides/web-setup) is a quick and easy way to include web analytics into your website. This is fantastic for blogs, landing pages, static websites, and content-driven websites.

- If you are building a JavaScript application – a Progressive Web App written in React, Vue, Angular, Svelte, Ember, or mobile or desktop apps written with React Native, Electron, Ionic, and so on, you should read this guide.

[Our blog post](/blog/js-sdk-2-0/) explains the differences between the two SDKs in more detail.

{% endnoteinfo %}

## Set Up

When setting up, you need to check wether the platform you're working on has the SubtleCrytpo API available.

Anytime you're in a browser context, your code will have access to the default SubtleCrypto implementation. If you're in Node.js on a server, or in a React Native app, you need to pass in an alternative implementation of the SubtleCrypto API.

The next two sections explain these two cases in detail. Either way, please install the package using npm or the package manager of your choice, such as NPM.

### Set up in Browser Based Applications

This is the correct setup procedure for JavaScript code that runs in a browser and can install an NPM package. For example:

- React
- Vue
- Angular
- Svelte
- Ember
- Probably your favorite framework

Initialize the TelemetryDeck SDK with your app ID and your user's user identifer.

```javascript
import TelemetryDeck from '@telemetrydeck/sdk';

const td = new TelemetryDeck({
  appID: '<YOUR_APP_ID>'
  user: '<YOUR_USER_IDENTIFIER>',
});
```

Please replace `<YOUR_APP_ID>` with the app ID in TelemetryDeck ([Dashboard](https://dashboard.telemetrydeck.com) -> App -> Set Up App).

You also need to identify your logged in user. Instead of `<YOUR_USER_IDENTIFIER>`, pass in any string that uniquely identifies your user, such as an email address. It will be cryptographically anonymized with a hash function.

If can't specify a user identifer at initialization, you can set it later by setting `td.clientUser`.

Please note that `td.signal` is an async function that returns a promise.

### Set up in Node.js Applications

Initialize the TelemetryDeck SDK with your app ID and your user's user identifer. Since `globalThis.crypto.subtle` does not exist in Node.js, you need to pass in an alternative implementation provided by Node.js.

```javascript
import TelemetryDeck from '@telemetrydeck/sdk';
import crypto from 'crypto';

const td = new TelemetryDeck({
  appID: '<YOUR_APP_ID>'
  user: '<YOUR_USER_IDENTIFIER>',
  subtleCrypto: crypto.webcrypto.subtle,
});
```

Please replace `<YOUR_APP_ID>` with the app ID in TelemetryDeck ([Dashboard](https://dashboard.telemetrydeck.com) -> App -> Set Up App).

You also need to identify your logged in user. Instead of `<YOUR_USER_IDENTIFIER>`, pass in any string that uniquely identifies your user, such as an email address. It will be cryptographically anonymized with a hash function.

If can't specify a user identifer at initialization, you can set it later by setting `td.clientUser`.

Please note that `td.signal` is an async function that returns a promise.

### Advanced Initalization Options

See the [source code](https://github.com/TelemetryDeck/JavaScriptSDK/blob/main/src/telemetrydeck.js#L6-L17) for a full list of availble options acepted by the `TelemetryDeck` constructor.

## Sending Signals

Send a basic signal by calling `td.signal()` with a signal type:

```javascript
td.signal("<SIGNAL_TYPE>");
```

Send a signal with a custom payload by passing an object as the second argument. The payload's values will be [converted to Strings](./src/tests/store.test.js.js#L278-L310), except for `floatValue`, which can be a Float.

```javascript
td.signal("Volume.Set", {
  band: "Spinal Tap",
  floatValue: 11.0,
});
```

## Privacy Policy and Opt-Out

You don't need to update your privacy policy, [but we recommend you do it anyway](/docs/guides/privacy-faq/#do-i-need-to-add-telemetrydeck-to-my-privacy-policy%3F).

## Advanced: Queueing Signals

The `TelemetryDeck` class comes with a built-in queuing mechanism for storing signals until they are flushed in a single request. Queued signals are sent with `receivedAt` prefilled with the time they were queued.

Queueing signals can be helpful in situations where you're battery- or network-constrained and want to be mindful of the user's available resources. For example, a mobile app might want to queue signals while the user is offline and flush them when the user is back online.

To queue signals instead of sending them immediately, please use `td.queue()` instead of `td.signal()`, with the same arguments.

```javascript
td.queue("Band.Setup", {
  band: "Spinal Tap",
});

td.queue("Volume.Set", {
  band: "Spinal Tap",
  floatValue: 11.0,
});

td.queue("Concert.Begin");

// Send all queued signals in a single request
td.flush();
```

This uses an in-memory store by default. The store is not persisted between page reloads or app restarts. If you want to persist the store, you can pass a `store` object to the `TelemetryDeck` constructor. The store must implement the following interface:

```javascript
export class Store {
  async push() // signal bodys are async and need to be awaited before stored
  clear() // called after flush
  values() // returns an array of resolved signal bodys in the order they were pushed
}
```

The default implementation can be found in `src/utils/store.js`.

---

[TelemetryDeck](https://telemetrydeck.com?source=github) helps you build better products with live usage data. Try it out for free.
