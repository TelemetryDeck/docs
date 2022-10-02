---
title: Get an API Token
featured: true
tags: advanced
description: How to get a Bearer Token to authenticate against the TelemetryDeck API
lead: To interact with the TelemetryDeck API, you'll have to supply a 🐻 bearer token with each request that authenticates you with the API servers. Treat the bearer token as a secret, and store it as safely as a password.
order: 1
---

{% noteinfo "The Future is bright!" %}

In the future, we'll make it easier for you to generate API tokens via the Dashboard, but for now, you'll have to generate a token manually using HTTP POST requests.

Officially, we only allow API access for users in our Tier 2 Pricing tier and above. However, this is currently not enforced by the API, and there will be a grace period before it is. Feel free to try things out and let us know what you think! <3

{% endnoteinfo %}

{% notewarning "This is a beta feature" %}

[We're still working a lot on the API](https://api.telemetrydeck.com), so we'll be adding new features and improvements as we go. This also means that sometimes things might break, although we're doing our best to prevent that. Let us know if you see any issues.
{% endnotewarning %}

## Generating a Bearer Token with the API

To retrieve a bearer token, send a a POST request to the following URL:

`https://api.telemetrydeck.com/api/v1/users/login`

The POST request needs to have its `Authorization` header set to `Basic <base64 encoded username:password>`. A body is not necessary.

```text
POST /api/v1/users/login HTTP/1.1
Authorization: Basic <base64 encoded username:password>
Content-Length: 0
Host: api.telemetrydeck.com
```

You will receive a response with a bearer token.

```json
{
  "expiresAt": "2023-01-07T13:27:22+0000",
  "id": "de1e7e-facade-c0ffee-0ff1ce",
  "user": {
    "id": "BADA55-BADGE5"
  },
  "value": "🐻🐻🐻🐻🐻🐻🐻🐻🐻🐻🐻🐻🐻"
}
```

Store the `value` as your bearer token and use it as the `Authorization` header in subsequent requests.

## Example: Retrieving your user information

As an example, lets retrieve your user information using the API:

```text
GET /api/v1/users/me HTTP/1.1
Authorization: Bearer 🐻🐻🐻🐻🐻🐻🐻🐻🐻🐻🐻🐻🐻
Host: api.telemetrydeck.com
```

The response for this should look like this:

````json
{
  "email": "you@example.com",
  "emailIsVerified": true,
  "firstName": "Daniel",
  "id": "BADA55-BADGE5",
  "isFoundingUser": true,
  "lastName": "Jilg",
  "organization": {
    "createdAt": "2020-12-31T23:00:00+0000",
    "name": "TelemetryDeck",
    "updatedAt": "2022-07-11T01:27:20+0000"
  },
  "receiveReports": "weekly"
}
```

### Example 2: Retrieving your user information

As an example, lets retrieve your user information using the API:

```text
GET /api/v1/users/me HTTP/1.1
Authorization: Bearer 🐻🐻🐻🐻🐻🐻🐻🐻🐻🐻🐻🐻🐻
Host: api.telemetrydeck.com
```

The response for this should look like this:

```json
{
  "email": "you@example.com",
  "emailIsVerified": true,
  "firstName": "Daniel",
  "id": "BADA55-BADGE5",
  "isFoundingUser": true,
  "lastName": "Jilg",
  "organization": {
    "createdAt": "2020-12-31T23:00:00+0000",
    "name": "TelemetryDeck",
    "updatedAt": "2022-07-11T01:27:20+0000"
  },
  "receiveReports": "weekly"
}
```
