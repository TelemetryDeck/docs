---
title: Main Parameters
tags:
- app analytics
- web analytics
---

## Introduction

The Main Parameters are sent with every event. They are currently not namespaced, please avoid using them in your own code.

## Parameters

**Name**: `appID`</br>
**Type**: String</br>
**Description**: The ID of the app in TelemetryDeck. This is used to access the data of one particular app and not the whole organization. The required pattern for that is the ‘baseFilters’ must be ‘thisApp’ and the appID be inserted in the field ‘appID’.

**Name**: `clientUser`</br>
**Type**: String</br>
**Description**: The ID of the user. This is used oftentimes to aggregate users via the thetaSketch algorhithm used in the userCount aggregator. But filtering for a specific userID to check the activity of a particular user is also possible (however, as data is anonymized it is not known who that user is).

**Name**: `type`</br>
**Type**: String</br>
**Description**: The type of the event. This allows to filter or aggregate for specific events, for example ‘TelemetryDeck.Acquisition.newInstallDetected’ to only get information for new users.

**Name**: `__time`</br>
**Type**: Date</br>
**Description**: The date and time the signal was received by TelemetryDeck, which allows to set different granularities and to track trends over time.

**Name**: `count`</br>
**Type**: Int</br>
**Description**: The number of events sent with the signal (automatically incremented by the server). This means if an identical signal is received multiple times the count is incremented instead of adding an additional line to the database. For that reason, the longSum aggregator on the count field should usually be used rather than the count aggregator, which simply counts the number of lines in the database.

**Name**: `isTestMode`</br>
**Type**: Bool</br>
**Description**: Provides information whether the signal was sent in test mode.

**Name**: `sessionID`</br>
**Type**: String</br>
**Description**: The ID of the session. The fact that each session get its own ID allows for the thetaSketch-aggregator to be used for counting the amount of sessions ( i.e. ‘fieldName’ = ‘sessionID’, ‘name’: ‘Session Count’, ‘type’: ‘thetaSketch’).

**Name**: floatValue</br>
**Type**: Double</br>
**Description**: A float value that can be sent with the signal. This is a reserved field within every event for numerical values, which may not be used though. It depends on the way customers use this option when integrating TelemetryDeck.