---
title: How to update a Swift package
tags:
  - setup
  - package
  - SDK
  - Swift
testedOn: Xcode 15.2 & Swift 5.9
description: Xcode doesn't update packages automatically. How do you tell Xcode to update to the newest version of a Swift Package? Or update all packages at once?
lead: Xcode doesn't update packages automatically. How do you tell Xcode to update to the newest version of a Swift Package? Or update all packages at once?
keywords: Xcode, swift, package, update
order: 10
headerImage: /img/sondrine-package.jpg
---

Even if you tell Xcode to accept all versions of a Swift package up to the next major version, it will not automatically check and download new versions of the package unless you tell it to. Here is how!

Every time you add a Swift package, the Swift Package Manager will download the newest version of that package that conforms to your version requirements, and add a reference to the exact version number to its [Package.resolved](https://github.com/apple/swift-package-manager/blob/main/Documentation/Usage.md#resolving-versions-packageresolved-file) file. Some people check this file into version control – in that case, this ensures that the whole team is working with the exact same version of the package.

While most Swift packages adhere to a <a href="https://semver.org">Semantic Versioning Scheme</a> that promises that no breaking changes occur in a point release, sometimes accidents still happen: A bug will slip into the newest version, or a change will break compatibility with your code. This is why Swift Package Manager, like most package managers, pins down the exact version being used in the <code>Package.resolved</code> file, and expects you to update your packages manually.

When updating manually, you can run the update at a time of your choosing. This ensures that you are aware that something in your code has changed, and you can test your application and check if everything is still working as expected.

With that in mind, here's how to manually update a Swift package using Xcode:

## How to update a Swift Package in Xcode

![Screenshot of the left sidebar in Xcode 14, with the TelemetryDeck Swift Package highlighted](/docs/images/update_package.png)

Updating packages in Xcode can be done using one of two ways. If you want to just update a single package individually – which we recommend by the way – do this:

1. Navigate to the package you want to update in the Xcode navigator. It should be at the bottom of the list, in a section called **Package Dependencies**.
2. Right-click the package you want to update.
3. Choose **Update Package**.

This will download the newest version of the package that is compatible with your version requirements, and update the reference in the `Package.resolved` file. If you want to update to the next **major** version of a package, see the next section.

Instead, you can also update every single Swift Package in your project at once. To do this, open the **Files** menu, navigate to **Packages** and then click **Update to Latest Package Versions**. Afterwards, make sure to test your project to see if everything still works, especially in projects with a lot of package dependencies. See further down for more troubleshooting tips.

{% callToAction "TelemetryDeck: Privacy-first analytics for Swift apps" "Make your app even more awesome" %}

## Updating to the next major version of a Swift Package

By default, Xcode and Swift Package Manager will not update the Major version of a package automatically. (The major version is the first number in the version string, e.g. `1.2.3` has a major version of `1`.)

If you want to update to the next major version of a package, you can do this by manually changing the version requirement in the Xcode project. To do that, navigate to the project, select "Package Dependencies" and manually update the minimum version requirement to the next major version.

![Screenshot of the left sidebar in Xcode 14, with the TelemetryDeck Swift Package highlighted](/docs/images/update_next_major_version.png)

For example, if you have a package that is currently at version `1.2.3`, and you want to update to version `2.0.0`, you can change the version requirement in the Xcode project to `2.0.0`. This will tell the Swift Package Manager to download the newest version of the package that is greater than `2.0.0`, but less than `3.0.0`. When a `2.0.1` comes out, you can update to that version by following the steps above.

## Troubleshooting Issues with Xcode and Swift Packages

Sometimes Xcode's package cache gets confused. This will usually result in weird build errors that can't really be explained. Here are two things that might help:

1. **Resetting the Xcode Package Cache**: To reset the package cache, open the **File** menu, navigate to **Packages**, and click **Reset Package Caches**. This will delete all local package data and re-download each package from its source online.
2. **Cleaning the Build Folder**: To clean your build folder, open the **Product** menu in Xcode, and click **Clean Build Folder**. This will clean the partial build caches, so that your next build will start without any pre-compiled artifacts. This can also sometimes help resolve an issue.
