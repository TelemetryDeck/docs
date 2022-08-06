---
title: How to write this Documentation
tags: documentation
lead: The TelemetryDeck documentation lives in a public Github repository. Here's how to contribute.
order: 999999999
---

## Document Metadata

All metadata for a documentation article is specified in the YAML header at the top of each markdown file (also called the frontmatter of the document). Most of the metadata is optional, but the `title` and `lead` are required:

```yaml
---
title: How to write this Documentation
lead: The TelemetryDeck documentation lives in a public Github repository. Here's how to contribute.
---
```

Here are examples for all possible metadata values:

```yaml
---
title: Setting Up Your Application in SwiftUI
tags:
  - Setup
  - Quickstart
  - Code
testedOn: Xcode 12.2 & Swift 5.3
featured: true
description: How to configure TelemetryClient in SwiftUI based applications
lead: In Scene-based SwiftUI applications, this is how you configure TelemetryClient
searchEngineTitle: Setting up your SwiftUI application with TelemetryDeck
searchEngineDescription: How to configure TelemetryDeck SDK in SwiftUI based applications
order: 1337
---
```

### Title, Lead and Description

The `title` string is how your article is titled in the left sidebar, at the top of the documentation page and in the "Getting Started" page, should it appear there.

The `lead` string is shown on the documentation page, right underneath the title. It is a short description of the article.

The `description` is used to generate the short descriptive text shown in the "Getting Started" page for `featured` pages. If not specified, the `lead` string is used.

### Search Engine Title and Description

The `searchEngineTitle` string is used to generate the title of the search engine result for your article. If not specified, it defaults to the `title` string.

The `searchEngineDescription` string is used to generate the description of the search engine result for your article. If not specified, it defaults to the `description` string.

### Tags

Tags are used to organize documentation articles in the sidebar and to link related articles together.

One tag:

```yaml
tags: Swift
```

Multiple tags:

```yaml
tags:
  - Setup
  - Quickstart
  - Code
  - Swift
```

Organizational tags like `docs` and `guides` are automatically applied. Use the `tags` metadata to add additional tags that link articles together, such as

- The type of article (`setup`, `code`)
- The software stack or language (`swiftui`, `android`, `kotlin` etc.)
- The experience level of the reader (`beginner`, `intermediate`, `advanced`)
- The type of query (`filter`, `cohorts`, etc.)

{% noteinfo "You don't need to add 'docs' and 'articles' as tags" %}

All markdown files in the `docs` repository automatically get the `docs` tag applied to them (by `docs.11tydata.js`). In addition, the respective directories apply their own tags as well:

- Files in the `intro` directory get the `intro` tag applied.
- Files in the `guides` directory get the `guides` tag applied.
- Files in the `articles` directory get the `articles` tag applied.
- Files in the `api` directory get the `api` tag applied.

{% endnoteinfo %}

### Order

You can specify an `order` metadata value to tell the documentation system in which order to display pages. Pages are sorted within their category by `order` value ascending.

The order value affects the display in the left sidebar as well as the "previous" and "next" links at the bottom of a page.

```yaml
order: 42
```

### Featured

Documentation pages can be marked as `featured` to be displayed in the "Getting Started" page.

```yaml
featured: true
```

### Tested On

If the documentation page deals with a specific version of an API or SDK, or something else that might change in the future, it is common courtesy to tell the reader what version of the software or SDK the documentation page or code examples were last tested on. If the value is older, readers can at least infer that they might have to update the code to make it work.

```yaml
testedOn: Xcode 12.2 & Swift 5.3
```

The string value of the `testedOn` field is displayed in the right sidebar.

### Compatibility and Contribution

The right sidebar contains a list of compatibility information for the documentation page. If `testedOn` is set, it will display the `testedOn` value. In addition, it will show the date when the markdown file for the documentation page was last updated. This gives the reader additional hints as to how outdated or current the page is.

The right sidebar will also display a list of contributors who have written an git commit that touches the specific markdown file. The documentation system will try and retrieve the github avatar images for the contributors by

1. Retrieving the committer email from the git commit
1. Searching for that email in the github API
1. Downloading the avatar image from the github API

This will fail if the email is not found in the github API, or if the email is not set as "public email" in the contributor's github profile.

## Markdown

Documentation is written in [Markdown](https://www.markdownguide.org). This means you can write documentation in plain text, and it will be converted to HTML. All standard Markdown elements are supported, such as **bold text**, _italic text_, `inline code`, and [links](https://www.markdownguide.org/basic-syntax/#link).

- Unordered lists
- are just dashes

1. And ordered
1. lists
1. are just numbers

Here is the markdown code for the previous paragraphs:

```markdown
All standard Markdown elements are supported,
such as **bold text**, _italic text_, `inline code`,
and [links](https://www.markdownguide.org/basic-syntax/#link).

- Unordered lists
- are just dashes

1. And ordered
1. lists
1. are just numbers
```

## Code Blocks

Code blocks begin with three backticks (\`) and end with three backticks (\`). On the same line as the opening backticks, you **must** specify the programming language of the code block.

````text
```swift
print("Hello, world!")
```
````

Results in:

```swift
print("Hello, world!")
```

If you can't specify a language, please use `text` instead.

````text
```text
this is
   just
    plain text
```
````

## Custom Shortcodes

In addition to the standard shortcodes, you can also use custom shortcodes. These allow you to display info boxes and other custom elements.

### Info Box

Use the `noteinfo` shortcode to display a box giving the reader additional information .

```markdown
{% raw %}{% noteinfo "Your pizza is ready 🍕" %}
It is time. You can now take your pizza out of the oven.
{% endnoteinfo %}{% endraw %}
```

Here is how this looks like:

{% noteinfo "Your pizza is ready 🍕" %}
It is time. You can now take your pizza out of the oven.
{% endnoteinfo %}

### Warning Box

Just as with `noteinfo`, you can also use `notewarning` to warn the readers of dangerous actions or consequences:

```markdown
{% raw %}{% notewarning "Take care of your pizza!" %}
When removing your pizza out of the oven, please make sure to not burn your fingers. Also make sure your cat won't eat it while you look at this document.
{% endnotewarning %}{% endraw %}
```

This is how the `notewarning` output looks like:

{% notewarning "Take care of your pizza!" %}
When removing your pizza out of the oven, please make sure to not burn your fingers. Also make sure your cat won't eat it while you look at this document.
{% endnotewarning %}
