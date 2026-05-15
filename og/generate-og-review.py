"""Generate og-review.png — 1200x630 share card with embedded QR for cnattitle.tech/review."""
from pathlib import Path
import qrcode
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "og-review.png"
FONTS = Path("/tmp/fonts/Montserrat-master/fonts/ttf")

W, H = 1200, 630
NAVY_BG = (11, 19, 34)
NAVY_BG_MID = (17, 31, 51)
NAVY_DARK = (9, 29, 79)
YELLOW = (250, 237, 54)
YELLOW_DIM = (201, 182, 21)
BLUE = (74, 154, 232)
BLUE_DEEP = (45, 125, 210)
WHITE = (255, 255, 255)
TEXT_DIM = (159, 178, 201)
TEXT_FAINT = (136, 146, 164)

URL = "https://cnattitle.tech/review"

def font(name, size):
    return ImageFont.truetype(str(FONTS / f"Montserrat-{name}.ttf"), size)

def radial(canvas, center, radius, color, opacity_start=1.0):
    cx, cy = center
    overlay = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay)
    steps = 60
    for i in range(steps, 0, -1):
        r = radius * (i / steps)
        a = int(255 * opacity_start * (1 - i / steps) ** 2)
        od.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(*color, a))
    canvas.alpha_composite(overlay)

def gradient_bg():
    img = Image.new("RGBA", (W, H), (0, 0, 0, 255))
    d = ImageDraw.Draw(img)
    for y in range(H):
        t = y / H
        # diagonal-ish blend NAVY_BG -> NAVY_BG_MID -> NAVY_BG
        if t < 0.5:
            k = t * 2
            r = int(NAVY_BG[0] + (NAVY_BG_MID[0] - NAVY_BG[0]) * k)
            g = int(NAVY_BG[1] + (NAVY_BG_MID[1] - NAVY_BG[1]) * k)
            b = int(NAVY_BG[2] + (NAVY_BG_MID[2] - NAVY_BG[2]) * k)
        else:
            k = (t - 0.5) * 2
            r = int(NAVY_BG_MID[0] + (NAVY_BG[0] - NAVY_BG_MID[0]) * k)
            g = int(NAVY_BG_MID[1] + (NAVY_BG[1] - NAVY_BG_MID[1]) * k)
            b = int(NAVY_BG_MID[2] + (NAVY_BG[2] - NAVY_BG_MID[2]) * k)
        d.line([(0, y), (W, y)], fill=(r, g, b, 255))
    # yellow glow top-right, blue glow bottom-left (matching og-setup pattern)
    radial(img, (int(W * 0.85), int(H * 0.15)), 520, YELLOW, 0.18)
    radial(img, (int(W * 0.15), int(H * 0.85)), 560, BLUE_DEEP, 0.22)
    return img

def grid_overlay():
    g = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(g)
    step = 48
    line = (255, 255, 255, 6)
    for x in range(0, W, step):
        d.line([(x, 0), (x, H)], fill=line)
    for y in range(0, H, step):
        d.line([(0, y), (W, y)], fill=line)
    # radial mask so grid fades at edges
    mask = Image.new("L", (W, H), 0)
    md = ImageDraw.Draw(mask)
    cx, cy = W // 2, H // 2
    for i in range(60, 0, -1):
        r = max(W, H) * (i / 60) * 0.7
        v = int(220 * (1 - (i / 60) ** 1.4))
        md.ellipse([cx - r, cy - r, cx + r, cy + r], fill=v)
    g.putalpha(mask)
    return g

