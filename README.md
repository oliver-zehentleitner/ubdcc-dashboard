# UBDCC Dashboard

[![GitHub Release](https://img.shields.io/github/v/release/oliver-zehentleitner/ubdcc-dashboard.svg)](https://github.com/oliver-zehentleitner/ubdcc-dashboard/releases)
[![PyPI Version](https://img.shields.io/pypi/v/ubdcc-dashboard.svg)](https://pypi.org/project/ubdcc-dashboard/)
[![PyPI - Status](https://img.shields.io/pypi/status/ubdcc-dashboard.svg)](https://github.com/oliver-zehentleitner/ubdcc-dashboard/issues)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ubdcc-dashboard.svg?logo=python)](https://www.python.org/downloads/)
[![License](https://img.shields.io/github/license/oliver-zehentleitner/ubdcc-dashboard.svg)](https://github.com/oliver-zehentleitner/ubdcc-dashboard/blob/master/LICENSE)

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
- **Add DepthCaches** modal with live `exchangeInfo` symbol lookup for spot,
  margin, futures, options (incl. testnets). Shows only actively tradable
  symbols. Free-text fallback for exchanges without a public `exchangeInfo`.
- **Bulk `× Remove filtered`** with two-click confirmation — only active when a
  filter is set, so you can never accidentally remove every DC.
- **Per-tile `×`** remove with two-click confirmation and 3 s auto-disarm.
- **Disconnect** button to stop polling and cut load on the cluster.
- Refresh-rate throttle from `max` down to `2 s`. Default `2 s` is polite to
  the cluster; crank it up when you need a live feel.
- **Dark theme**, tabular-numeric fonts, no framework, no tracking — a single
  HTML file served by a minimal stdlib HTTP server.

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

The `unicorn-binance-depth-cache-cluster` project is the server side of this
story — the dashboard just paints what the cluster already exposes via its
REST API.

---

## Source Code

https://github.com/oliver-zehentleitner/ubdcc-dashboard

## Issue tracker

https://github.com/oliver-zehentleitner/ubdcc-dashboard/issues

## Security

Please report security issues via [GitHub Security Advisories](https://github.com/oliver-zehentleitner/ubdcc-dashboard/security/advisories/new) — see [SECURITY.md](SECURITY.md).

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) and the [Code of Conduct](CODE_OF_CONDUCT.md).

## Changelog

See [CHANGELOG.md](CHANGELOG.md).

## Get a Developer Chat
Join our [Telegram group](https://t.me/unicorndevs) and come chat with us!
