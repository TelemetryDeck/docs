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

## Web Analytics

Web analytics have their own sets of parameters that are usually determined by the web ingest api when you send events from the Web SDK. However, you can send these with any SDK and they will show up in the web analytics dashboard.

By default the web SDK will send signals of type `pageView` with the following parameters:

These parameters are currently not namespaced. Expect this to change in the future.

#### URL Data

- `url` (String): The URL of the page, e.g. `https://example.com/about`.
- `host` (String): The host portion of the URL, e.g. `example.com`.
- `path` (String): The path portion of the URL, e.g. `/about` or `/blog/my-post`.
- `scheme` (String): The scheme portion of the URL, e.g. `https`.
- `referer` (String): The referrer of the page, e.g. `https://example.com`.
- `TelemetryDeck.Navigation.identifier` (String): String that uniquely identifies the navigation in the format `referrer -> url`.

#### URL Parameters

TelemetryDeck will extract URL these URL parameters from the url and offer them as parameters attached to the signal:

- `combinedSource` (String): The value of either `ref`, `source`, `utm_source` or `src` in that order of preference.
- `ref`
- `source`
- `src`
- `utm_source`
- `utm_medium`
- `utm_campaign`
- `utm_term`
- `utm_content`
- `MSCLKID`
- `GCLID`

#### Country and Region Data

- `country.isoCode` (String): The [ISO 3166-1 alpha-2 country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the country, extracted from the origin IP address.
- `country.isInEuropeanUnion` (Bool): Whether the country is in the European Union, extracted from the origin IP address.
- `continent.code` (String): The code of the continent, extracted from the origin IP address. E.g. `EU`, `NA`, `SA`, `AS`, `AF`, `AN`.

#### User Agent Data

- `systemVersion` (String): The version of the operating system, extracted from the user agent string.
- `majorSystemVersion` (String): The major version of the operating system, extracted from the user agent string.
- `majorMinorSystemVersion` (String): The major and minor version of the operating system, extracted from the user agent string.
- `platform` (String): The platform of the device (macOS, iOS, Windows, etc.), extracted from the user agent string.
- `modelName` (String): The model name of the device, extracted from the user agent string.
- `browserName` (String): The browser family, extracted from the user agent string.
- `browserVersion` (String): The browser version, extracted from the user agent string.
- `device` (String): The type of device, extracted from the user agent string.
- `isMobile` (Bool): Whether the device is a mobile device, extracted from the user agent string.
- `isTablet` (Bool): Whether the device is a tablet, extracted from the user agent string.
- `isTouchCapable` (Bool): Whether the device is touch capable, extracted from the user agent string.
- `isDesktop` (Bool): Whether the device is a desktop, extracted from the user agent string.
- `isBot` (Bool): Whether the device is a bot, extracted from the user agent string and additional heuristics.

## Navigation Analytics

Navigation analytics signals have these parameters, which can be included in any signal type.

- `TelemetryDeck.Navigation.schemaVersion` (String): The schema version of the navigation. Must be `1`.
- `TelemetryDeck.Navigation.sourcePath` (String): The source path of the navigation, e.g. `/host/info/about` or `app.settings.privacy`.
- `TelemetryDeck.Navigation.destinationPath` (String): The destination path of the navigation, e.g. `/host/info/about` or `app.settings.privacy`.
- `TelemetryDeck.Navigation.identifier` (String): String that uniquely identifies the navigation in the format `sourcePath -> destinationPath`.

## Acquisition Analytics


- `TelemetryDeck.Calendar.dayOfMonth`: The day-of-month (1..31) component of the date.
- `TelemetryDeck.Calendar.dayOfWeek`: The ISO 8601 number of the given day of the week. Monday is 1, Sunday is 7.
- `TelemetryDeck.Calendar.dayOfYear`: The 1-based day-of-year component of the date.
- `TelemetryDeck.Calendar.weekOfYear`: The week number within the current year as defined by `getFirstDayOfWeek()` and `getMinimalDaysInFirstWeek()`.
- `TelemetryDeck.Calendar.isWeekend`: `true` if the day of the week is Saturday or Sunday, `false` otherwise.
- `TelemetryDeck.Calendar.monthOfYear`: The number-of-the-month (1..12) component of the date.
- `TelemetryDeck.Calendar.quarterOfYear`: The the quarter-of-year (1..4). For API 26 and earlier, it's the number of the month divided by 3.
- `TelemetryDeck.Calendar.hourOfDay`: The hour-of-day (0..23) time component of this time value.
- `TelemetryDeck.Acquisition.firstSessionDate`: The date of the first session e.g. 2025-02-22
- `TelemetryDeck.Retention.averageSessionSeconds`: The average session duration in seconds.
- `TelemetryDeck.Retention.distinctDaysUsed`: The number of distinct dates on which the app was used.
- `TelemetryDeck.Retention.totalSessionsCount`: The total number of sessions.
- `TelemetryDeck.Retention.previousSessionSeconds`: The duration of the previous session in seconds.
- `TelemetryDeck.Retention.distinctDaysUsedLastMonth`: The number of distinct dates on which the app was used in the last month.

## API

Information about which TelemetryDeck API this signal was sent to.

- `TelemetryDeck.API.Ingest.version` (String): The Ingest API Version this signal was sent to. This will get overwritten by the ingest API server.
- `TelemetryDeck.API.namespace` (String): The namespace in which to store your data. This usually gets set by the ingest API server when you call it via the `/v2/namespace/<namespace>/` endpoint.

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
