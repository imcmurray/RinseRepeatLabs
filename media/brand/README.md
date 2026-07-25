# Rinse Repeat Labs — brand assets

Canonical, cleaned-up logo set. **Use these files.** The loose assets in
`media/` (see "Legacy" below) are the older, effect-heavy versions and should be
retired.

## Colors

| Role        | Hex       |
|-------------|-----------|
| Cyan (wave) | `#1ea4d9` |
| Navy (loop) | `#102f4b` |
| Ink (mono)  | `#0f0f0f` |

Wordmark type is **Adwaita Sans, weight 800**. In these files the wordmark is
**outlined to paths**, so no font install is required to render them. Keep the
font name handy only if you need to re-typeset the wordmark from scratch.

## What to use when

```
Primary (color contexts) ....... rrl-lockup-color.svg
One-ink / print / etched ....... rrl-lockup-black.svg  /  rrl-lockup-white.svg
Icon only, wide framing ........ rrl-mark-color / -black / -white .svg
Icon only, square (favicon) .... rrl-glyph-* .svg
Wordmark alone ................. rrl-wordmark-black / -white .svg
```

### Mark vs. glyph
Same artwork, different framing. The **mark** (`rrl-mark-*`) is the logo cropped
tight to its natural landscape shape — use it where width is free. The **glyph**
(`rrl-glyph-*`) is the identical mark centered in a **square** canvas, for
favicons, app icons, and avatars. It stays fully your logo — wave, splash, and
two-tone intact — it's just squared up. (At 16px the fine splash detail softens,
which is unavoidable for a mark this detailed; it still reads as the infinity.)

## Files

### Vector (scalable — prefer these)
- `rrl-lockup-color.svg` — **primary.** Flat mark + navy wordmark, no effects.
- `rrl-lockup-black.svg`, `rrl-lockup-white.svg` — one-color lockups.
- `rrl-mark-color.svg`, `rrl-mark-black.svg`, `rrl-mark-white.svg` — mark only.
- `rrl-wordmark-black.svg`, `rrl-wordmark-white.svg` — wordmark only (outlined).
- `rrl-glyph-color.svg`, `rrl-glyph-black.svg`, `rrl-glyph-white.svg` — square glyph.

### Raster (`png/`)
Transparent-background exports for slides/social where SVG isn't accepted.
- `rrl-lockup-color-2000.png`, `-1000.png`
- `rrl-lockup-black-2000.png`, `rrl-lockup-white-2000.png`
- `rrl-mark-color-1600.png`
- `rrl-wordmark-black-2000.png`, `rrl-wordmark-white-2000.png`

### Web icons (`favicon/`)
- `favicon.ico` (16/32/48 bundled), `favicon-16.png`, `favicon-32.png`, `favicon-48.png`
- `apple-touch-icon-180.png` (white glyph on a navy tile — iOS ignores transparency)
- `icon-512.png` (PWA / large app icon)

Suggested HTML:
```html
<link rel="icon" href="/media/brand/favicon/favicon.ico" sizes="any">
<link rel="icon" type="image/svg+xml" href="/media/brand/rrl-glyph-color.svg">
<link rel="apple-touch-icon" href="/media/brand/favicon/apple-touch-icon-180.png">
```

## Clear space & min size
- Keep clear space around any lockup ≥ the height of the "R" in the wordmark.
- Don't place `rrl-lockup-color` below ~120px wide — use the glyph instead.
- Never re-add drop shadows, outlines, bevels, or multi-color wordmark fills.
  The flat two-tone reads because of value contrast; effects only weaken it.

## Legacy (retire)
These older files carried drop shadows, outlines, tri-color shadowed wordmarks,
"dpi"-named rasters, or live (non-outlined) text, and are superseded:
`infinite-cycle-logo-*.png`, `infinity-logo.svg`, `ship-it-logo.svg`,
the `RRL-Mono-*` / `RRL-*-1000/2000` raster stacks, and the `name-logo-*` /
`infinity-logo-mono-*` sources. Keep `while-true-logo.svg` as a fun
merch/sticker secondary — it's fine, just not a primary.
