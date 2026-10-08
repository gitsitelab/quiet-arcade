# Quiet Arcade

Four small arcade games for your phone, in one page: Drift Defense, Fracture Field, Layline and Upstream.

Play: https://gitsitelab.github.io/quiet-arcade/

## How this repository works

- `src/part*.html` are slices of the game page. The build joins them into `index.html`
  and checks the result against `src/index.sha256`, so a broken upload never goes live.
- `tools/make_icons.py` draws the home-screen icons during the build.
- `.github/workflows/pages.yml` publishes everything to GitHub Pages on each change to `main`.
- When the game changes, also bump `VERSION` in `sw.js` so saved copies on phones update.
