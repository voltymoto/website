#!/usr/bin/env python3
"""
Volty site generator.
  python3 pages.py            -> builds every page into dist/

SOURCE OF TRUTH lives here and in site/. dist/*.html is BUILD OUTPUT.
Do not hand-edit dist/. Edit site/ + this file, then rebuild.

  site/css/base.css    shared stylesheet (extracted from the original build)
  site/css/hero.css    interactive hero engine styles
  site/js/app.js       nav, reveal-on-scroll, index hero tilt
  site/js/hero.js      interactive hero engine
  site/js/i18n.js      EN/VI DOM walker
  site/vi.json         EN -> VI string map
  site/assets/*        images, inlined as data URIs at build time
  site/content/*.html  page bodies; reference images as {{asset:name}}
"""
import base64, json, mimetypes, pathlib, re, sys

ROOT = pathlib.Path(__file__).parent
SITE = ROOT / "site"
DIST = ROOT / "dist"

# --------------------------------------------------------------------------
# assets
# --------------------------------------------------------------------------
MANIFEST = json.loads((SITE / "assets/manifest.json").read_text())
_cache = {}

def asset(name: str) -> str:
    if name not in _cache:
        fn = MANIFEST.get(name)
        if not fn:
            raise KeyError(f"unknown asset '{name}' (see site/assets/manifest.json)")
        path = SITE / "assets" / fn
        mime = mimetypes.guess_type(fn)[0] or "application/octet-stream"
        if fn.endswith(".svg"):
            mime = "image/svg+xml"
        b64 = base64.b64encode(path.read_bytes()).decode()
        _cache[name] = f"data:{mime};base64,{b64}"
    return _cache[name]

def inline_assets(html: str) -> str:
    return re.sub(r"\{\{asset:([a-z0-9\-]+)\}\}", lambda m: asset(m.group(1)), html)

# --------------------------------------------------------------------------
# nav  (routing lives in ONE place)
# --------------------------------------------------------------------------
NAV = [
    ("Vision",     "vision.html",      "page"),
    ("Design",     "design.html",      "page"),
    ("Difference", "difference.html",  "page"),
    ("Vehicle",    "vehicle.html",     "page"),
    ("Technology", "technology.html",  "page"),
    ("Audience",   "audience.html",    "page"),
]
ECON = [
    ("Fleet Economics", "fleet-economics.html", "Per rider"),
    ("Fleet TCO",       "fleet-tco.html",       "Per unit, 3 year"),
]

def nav_html(slug: str) -> str:
    home = slug == "index"
    links = []
    for label, href, kind in NAV:
        cls = ' class="on"' if href == f"{slug}.html" else ""
        links.append(f'<a href="{href}"{cls}>{label}</a>')
    dd = "".join(
        f'<a href="{h}"><b>{t}</b><span class="eyebrow" style="color:var(--faint)">{s}</span></a>'
        for t, h, s in ECON
    )
    contact = "contact.html"
    brand = "index.html"
    return f'''<nav id="nav"><a class="brand" href="{brand}"><span class="mk"></span>VOLTY</a>
<div class="navlinks">{''.join(links)}
<div class="dd" id="dd"><button type="button">Economics <svg viewBox="0 0 10 10" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M1 3l4 4 4-4"/></svg></button><div class="ddmenu">{dd}</div></div>
<span class="cfg-soon" data-soon="Coming Soon">Configure</span></div>
<div class="navr"><a class="navcta" href="{contact}">Contact</a>
<div class="langsw" role="group" aria-label="Language"><button class="lb on" data-l="en" onclick="__setLang('en')">EN</button><button class="lb" data-l="vi" onclick="__setLang('vi')">VI</button></div>
<button class="burger" id="burger" aria-label="Menu"><span></span><span></span><span></span></button></div></nav>
<div class="mpanel" id="mpanel">{''.join(f'<a href="{h}">{l}</a>' for l,h,k in NAV)}
{''.join(f'<a href="{h}" class="sub">Economics / {t}</a>' for t,h,_ in ECON)}
<span class="mpanel-soon">Configure <i>Coming Soon</i></span><a href="{contact}">Contact</a></div>'''

# --------------------------------------------------------------------------
# hero renderers
# --------------------------------------------------------------------------
def hero_head(p):
    crumb = p.get("crumb", "")
    crumb_html = f'<div class="xh-crumb"><a href="index.html">Volty</a> / {crumb}</div>' if crumb else ""
    return f'''<div class="xh-head">{crumb_html}
    <h1>{p["h1"]}</h1>
    <p class="lead">{p["lead"]}</p>
  </div>'''

