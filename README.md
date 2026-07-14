# Volty site

Ten pages, one generator. `dist/` is BUILD OUTPUT. Do not hand-edit it.

## Rebuild
    cd build && python3 pages.py     # writes ../dist/*.html

## Information architecture

Index is an INTRO, not a scroll. It carries the hero, the positioning thesis,
"Why Now" (the regulatory forcing function), a directory into the site, and a
pilot CTA. Everything else lives on its own page.

Reading order (drives the prev/next pager, defined once in `pages.py` -> `ORDER`):

    index -> vision -> design -> difference -> vehicle -> technology
          -> audience -> fleet-economics -> fleet-tco -> contact

| Page | Hero | Content |
|---|---|---|
| index | bespoke bike hero | thesis, Why Now, directory, CTA |
| vision | still (side profile) | What We Are Building |
| design | still (exploded view) | Every part earns its place |
| difference | still (clean bike) | Open vs closed ecosystem, market comparison |
| vehicle | **hotspot** | Specs, expandable system, ad panel, economics teaser |
| technology | **swap simulator** | Battery bay, swap cabinets |
| audience | **segment switcher** | Fleet gallery, partnership models |
| fleet-economics | (hand-built) | Per rider |
| fleet-tco | (hand-built) | Per unit, 3 year |
| contact | still (text) | Contact and collaboration |

## Where to edit
| File | What |
|---|---|
| `page_defs.py` | Page copy + hero config. **Most edits go here.** |
| `pages.py` | Generator: `NAV` routing, `ORDER` pager, hero renderers, asset inlining. |
| `site/content/*.html` | Page bodies. `_s_*.html` are the source sections. |
| `site/css/base.css` | Shared styles. |
| `site/css/hero.css` | Hero engine, pager, directory grid. |
| `site/js/hero.js` | Hero engine (hotspot / swap / segments). |
| `site/vi.json` | EN -> VI. Keys must be the TRIMMED text node, no trailing spaces. |
| `site/assets/` | Images, inlined as data URIs at build time. |

## Known gaps
1. `fleet-economics.html` and `fleet-tco.html` are still hand-built, OUTSIDE the
   generator. Their nav and pager are patched in post-build. Fold them into
   `page_defs.py` next.
2. `terms.html` and `privacy.html` are linked from the footer but do not exist.
   This predates the rebuild. Either write them or drop the footer links.
3. Assets are base64-inlined, which is why `design.html` is ~1.2 MB. Switching to
   linked files is a one-line change in `pages.py` (`asset()`).
