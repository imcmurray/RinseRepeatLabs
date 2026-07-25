import math, sys

CYAN = "#1ea4d9"

def P(cx, cy, r, deg):
    a = math.radians(deg)
    return (cx + r*math.cos(a), cy + r*math.sin(a))

def f(x): return f"{x:.2f}"

def droplet(cx, cy, R, apex_y, sw, color):
    """Custom teardrop: rounded bottom circle, tapered apex. Sides meet circle
    tangentially (vertical) so the join is smooth. apex_y is the top point y."""
    apex = (cx, apex_y)
    left = (cx - R, cy)
    right = (cx + R, cy)
    # control points: near apex the curve leans out gently; near the circle sides
    # it must be vertical (cp directly above the side point) for a tangent meet.
    up = R * 0.62            # vertical control distance above side points
    ax = R * 0.30            # apex horizontal control spread
    ay = (cy - apex_y) * 0.42
    d = (f"M{f(apex[0])},{f(apex[1])} "
         # apex -> left side (arrives vertical)
         f"C{f(cx-ax)},{f(apex_y+ay)} {f(left[0])},{f(cy-up)} {f(left[0])},{f(left[1])} "
         # left -> around the bottom -> right
         f"A{f(R)},{f(R)} 0 0 0 {f(right[0])},{f(right[1])} "
         # right side -> apex (leaves vertical)
         f"C{f(right[0])},{f(cy-up)} {f(cx+ax)},{f(apex_y+ay)} {f(apex[0])},{f(apex[1])} Z")
    return f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{sw}" stroke-linejoin="round"/>'

def _arrow(cx, cy, rc, hw, As, Ah):
    """One curved-arrow silhouette (closed path), travelling clockwise from tail
    As to head at Ah. The arrowhead is a symmetric triangle about the tangent at
    Ah. The tail is bevel-cut parallel to the head's inner edge (which, by the
    180deg symmetry of the pair, is parallel to the *adjacent* arrow's head) so
    the two arrows nest along a clean diagonal instead of a blunt radial stub."""
    tiplen  = hw*2.6      # tip distance ahead of the head centre
    backlen = hw*0.7      # barbs sit slightly behind the head centre
    halfw   = hw*2.1      # barb half-width (wider than the band)
    gap     = 6           # band ends this many degrees before the head centre
    Ab = Ah - gap
    ro, ri = rc + hw, rc - hw
    a = math.radians(Ah)
    C  = P(cx, cy, rc, Ah)
    td = (-math.sin(a), math.cos(a))    # tangent (clockwise travel)
    nd = (math.cos(a),  math.sin(a))    # radial outward
    Hob = P(cx, cy, ro, Ab);  Hib = P(cx, cy, ri, Ab)
    TIP = (C[0]+td[0]*tiplen,               C[1]+td[1]*tiplen)
    Bo  = (C[0]-td[0]*backlen+nd[0]*halfw,  C[1]-td[1]*backlen+nd[1]*halfw)
    Bi  = (C[0]-td[0]*backlen-nd[0]*halfw,  C[1]-td[1]*backlen-nd[1]*halfw)
    # --- beveled tail ---
    # cut line passes through the tail centreline point Q, parallel to (TIP-Bi);
    # tail corners = where that line meets the outer/inner band circles.
    bx, by = TIP[0]-Bi[0], TIP[1]-Bi[1]
    bl = math.hypot(bx, by); dvec = (bx/bl, by/bl)
    ar = math.radians(As); e = (math.cos(ar), math.sin(ar))
    Q  = P(cx, cy, rc, As)
    edp = e[0]*dvec[0] + e[1]*dvec[1]
    def corner(R):
        disc = rc*rc*edp*edp - (rc*rc - R*R)
        if disc < 0:                       # line misses circle -> radial fallback
            return P(cx, cy, R, As)
        sq = math.sqrt(disc)
        s1, s2 = -rc*edp + sq, -rc*edp - sq
        s = s1 if abs(s1) < abs(s2) else s2   # nearest intersection to Q
        return (Q[0] + s*dvec[0], Q[1] + s*dvec[1])
    To = corner(ro);  Ti = corner(ri)
    large = 1 if abs(Ab-As) > 180 else 0
    return (f"M{f(To[0])},{f(To[1])} A{f(ro)},{f(ro)} 0 {large} 1 {f(Hob[0])},{f(Hob[1])} "
            f"L{f(Bo[0])},{f(Bo[1])} L{f(TIP[0])},{f(TIP[1])} L{f(Bi[0])},{f(Bi[1])} L{f(Hib[0])},{f(Hib[1])} "
            f"A{f(ri)},{f(ri)} 0 {large} 0 {f(Ti[0])},{f(Ti[1])} Z")

def refresh(cx, cy, rc, color, mode="solid", hw=None, sw=11):
    """Two curved arrows forming a sync/repeat ring, with clean symmetric heads.
    mode='solid' -> filled arrows (bold, for the glyph);
    mode='outline' -> contour only (line-art, for the icon)."""
    if hw is None: hw = rc*0.22
    top = _arrow(cx, cy, rc, hw, 205, 340)   # over the top, head lower-right
    bot = _arrow(cx, cy, rc, hw, 25, 160)    # under the bottom, head upper-left
    if mode == "solid":
        st = f'fill="{color}" stroke="none"'
    else:
        st = f'fill="none" stroke="{color}" stroke-width="{sw}" stroke-linejoin="round"'
    return f'<path d="{top}" {st}/>\n<path d="{bot}" {st}/>'

def brace(cx, cy, H, arm, nub, sw, color, left=True):
    """Monoline curly brace. Tips at top/bottom curl toward center; middle nub
    points outward. left=True draws '{' (tips point right, nub points left)."""
    s = 1 if left else -1          # s=+1: nub to the left, tips to the right
    tipx = cx + arm*s
    nubx = cx - nub*s
    spinex = cx
    yT, yB = cy - H, cy + H
    k = H*0.28
    d = (f"M{f(tipx)},{f(yT)} "
         f"C{f(spinex)},{f(yT)} {f(spinex)},{f(yT+k)} {f(spinex)},{f(cy-k)} "   # top tip -> spine down
         f"C{f(spinex)},{f(cy-k*0.35)} {f(nubx)},{f(cy-k*0.35)} {f(nubx)},{f(cy)} "  # spine -> nub
         f"C{f(spinex)},{f(cy+k*0.35)} {f(spinex)},{f(cy+k*0.35)} {f(spinex)},{f(cy+k)} "  # nub -> spine
         f"C{f(spinex)},{f(yB-k)} {f(spinex)},{f(yB)} {f(tipx)},{f(yB)}")             # spine down -> bottom tip
    return f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"/>'

def icon(color=CYAN, sw=13):
    cx = 500
    dcx, dcy, R, apex = 500, 372, 118, 168
    parts = [
        droplet(dcx, dcy, R, apex, sw, color),
        refresh(dcx, dcy+18, 46, sw, color),
        brace(360, dcy, 150, 34, 40, sw, color, left=True),
        brace(640, dcy, 150, 34, 40, sw, color, left=False),
    ]
    body = "\n".join(parts)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="230 140 540 480" width="540" height="480">\n'
            f'{body}\n</svg>\n')

if __name__ == "__main__":
    open("concept_icon.svg","w").write(icon())
    print("wrote concept_icon.svg")
