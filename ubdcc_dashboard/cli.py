"""UBDCC Dashboard command-line interface."""
from __future__ import annotations

import argparse
import os
import sys
import threading
import webbrowser

from . import __version__
from .server import serve, PROXY_TIMEOUT_DEFAULT, BATCH_WORKERS_DEFAULT

DEFAULT_HOST = "127.0.0.1"
DEFAULT_PORT = 8080


def _hyperlink(url: str, text: str | None = None) -> str:
    """Emit an OSC 8 clickable hyperlink if the terminal supports it."""
    text = text or url
    if os.environ.get("NO_COLOR") or not sys.stdout.isatty():
        return url
    return f"\033]8;;{url}\033\\{text}\033]8;;\033\\"


def _parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="ubdcc-dashboard",
        description="Browser-based live dashboard for the UNICORN Binance DepthCache Cluster (UBDCC).",
    )
    p.add_argument("-V", "--version", action="version",
                   version=f"ubdcc-dashboard {__version__}")
    sub = p.add_subparsers(dest="command", metavar="COMMAND")

    start = sub.add_parser("start", help="Start the local dashboard server.")
    start.add_argument("--host", default=DEFAULT_HOST,
                       help=(f"Interface to bind. Default: {DEFAULT_HOST} (localhost only, "
                             f"secure). Use 0.0.0.0 to expose on the network."))
    start.add_argument("--port", type=int, default=DEFAULT_PORT,
                       help=f"TCP port to listen on. Default: {DEFAULT_PORT}.")
    start.add_argument("--no-browser", action="store_true",
                       help="Do not auto-open the dashboard in the default browser.")
    start.add_argument("--proxy-timeout", type=float, default=PROXY_TIMEOUT_DEFAULT,
                       help=f"CORS-proxy fetch timeout in seconds. Default: {PROXY_TIMEOUT_DEFAULT}.")
    start.add_argument("--batch-workers", type=int, default=BATCH_WORKERS_DEFAULT,
                       help=f"Worker threads for /proxy_batch. Default: {BATCH_WORKERS_DEFAULT}.")

    return p


def _cmd_start(args: argparse.Namespace) -> int:
    # Host resolution for user-facing URL (keep 127.0.0.1 if bound to loopback,
    # use localhost for 0.0.0.0 so the link is clickable locally).
    shown_host = "localhost" if args.host in ("0.0.0.0", "::") else args.host
    url = f"http://{shown_host}:{args.port}/"

    banner = (
        f"UBDCC Dashboard {__version__}\n"
        f"Serving on {_hyperlink(url)}\n"
        f"Bound to {args.host}:{args.port}"
        + ("  (localhost only — use --host 0.0.0.0 to expose)" if args.host in ("127.0.0.1", "::1") else "")
        + "\nPress Ctrl+C to stop."
    )
    print(banner, flush=True)

    if not args.no_browser:
        threading.Timer(0.4, lambda: webbrowser.open(url)).start()

    try:
        serve(host=args.host, port=args.port,
              proxy_timeout=args.proxy_timeout,
              batch_workers=args.batch_workers)
    except OSError as e:
        print(f"error: {e}", file=sys.stderr)
        return 1
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = _parser()
    args = parser.parse_args(argv)

    if args.command == "start":
        return _cmd_start(args)

    parser.print_help()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