def render_hotspot(p):
    h = p["hero"]
    spots = "".join(
        f'<button class="xh-spot" style="left:{s["x"]};top:{s["y"]}" aria-label="{s["t"]}"><i></i></button>'
        for s in h["spots"]
    )
    rail = "".join(f'<button type="button">{s["t"]}</button>' for s in h["spots"])
    return f'''<section class="xhero"><div class="xh-aura"></div><div class="xh-grid"></div><div class="wrap">
  {hero_head(p)}
  <div class="xh-stage">
    <div class="xh-floor"></div>
    <div class="xh-plate">
      <img class="xh-bike" src="{{{{asset:{h["img"]}}}}}" alt="{h["alt"]}">
      <div class="xh-spots">{spots}</div>
      <div class="xh-card"><span class="k"></span><b></b><p></p><span class="m"></span></div>
    </div>
  </div>
  <div class="xh-rail">{rail}</div>
  <div class="xh-hint">Hover a point to inspect. <b>Click to pin.</b></div>
</div></section>'''

def render_swap(p):
    h = p["hero"]
    nets = "".join(
        f'''<button class="xh-net" type="button"><span class="dot"></span><span class="t"><b>{n["name"]}</b><span>{n["desc"]}</span></span><span class="s">{n["status"]}</span></button>'''
        for n in h["nets"]
    )
    cells = "".join(
        f'<rect class="xh-cell" x="{18+i*13}" y="12" width="9" height="34" rx="1" fill="var(--red)" opacity=".3"/>'
        for i in range(4)
    )
    pack = lambda cls, x: f'''<g class="xh-pack {cls}" transform="translate({x},0)">
      <rect x="0" y="0" width="76" height="112" rx="4" fill="#141418" stroke="var(--line2)"/>
      <rect x="8" y="8" width="60" height="42" rx="2" fill="#08080a" stroke="rgba(255,255,255,.06)"/>
      <g transform="translate(2,0)">{cells}</g>
      <rect x="8" y="60" width="60" height="6" rx="3" fill="rgba(255,255,255,.10)"/>
      <rect x="8" y="72" width="38" height="6" rx="3" fill="rgba(255,255,255,.06)"/>
      <circle cx="60" cy="90" r="7" fill="none" stroke="var(--red)" stroke-width="1.6"/>
      <path d="M57 90h6M60 87v6" stroke="var(--red)" stroke-width="1.6"/>
    </g>'''
    return f'''<section class="xhero"><div class="xh-aura"></div><div class="xh-grid"></div><div class="wrap">
  {hero_head(p)}
  <div class="xh-swap">
    <div>
      <div class="xh-bay">
        <svg viewBox="0 0 380 210" role="img" aria-label="Battery bay with two swappable packs">
          <rect x="8" y="150" width="364" height="52" rx="3" fill="#0e0e11" stroke="var(--line)"/>
          <text x="20" y="181" font-family="Space Mono, monospace" font-size="11" fill="#6c6c73" letter-spacing="2">CHASSIS / BAY</text>
          <rect x="118" y="24" width="184" height="126" rx="4" fill="none" stroke="var(--line)" stroke-dasharray="4 5"/>
          {pack("p1", 124)}
          {pack("p2", 212)}
        </svg>
        <div class="xh-timer"><span>Swap elapsed</span><b>0:00</b></div>
        <div class="xh-bar"><i></i></div>
      </div>
    </div>
    <div>
      <div class="xh-nets">{nets}</div>
      <button class="xh-swapbtn" type="button">Run a swap</button>
    </div>
  </div>
</div></section>'''

def render_segments(p):
    h = p["hero"]
    segs = "".join(f'<button class="xh-seg" type="button">{s["name"]}</button>' for s in h["segments"])
    spots = "".join(
        f'<button class="xh-spot" style="left:{s["x"]};top:{s["y"]}" aria-label="{s["t"]}" tabindex="-1"><i></i></button>'
        for s in h["rig"]
    )
    outs = "".join('<div><span></span><b data-v="0">0</b></div>' for _ in range(4))
    return f'''<section class="xhero"><div class="xh-aura"></div><div class="xh-grid"></div><div class="wrap">
  {hero_head(p)}
  <div class="xh-segs">{segs}</div>
  <div class="xh-stage">
    <div class="xh-floor"></div>
    <div class="xh-plate">
      <img class="xh-bike" src="{{{{asset:{h["img"]}}}}}" alt="{h["alt"]}">
      <div class="xh-spots">{spots}</div>
    </div>
  </div>
  <div class="xh-readout">{outs}</div>
  <p class="xh-segnote"></p>
</div></section>'''

