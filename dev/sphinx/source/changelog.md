# ubdcc-dashboard Change Log

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/) and this project adheres to
[Semantic Versioning](http://semver.org/).

[Discussions about ubdcc-dashboard releases!](https://github.com/oliver-zehentleitner/ubdcc-dashboard/discussions/categories/releases)

[How to upgrade to the latest version!](https://oliver-zehentleitner.github.io/ubdcc-dashboard/readme.html#installation-and-upgrade)

## 0.1.1
### Added
- Initial release.
- Single-file vanilla-JS dashboard with compact mini-orderbook tiles per DepthCache,
  dark theme, continuous polling loop, per-tile visibility and filter-gated requests.
- Local HTTP server with CORS proxy (`/proxy`, `/proxy_batch`) so the browser can
  query a remote UBDCC cluster without modifying the cluster.
- `Add DepthCaches` modal: live symbol lookup via Binance `exchangeInfo` for spot /
  margin / futures / options (incl. testnets); free-text fallback for exchanges
  without a public `exchangeInfo` endpoint. Filtered to actively tradable symbols
  only (`status === "TRADING"` + `isSpotTradingAllowed` / `isMarginTradingAllowed`).
- `× Remove filtered` bulk action with two-click confirmation; requires an active
  filter and refuses when every DC would be removed.
- Per-tile `×` remove with two-click confirmation and 3 s auto-disarm.
- Exchange filter dropdown is rebuilt after every `reloadDcs()`, so newly added
  exchanges appear without reconnecting.
- `Disconnect` button: stops polling and clears the view to reduce cluster load.
- CLI: `ubdcc-dashboard start` starts the server, auto-opens the default browser,
  prints a clickable OSC-8 terminal hyperlink. Flags: `--host` (default
  `127.0.0.1` — localhost only), `--port` (default `8080`), `--no-browser`,
  `--proxy-timeout`, `--batch-workers`.
