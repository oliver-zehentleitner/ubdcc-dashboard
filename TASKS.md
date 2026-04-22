# TASKS — ubdcc-dashboard

Open development tasks and decisions. Grows and shrinks as things land.

---

## Open

- **Bulk endpoint `/get_all_depthcaches?levels=N`** in `ubdcc-restapi`:
  one request instead of `2 × N` for a full refresh. Unlocks sub-300 ms
  refresh even for clusters with hundreds of DCs. Server side still needs
  discussion (DCN-side optimisations, payload shape) — once it lands on
  the cluster side, switch the dashboard's polling path.

## Ideas (not committed)

- Auth token header for the proxy, enforced when `--host` is not a
  loopback address.
- Per-exchange credential groups quick-view.
- Remote config persistence (save DCC-URL + filters in localStorage).