def render_still(p):
    h = p["hero"]
    if not h.get("img"):
        return f'''<section class="xhero"><div class="xh-aura"></div><div class="xh-grid"></div><div class="wrap">
  <div class="xh-textonly">{hero_head(p)}</div>
</div></section>'''
    return f'''<section class="xhero"><div class="xh-aura"></div><div class="xh-grid"></div><div class="wrap">
  {hero_head(p)}
  <div class="xh-still"><div class="xh-plate"><img src="{{{{asset:{h["img"]}}}}}" alt="{h["alt"]}"></div></div>
</div></section>'''

RENDER = {"hotspot": render_hotspot, "swap": render_swap,
          "segments": render_segments, "still": render_still}

def hero_config(p):
    h = dict(p["hero"])
    h.pop("img", None); h.pop("alt", None)
    if p["hero"]["mode"] == "segments":
        h["rig"] = None  # positions already in DOM; JS only needs the index lists
        h = {k: v for k, v in h.items() if v is not None}
    return json.dumps(h, ensure_ascii=False, separators=(",", ":"))

# --------------------------------------------------------------------------
# reading order  (drives the prev/next pager)
# --------------------------------------------------------------------------
ORDER = [
    ("index",           "Intro"),
    ("vision",          "Vision"),
    ("design",          "Design"),
    ("difference",      "Difference"),
    ("vehicle",         "Vehicle"),
    ("technology",      "Technology"),
    ("audience",        "Audience"),
    ("fleet-economics", "Fleet Economics"),
    ("fleet-tco",       "Fleet TCO"),
    ("contact",         "Contact"),
]

def pager(slug):
    slugs = [s for s, _ in ORDER]
    if slug not in slugs:
        return ""
    i = slugs.index(slug)
    prev = ORDER[i - 1] if i > 0 else None
    nxt  = ORDER[i + 1] if i < len(ORDER) - 1 else None
    l = (f'<a class="prev" href="{prev[0]}.html"><span class="k">&larr; Previous</span><b>{prev[1]}</b></a>'
         if prev else '<div class="sp"></div>')
    r = (f'<a class="next" href="{nxt[0]}.html"><span class="k">Next &rarr;</span><b>{nxt[1]}</b></a>'
         if nxt else '<div class="sp"></div>')
    return f'<section class="pager"><div class="wrap">{l}{r}</div></section>'

# --------------------------------------------------------------------------
# page shell
# --------------------------------------------------------------------------
BASE_CSS = (SITE / "css/base.css").read_text()
HERO_CSS = (SITE / "css/hero.css").read_text()
APP_JS   = (SITE / "js/app.js").read_text()
HERO_JS  = (SITE / "js/hero.js").read_text()
I18N_JS  = (SITE / "js/i18n.js").read_text()
VI       = json.loads((SITE / "vi.json").read_text())
FOOTER   = (SITE / "content/_footer.html").read_text()
CONTACT  = (SITE / "content/_s_contact.html").read_text()

def build(p):
    slug = p["slug"]
    body = (SITE / "content" / f"{slug}.html").read_text()
    hero = RENDER[p["hero"]["mode"]](p) if p.get("hero") else ""
    hero_js = ""
    if p.get("hero"):
        hero_js = f"<script>window.__HERO={hero_config(p)};</script>\n<script>{HERO_JS}</script>"

    html = f'''<!doctype html><html lang="en"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="{p['desc']}">
<meta property="og:site_name" content="VOLTY">
<meta property="og:title" content="{p['title']}">
<meta property="og:description" content="{p['desc']}">
<meta property="og:type" content="website">
<title>{p['title']}</title>
<link rel="icon" type="image/png" sizes="32x32" href="{{{{asset:favicon-63ca}}}}">
<link rel="icon" type="image/svg+xml" href="{{{{asset:favicon-677d}}}}">
<link rel="apple-touch-icon" href="{{{{asset:favicon-bd35}}}}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Saira+Condensed:wght@500;600;700;800;900&family=Sora:wght@300;400;500;600;700&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>{BASE_CSS}
{HERO_CSS}</style></head><body>
{nav_html(slug)}
{hero}
{body}
{pager(slug)}
{FOOTER}
<script>{APP_JS}</script>
{hero_js}
<script>var __VI={json.dumps(VI, ensure_ascii=False)};
{I18N_JS}</script>
</body></html>'''
    return inline_assets(html)

# --------------------------------------------------------------------------
# PAGE DEFINITIONS
# --------------------------------------------------------------------------
from page_defs import PAGES   # noqa: E402

def main():
    DIST.mkdir(exist_ok=True)
    total = 0
    for p in PAGES:
        out = build(p)
        f = DIST / f"{p['slug']}.html"
        f.write_text(out)
        kb = len(out) // 1024
        total += kb
        print(f"  {f.name:<22} {kb:>5} KB")
    print(f"  {'total':<22} {total:>5} KB")

if __name__ == "__main__":
    main()
