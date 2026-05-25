# TelemetryDeck Documentation

Welcome to the public documentation for TelemetryDeck. The output of these pages is hosted at https://telemetrydeck.com/docs.

We're incredibly grateful for pull requests or issues that improve things or let us know about errata and missing or unclear bits of information! <3

Check out `articles/documentation.md` for an overview of how documentation pages are formatted.


## Local Development

We use Python `pip`. You can follow the setups at https://zensical.org/docs/get-started/#installation for the initial setup.

Note: Make sure the Python version is recent e.g. 3.14 or later (`python3 --version`).

## LLM and agent friendly output

Every page is also published as raw Markdown alongside the rendered HTML. After `zensical build`, run `python3 scripts/build_llms.py` to:

- copy each source `.md` from `docs/` into the corresponding location in `site/` (so `https://docs.telemetrydeck.com/articles/insights.md` returns the source for `/articles/insights/`),
- write `site/llms.txt` following the [llms.txt](https://llmstxt.org) convention,
- write `site/llms-full.txt` containing every page concatenated for one-shot ingestion.

Both deploy workflows run this step automatically after the Zensical build.
