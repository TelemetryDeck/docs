# Signal Spec

!!! warning

    This specification is outdated and needs to be updated

As TelemetryDeck is an analytics software, it analyzes events that occur in your apps' life cycles. In TelemetryDeck,
these events are called *Signals*. You can think about them like this: An **event** occurs, prompting your app to
send a **signal** to the TelemetryDeck server. Through aggregation and statistical analysis, your 
[Insights](insights-reference.html) can then extract meaningful data out of the set of signals you have received. 

Here is an example signal: 

```json
{
    "type":"PlayAction",
    "appID":"8BADF00D",
    "clientUser":"C00010FFBAAAAAADDEADFA11",
    "receivedAt":"2021-04-14T16:41:15+0000",
    "payload": {
      "isAppStore": "true",
      "platform": "iOS",
      "targetEnvironment": "native",
      "buildNumber": "2",
      "signalClientUser": "C00010FFBAAAAAADDEADFA11",
      "isSimulator": "false",
      "modelName": "iPhone12,1",
      "operatingSystem": "iOS",
      "isTestFlight": "false",
      "appVersion": "3.12.0",
      "architecture": "arm64",
      "systemVersion": "iOS  14.4.2",
      "signalType": "PlayAction"
    }
}
```

## Type

Signals always have a type. This a short string that describes the event that caused the signal to be sent. It is 
recommended to use short, camel-cased half-sentences like these:

- `appLaunchedRegularly`
- `appEnteredBackground`
- `settingsOpened`

When you're setting up your [Insights](insights-reference.html) later, you'll be able to **filter** by Signal Type.
This is 

## Client User

Signals have a `clientUser` property, which stores a string. All signals with the same client user property will be 
assumed to originate from the same user.

By default, the client user will be a UUID, usually supplied by the devices `identifierForVendor` method. But you can
overwrite this by supplying your own client user identifier: If you'd rather not track users at all, you can pass
an empty string instead. This will effectively disable user counting, but you can still count sessions and signals,
and get a very good idea of your user base this way.

The TelemetryDeck client library will hash any value saved into this property before sending it to the server. In 
addition, the server will *also* hash any client user value *again*, just to be extra sure. We *really* do not want to 
know your users' email addresses!

## Metadata Payload

Signals have a metadata payload dictionary that contains things like platform, os version, and any data you throw in 
there. This is highly useful for filtering and aggregation insights.

The default client library will automatically send a base payload with these keys:

- platform
- systemVersion
- appVersion
- buildNumber
- isSimulator
- isTestFlight
- isAppStore
- modelName
- architecture
- operatingSystem
- targetEnvironment

You can add any additional keys and values, or overwrite existing ones. For example, it might be a good idea to send 
your application's settings with each call. This way, you'll get a good overview of which percentage of your users
have a certain feature enabled, and which configurations deserve the most effort from you.

## Time Stamp

Signals have a "created at" property that is set to the time (in UTC) when the signal was received on the server. This
allows you to group them by time. 

<div class="alert alert-info" role="alert">
Note: In a future version of TelemetryDeck, you'll be able to <a href="https://github.com/TelemetryDeck/SwiftClient/issues/19">store signals locally in the app before sending them</a>.
If you are using that technique, the server will no longer set the time the signal was created, but it will instead be
set on the client.
</div>


## Future Features

These are not implemented yet, but in future versions, the signal API will also accept these properties:

- [Session ID](https://github.com/TelemetryDeck/TelemetryViewer/issues/59), so you can count sessions and session length
- [Numerical Metrics](https://github.com/TelemetryDeck/TelemetryViewer/issues/60), so you can show, e.g., a graph of the average number of items in your users' databases