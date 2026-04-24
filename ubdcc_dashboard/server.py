"""UBDCC Dashboard — local HTTP server + CORS proxy.

Serves the bundled static dashboard (index.html) and proxies browser requests
to a UBDCC MGMT node so the Same-Origin-Policy does not block them.
"""
from __future__ import annotations

import concurrent.futures
import http.server
import json
import os
import socketserver
import sys
import urllib.error
import urllib.parse
import urllib.request
from importlib import resources

from . import __version__

PROXY_TIMEOUT_DEFAULT = 10.0
BATCH_WORKERS_DEFAULT = 32


def _static_dir() -> str:
    """Return the absolute path to the bundled static/ directory."""
    ref = resources.files("ubdcc_dashboard").joinpath("static")
    # Works for both a regular install (directory) and a zipped wheel
    # (resources.as_file would be needed there). We assume a normal install.
    return str(ref)


def _fetch(url: str, timeout: float, method: str = "GET", body: bytes | None = None,
           content_type: str | None = None) -> tuple[int, dict]:
    req = urllib.request.Request(url, method=method, data=body)
    if content_type:
        req.add_header("Content-Type", content_type)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            raw = r.read()
            try:
                return r.status, json.loads(raw)
            except json.JSONDecodeError:
                return r.status, {"raw": raw.decode("utf-8", errors="replace")}
    except urllib.error.HTTPError as e:
        raw = e.read()
        try:
            return e.code, json.loads(raw)
        except json.JSONDecodeError:
            return e.code, {"result": "ERROR", "error_id": f"#HTTP{e.code}",
                            "message": raw.decode("utf-8", errors="replace")}
    except Exception as e:
        return 502, {"result": "ERROR", "error_id": "#PROXY",
                     "message": f"{type(e).__name__}: {e}"}


def make_handler(proxy_timeout: float, batch_workers: int) -> type[http.server.SimpleHTTPRequestHandler]:
    class Handler(http.server.SimpleHTTPRequestHandler):
        server_version = "UBDCC-Dashboard"

        def _cors(self) -> None:
            self.send_header("Access-Control-Allow-Origin", "*")
            self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
            self.send_header("Access-Control-Allow-Headers", "Content-Type")

        def _json(self, status: int, payload) -> None:
            body = json.dumps(payload).encode()
            self.send_response(status)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self._cors()
            self.end_headers()
            self.wfile.write(body)

        def do_OPTIONS(self) -> None:  # noqa: N802
            self.send_response(204)
            self._cors()
            self.end_headers()

        def do_GET(self) -> None:  # noqa: N802
            parsed = urllib.parse.urlparse(self.path)
            if parsed.path == "/version":
                self._json(200, {"version": __version__})
                return
            if parsed.path == "/proxy":
                params = urllib.parse.parse_qs(parsed.query)
                target = (params.get("url") or [None])[0]
                if not target:
                    self._json(400, {"result": "ERROR", "message": "missing url param"})
                    return
                status, payload = _fetch(target, proxy_timeout)
                self._json(status, payload)
                return
            super().do_GET()

        def do_POST(self) -> None:  # noqa: N802
            parsed = urllib.parse.urlparse(self.path)
            length = int(self.headers.get("Content-Length", 0))
            raw = self.rfile.read(length) if length else b""
            try:
                payload = json.loads(raw) if raw else {}
            except json.JSONDecodeError:
                self._json(400, {"result": "ERROR", "message": "invalid json body"})
                return

            if parsed.path == "/proxy_batch":
                base = (payload.get("base") or "").rstrip("/")
                requests = payload.get("requests") or []
                if not base:
                    self._json(400, {"result": "ERROR", "message": "missing base"})
                    return

                def one(item):
                    qs = urllib.parse.urlencode(item.get("params") or {})
                    path = item.get("path") or "/"
                    url = f"{base}{path}?{qs}" if qs else f"{base}{path}"
                    status, body = _fetch(url, proxy_timeout)
                    return item.get("id"), {"status": status, "body": body}

                with concurrent.futures.ThreadPoolExecutor(max_workers=batch_workers) as ex:
                    results = dict(ex.map(one, requests))
                self._json(200, {"results": results})
                return

            if parsed.path == "/proxy":
                target = payload.get("url")
                body = payload.get("body")
                if not target:
                    self._json(400, {"result": "ERROR", "message": "missing url"})
                    return
                data = json.dumps(body).encode() if body is not None else None
                status, resp = _fetch(target, proxy_timeout, method="POST", body=data,
                                      content_type="application/json")
                self._json(status, resp)
                return

            self._json(404, {"result": "ERROR", "message": "not found"})

        def log_message(self, fmt: str, *args) -> None:
            sys.stderr.write(f"{self.address_string()} - {fmt % args}\n")

    return Handler


class ThreadedServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    allow_reuse_address = True
    daemon_threads = True


def serve(host: str, port: int,
          proxy_timeout: float = PROXY_TIMEOUT_DEFAULT,
          batch_workers: int = BATCH_WORKERS_DEFAULT) -> None:
    """Start the dashboard HTTP server.

    Blocks until interrupted.
    """
    os.chdir(_static_dir())
    handler_cls = make_handler(proxy_timeout, batch_workers)
    with ThreadedServer((host, port), handler_cls) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass
