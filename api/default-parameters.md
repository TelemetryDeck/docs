---
title: Default Parameters
description: A list of default parameters that our SDKs send with every signal.
lead: A list of default parameters that our SDKs send with every signal.
---

Most of TelemetryDeck's SDKs send a set of default parameters with every signal. These are not required to be sent by the user, but are useful. Our default UI will use them to provide more context. All of these parameters are namespaced under `TelemetryDeck` to avoid conflicts.

## Main Parameters

These parameters are sent with every signal and are currently not namespaced. Please avoid using them in your own code.

- `appID`: The ID of the app.
- `clientUser`: The ID of the user.
- `type`: The type of the signal.
- `receivedAt`: The date and time the signal was received by TelemetryDeck.
- `count`: The number of events sent with the signal (automatically incremented by the server)
- `isTestMode`: Whether the signal was sent in test mode.
- `sessionID`: The ID of the session.
- `floatValue`: A float value that can be sent with the signal.

## App Info

Information about the specific app build, such as version, build number, or SDKs compiled with.

- `TelemetryDeck.AppInfo.buildNumber`: The build number of the app.
- `TelemetryDeck.AppInfo.version`: The version of the app.
- `TelemetryDeck.AppInfo.versionAndBuildNumber`: The version and build number of the app, separated by a space.

## Device

Information about the device running the application, such as operating system, model name, or architecture.

- `TelemetryDeck.Device.architecture`: The architecture of the device.
- `TelemetryDeck.Device.modelName`: The model name of the device.
- `TelemetryDeck.Device.operatingSystem`: The operating system of the device.
- `TelemetryDeck.Device.orientation`: The orientation of the device.
- `TelemetryDeck.Device.platform`: The platform of the device.
- `TelemetryDeck.Device.screenResolutionHeight`: The height of the screen in points.
- `TelemetryDeck.Device.screenResolutionWidth`: The width of the screen in points.
- `TelemetryDeck.Device.screenScaleFactor`: The scale factor to calculate pixels from points (e.g. `2.0` for Retina).
- `TelemetryDeck.Device.systemMajorMinorVersion`: The major and minor version of the operating system.
- `TelemetryDeck.Device.systemMajorVersion`: The major version of the operating system.
- `TelemetryDeck.Device.systemVersion`: The version of the operating system.
- `TelemetryDeck.Device.timeZone`: The time zone of the device.
- `TelemetryDeck.Device.screenDensity`: The screen density of the device.
- `TelemetryDeck.Device.brand`: The brand of the device.

## Run Context

Information about the context the app runs in, such as whether it's running in a simulator, debug mode, or target environment.

- `TelemetryDeck.RunContext.isAppStore`: Whether the app is running in the App Store.
- `TelemetryDeck.RunContext.isDebug`: Whether the app is running in debug mode.
- `TelemetryDeck.RunContext.isSimulator`: Whether the app is running in a simulator.
- `TelemetryDeck.RunContext.isTestFlight`: Whether the app is running in TestFlight.
- `TelemetryDeck.RunContext.language`: The language of the app.
- `TelemetryDeck.RunContext.locale`: The locale of the app.
- `TelemetryDeck.RunContext.targetEnvironment`: The target environment of the app.
- `TelemetryDeck.RunContext.extensionIdentifier`: The identifier of the extension the app is running in. This provides a value such as `com.apple.widgetkit-extension` when TelemetryDeck is run from a widget.
- `TelemetryDeck.RunContext.isSideLoaded`: Whether the app is running as a side loaded app.
- `TelemetryDeck.RunContext.sourceMarketplace`: The source marketplace of the app.

## User Preference

Information about the user's preferences, such as language and region.

- `TelemetryDeck.UserPreference.colorScheme`: `Dark` or `Light`, depending on the user preference.
- `TelemetryDeck.UserPreference.language`: The language of the user.
- `TelemetryDeck.UserPreference.layoutDirection`: `leftToRight` or `rightToLeft`, based on user preference.
- `TelemetryDeck.UserPreference.region`: The region of the user.

## SDK

Information about the TelemetryDeck SDK, such as its name or version number.

- `TelemetryDeck.SDK.name`: The name of the SDK.
- `TelemetryDeck.SDK.nameAndVersion`: The name and version of the SDK, separated by a space.
- `TelemetryDeck.SDK.version`: The version of the SDK.
- `TelemetryDeck.SDK.buildType`: The build type of the SDK.

## Accessibility

