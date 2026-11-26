---
title: API Parameters
tags:
- app analytics
- web analytics
---

## Introduction

API Parameters provide information about which TelemetryDeck API this signal was sent to.

## Parameters

**Name**: `TelemetryDeck.API.Ingest.version`</br>
**Type**: String</br>
**Description**: The Ingest API Version this signal was sent to. This will get overwritten by the ingest API server.

**Name**: `TelemetryDeck.API.namespace`</br>
**Type**: String</br>
**Description**: The namespace in which to store your data. This usually gets set by the ingest API server when you call it via the /v2/namespace// endpoint.