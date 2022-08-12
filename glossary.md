---
title: Glossary of Terms
tags:
  - Glossary
  - intro
description: A list of common terms used in the TelemetryDeck ecosystem and what they mean
lead: A list of common terms used in the TelemetryDeck ecosystem and what they mean.
---

TelemetryDeck
: TelemetryDeck is a platform for collecting and visualizing data from apps and web apps. It is a powerful tool for building data-driven applications and dashboards, all while respecting the privacy of user privacy. Because of our _Double Hashing_ algorithm, TelemetryDeck is able to guarantee that no personal data is ever collected or stored, making TelemetryDeck a solution that is safe, trustworthy and 100% compatible with the GDPR and other privacy regulations.  
TelemetryDeck also aims to be simple, easy to use, and easy to understand. You should not need a horde of data scientists and analysts to improve your app. Instead, we'll try and help you find the low hanging fruit to make your app more efficient.

App
: In TelemetryDeck, an app is a reference to one of your released apps. The _app_ object's most important properties are its _App Identifier_, which uniquely references your app to the TelemetryDeck API, and its _App Name_, which is the name of your app.

Organization
: Because TelemetryDeck allows multiple users to share access to their apps, an _organization_ is a group of users who have access to the same apps.  
If you belong to a company or non-profit, your organization name will usually be the name of that organization. If you're a single developer, feel free to choose a fun name for your organization, or just use your first and last name.

Organization member
: Someone who has access to your organization.

App Identifier
: A unique identifier for your app. This is used to reference your app to the TelemetryDeck API and when sending signals out of your app using the _TelemetryDeck Package_.

TelemetryDeck Package
: Also called _TelemetryDeck SDK_, a package is a small open source code package that contains code to anonymize user data and send signals to TelemetryDeck. We offer packages for Apple Platforms, Android, Java/Kotlin, and the Web (JavaScript).  
Packages are open source on our [GitHub account](https://github.com/TelemetryDeck)

TelemetryDeck SDK
: See _TelemetryDeck Package_

Group
: A _Group_ or _Insight Group_ is a collection of _Insights_ that belong to an app. An app can have multiple groups, and each group can have multiple insights.  
Groups can be used to organize insights into logical categories or can be used as a dashboard – for example, you could have a group called "Objectives and Key Results" and display that on a large screen.

Insight
: An _Insight_ is one of the primary building blocks of TelemetryDeck. In essence, you can think of an insight as one of the little cards with data in an insight group. They have a title, a _Query_, and a _Display Mode_. The query is used to retrieve data from the TelemetryDeck API, and the display mode is used to determine how the data is displayed, e.g. as a bar chart, or a line chart.

Query
: A _Query_ is an object that contains the information needed to retrieve data from the TelemetryDeck API. There are various _Query Types_, which determines the way data is retrieved. You can either generate queries using the dashboard's query editor UI, or you can write them by hand in JSON using the _TelemetryDeck Query Language_.

Display Mode
: How an _Insight_ displays the results of its _Query_. This will usually be a type of chart, or a table.

TelemetryDeck Query Language
: A JSON based language that is used to retrieve data from the TelemetryDeck API. The language is based on the [Query language for Apache Druid](hhttps://druid.apache.org/docs/latest/querying/querying.html), but we've made various additions and changes to it, such as the ability to use relative dates. You could say TQL is a **superset** of Druid's Query language.

Double Hashing
: TelemetryDeck uses a _Double Hashing_ algorithm to anonymize user data. On the device your user's app is running on, we salt and hash the user identifier you provide to TelemetryDeck. This way we can ensure that the TelemetryDeck API has no access to your actual user identifiers.  
Because of the peculiarities of the GDPR, just hashing your identifier once does not count as anonymization – the identifier is ony \*_pseudonymized_. This is because you as our customer could in theory keep a list of all the identifiers you have provided to TelemetryDeck, hash them using the same salt, and then compare that rainbow table to our database of hashed identifiers. If the rainbow table matches, then you have access to your user data.  
To prevent that, we add our own salt to the user identifiers on receival in the _Ingestion API_ and hash it again. This way, neither you nor us can reverse engineer the original identifier, even with additional data.

TelemetryDeck Dashboard
: Our main user interface for our customers. A web application available at https://dashboard.telemetrydeck.com that allows our customers to create and manage their _Apps_ and _Insight Groups_, and view and edit their _Insights_.

TelemetryDeck API
: The REST based API that you can use to retrieve insights, run queries, and interact with TelemetryDeck as our customer. Usually you'd mostly interact with the API using the _TelemetryDeck Dashboard_ at https://dashboard.telemetrydeck.com but you can also use the API directly.

Ingestion API
: An API for the _TelemetryDeck Package_ to send signals to. Whenever your app sends a signal, it goes to the Ingestion API at https://nom.telemetrydeck.com

Customers
: Because we're a developer services product, we need to distinguish between **our customers** – people who use TelemetryDeck and include the _TelemetryDeck Package_ into their apps – and **our customer's users** – people who use the apps that our _customers_ develop. With _users_ we always mean end users of apps that our _customers_ develop. With _customers_ we mean people who use TelemetryDeck.

Users
: People who use the apps that are developed by our _customers_. These are the people whose privacy we want to protect the most.
