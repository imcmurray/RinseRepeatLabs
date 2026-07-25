# Rinse Repeat Labs — Droplet brand

A new brand direction: a monoline **water droplet** (rinse) holding a **refresh
loop** (repeat), flanked by code **`{ }` braces** (labs / dev). Clean line-art,
single weight, no effects.

This is a self-contained set and does **not** replace the infinity-wave brand in
`../brand/`. Keep whichever you decide to ship; delete the other folder when you
commit to one.

## Colors

| Role                  | Hex       |
|-----------------------|-----------|
| Navy (droplet/braces) | `#102f4b` |
| Cyan (loop accent)    | `#1ea4d9` |
| Ink (mono)            | `#0f0f0f` |

**Color treatment (two-tone "A"):** navy droplet + navy braces, with the
**cyan reserved for the loop** — the accent lands on the "repeat." Wordmark is
navy. The glyph (favicon) is a solid navy droplet with a cyan loop.

Wordmark: **Adwaita Sans, weight 500**, outlined to paths (no font install
needed). Weight 500 is chosen to match the icon's monoline stroke — don't pair
this icon with a heavy wordmark, it breaks the balance.

## What to use when

```
Primary (color) ................ rrl-lockup-color.svg
One-ink / print ................ rrl-lockup-black.svg  /  rrl-lockup-white.svg
Icon only (line-art) ........... rrl-icon-color / -black / -white .svg
Favicon / app icon / avatar .... rrl-glyph-* .svg   (bold solid cut — see note)
Wordmark alone ................. rrl-wordmark-color / -black / -white .svg
```

### Icon vs. glyph — important
The **icon** (`rrl-icon-*`) is the full line-art lockup element: droplet + loop
+ braces. Its thin strokes and detached braces **fall apart below ~32px**, which
is normal for line-art. So small sizes use the **glyph** (`rrl-glyph-*`): a
**solid** droplet with the loop reversed out and the braces dropped. That solid
cut stays crisp down to 16px. Use the icon large, the glyph small — never shrink
the line-art icon into a favicon.

## Files

### Vector (prefer these)
- `rrl-lockup-color.svg` — **primary.** Icon + wordmark, cyan.
- `rrl-lockup-black.svg`, `rrl-lockup-white.svg` — one-color.
- `rrl-icon-color/black/white.svg` — line-art icon only.
- `rrl-glyph-color/black/white.svg` — solid droplet cut (square) for small sizes.
- `rrl-wordmark-color/black/white.svg` — wordmark only (outlined).

### Raster (`png/`)
Transparent exports for slides/social where SVG isn't accepted:
lockup (2000/1000, + black & white 2000), icon 1200, wordmark 2000.

### Web icons (`favicon/`)
- `favicon.ico` (16/32/48), `favicon-16/32/48.png`
- `apple-touch-icon-180.png` — white droplet + cyan loop on a navy tile
- `icon-512.png` — PWA / large app icon

```html
<link rel="icon" href="/media/brand-droplet/favicon/favicon.ico" sizes="any">
<link rel="icon" type="image/svg+xml" href="/media/brand-droplet/rrl-glyph-color.svg">
<link rel="apple-touch-icon" href="/media/brand-droplet/favicon/apple-touch-icon-180.png">
```

## Rules
- Keep clear space around the lockup ≥ the cap-height of the wordmark.
- Don't use `rrl-lockup-color` below ~140px wide — switch to the glyph.
- Never add shadows, gradients, or a second wordmark weight.
- The braces are part of the icon's balance — don't spread them further apart.

## Regenerating
The icon geometry is parametric. Sources in the build scratchpad:
`concept.py` (droplet / refresh / brace path math) and
`build_final_concept.py` (assembles every variant). Re-run to change stroke
weight, brace spacing, or colors, then re-export PNGs/favicons with the same
`rsvg-convert` / `magick` commands used here.
