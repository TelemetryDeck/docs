---
title: Deprecated Parameters
tags:
- deprecated parameters
---

## Introduction

Some parameters have been changed compared to earlier SDKs and others have been deleted. The following provides an overview of these two cases.

## Parameters

- These parameters have been replaced by other parameters:

**Name**: `buildNumber`</br>
**Type**: String</br>
**Description**: Has been replaced by `TelemetryDeck.AppInfo.buildNumber`.

**Name**: `dartVersion`</br>
**Type**: String</br>
**Description**: Has been replaced by `TelemetryDeck.AppInfo.dartVersion`.

**Name**: `appVersion`</br>
**Type**: String</br>
**Description**: Has been replaced by `TelemetryDeck.AppInfo.version`.

**Name**: `architecture`</br>
**Type**: String</br>
**Description**: Has been replaced by `TelemetryDeck.Device.architecture`.

**Name**: `brand`</br>
**Type**: String</br>
**Description**: Has been replaced by `TelemetryDeck.Device.brand`.

**Name**: `modelName`</br>
**Type**: String</br>
**Description**: Has been replaced by `TelemetryDeck.Device.modelName`.

**Name**: `operatingSystem`</br>
**Type**: String</br>
**Description**: Has been replaced by `TelemetryDeck.Device.operatingSystem`.

**Name**: `platform`</br>
**Type**: String</br>
**Description**: Has been replaced by `TelemetryDeck.Device.platform`.

**Name**: `majorSystemVersion`</br>
**Type**: String</br>
**Description**: Has been replaced by `TelemetryDeck.Device.systemMajorVersion`.

**Name**: `majorMinorSystemVersion`</br>
**Type**: String</br>
**Description**: Has been replaced by `TelemetryDeck.Device.systemMajorMinorVersion`.

**Name**: `systemVersion`</br>
**Type**: String</br>
**Description**: Has been replaced by `TelemetryDeck.Device.systemVersion`.

**Name**: `extensionIdentifier`</br>
**Type**: String</br>
**Description**: Has been replaced by `TelemetryDeck.RunContext.extensionIdentifier`.

**Name**: `isAppStore`</br>
**Type**: Bool</br>
**Description**: Has been replaced by `TelemetryDeck.RunContext.isAppStore`.

**Name**: `isDebug`</br>
**Type**: Bool</br>
**Description**: Has been replaced by `TelemetryDeck.RunContext.isDebug`.

**Name**: `isSimulator`</br>
**Type**: Bool</br>
**Description**: Has been replaced by `TelemetryDeck.RunContext.isSimulator`.

**Name**: `isTestFlight`</br>
**Type**: Bool</br>
**Description**: Has been replaced by `TelemetryDeck.RunContext.isTestFlight`.

**Name**: `locale`</br>
**Type**: String</br>
**Description**: Has been replaced by `TelemetryDeck.RunContext.locale`.

**Name**: `targetEnvironment`</br>
**Type**: String</br>
**Description**: Has been replaced by `TelemetryDeck.RunContext.targetEnvironment`.

**Name**: `telemetryClientVersion`</br>
**Type**: String</br>
**Description**: Has been replaced by `TelemetryDeck.SDK.nameAndVersion`.

**Name**: `NewSessionBegan`</br>
**Type**: String</br>
**Description**: Has been replaced by `TelemetryDeck.Session.started`.

**Name**: `newSessionBegan`</br>
**Type**: String</br>
**Description**: Has been replaced by `TelemetryDeck.Session.started`.

- The following parameters have been deleted as they were sending too many events:

**Name**: ActivityCreated</br>
**Type**: String</br>
**Description**: Has been deleted.

**Name**: ActivityDestroyed</br>
**Type**: String</br>
**Description**: Has been deleted.

**Name**: ActivityPaused</br>
**Type**: String</br>
**Description**: Has been deleted.

**Name**: ActivityResumed</br>
**Type**: String</br>
**Description**: Has been deleted.

**Name**: ActivitySaveInstanceState</br>
**Type**: String</br>
**Description**: Has been deleted.

**Name**: ActivityStarted</br>
**Type**: String</br>
**Description**: Has been deleted.

**Name**: ActivityStopped</br>
**Type**: String</br>
**Description**: Has been deleted.

**Name**: AppBackground</br>
**Type**: String</br>
**Description**: Has been deleted.

**Name**: AppForeground</br>
**Type**: String</br>
**Description**: Has been deleted.