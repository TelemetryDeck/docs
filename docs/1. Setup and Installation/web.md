Sending signals are just a `HTTP POST` request. You don't *need* a Swift Package to do it, you can do it by hand in any language that gives you basic HTTP capabilities. Let's try this out in JavaScript!

## Sending a Signal, Any Signal

Here's how to send a signal using JavaScript:

```html
<script>
let sendTelemetry = function (signalType) {
    fetch('https://nom.telemetrydeck.com/api/v1/apps/<YOUR-APP-ID>/signals/', {
        method: 'POST',
        headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
        },
        body: JSON.stringify({
                "clientUser": navigator.userAgent,
                "type": signalType,
                "payload": {
                        "url": window.location.href,
                        "useragent": navigator.userAgent,
                        "language": navigator.language,
                        "platform": navigator.platform,
                        "vendor": navigator.vendor,
                }
        })
    });
}

sendTelemetry("pageLoad")
</script>
```

With this in your page, loading a site will send a `pageLoad` signal, containing the URL that was loaded. 

<div class="alert alert-info" role="alert">
    In this example we do not get an individual <code>clientUser</code> for each user. Instead, we use the browser's 
    userAgent string as an identifier, which is not very helpful for distinguishing users, but enough for our purposes.
    To do distinguish between individual users, we'd either need a login function, or to generate a 
    UUID for each user and store that in a cookie, which is outside of the scope of this example.
</div>

## Including Meta Information

Without saving an ID, we don't get information about individual users, but with not much effort we can 
get a slew of meta information from the browser's User Agent String. 

The best way to do this is to include [platform.js](https://github.com/bestiejs/platform.js/), a tiny
Javascript library that will parse the browser's User Agent String and give you all the necessary information. 
Download platform.js and add it to your site's sources, then you can update your javascript like this:

```html
<script src="js/platform.js"></script>

<script>
        let sendTelemetry = function (signalType) {
                fetch('https://nom.telemetrydeck.com/api/v1/apps/<YOUR-APP-ID>/signals/', {
                    method: 'POST',
                    headers: {
                            'Accept': 'application/json',
                            'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                            "clientUser": navigator.userAgent,
                            "type": signalType,
                            "payload": {
                                    "url": window.location.href,
                                    "useragent": navigator.userAgent,
                                    "language": navigator.language,
                                    "platform": navigator.platform,
                                    "vendor": navigator.vendor,
                                    "name": String(platform.name),
                                    "version": String(platform.version),
                                    "layout": String(platform.layout),
                                    "os": String(platform.os),
                                    "description": String(platform.description),
                                    "product": String(platform.product),
                                    "manufacturer": String(platform.manufacturer)
                            }
                    })
                });
        }

        sendTelemetry("pageLoad")
</script>
```

And just like that, you'll get the user's browser vendor and version, their OS version, and if they are using a tablet or phone.

We still do not get individual users, but we get a lot of information that will help us make our website better!

## Getting Even More Info

One thing that you might want to do is send heartbeat signal every `x` minutes, to see which of your pages users stay on
for the longest time. Or, if you use cookies anyway, update the above code to send actual hashed user identifiers. Both
of these are left as an exercise for the reader because I *alwayws* wanted to write that muahahah!

Also, if you use cookies, don't forget to ask the user for permission to store that data.
