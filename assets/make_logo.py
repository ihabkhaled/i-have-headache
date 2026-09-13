"""Draw the i-have-headache logo: a man holding his head.

Run: python assets/make_logo.py
Writes assets/logo.png (512) and assets/composer-icon.png (256), both square.
Drawn at 4x and downsampled, which is what gives the edges their smoothness.
"""
from PIL import Image, ImageDraw

S = 1024          # design space
F = 4             # supersample factor
W = S * F

def p(*xy):       # scale design coords to render coords
    return tuple(v * F for v in xy)

def box(cx, cy, rx, ry):
    return p(cx - rx, cy - ry, cx + rx, cy + ry)

BG_TOP    = (62, 48, 104)
BG_BOT    = (32, 25, 58)
SKIN      = (240, 193, 152)
SKIN_DARK = (206, 156, 116)
HAIR      = (48, 36, 44)
SHIRT     = (99, 91, 214)
SHIRT_DK  = (74, 67, 173)
THROB     = (255, 106, 92)
INK       = (58, 40, 52)

img = Image.new("RGB", (W, W), BG_BOT)
d = ImageDraw.Draw(img)

# background gradient
for y in range(W):
    t = y / (W - 1)
    d.line([(0, y), (W, y)], fill=tuple(
        round(a + (b - a) * t) for a, b in zip(BG_TOP, BG_BOT)))

# throbbing pain arcs, behind everything
for cx, a0, a1 in ((196, 148, 256), (828, 284, 392)):
    for i, r in enumerate((58, 104, 150)):
        d.arc(box(cx, 286, r, r), a0, a1, fill=THROB,
              width=round(16 * F * (1 - i * 0.18)))

# shoulders
d.rounded_rectangle(p(168, 828, 856, 1120), radius=150 * F, fill=SHIRT)

# arms: upper arm in sleeve, forearm bare, hand at the temple
for sx, ex, wx in ((300, 205, 300), (724, 819, 724)):
    d.line([p(sx, 880), p(ex, 690)], fill=SHIRT_DK, width=92 * F, joint="curve")
    d.line([p(ex, 690), p(wx, 566)], fill=SKIN, width=74 * F, joint="curve")

# neck and head
d.rounded_rectangle(p(456, 690, 568, 850), radius=44 * F, fill=SKIN_DARK)
d.ellipse(box(512, 520, 175, 200), fill=SKIN)

# hair: top half of a slightly larger head, then the forehead drawn back over it
d.pieslice(box(512, 520, 181, 206), 180, 360, fill=HAIR)
d.ellipse(box(512, 555, 166, 178), fill=SKIN)

# eyes squeezed shut
for a, b, c in ((392, 428, 464), (632, 596, 560)):
    d.line([p(a, 516), p(b, 486), p(c, 516)], fill=INK,
           width=15 * F, joint="curve")

# brows angled down and in
d.line([p(378, 448), p(468, 476)], fill=HAIR, width=18 * F, joint="curve")
d.line([p(646, 448), p(556, 476)], fill=HAIR, width=18 * F, joint="curve")

# grimace
d.arc(box(512, 640, 52, 34), 200, 340, fill=INK, width=14 * F)

# hands clamped over the temples
for mirror in (False, True):
    def mx(x):
        return 1024 - x if mirror else x
    d.ellipse(box(mx(332), 524, 68, 86), fill=SKIN)
    for y0, y1, x0, x1 in ((466, 430, 330, 404),
                           (500, 470, 338, 416),
                           (534, 510, 344, 412)):
        d.line([p(mx(x0), y0), p(mx(x1), y1)], fill=SKIN,
               width=27 * F, joint="curve")
        d.line([p(mx(x0), y0 + 15), p(mx(x1), y1 + 14)], fill=SKIN_DARK,
               width=3 * F, joint="curve")

for size, name in ((512, "logo.png"), (256, "composer-icon.png")):
    img.resize((size, size), Image.LANCZOS).save(f"assets/{name}")
    print(f"assets/{name}  {size}x{size}")
