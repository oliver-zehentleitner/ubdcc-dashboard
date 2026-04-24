> ⚠️ Security Warning: There are currently fraudulent repositories (e.g., under the user gesine1541ro7) impersonating this project to distribute malware. Please ensure you are only using the official source: oliver-zehentleitner/unicorn-binance-websocket-api.
[Read the full technical analysis and campaign details here!](https://blog.technopathy.club/security-warning-fraudulent-github-repository-impersonating-unicorn-binance-websocket-api)

[![GitHub Release](https://img.shields.io/github/release/oliver-zehentleitner/ubdcc-dashboard.svg?label=github&color=blue)](https://github.com/oliver-zehentleitner/ubdcc-dashboard/releases)
[![GitHub Downloads](https://img.shields.io/github/downloads/oliver-zehentleitner/ubdcc-dashboard/total?color=blue)](https://github.com/oliver-zehentleitner/ubdcc-dashboard/releases)
[![PyPi Release](https://img.shields.io/pypi/v/ubdcc-dashboard?color=blue)](https://pypi.org/project/ubdcc-dashboard/)
[![PyPi Downloads](https://pepy.tech/badge/ubdcc-dashboard)](https://pepy.tech/project/ubdcc-dashboard)
[![License](https://img.shields.io/badge/license-MIT-blue)](https://oliver-zehentleitner.github.io/ubdcc-dashboard/license.html)
[![Supported Python Version](https://img.shields.io/pypi/pyversions/ubdcc-dashboard.svg?logo=python)](https://www.python.org/downloads/)
[![PyPI - Status](https://img.shields.io/pypi/status/ubdcc-dashboard.svg)](https://github.com/oliver-zehentleitner/ubdcc-dashboard/issues)
[![CodeQL](https://github.com/oliver-zehentleitner/ubdcc-dashboard/actions/workflows/codeql.yml/badge.svg)](https://github.com/oliver-zehentleitner/ubdcc-dashboard/actions/workflows/codeql.yml)
[![Unit Tests](https://github.com/oliver-zehentleitner/ubdcc-dashboard/actions/workflows/unit-tests.yml/badge.svg)](https://github.com/oliver-zehentleitner/ubdcc-dashboard/actions/workflows/unit-tests.yml)
[![Build and Publish GH+PyPi](https://github.com/oliver-zehentleitner/ubdcc-dashboard/actions/workflows/build_wheels.yml/badge.svg)](https://github.com/oliver-zehentleitner/ubdcc-dashboard/actions/workflows/build_wheels.yml)
[![Read the Docs](https://img.shields.io/badge/read-%20docs-yellow)](https://oliver-zehentleitner.github.io/ubdcc-dashboard/)
[![Read How To`s](https://img.shields.io/badge/read-%20howto-yellow)](https://blog.technopathy.club/series/unicorn-binance-suite)
[![Github](https://img.shields.io/badge/source-github-cbc2c8)](https://github.com/oliver-zehentleitner/ubdcc-dashboard)
[![Telegram](https://img.shields.io/badge/community-telegram-41ab8c)](https://t.me/unicorndevs)
[![UBS-Banner](https://raw.githubusercontent.com/oliver-zehentleitner/unicorn-binance-suite/master/images/logo/UBS-Banner-Readme.png)](https://github.com/oliver-zehentleitner/unicorn-binance-suite)

# UBDCC Dashboard

Browser-based live dashboard for the [UNICORN Binance DepthCache Cluster (UBDCC)](https://github.com/oliver-zehentleitner/unicorn-binance-depth-cache-cluster) —
monitor every depth cache in your cluster at a glance, spot out-of-sync caches
instantly, and add or remove caches on the fly.

Part of the [UNICORN Binance Suite](https://github.com/oliver-zehentleitner/unicorn-binance-suite).

---

## Features

- Compact **mini-orderbook tiles** per depth cache — top-3 asks/bids with
  quantity bars and spread in bps.
- **Continuous, low-overhead polling**: `IntersectionObserver` + filter gate
  means only on-screen, matching tiles hit the cluster.
- **Status colouring** per tile: out-of-sync (`error_id #6000`) turns red,
  other errors yellow with a compact error message.
- **Cluster Status** header button with a live health dot (green /
  yellow / red) driven by a 30 s `/get_cluster_info` poll. Click for a
  full breakdown — pods grouped by role, node topology, per-DepthCache
  replica donut with distribution state and (when available) sync
  state, credentials summary.
- **Credentials Manager** — add / remove / list Binance API key pairs
  on a running cluster right from the dashboard. `api_secret` input is
  masked, stored keys show only a preview, remove requires two-click
  confirm.
- **API Builder** — onboarding helper for developers. Pick a task
  (create DepthCache, get asks/bids, add credentials, ...), fill in
  the form, copy a ready-to-paste snippet in **curl, HTTPie, Python
  (using the official UBLDC `Cluster` client), JavaScript, Go, C#,
  Java or Rust**. "Try it" runs GET-safe tasks through the dashboard's
  CORS proxy and shows the pretty-printed JSON response.
- **Version badge** next to the title. On load, the dashboard asks
  PyPI for the latest release of `ubdcc-dashboard`. Up to date →
  badge stays in the accent colour. Outdated → animated rainbow
  gradient with a `pip install -U` hint in the hover tooltip. Backed
  by a local `/version` endpoint on the launcher HTTP server.
- **Add DepthCaches** modal with live `exchangeInfo` symbol lookup for spot,
  cross / isolated margin, futures, options (incl. testnets). Shows only
  actively tradable symbols. Free-text fallback for exchanges without a
  public `exchangeInfo`.
- **Bulk `× Remove filtered`** with two-click confirmation — only active when a
  filter is set, so you can never accidentally remove every DC.
- **Per-tile `×`** remove with two-click confirmation and 3 s auto-disarm.
- **Disconnect** button to stop polling and cut load on the cluster.
- Refresh-rate throttle from `max` down to `10 s`. Default `2 s` is
  polite to the cluster; crank it up to `max` for live feel, or drop
  down to `5 s` / `10 s` for gentler polling on lightly-used clusters.
- **Dark theme**, tabular-numeric fonts, no framework, no tracking — a single
  HTML file served by a minimal stdlib HTTP server.

---

## Screenshot
The dashboard provides a compact live view of your UBDCC cluster in the browser: mini-orderbook tiles, sync/error state 
visibility, and quick DepthCache management in one place.
![UBDCC Dashboard Screenshot](https://raw.githubusercontent.com/oliver-zehentleitner/ubdcc-dashboard/refs/heads/master/images/misc/ubdcc-dashboard.png)

---

## Authorship & License

Author / Maintainer: Oliver Zehentleitner (https://github.com/oliver-zehentleitner)
License: **MIT** — free for commercial and private use. No paid license,
no subscription, no commercial tier.

---

## Installation and Upgrade

```sh
pip install -U ubdcc-dashboard
```

Requires Python 3.9+. No external dependencies — uses only the standard
library.

**Cluster target:** UBDCC ≥ 0.7.0 (with UBLDC ≥ 2.14.0 for margin /
isolated-margin support). Older clusters work for the orderbook view
but reject the renamed credential endpoints used by the Credentials
manager and the API Builder.

---

## Quick Start

```sh
ubdcc-dashboard start
```

The server binds to `127.0.0.1:8080` (localhost only) by default and opens
the dashboard in your browser. Enter the URL of your UBDCC MGMT node
(typical: `http://<cluster-host>:42081`) and hit `Connect`.

### CLI options

```
ubdcc-dashboard start [--host HOST] [--port PORT] [--no-browser]
                      [--proxy-timeout SECONDS] [--batch-workers N]
```

| Flag | Default | Description |
|---|---|---|
| `--host` | `127.0.0.1` | Interface to bind. **Localhost only by default — secure.** Use `--host 0.0.0.0` to expose the dashboard on your network. |
| `--port` | `8080` | TCP port to listen on. |
| `--no-browser` | *off* | Do not auto-open the browser on start. |
| `--proxy-timeout` | `10.0` | Timeout (seconds) for the CORS proxy's outbound fetches. |
| `--batch-workers` | `32` | Worker threads used for `/proxy_batch` fan-out. |

### Exposing on the network

```sh
ubdcc-dashboard start --host 0.0.0.0 --port 8080
```

> **Note:** The proxy is unauthenticated. Only expose the dashboard on a
> trusted network.

---

## How it works

The dashboard is a single `index.html` (vanilla JS, no framework) served by
a small stdlib HTTP server. The server also acts as a tiny **CORS proxy** so
the browser can query a remote UBDCC cluster that does not send
`Access-Control-Allow-Origin` headers.

Under the hood:

- `GET /proxy?url=…` — passes a single GET through.
- `POST /proxy {url, body}` — passes a single JSON POST through.
- `POST /proxy_batch {base, requests}` — fans out a list of GETs over a
  thread pool (default 32 workers) for snappy orderbook refreshes.
- `GET /version` — returns `{"version": "..."}` read from
  `ubdcc_dashboard.__version__`. Used by the header version badge and
  usable as a health-check target.

The `unicorn-binance-depth-cache-cluster` project is the server side of this
story — the dashboard just paints what the cluster already exposes via its
REST API.

---

## Change Log
[https://oliver-zehentleitner.github.io/ubdcc-dashboard/changelog.html](https://oliver-zehentleitner.github.io/ubdcc-dashboard/changelog.html)

## Documentation
- [General](https://oliver-zehentleitner.github.io/ubdcc-dashboard)
- [CLI Reference](https://oliver-zehentleitner.github.io/ubdcc-dashboard/readme.html#cli-options)

## Related Articles
- [UNICORN Binance Suite Article Series](https://blog.technopathy.club/series/unicorn-binance-suite)

## Project Homepage
[https://github.com/oliver-zehentleitner/ubdcc-dashboard](https://github.com/oliver-zehentleitner/ubdcc-dashboard)

## Wiki
[https://github.com/oliver-zehentleitner/ubdcc-dashboard/wiki](https://github.com/oliver-zehentleitner/ubdcc-dashboard/wiki)

## Social
- [Discussions](https://github.com/oliver-zehentleitner/ubdcc-dashboard/discussions)
- [https://t.me/unicorndevs](https://t.me/unicorndevs)
- [https://dev.binance.vision](https://dev.binance.vision)

## Receive Notifications
To receive notifications on available updates you can
[watch](https://github.com/oliver-zehentleitner/ubdcc-dashboard/watchers)
the repository on [GitHub](https://github.com/oliver-zehentleitner/ubdcc-dashboard), or subscribe to the
[releases discussion category](https://github.com/oliver-zehentleitner/ubdcc-dashboard/discussions/categories/releases).

To receive news (like inspection windows/maintenance) about the Binance API's subscribe to their telegram groups:

- [https://t.me/binance_api_announcements](https://t.me/binance_api_announcements)
- [https://t.me/binance_api_english](https://t.me/binance_api_english)
- [https://t.me/Binance_USA](https://t.me/Binance_USA)
- [https://t.me/TRBinanceTR](https://t.me/TRBinanceTR)
- [https://t.me/BinanceExchange](https://t.me/BinanceExchange)

## How to report Bugs or suggest Improvements?
[List of planned features](https://github.com/oliver-zehentleitner/ubdcc-dashboard/issues?q=is%3Aissue+is%3Aopen+label%3Aenhancement) —
give a 👍 if you need one of them, or suggest a new feature!

Before you report a bug, [try the latest release](https://github.com/oliver-zehentleitner/ubdcc-dashboard#installation-and-upgrade). If the issue still exists, provide the error trace, OS, Python version, browser, and explain how to reproduce the error. A minimal reproduction (commands + cluster setup) is appreciated.

If you don't find an issue related to your topic, please open a new [issue](https://github.com/oliver-zehentleitner/ubdcc-dashboard/issues)!

[Report a security bug!](https://github.com/oliver-zehentleitner/ubdcc-dashboard/security/policy)

## Contributing
[UBDCC Dashboard](https://github.com/oliver-zehentleitner/ubdcc-dashboard) is an open source project which welcomes contributions which can be anything from simple documentation fixes and reporting dead links to new features. To contribute follow
[this guide](https://github.com/oliver-zehentleitner/ubdcc-dashboard/blob/master/CONTRIBUTING.md).

### Contributors
[![Contributors](https://contributors-img.web.app/image?repo=oliver-zehentleitner/ubdcc-dashboard)](https://github.com/oliver-zehentleitner/ubdcc-dashboard/graphs/contributors)

We ❤ open source!

---

## AI Integration

This project provides a [`llms.txt`](https://raw.githubusercontent.com/oliver-zehentleitner/ubdcc-dashboard/refs/heads/master/llms.txt) file for AI tools (ChatGPT, Claude, Copilot, etc.) with structured usage instructions, CLI reference and architecture notes.

---

## Disclaimer
This project is for informational purposes only. You should not construe this information or any other material as legal, tax, investment, financial or other advice. Nothing contained herein constitutes a solicitation, recommendation, endorsement or offer by us or any third party provider to buy or sell any securities or other financial instruments in this or any other jurisdiction in which such solicitation or offer would be unlawful under the securities laws of such jurisdiction.

### If you intend to use real money, use it at your own risk!

Under no circumstances will we be responsible or liable for any claims, damages, losses, expenses, costs or liabilities of any kind, including but not limited to direct or indirect damages for loss of profits.
