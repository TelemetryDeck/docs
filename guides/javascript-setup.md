---
title: JavaScript Setup Guide
tags:
  - Setup
  - JavaScript
  - Node
  - NPM
  - Websites
featured: true
description: How to include the TelemetryDeck SDK in Your JavaScript Application or website
lead: You have an account, and you have an app ID. Now let's include the TelemetryClient Package in your website or JS application.
order: 300
---

To get started with TelemetryDeck, you need to include the TelemetryClient Package in your website or JS application. You can do this in one of two ways:

- **With a simple script tag, similar to Google Analytics.** This is our recommended way to include the TelemetryClient Package into blogs and most websites.
- **Using an NPM package directly.** We recommend this for developers who know what an NPM package is and are writing more complex apps.

Be sure to also check out the [TelemetryDeck JavaScript SDK on GitHub](https://github.com/TelemetryDeck/JavaScriptSDK).

{% noteinfo "You need an App ID" %}

Every application and website registered to TelemetryDeck has its own unique ID that we use to assign incoming signals to the correct app. To get started, create a new app in the [TelemetryDeck Dashboard](https://dashboard.telemetrydeck.com) and copy its ID.
{% endnoteinfo %}

---

## Usage via Script tag

Include the following snippet inside the `<head>` of your HTML page:

```html
<script
  src="https://unpkg.com/@telemetrydeck/sdk/dist/telemetrydeck.min.js"
  defer
></script>
<script>
  // This will send a TelemetrDeck signal of type "pageLoad" every time the page loads
  // It will automatically include the current URL in the payload, as well as the user
  // agent string, platform, and locale.
  window.td = window.td || [];
  td.push(["app", YOUR_APP_ID], ["user", USER_IDENTIFIER], ["signal"]);
</script>
```

Please replace `YOUR_APP_ID` with the app ID you received from TelemetryDeck, and `USER_IDENTIFIER` with a user identifier. If you have none, consider `anonymous`.

<div class="alert alert-info" role="alert">
    In this example we do not get an individual <code>USER_IDENTIFIER</code> for each user. Theoretically, we could use the browser's 
    `userAgent` string as an identifier, which is not helpful for distinguishing users, but enough for some purposes.
    To distinguish between individual users, we'd either need a login function, or to generate a 
    UUID for each user and store that in a cookie, which is outside of the scope of this example. (Also note that you might have to 
    ask for the user's consent to store an identifier for them in a cookie.)
</div>

You can add as many signals as you need to track different interactions with your page. Once the page and script are fully loaded, signals will be sent immediately.

Here's how to send custom signals:

```js
// basic page load signal
td.push(["signal"]);

// with custom data
td.push(["signal", { route: "some/page/path" }]);
```

---

## Advanced usage as a Package for applications that use a bundler (like Webpack, Rollup, …)

After installing the package via NPM, use it like this:

```js
import { TelemetryDeck } from "@telemetrydeck/sdk";

const td = new TelemetryDeck({ app: YOUR_APP_ID, user: YOUR_USER_IDENTIFIER });

// Process any events that have been qeued up
// Queued signals do not contain a client side timestamp and will be timestamped
// on the server at the time of arrival. Consider adding a timestamp value to
// your payloads if you need to be able to correlate them.
const queuedEvents = [
  ["app", YOUR_APP_ID],
  ["user", YOUR_USER_IDENTIFIER],
  ["signal"],
  ["signal", { route: "some/page/path" }],
];
td.ingest(qeuedEvents);

// Basic signal
td.signal();

// Update app or user identifier
td.app(YOUR_NEW_APP_ID);
td.user(YOUR_NEW_USER_IDENTIFIER);

// Signal with custom payload
td.signal({
  route: "some/page/path",
});
```

Please replace `YOUR_APP_ID` with the app ID you received from TelemetryDeck. If you have any string that identifies your user, such as an email address, use it as `YOUR_USER_IDENTIFIER` – it will be cryptographically anonymized with a hash function.

If you want to pass optional parameters to the signal being sent, add them to the optional payload object.

---

## Optional: User Identifiers

TelemetryDeck can count users if you assign it a unique identifier for each user that doesn't change. This identifier can be any string that is unique to the user, such as their email address, or a randomly generated UUID.

Feel free to use personally identifiable information as the user identifier: We use a cryptographically secure double-hashing process on client and server to make sure the data that arrives at our servers is anonymized and can not be traced back to individual users via their identifiers. A user's identifier is hashed inside the library, and then salted+hashed again on arrival at the server. This way the data is anonymized as defined by the GDPR and you don't have to ask for user consent to process or store this data.

## Optional: Payload

You can optionally attach an object with string values to the signal. This will allow you to filter and aggregate signals by these values in the dashboard.
