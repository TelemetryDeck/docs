---
title: Run Context parameters
tags:
- app analytics
- run context
---

## Introduction

Run Context Parameters provide information about the context the app runs in, such as whether it's running in a simulator, debug mode, or target environment.

## Parameters

**Name**: `TelemetryDeck.RunContext.isAppStore`</br>
**Type**: Bool</br>
**Description**: Information whether the app is running in the App Store.

**Name**: `TelemetryDeck.RunContext.isDebug`</br>
**Type**: Bool</br>
**Description**: Information whether the app is running in debug mode.

**Name**: `TelemetryDeck.RunContext.isSimulator`</br>
**Type**: Bool</br>
**Description**: Information whether the app is running in a simulator.

**Name**: `TelemetryDeck.RunContext.isTestFlight`</br>
**Type**: Bool</br>
**Description**: Information whether the app is running in TestFlight.

**Name**: `TelemetryDeck.RunContext.language`</br>
**Type**: String</br>
**Description**: The language of the app.

**Name**: `TelemetryDeck.RunContext.locale`</br>
**Type**: String</br>
**Description**: The locale of the app.

**Name**: `TelemetryDeck.RunContext.targetEnvironment`</br>
**Type**: String</br>
**Description**: The target environment of the app.

**Name**: `TelemetryDeck.RunContext.extensionIdentifier`</br>
**Type**: String</br>
**Description**: The identifier of the extension the app is running in. This provides a value such as `com.apple.widgetkit-extension` when TelemetryDeck is run from a widget.

**Name**: `TelemetryDeck.RunContext.isSideLoaded`</br>
**Type**: Bool</br>
**Description**: Information whether the app is running as a side loaded app.

**Name**: `TelemetryDeck.RunContext.sourceMarketplace`</br>
**Type**: String</br>
**Description**: The source marketplace of the app.