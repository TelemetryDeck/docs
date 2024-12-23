---
title: Default Parameters
description: A list of default parameters that our SDKs send with every signal.
lead: A list of default parameters that our SDKs send with every signal.
---

Most of TelemetryDeck's SDKs send a set of default parameters with every signal. These are not required to be sent by the user, but are useful. Our default UI will use them to provide more context. All of these parameters are namespaced under `TelemetryDeck` to avoid conflicts.

## Main Parameters

These parameters are sent with every signal and are currently not namespaced. Please avoid using them in your own code.

- `appID` (String): The ID of the app.
- `clientUser` (String): The ID of the user.
- `type` (String): The type of the signal.
- `receivedAt` (Date): The date and time the signal was received by TelemetryDeck.
- `count` (Int): The number of events sent with the signal (automatically incremented by the server)
- `isTestMode` (Bool): Whether the signal was sent in test mode.
- `sessionID` (String): The ID of the session.
- `floatValue` (Double): A float value that can be sent with the signal.

## App Info

Information about the specific app build, such as version, build number, or SDKs compiled with.

- `TelemetryDeck.AppInfo.buildNumber` (String): The build number of the app.
- `TelemetryDeck.AppInfo.version` (String): The version of the app.
- `TelemetryDeck.AppInfo.versionAndBuildNumber` (String): The version and build number of the app, separated by a space.

## Device

Information about the device running the application, such as operating system, model name, or architecture.

- `TelemetryDeck.Device.architecture` (String): The architecture of the device.
- `TelemetryDeck.Device.modelName` (String): The model name of the device.
- `TelemetryDeck.Device.operatingSystem` (String): The operating system of the device.
- `TelemetryDeck.Device.orientation` (String): The orientation of the device.
- `TelemetryDeck.Device.platform` (String): The platform of the device.
- `TelemetryDeck.Device.screenResolutionHeight` (Double): The height of the screen in points.
- `TelemetryDeck.Device.screenResolutionWidth` (Double): The width of the screen in points.
- `TelemetryDeck.Device.screenScaleFactor` (Double): The scale factor to calculate pixels from points (e.g. `2.0` for Retina).
- `TelemetryDeck.Device.systemMajorMinorVersion` (String): The major and minor version of the operating system.
- `TelemetryDeck.Device.systemMajorVersion` (String): The major version of the operating system.
- `TelemetryDeck.Device.systemVersion` (String): The version of the operating system.
- `TelemetryDeck.Device.timeZone` (String): The time zone of the device.
- `TelemetryDeck.Device.screenDensity` (Double): The screen density of the device.
- `TelemetryDeck.Device.brand` (String): The brand of the device.

## Run Context

Information about the context the app runs in, such as whether it's running in a simulator, debug mode, or target environment.

- `TelemetryDeck.RunContext.isAppStore` (Bool): Whether the app is running in the App Store.
- `TelemetryDeck.RunContext.isDebug` (Bool): Whether the app is running in debug mode.
- `TelemetryDeck.RunContext.isSimulator` (Bool): Whether the app is running in a simulator.
- `TelemetryDeck.RunContext.isTestFlight` (Bool): Whether the app is running in TestFlight.
- `TelemetryDeck.RunContext.language` (String): The language of the app.
- `TelemetryDeck.RunContext.locale` (String): The locale of the app.
- `TelemetryDeck.RunContext.targetEnvironment` (String): The target environment of the app.
- `TelemetryDeck.RunContext.extensionIdentifier` (String): The identifier of the extension the app is running in. This provides a value such as `com.apple.widgetkit-extension` when TelemetryDeck is run from a widget.
- `TelemetryDeck.RunContext.isSideLoaded` (Bool): Whether the app is running as a side loaded app.
- `TelemetryDeck.RunContext.sourceMarketplace` (String): The source marketplace of the app.

## User Preference

Information about the user's preferences, such as language and region.

- `TelemetryDeck.UserPreference.colorScheme` (Enum): `Dark` or `Light`, depending on the user preference.
- `TelemetryDeck.UserPreference.language` (String): The language of the user.
- `TelemetryDeck.UserPreference.layoutDirection` (Enum): `leftToRight` or `rightToLeft`, based on user preference.
- `TelemetryDeck.UserPreference.region` (String): The region of the user.

## SDK

Information about the TelemetryDeck SDK, such as its name or version number.

- `TelemetryDeck.SDK.name` (String): The name of the SDK.
- `TelemetryDeck.SDK.nameAndVersion` (String): The name and version of the SDK, separated by a space.
- `TelemetryDeck.SDK.version` (String): The version of the SDK.
- `TelemetryDeck.SDK.buildType` (String): The build type of the SDK.

## Accessibility

Information about the user's accessibility device settings to help make apps more inclusive.

- `TelemetryDeck.Accessibility.isReduceMotionEnabled` (Bool): Whether Reduce Motion is enabled.
- `TelemetryDeck.Accessibility.isBoldTextEnabled` (Bool): Whether Bold Text is enabled.
- `TelemetryDeck.Accessibility.isInvertColorsEnabled` (Bool): Whether Invert Colors is enabled.
- `TelemetryDeck.Accessibility.isDarkerSystemColorsEnabled` (Bool): Whether Darker System Colors are enabled.
- `TelemetryDeck.Accessibility.isReduceTransparencyEnabled` (Bool): Whether Reduce Transparency is enabled.
- `TelemetryDeck.Accessibility.shouldDifferentiateWithoutColor` (Bool): Whether UI should differentiate without color.
- `TelemetryDeck.Accessibility.preferredContentSizeCategory` (String): User's preferred text size category (e.g. `L`, `XXL`).

## API

Information about which TelemetryDeck API this signal was sent to.

- `TelemetryDeck.API.Ingest.version` (String): The Ingest API Version this signal was sent to. This will get overwritten by the ingest API server.

## RevenueCat Parameters

Parameters related to RevenueCat.

- `RevenueCat.event.commission_percentage` (Double)
- `RevenueCat.event.price` (Double)
- `RevenueCat.event.price_in_purchased_currency` (Double)
- `RevenueCat.event.takehome_percentage` (Double)
- `RevenueCat.event.tax_percentage` (Double)

## Deprecated Parameters

These parameters are deprecated because they are not yet namespaced, and will be removed in a future release. All of them have replacements in some name spaces. See the [grand rename](/articles/grand-rename/) article for a mapping of the old names to the new ones.

- `platform` (String): The platform of the device.
- `systemVersion` (String): The version of the operating system.
- `majorSystemVersion` (String): The major version of the operating system.
- `majorMinorSystemVersion` (String): The major and minor version of the operating system.
- `appVersion` (String): The version of the app.
- `buildNumber` (String): The build number of the app.
- `isSimulator` (Bool): Whether the app is running in a simulator.
- `isDebug` (Bool): Whether the app is running in debug mode.
- `isTestFlight` (Bool): Whether the app is running in TestFlight.
- `isAppStore` (Bool): Whether the app is running in the App Store.
- `modelName` (String): The model name of the device.
- `architecture` (String): The architecture of the device.
- `operatingSystem` (String): The operating system of the device.
- `targetEnvironment` (String): The target environment of the app.
- `locale` (String): The locale of the app.
- `region` (String): The region of the user.
- `appLanguage` (String): The language of the app.
- `preferredLanguage` (String): The preferred language of the user.
- `telemetryClientVersion` (String): The version of the TelemetryDeck SDK.
- `telemetryAPIVersion` (String): The API Version this signal was sent to.

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
