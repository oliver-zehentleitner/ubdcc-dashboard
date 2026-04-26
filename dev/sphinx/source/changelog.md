# ubdcc-dashboard Change Log

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/) and this project adheres to
[Semantic Versioning](http://semver.org/).

[Discussions about ubdcc-dashboard releases!](https://github.com/oliver-zehentleitner/ubdcc-dashboard/discussions/categories/releases)

[How to upgrade to the latest version!](https://oliver-zehentleitner.github.io/ubdcc-dashboard/readme.html#installation-and-upgrade)

## 0.3.1.dev (development stage/unreleased/unstable)

## 0.3.1
### Fixed
- Main grid empty-state message ("No DepthCaches configured yet —
  click `DepthCaches` to add one.") was set only once in `connect()`
  and never re-evaluated. After creating the first DepthCache the
  hint stayed visible behind the new tiles until the user hit F5;
  removing the last DepthCache left the area blank without the
  hint. Moved the toggle into `reloadDcs()` so the message reflects
  the current `state.dcs.length` after every add / remove / initial
  reload.

## 0.3.0
### Added
- **Cluster Status modal: tabbed layout** — split into **Pods**,
  **DepthCaches**, **DCNs** and **Credentials** tabs with live counts.
  Top strip (health + counts + mgmt version + db sync age) stays
  pinned above the tabs so the at-a-glance view is preserved.
- **Cluster Status: new DCNs tab** — DCN-centric view. Each DCN pod
  shown as a card with status pill, node, version, and the list of
  DepthCaches it hosts (exchange / market / restarts / per-replica
  status). Sorted by load (most-loaded DCNs first), idle DCNs
  flagged with "no depthcaches assigned — DCN is idle". Useful for
  spotting unbalanced distribution and idle capacity at a glance.
- API Builder: two more languages — **PHP** (built-in cURL extension,
  no Composer required) and **C/C++** (libcurl, single template that
  compiles with both `gcc` and `g++`). Brings the total to ten.
- API Builder modal footer: link to
  [Open an issue](https://github.com/oliver-zehentleitner/ubdcc-dashboard/issues)
  next to the OpenAPI reference, so users can flag wrong snippets and
  we can fix the generators.
### Changed
- API Builder modal footer: text bumped from `10px italic muted` to
  `12px text-color` and the OpenAPI / Open-an-issue links recoloured
  with `var(--accent)` + underline so they're readable on the dark
  background.
### Fixed
- API Builder: the **Markets** textarea on
  `POST /create_depthcaches` (bulk) rendered with the browser-default
  white background. The global form-input rule in `static/index.html`
  only covered `input, button, select`; extended to include
  `textarea` so it picks up the dark theme like every other field.

## 0.2.0
### Added
- **Version badge** next to the header title: shows the installed
  dashboard version, queries PyPI once on load, turns into an animated
  rainbow gradient when a newer release is available (with a `pip install -U`
  hint in the hover tooltip) and stays in the accent colour when up to date.
- Server endpoint **`/version`** on the launcher HTTP server returns
  `{"version": "..."}` from `ubdcc_dashboard.__version__` — used by the
  badge and available for external health checks.
- Min-gap dropdown now offers **`5 s`** and **`10 s`** in addition to the
  existing presets — gentler polling for lightly-used clusters.
- **Cluster Status** header button with a live health dot
  (green / yellow / red) driven by a 30 s `/get_cluster_info` poll.
  Click opens a modal with:
  - Top strip: `HEALTHY` / `DEGRADED` / `ERROR`, pod count, DC count,
    mgmt version, DB-sync age
  - Pods grouped by role (MGMT / REST API / DCN) with per-pod status
    pill, node, IP:port, version, `UBLDC_VERSION` (DCNs), `last seen Xs ago`
  - Node topology grid (how many mgmt / rest / dcn pods per node)
  - DepthCaches list with a replica donut (running / desired) and
    optional sync-state label (`in sync` / `out of sync` / `error`)
    sourced from the main grid's already-polled tiles, plus a restart
    counter when restarts > 0
  - Credentials summary grouped by account_group
  - Live-ticking `updated Xs ago`, manual `Refresh` button, modal
    cleanly stops its tick timer on close.
- **Credentials** header button + manager modal: add / remove / list
  Binance API key pairs on a running cluster. Secrets masked in the list,
  `api_secret` input is `type=password`, two-click confirm on remove with
  3 s auto-disarm, inline error feedback, footer hint about proxy trust.
- **API Builder** header button + modal — onboarding helper for devs.
  Generates ready-to-paste REST-API calls in **eight languages**:
  - `curl` (POSIX-safe quoting, heredoc bodies)
  - `HTTPie` (`==` for query, `=` / `:=` for body)
  - `Python` — uses the official UBLDC cluster client
    (`BinanceLocalDepthCacheManager` context manager + `ubldc.cluster.*`),
    matching the pattern in UBLDC's `examples/` folder
  - `JavaScript` (`fetch` + `URLSearchParams`, async/await)
  - `Go` (`net/http`, no external deps)
  - `C#` (`HttpClient`, top-level .NET 6+)
  - `Java` (`java.net.http.HttpClient`, JDK 11+, no external deps)
  - `Rust` (`reqwest::blocking`, raw-string JSON bodies with auto-bumped
    hash count so devs don't have to think about escaping)

  Eleven tasks in four groups — Credentials (add / remove / list),
  DepthCaches (create / create-bulk / stop / info / list), Order Book
  (asks / bids), Cluster (info). Editable Base URL, method-coloured
  badge, `Try it →` button for safe GET + DC-create/stop tasks, Copy
  button, link to the cluster's OpenAPI (`/docs`) in the footer.
- **Margin / isolated_margin (+ testnet)** exchange strings added to
  the Add-DC exchange dropdown and the `exchangeInfo` URL map.
  Requires UBLDC ≥ 2.14.0 + UBDCC ≥ 0.7.0.
### Changed
- Header title: `UBDCC LIVE` → `UBDCC DASHBOARD` (full caps, matches
  the other header buttons).
- Empty-state message is now context-sensitive: "Enter the URL…"
  when disconnected, "No DepthCaches configured yet — click
  DepthCaches to add one." when connected with 0 DCs, hidden when DCs
  are present. Wording corrected from "MGMT node" to "REST API node"
  — users connect to restapi on `:42081`, not mgmt on `:42080`.
- Internal `fetch("/proxy", POST)` duplicates consolidated into a
  `proxyPost(url, body)` helper symmetric with the existing `proxyGet`
  / `proxyBatch`.
- Header: `+ Add DC` renamed to `DepthCaches` and `DCC URL` label
  renamed to `UBDCC URL` — one consistent noun style across
  `Cluster ● · Credentials · DepthCaches · API Builder`.
- Default UBDCC URL in the connect field is now `http://127.0.0.1:42081`
  (the standard local-install port) instead of a baked-in LAN IP.
- Credential endpoint paths used across the dashboard match the renamed
  UBDCC REST API — `/add_credentials`, `/remove_credentials`,
  `/get_credentials_list`. Requires **UBDCC ≥ 0.7.0**.
- Cluster-info DC cards use the label `X/Y replicas` (distribution
  count) instead of `running` — distribution STATUS only means
  "pod process started", not "cache synchronised". The sync state is
  shown as a separate `in sync` / `out of sync` meta entry when the
  main grid has already polled that DC.
### Fixed
- Main polling loop no longer blocks the first data fetch behind the
  min-gap wait. With the new 5 s / 10 s options the viewport-visibility
  detection would otherwise delay the initial render by a full gap
  cycle. The loop now only throttles after cycles that actually
  fetched.
- API Builder Copy button keeps its "Copied" confirmation through form
  edits — the state now only resets when the generated snippet text
  actually changes.
- HTTPie snippet generator emits bare numeric/boolean query values
  (`debug==true`) instead of wrapping them in single quotes.
- Cluster-info poll is paused while the browser tab is hidden AND the
  modal is closed; refreshes once on `visibilitychange` when the tab
  becomes visible again — avoids overnight chatter against the mgmt
  node.
- Credentials modal surfaces network errors inline in red instead of
  silently rendering "no credentials configured".
- Minor XSS hardening: the Add-DepthCache modal's `exchangeInfo`-failed
  error path now builds the error element via `el()` instead of
  interpolating the API-returned message into `innerHTML`.
- `stopClusterPoll` also clears the 1 s `tickTimer` as a belt-and-
  suspenders cleanup on disconnect.
- API Builder Copy button now works over plain HTTP on a LAN IP
  (`navigator.clipboard` is only available in a secure context;
  fall back to `document.execCommand('copy')` via a hidden textarea).
- Cluster Info modal: fixed scroll so Close / Refresh stay reachable
  when many DCs are configured (flex sizing was blocking the inner
  scroller from shrinking below content size).

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
