"""Draws the app icons: a plate with a fork and a knife. Run once; the PNGs are kept in
the repository. Needs Pillow.

    python make_icons.py

Two kinds are made. "icon" fills the square and is used as it is. "maskable" keeps the
drawing inside the middle of the square, because Android cuts launcher icons to a circle,
a squircle or another shape, and anything outside the central 80% may be lost.
"""
import os
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
BACKGROUND = (27, 175, 122)     # the app's green
WHITE = (255, 255, 255)
SCALE = 4                       # draw large, then shrink, for smooth edges
MASKABLE_SCALE = 0.66           # the drawing spans 19..91 of 100; this brings it within 26..74


def draw_icon(size, shrink=1.0):
    s = size * SCALE
    img = Image.new("RGB", (s, s), BACKGROUND)
    d = ImageDraw.Draw(img)
    u = s / 100 * shrink        # the design is laid out on a 100 x 100 grid
    ox = (s - 110 * u) / 2      # the drawing's own centre is at x = 55, y = 50
    oy = (s - 100 * u) / 2

    def box(x0, y0, x1, y1):
        return [ox + x0 * u, oy + y0 * u, ox + x1 * u, oy + y1 * u]

    # plate: a ring
    d.ellipse(box(34, 31, 72, 69), outline=WHITE, width=round(4.5 * u))

    # fork, left of the plate: three tines, a neck and a handle
    for x in (20.5, 24.5, 28.5):
        d.rounded_rectangle(box(x - 1.1, 27, x + 1.1, 43), radius=1.1 * u, fill=WHITE)
    d.rounded_rectangle(box(19.4, 40, 29.6, 46), radius=3 * u, fill=WHITE)
    d.rounded_rectangle(box(22.7, 43, 26.3, 73), radius=1.8 * u, fill=WHITE)

    # knife, right of the plate: a blade and a handle
    d.pieslice(box(77, 27, 91, 71), start=90, end=270, fill=WHITE)
    d.rounded_rectangle(box(82.2, 47, 85.8, 73), radius=1.8 * u, fill=WHITE)

    return img.resize((size, size), Image.LANCZOS)


for size in (192, 512):
    for name, shrink in (("icon", 1.0), ("maskable", MASKABLE_SCALE)):
        path = os.path.join(HERE, f"{name}-{size}.png")
        draw_icon(size, shrink).save(path, optimize=True)
        print("wrote", path)
