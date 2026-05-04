---
title: Get a Personal Access Token
featured: false
tags: advanced
description: How to generate a personal access token to authenticate against the TelemetryDeck API
lead: To interact with the TelemetryDeck API, you need a personal access token (PAT) that authenticates you with the API servers. Treat the token as a secret and store it as safely as a password.
order: 1
---

{% notewarning "Paid plans only" %}

Personal access tokens are available on TelemetryDeck's paid plans. If your organization is on the free plan, upgrade your plan first and the feature will become available in the dashboard.

{% endnotewarning %}

## Generating a Personal Access Token

You generate personal access tokens directly from the TelemetryDeck dashboard. No API call is required.

1. Sign in to [your TelemetryDeck dashboard](https://dashboard.telemetrydeck.com).
2. Click your name in the top right of the header to open the user menu.
3. Choose **Personal Access Tokens**.
4. Click **Generate new token**.
5. Give the token a memorable name (for example, "Claude assistant" or "CI export script") and pick an expiration window. Tokens cannot live longer than one year.
6. Click **Generate token**.

You'll see the new token displayed once. Copy it immediately and store it somewhere safe — TelemetryDeck will never show the raw token to you again. Each token starts with the prefix `tdpat_`, so you can recognise it as a TelemetryDeck personal access token.

If you lose a token, you cannot recover it; revoke the lost token from the same screen and generate a new one.

## Revoking a Token

To revoke a token, return to **Personal Access Tokens** in the user menu and click **Revoke** on the token you want to invalidate. Anything using the revoked token will stop working immediately.

## Example: Retrieving your user information

Send the token in the `Authorization` header of any API request, prefixed with `Bearer `:

```text
GET /api/v3/users/info HTTP/1.1
Authorization: Bearer tdpat_…
Host: api.telemetrydeckapi.com
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

A personal access token has the same permissions as your user account. If you belong to multiple organizations, the token can access data from all of them, the same way you can in the dashboard.