Information about the user's accessibility device settings to help make apps more inclusive.

- `TelemetryDeck.Accessibility.isVoiceOverEnabled`: Whether VoiceOver is running.
- `TelemetryDeck.Accessibility.isReduceMotionEnabled`: Whether Reduce Motion is enabled.
- `TelemetryDeck.Accessibility.isBoldTextEnabled`: Whether Bold Text is enabled.
- `TelemetryDeck.Accessibility.isInvertColorsEnabled`: Whether Invert Colors is enabled.
- `TelemetryDeck.Accessibility.isDarkerSystemColorsEnabled`: Whether Darker System Colors are enabled.
- `TelemetryDeck.Accessibility.isReduceTransparencyEnabled`: Whether Reduce Transparency is enabled.
- `TelemetryDeck.Accessibility.shouldDifferentiateWithoutColor`: Whether UI should differentiate without color.
- `TelemetryDeck.Accessibility.preferredContentSizeCategory`: User's preferred text size category (e.g. `L`, `XXL`).
- `TelemetryDeck.Accessibility.isSwitchControlEnabled`: Whether Switch Control is running.

## API

Information about which TelemetryDeck API this signal was sent to .

- `TelemetryDeck.API.Ingest.version`: The Ingest API Version this signal was sent to. This will get overwritten by the ingest API server.

## Deprecated Parameters

These parameters are deprecated because they are not yet namespaced, and will be removed in a future release. All of them have replacements in some name spaces. See the [grand rename](/articles/grand-rename/) article for a mapping of the old names to the new ones.

- `platform`: The platform of the device.
- `systemVersion`: The version of the operating system.
- `majorSystemVersion`: The major version of the operating system.
- `majorMinorSystemVersion`: The major and minor version of the operating system.
- `appVersion`: The version of the app.
- `buildNumber`: The build number of the app.
- `isSimulator`: Whether the app is running in a simulator.
- `isDebug`: Whether the app is running in debug mode.
- `isTestFlight`: Whether the app is running in TestFlight.
- `isAppStore`: Whether the app is running in the App Store.
- `modelName`: The model name of the device.
- `architecture`: The architecture of the device.
- `operatingSystem`: The operating system of the device.
- `targetEnvironment`: The target environment of the app.
- `locale`: The locale of the app.
- `region`: The region of the user.
- `appLanguage`: The language of the app.
- `preferredLanguage`: The preferred language of the user.
- `telemetryClientVersion`: The version of the TelemetryDeck SDK.
- `telemetryAPIVersion`: The API Version this signal was sent to

## RevenueCat Parameters

Parameters related to RevenueCat.

- `RevenueCat.event.commission_percentage`
- `RevenueCat.event.price`
- `RevenueCat.event.price_in_purchased_currency`
- `RevenueCat.event.takehome_percentage`
- `RevenueCat.event.tax_percentage`

## Reserved Parameters

Reserved parameters are parameters that are reserved for internal or future use by TelemetryDeck and should not be used by customers.

