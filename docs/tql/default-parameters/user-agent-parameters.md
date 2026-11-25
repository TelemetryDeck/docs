---
title: User Agent Parameters
tags:
- web analytics
- user agent
---

## Introduction

Web analytics have their own sets of parameters that are usually determined by the web ingest api when you send events from the Web SDK. However, you can send these with any SDK and they will show up in the web analytics dashboard.
By default the web SDK will send events of type pageView.

Following are parameters with data extracted from user agent string. These parameters are currently not namespaced. Expect this to change in the future.

## Parameters

**Name**: `systemVersion`</br>
**Type**: String</br>
**Description**: The version of the operating system.

**Name**: `majorSystemVersion`</br>
**Type**: String</br>
**Description**: The major version of the operating system.

**Name**: `majorMinorSystemVersion`</br>
**Type**: String</br>
**Description**: The major and minor version of the operating system.

**Name**: `platform`</br>
**Type**: String</br>
**Description**: The platform of the device (macOS, iOS, Windows, etc.).

**Name**: `modelName`</br>
**Type**: String</br>
**Description**: The model name of the device.

**Name**: `browser`</br>
**Type**: String</br>
**Description**: The browser family.

**Name**: `browserVersion`</br>
**Type**: String</br>
**Description**: The browser version.

**Name**: `device`</br>
**Type**: String</br>
**Description**: The type of device.

**Name**: `isMobile`</br>
**Type**: Bool</br>
**Description**: Information whether the device is a mobile device.

**Name**: `isTablet`</br>
**Type**: Bool</br>
**Description**: Information whether the device is a tablet.

**Name**: `isTouchCapable`</br>
**Type**: Bool</br>
**Description**: Information whether the device is touch capable.

**Name**: `isDesktop`</br>
**Type**: Bool</br>
**Description**: Information whether the device is a desktop.

**Name**: `isBot`</br>
**Type**: Bool</br>
**Description**: Information whether the device is a bot, extracted from the user agent string and additional heuristics.