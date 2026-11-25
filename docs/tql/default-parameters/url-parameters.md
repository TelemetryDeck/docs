---
title: URL Parameters
tags:
- web analytics
- url
---

## Introduction

Web analytics have their own sets of parameters that are usually determined by the web ingest api when you send events from the Web SDK. However, you can send these with any SDK and they will show up in the web analytics dashboard.
By default the web SDK will send events of type pageView.

Following are parameters including the URL and information extracted from the URL. These parameters are currently not namespaced. Expect this to change in the future.

## Parameters

**Name**: `url`</br>
**Type**: String</br>
**Description**: The URL of the page, e.g. [https://example.com/about](https://example.com/about).

**Name**: `host`</br>
**Type**: String</br>
**Description**: The host portion of the URL, e.g. example.com.

**Name**: `path`</br>
**Type**: String</br>
**Description**: The path portion of the URL, e.g. /about or /blog/my-post.

**Name**: `scheme`</br>
**Type**: String</br>
**Description**: The scheme portion of the URL, e.g. https.

**Name**: `referer`</br>
**Type**: String</br>
**Description**: The referrer of the page, e.g. [https://example.com](https://example.com/).

**Name**: `TelemetryDeck.Navigation.identifier`</br>
**Type**: String</br>
**Description**: String that uniquely identifies the navigation in the format referrer -> url.

**Name**: `combinedSource`</br>
**Type**: String</br>
**Description**: The value of either ref, source, utm_source or src in that order of preference.

**Name**: `ref`</br>
**Type**: String</br>
**Description**: The value of the ref.

**Name**: `source`</br>
**Type**: String</br>
**Description**: The value of source.

**Name**: `utm_source`</br>
**Type**: String</br>
**Description**: The Urchin Tracking Module – Source.

**Name**: `src`</br>
**Type**: String</br>
**Description**: The value of src.

**Name**: `utm_medium`</br>
**Type**: String</br>
**Description**: The Urchin Tracking Module – Medium.

**Name**: `utm_campaign`</br>
**Type**: String</br>
**Description**: The Urchin Tracking Module – Campaign.

**Name**: `utm_term`</br>
**Type**: String</br>
**Description**: The Urchin Tracking Module – Term.

**Name**: `utm_content`</br>
**Type**: String</br>
**Description**: The Urchin Tracking Module – Content.

**Name**: `MSCLKID`</br>
**Type**: String</br>
**Description**: The Microsoft Click ID.

**Name**: `GCLID`</br>
**Type**: String</br>
**Description**: The Google Click Identifier.