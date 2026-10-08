# Draws the home-screen icons: three shapes above the orange ship on the Night background.
import os
from PIL import Image, ImageDraw
BG, TXT, ACC = (0x14, 0x14, 0x13), (0xEC, 0xEA, 0xE3), (0xD9, 0x77, 0x57)
def icon(size, pad=0.0):
    S = 1024
    im = Image.new('RGB', (S, S), BG)
    d = ImageDraw.Draw(im)
    k, o = 1 - pad * 2, S * pad
    P = lambda x, y: (o + x * k, o + y * k)
    d.polygon([P(232, 330), P(392, 330), P(312, 458)], fill=TXT)
    cx, cy = P(512, 388); r = 70 * k
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=TXT)
    x0, y0 = P(642, 322); x1, y1 = P(782, 462)
    d.rectangle([x0, y0, x1, y1], fill=TXT)
    d.polygon([P(512, 560), P(712, 820), P(582, 756), P(442, 756), P(312, 820)], fill=ACC)
    return im.resize((size, size), Image.LANCZOS)
out = os.path.join('_site', 'icons'); os.makedirs(out, exist_ok=True)
icon(180).save(os.path.join(out, 'apple-touch-icon.png'))
icon(192).save(os.path.join(out, 'icon-192.png'))
icon(512).save(os.path.join(out, 'icon-512.png'))
icon(512, pad=0.1).save(os.path.join(out, 'icon-maskable-512.png'))