- `TelemetryDeck.Presets.Onboarding.step`
- `TelemetryDeck.Metrics.Swift.applicationExitMetrics.backgroundExitData.cumulativeMemoryPressureExitCount`
- `TelemetryDeck.Metrics.Swift.applicationLaunchMetrics.histogrammedExtendedLaunch.histogramNumBuckets`
- `TelemetryDeck.Metrics.Swift.applicationLaunchMetrics.histogrammedOptimizedTimeToFirstDrawKey.histogramNumBuckets`
- `TelemetryDeck.Metrics.Swift.applicationLaunchMetrics.histogrammedResumeTime.histogramNumBuckets`
- `TelemetryDeck.Metrics.Swift.applicationLaunchMetrics.histogrammedTimeToFirstDrawKey.histogramNumBuckets`
- `TelemetryDeck.Metrics.Swift.applicationResponsivenessMetrics.histogrammedAppHangTime.histogramNumBuckets`
- `TelemetryDeck.Metrics.Swift.applicationResponsivenessMetrics.histogrammedAppHangTime.histogramValue.0.bucketCount`
- `TelemetryDeck.Metrics.Swift.applicationResponsivenessMetrics.histogrammedAppHangTime.histogramValue.0.bucketEnd.ms`
- `TelemetryDeck.Metrics.Swift.applicationResponsivenessMetrics.histogrammedAppHangTime.histogramValue.0.bucketStart.ms`
- `TelemetryDeck.Metrics.Swift.applicationResponsivenessMetrics.histogrammedAppHangTime.histogramValue.1.bucketCount`
- `TelemetryDeck.Metrics.Swift.applicationResponsivenessMetrics.histogrammedAppHangTime.histogramValue.1.bucketEnd.ms`
- `TelemetryDeck.Metrics.Swift.applicationResponsivenessMetrics.histogrammedAppHangTime.histogramValue.1.bucketStart.ms`
- `TelemetryDeck.Metrics.Swift.applicationTimeMetrics.cumulativeBackgroundAudioTime.sec`
- `TelemetryDeck.Metrics.Swift.applicationTimeMetrics.cumulativeBackgroundLocationTime.sec`
- `TelemetryDeck.Metrics.Swift.applicationTimeMetrics.cumulativeBackgroundTime.sec`
- `TelemetryDeck.Metrics.Swift.applicationTimeMetrics.cumulativeForegroundTime.sec`
- `TelemetryDeck.Metrics.Swift.cellularConditionMetrics.cellConditionTime.histogramNumBuckets`
- `TelemetryDeck.Metrics.Swift.cellularConditionMetrics.cellConditionTime.histogramValue.0.bucketCount`
- `TelemetryDeck.Metrics.Swift.cellularConditionMetrics.cellConditionTime.histogramValue.0.bucketEnd.bars`
- `TelemetryDeck.Metrics.Swift.cellularConditionMetrics.cellConditionTime.histogramValue.0.bucketStart.bars`
- `TelemetryDeck.Metrics.Swift.cellularConditionMetrics.cellConditionTime.histogramValue.1.bucketCount`
- `TelemetryDeck.Metrics.Swift.cellularConditionMetrics.cellConditionTime.histogramValue.1.bucketEnd.bars`
- `TelemetryDeck.Metrics.Swift.cellularConditionMetrics.cellConditionTime.histogramValue.1.bucketStart.bars`
- `TelemetryDeck.Metrics.Swift.cpuMetrics.cumulativeCPUInstructions.kiloinstructions`
- `TelemetryDeck.Metrics.Swift.cpuMetrics.cumulativeCPUTime.sec`
- `TelemetryDeck.Metrics.Swift.diskIOMetrics.cumulativeLogicalWrites.kB`
- `TelemetryDeck.Metrics.Swift.displayMetrics.averagePixelLuminance.averageValue.apl`
- `TelemetryDeck.Metrics.Swift.displayMetrics.averagePixelLuminance.sampleCount`
- `TelemetryDeck.Metrics.Swift.gpuMetrics.cumulativeGPUTime.sec`
- `TelemetryDeck.Metrics.Swift.locationActivityMetrics.cumulativeBestAccuracyForNavigationTime.sec`
- `TelemetryDeck.Metrics.Swift.locationActivityMetrics.cumulativeBestAccuracyTime.sec`
- `TelemetryDeck.Metrics.Swift.locationActivityMetrics.cumulativeHundredMetersAccuracyTime.sec`
- `TelemetryDeck.Metrics.Swift.locationActivityMetrics.cumulativeKilometerAccuracyTime.sec`
- `TelemetryDeck.Metrics.Swift.locationActivityMetrics.cumulativeNearestTenMetersAccuracyTime.sec`
- `TelemetryDeck.Metrics.Swift.locationActivityMetrics.cumulativeThreeKilometersAccuracyTime.sec`
- `TelemetryDeck.Metrics.Swift.memoryMetrics.averageSuspendedMemory.averageValue.kB`
- `TelemetryDeck.Metrics.Swift.memoryMetrics.averageSuspendedMemory.sampleCount`
- `TelemetryDeck.Metrics.Swift.memoryMetrics.peakMemoryUsage.kB`
- `TelemetryDeck.Metrics.Swift.metaData.pid`
- `TelemetryDeck.Metrics.Swift.networkTransferMetrics.cumulativeCellularDownload.kB`
- `TelemetryDeck.Metrics.Swift.networkTransferMetrics.cumulativeCellularUpload.kB`
- `TelemetryDeck.Metrics.Swift.networkTransferMetrics.cumulativeWifiDownload.kB`
- `TelemetryDeck.Metrics.Swift.networkTransferMetrics.cumulativeWifiUpload.kB`
- `TelemetryDeck.Metrics.Swift.displayMetrics.averagePixelLuminance.standardDeviation`
- `TelemetryDeck.Metrics.Swift.memoryMetrics.averageSuspendedMemory.standardDeviation`
