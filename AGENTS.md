# AGENTS.md — UBDCC Dashboard

> **End-user cheatsheet for AI-assisted consumption:** [`llms.txt`](llms.txt) — use that one if you're writing code *against* the dashboard.
> **This file** is for AI agents working *on* this repo itself.

## Planning & Backlog

Open development tasks and decisions are tracked in **[TASKS.md](TASKS.md)**.

---

## Project Overview

Single-file browser dashboard + tiny stdlib HTTP/CORS-proxy server, shipped
as a pip-installable CLI (`ubdcc-dashboard start`) for the
[UNICORN Binance DepthCache Cluster (UBDCC)](https://github.com/oliver-zehentleitner/unicorn-binance-depth-cache-cluster).

**Abbreviation:** ubdcc-dashboard
**Current Version:** 0.1.1
**Author:** Oliver Zehentleitner
**Python:** 3.9-3.14 on Linux, macOS, Windows
**Dependencies:** none (stdlib only)
**Build:** noarch wheel + sdist

---

## Layout

```
ubdcc_dashboard/
├── __init__.py        # __version__
├── cli.py             # argparse: `ubdcc-dashboard start`
├── server.py          # ThreadedHTTPServer + /proxy, /proxy_batch, static serve
└── static/
    └── index.html     # Single-page dashboard (vanilla JS)
```

- The HTML is the actual product. It's a single file, vanilla JS, no
  framework. Keep it dependency-free.
- `server.py` is deliberately tiny — `http.server.SimpleHTTPRequestHandler`
  subclass with three extra endpoints. No external deps.
- `cli.py` exposes exactly one subcommand today: `start`. Flags: `--host`
  (default `127.0.0.1`, localhost only), `--port` (default `8080`),
  `--no-browser`, `--proxy-timeout`, `--batch-workers`.
- The package is noarch. No Cython here.

---

## Versioning & Release

- Version is set in `pyproject.toml`, `setup.py`, `ubdcc_dashboard/__init__.py`,
  `llms.txt`, `CHANGELOG.md`, `dev/sphinx/source/conf.py`.
- `dev/set_version.py` + `dev/set_version_config.yml` bump them all in one go.
  **Do not run `set_version.py` yourself — the maintainer runs it.**
- Release flow: bump → tag `v<version>` → push tag → CI builds wheel +
  sdist and uploads to PyPI; `gh_release.yml` creates the GitHub release.
- CHANGELOG convention: keep `X.Y.Z.dev (development stage/unreleased/unstable)`
  as the top header. On release, add a new numbered section above it with
  the bump date, and bump the `.dev` header to the next planned version.
- When bumping, update the `Version:` line in `llms.txt` and the
  `Current Version` line in this file.

---

## Security defaults

- Default bind: `127.0.0.1` — localhost only. Users must explicitly pass
  `--host 0.0.0.0` to expose on a network.
- The proxy is unauthenticated. Any code that broadens access (remote bind,
  authentication, TLS) should be explicit and documented.

---

## Testing

- Manual smoke: `ubdcc-dashboard start` → browser opens → connect to a
  running UBDCC MGMT node → DCs tile-grid updates.
- Headless sanity: `python -c "from ubdcc_dashboard import cli; cli.main(['--help'])"`
  — currently part of `unit-tests.yml`.

---

## Coding style

- Python: stdlib only, no external runtime deps. `from __future__ import annotations`.
- JS (index.html): vanilla, no build step. Small helpers defined inline;
  prefer readability over micro-optimisation.
- Keep `server.py` small and dependency-free. Anything that needs a library
  belongs either in the dashboard (client-side) or in a separate tool.
