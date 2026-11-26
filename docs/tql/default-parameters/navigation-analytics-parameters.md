---
title: Navigation Analytics Parameters
tags:
- app analytics
- web analytics
- navigational analytics
---

## Introduction

Navigation analytics events have certain parameters, which can be included in any event type. These are the available options:

## Parameters

**Name**: `TelemetryDeck.Navigation.schemaVersion`</br>
**Type**: String</br>
**Description**: The schema version of the navigation. Must be 1.

**Name**: `TelemetryDeck.Navigation.sourcePath`</br>
**Type**: String</br>
**Description**: The source path of the navigation, e.g. /host/info/about or app.settings.privacy.

**Name**: `TelemetryDeck.Navigation.destinationPath`</br>
**Type**: String</br>
**Description**: The destination path of the navigation, e.g. /host/info/about or app.settings.privacy.

**Name**: `TelemetryDeck.Navigation.identifier`</br>
**Type**: String</br>
**Description**: String that uniquely identifies the navigation in the format sourcePath -> destinationPath.