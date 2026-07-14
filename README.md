# Volty site build system

`dist/` is BUILD OUTPUT. Do not hand-edit it. Edit `build/`, then rebuild.

## Rebuild

    cd build && python3 pages.py      # writes ../dist/*.html

## Where things live

| File | What it is |
|---|---|
| `pages.py` | The generator. Shell, nav routing, hero renderers, asset inlining. |
| `page_defs.py` | Page copy and hero configuration. **Most edits go here.** |
| `site/content/*.html` | Page bodies. Reference images as `{{asset:name}}`. |
| `site/css/base.css` | Shared stylesheet (extracted from the original build). |
| `site/css/hero.css` | Interactive hero engine styles. |
| `site/js/hero.js` | Interactive hero engine (3 modes). |
| `site/js/app.js` | Nav, reveal-on-scroll, index hero tilt. |
| `site/js/i18n.js` | EN/VI DOM walker. |
| `site/vi.json` | EN -> VI strings. Keys must be the TRIMMED text node. |
| `site/assets/` | Images. Inlined as data URIs at build time. |

## Nav routing
Defined once in `pages.py` (`NAV`, `ECON`). Change it there, rebuild, every page updates.

## Hero modes
- `hotspot`  vehicle.html    Hover/click points on the bike, callout cards.
- `swap`     technology.html Animated pack ejection, live timer, network picker.
- `segments` audience.html   Fleet segment switcher, animated stat readouts.

## Known gap
`fleet-economics.html` and `fleet-tco.html` are still hand-built and sit OUTSIDE the
generator. Their nav has been patched to route to the new pages, but a future nav
change will not reach them automatically. Fold them into `page_defs.py` next.