def rounded_rect(size, radius, fill):
    img = Image.new("RGBA", size, (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([0, 0, size[0] - 1, size[1] - 1], radius=radius, fill=fill)
    return img

def make_qr():
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=14,
        border=2,
    )
    qr.add_data(URL)
    qr.make(fit=True)
    img = qr.make_image(fill_color=NAVY_DARK, back_color=WHITE).convert("RGBA")
    return img

def main():
    canvas = gradient_bg()
    canvas.alpha_composite(grid_overlay())

    # Right-side QR card
    card_size = 420
    card_x = W - card_size - 60
    card_y = (H - card_size) // 2
    # soft shadow
    shadow = rounded_rect((card_size + 40, card_size + 40), 36, (0, 0, 0, 110))
    shadow = shadow.filter(ImageFilter.GaussianBlur(18))
    canvas.alpha_composite(shadow, (card_x - 20, card_y - 14))
    # card
    card = rounded_rect((card_size, card_size), 28, (255, 255, 255, 255))
    canvas.alpha_composite(card, (card_x, card_y))
    # inner thin border ring
    ring = rounded_rect((card_size, card_size), 28, (0, 0, 0, 0))
    rd = ImageDraw.Draw(ring)
    rd.rounded_rectangle([0, 0, card_size - 1, card_size - 1], radius=28, outline=(*NAVY_DARK, 35), width=2)
    canvas.alpha_composite(ring, (card_x, card_y))

    # QR
    qr_img = make_qr()
    qr_target = card_size - 56
    qr_img = qr_img.resize((qr_target, qr_target), Image.NEAREST)
    canvas.alpha_composite(qr_img, (card_x + (card_size - qr_target) // 2, card_y + (card_size - qr_target) // 2))

    # Scan label under card
    d = ImageDraw.Draw(canvas)
    scan_font = font("Bold", 16)
    scan_text = "SCAN  ·  OR  ·  TAP"
    tw = d.textlength(scan_text, font=scan_font)
    d.text((card_x + (card_size - tw) // 2, card_y + card_size + 22), scan_text,
           font=scan_font, fill=BLUE, spacing=4)

    # Left-side content
    left_x = 70
    left_w = card_x - left_x - 40

    # Brand badge
    badge_text = "CNAT TITLE"
    badge_font = font("ExtraBold", 14)
    pad_x, pad_y = 18, 11
    btw = d.textlength(badge_text, font=badge_font)
    bw = int(btw) + pad_x * 2 + 18
    bh = 38
    by = 110
    badge_bg = Image.new("RGBA", (bw, bh), (0, 0, 0, 0))
    bd = ImageDraw.Draw(badge_bg)
    bd.rounded_rectangle([0, 0, bw - 1, bh - 1], radius=bh // 2,
                         fill=(74, 154, 232, 36), outline=(74, 154, 232, 110), width=1)
    bd.ellipse([14, bh // 2 - 4, 22, bh // 2 + 4], fill=YELLOW)
    bd.text((30, (bh - 14) // 2 - 1), badge_text, font=badge_font, fill=BLUE)
    canvas.alpha_composite(badge_bg, (left_x, by))

    # Headline
    h1_thin = font("Light", 76)
    h1_bold = font("ExtraBold", 76)
    line1 = "Leave Us a"
    line2 = "Review"
    y1 = by + bh + 28
    d.text((left_x, y1), line1, font=h1_thin, fill=WHITE)
    d.text((left_x, y1 + 84), line2, font=h1_bold, fill=YELLOW)

    # Subline
    sub_font = font("Regular", 20)
    sub = "Scan or tap — takes 30 seconds and means the world to us."
    d.text((left_x, y1 + 84 + 100), sub, font=sub_font, fill=TEXT_DIM)

    # Footer row: domain + tag
    footer_y = H - 90
    # divider
    d.line([(left_x, footer_y - 18), (left_x + left_w - 10, footer_y - 18)], fill=(255, 255, 255, 22))
    dom_font_bold = font("ExtraBold", 22)
    dom_font_med = font("Medium", 22)
    parts = [("cnattitle", WHITE, dom_font_bold), (".tech", TEXT_FAINT, dom_font_med),
             ("/review", YELLOW, dom_font_bold)]
    cx = left_x
    for txt, color, f in parts:
        d.text((cx, footer_y), txt, font=f, fill=color)
        cx += int(d.textlength(txt, font=f))

    # dot + tag
    dot_x = cx + 18
    dot_y = footer_y + 14
    d.ellipse([dot_x, dot_y, dot_x + 6, dot_y + 6], fill=BLUE)
    tag_font = font("ExtraBold", 13)
    tag_y = footer_y + 6
    tag_x = dot_x + 18
    d.text((tag_x, tag_y), "REAL FEEDBACK", font=tag_font, fill=TEXT_DIM)
    tw2 = d.textlength("REAL FEEDBACK ", font=tag_font)
    d.text((tag_x + int(tw2), tag_y), "·  REAL CLIENTS", font=tag_font, fill=YELLOW)

    canvas.convert("RGB").save(OUT, "PNG", optimize=True)
    print(f"Wrote {OUT} ({OUT.stat().st_size // 1024} KB)")

if __name__ == "__main__":
    main()
