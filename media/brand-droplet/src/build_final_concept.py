import re, os
import concept as C

CYAN, NAVY, BLACK, WHITE = "#1ea4d9", "#102f4b", "#0f0f0f", "#ffffff"
OUT = "concept_out"; os.makedirs(OUT, exist_ok=True)

# Two-tone "A": navy droplet + navy braces + cyan loop accent, navy wordmark.
ICON_VB = "230 140 540 480"
def icon_body(drop, brace, loop, sw=13):
    dcx, dcy, R, apex = 500, 372, 118, 168
    return "\n".join([
        C.droplet(dcx, dcy, R, apex, sw, drop),
        C.brace(360, dcy, 150, 34, 40, sw, brace, True),
        C.brace(640, dcy, 150, 34, 40, sw, brace, False),
        C.refresh(dcx, 368, 60, loop, mode="solid", hw=14),  # solid arrows, identical to the glyph
    ])

# per-variant (droplet, braces, loop, wordmark)
VARIANTS = {
    "color": (NAVY, NAVY, CYAN, NAVY),
    "black": (BLACK, BLACK, BLACK, BLACK),
    "white": (WHITE, WHITE, WHITE, WHITE),
}
# glyph (solid favicon cut): (droplet_fill, loop_color)
GLYPH = {"color": (NAVY, CYAN), "black": (BLACK, WHITE), "white": (WHITE, CYAN)}

def droplet_filled(cx, cy, R, apex_y, fill):
    d = re.search(r'd="([^"]+)"', C.droplet(cx, cy, R, apex_y, 0, "x")).group(1)
    return f'<path d="{d}" fill="{fill}" stroke="none"/>'

WMC = open("_wmc_paths.svg").read().strip()
WM_VB = "22.77 30.36 1159.52 140.26"
def wm(color):
    s = re.sub(r'fill:#[0-9a-fA-F]{6}', f'fill:{color}', WMC)
    s = re.sub(r'fill="#[0-9a-fA-F]{6}"', f'fill="{color}"', s)
    return f'<g fill="{color}">{s}</g>'

def svg(vb, w, h, body):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" width="{w}" height="{h}">\n{body}\n</svg>\n'
def write(name, body):
    open(os.path.join(OUT, name), "w").write(body); print("wrote", name)

for k, (drop, brace, loop, wcol) in VARIANTS.items():
    write(f"rrl-icon-{k}.svg", svg(ICON_VB, 540, 480, icon_body(drop, brace, loop)))
    write(f"rrl-wordmark-{k}.svg", svg(WM_VB, 1160, 141, wm(wcol)))
    IW, IH = 300, 295; IX = 450-IW/2; IY = 60
    TW, TH = 470, 56.8; TX = 450-TW/2; TY = IY+IH+45
    lb = (f'<svg x="{IX}" y="{IY}" width="{IW}" height="{IH}" viewBox="{ICON_VB}">{icon_body(drop,brace,loop)}</svg>\n'
          f'<svg x="{TX:.1f}" y="{TY}" width="{TW}" height="{TH:.1f}" viewBox="{WM_VB}">{wm(wcol)}</svg>')
    write(f"rrl-lockup-{k}.svg", svg("0 0 900 520", 900, 520, lb))

# glyphs (bold favicon cut)
FAV_VB = "313.25 142.25 373.5 373.5"
for k, (drop, loop) in GLYPH.items():
    # solid barbed arrows, centered in the bulb (cy 368), confident size
    body = droplet_filled(500, 372, 118, 168, drop) + "\n" + C.refresh(500, 368, 60, loop, mode="solid", hw=14)
    write(f"rrl-glyph-{k}.svg", svg(FAV_VB, 512, 512, body))
print("done")
