# TASKS — ubdcc-dashboard

Open development tasks and decisions. Grows and shrinks as things land.

---

## Open

- **CORS middleware in `ubdcc-restapi`** (upstream UBDCC): when
  `ubdcc-restapi` sends `Access-Control-Allow-Origin: *` (behind a config
  flag), this dashboard can run as a pure static `index.html` — no Python
  proxy needed. The bundled `server.py` would then become an optional dev
  launcher. Ship as an opt-in flag on the cluster side.
- **Bulk endpoint `/get_all_depthcaches?levels=N`** in `ubdcc-restapi`:
  one request instead of `2 × N` for a full refresh. Unlocks sub-300 ms
  refresh even for clusters with hundreds of DCs.
- **Docker image** for quick one-liner deployments.
- **Documentation**: Sphinx scaffolding exists; fill it with a real
  user-guide once the CLI stabilises.

## Ideas (not committed)

- Auth token header for the proxy, enforced when `--host` is not a
  loopback address.
- Per-exchange credential groups quick-view.
- Remote config persistence (save DCC-URL + filters in localStorage).
