---
title: Country & Region Parameters
tags:
- web analytics
- country and region
---

## Introduction

Web analytics have their own sets of parameters that are usually determined by the web ingest api when you send events from the Web SDK. However, you can send these with any SDK and they will show up in the web analytics dashboard.
By default the web SDK will send events of type pageView.

Following are parameters with information regarding country and / or region of users available for web analytics. These parameters are currently not namespaced. Expect this to change in the future.

## Parameters

**Name**: `country.isoCode`</br>
**Type**: String</br>
**Description**: The ISO 3166-1 alpha-2 country code of the country, extracted from the origin IP address.

**Name**: `country.isInEuropeanUnion`</br>
**Type**: Bool</br>
**Description**: Information whether the country is in the European Union, extracted from the origin IP address.

**Name**: `continent.code`</br>
**Type**: String</br>
**Description**: The code of the continent, extracted from the origin IP address. E.g. EU, NA, SA, AS, AF, AN.