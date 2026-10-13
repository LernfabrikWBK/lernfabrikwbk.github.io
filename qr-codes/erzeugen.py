"""Erzeugt die QR-Codes für alle Stationen aus config.js.

Ausgabe (in diesem Ordner):
  QR-Codes_Stationen.pdf   A4, 6 Karten pro Seite, zum Ausdrucken
  qr-<station>.png         eine Karte pro Station als Bild

Aufruf aus dem Repo-Hauptordner:
  pip install qrcode pillow reportlab
  python qr-codes/erzeugen.py
"""
import os
import re

import qrcode
from PIL import Image, ImageDraw, ImageFont
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

BASE = "https://lernfabrikwbk.github.io/?s="
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
FONT_R = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONT_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def stations():
    cfg = open(os.path.join(ROOT, "config.js"), encoding="utf-8").read()
    start = cfg.index("STATIONS:")
    return re.findall(r'"([^"]+)"', cfg[start:cfg.index("]", start)])


def slug(t):
    t = t.lower().replace("ä", "ae").replace("ö", "oe").replace("ü", "ue").replace("ß", "ss")
    return re.sub(r"^-|-$", "", re.sub(r"[^a-z0-9]+", "-", t))


def qr_image(url):
    q = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_Q, box_size=20, border=2)
    q.add_data(url)
    q.make(fit=True)
    return q.make_image(fill_color="black", back_color="white").convert("RGB")


def png_card(name, url, path):
    W, H = 1000, 1250
    im = Image.new("RGB", (W, H), "white")
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((10, 10, W - 10, H - 10), 40, outline="black", width=6)
    size = 64
    while size > 28 and d.textlength(name, font=ImageFont.truetype(FONT_B, size)) > W - 100:
        size -= 2
    d.text((W / 2, 110), name, fill="black", font=ImageFont.truetype(FONT_B, size), anchor="mm")
    im.paste(qr_image(url).resize((800, 800), Image.NEAREST), (100, 190))
    fr = ImageFont.truetype(FONT_R, 34)
    d.text((W / 2, 1040), "Station funktioniert nicht?", fill="#18201b", font=fr, anchor="mm")
    d.text((W / 2, 1090), "Code scannen, Schritt für Schritt prüfen.", fill="#18201b", font=fr, anchor="mm")
    d.text((W / 2, 1170), url.replace("https://", ""), fill="#5d6a61",
           font=ImageFont.truetype(FONT_R, 26), anchor="mm")
    im.save(path)


def pdf(names, path):
    pdfmetrics.registerFont(TTFont("DV", FONT_R))
    pdfmetrics.registerFont(TTFont("DVB", FONT_B))
    c = canvas.Canvas(path, pagesize=A4)
    c.setTitle("QR-Codes Stations-Check Lernfabrik")
    pw, ph = A4
    cw, ch = 90 * mm, 88 * mm
    mx, my = (pw - 2 * cw) / 3, (ph - 3 * ch) / 4
    for i, name in enumerate(names):
        k = i % 6
        if i and k == 0:
            c.showPage()
        x = mx + (k % 2) * (cw + mx)
        y = ph - my - (k // 2 + 1) * ch - (k // 2) * my
        url = BASE + slug(name)
        c.setLineWidth(1.2)
        c.roundRect(x, y, cw, ch, 5 * mm)
        size = 17
        while size > 9 and pdfmetrics.stringWidth(name, "DVB", size) > cw - 10 * mm:
            size -= 0.5
        c.setFont("DVB", size)
        c.drawCentredString(x + cw / 2, y + ch - 11 * mm, name)
        qs = 55 * mm
        c.drawImage(ImageReader(qr_image(url)), x + (cw - qs) / 2, y + ch - 14 * mm - qs, qs, qs)
        c.setFont("DV", 9.5)
        c.drawCentredString(x + cw / 2, y + 12 * mm, "Station funktioniert nicht?")
        c.drawCentredString(x + cw / 2, y + 8 * mm, "Code scannen, Schritt für Schritt prüfen.")
        c.setFont("DV", 7)
        c.setFillColorRGB(0.36, 0.42, 0.38)
        c.drawCentredString(x + cw / 2, y + 3.5 * mm, url.replace("https://", ""))
        c.setFillColorRGB(0, 0, 0)
    c.save()


if __name__ == "__main__":
    names = stations()
    for n in names:
        png_card(n, BASE + slug(n), os.path.join(HERE, f"qr-{slug(n)}.png"))
    pdf(names, os.path.join(HERE, "QR-Codes_Stationen.pdf"))
    print(f"{len(names)} QR-Codes erzeugt in {HERE}")
