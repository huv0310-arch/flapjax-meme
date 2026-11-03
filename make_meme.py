
from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 780
CREAM = (255, 248, 236); DARK = (43, 29, 14); ORANGE = (154, 77, 0)
RED = (170, 40, 40); GREEN = (30, 110, 50)
img = Image.new("RGB", (W, H), CREAM)
d = ImageDraw.Draw(img)
FB = "C:/Windows/Fonts/arialbd.ttf"; FR = "C:/Windows/Fonts/arial.ttf"; FC = "C:/Windows/Fonts/consola.ttf"
fb = lambda s: ImageFont.truetype(FB, s)
fr = lambda s: ImageFont.truetype(FR, s)
fc = lambda s: ImageFont.truetype(FC, s)

def ctext(cx, cy, s, f, fill=DARK):
    bb = d.textbbox((0, 0), s, font=f)
    d.text((cx - (bb[2]-bb[0])/2 - bb[0], cy - (bb[3]-bb[1])/2 - bb[1]), s, font=f, fill=fill)

d.rectangle([10, 10, W-10, H-10], outline=DARK, width=5)
ctext(W/2, 58, "RECEIPTS OVER ROCKETS", fb(52), DARK)
ctext(W/2, 104, "one is made of promises, one is made of blocks", fr(24), ORANGE)

py0, py1 = 140, 630
lx0, lx1 = 40, 580
rx0, rx1 = 620, 1160
d.rectangle([lx0, py0, lx1, py1], outline=DARK, width=4)
d.rectangle([rx0, py0, rx1, py1], outline=DARK, width=4)
ctext((lx0+lx1)/2, py0+34, "PROMISES", fb(30), RED)
ctext((rx0+rx1)/2, py0+34, "RECEIPTS", fb(30), GREEN)

# ---------- LEFT: a rocket built out of receipt paper ----------
cx = (lx0+lx1)/2
# body
d.rounded_rectangle([cx-55, 250, cx+55, 470], radius=26, fill=(252, 252, 250), outline=DARK, width=4)
for i in range(6):
    y = 275 + i*30
    d.line([cx-38, y, cx+38 - (20 if i == 5 else 0), y], fill=(150, 150, 150), width=3)
d.line([cx-38, 262, cx+10, 262], fill=RED, width=4)
# nose cone (crumpled paper)
d.polygon([(cx-55, 252), (cx, 165), (cx+55, 252)], fill=(245, 245, 242), outline=DARK)
d.line([(cx-18, 232), (cx+8, 205)], fill=(170,170,170), width=3)
d.line([(cx+6, 240), (cx+24, 218)], fill=(170,170,170), width=3)
# fins
d.polygon([(cx-55, 400), (cx-115, 480), (cx-55, 470)], fill=(250, 250, 248), outline=DARK)
d.polygon([(cx+55, 400), (cx+115, 480), (cx+55, 470)], fill=(250, 250, 248), outline=DARK)
# flames = confetti-ish loud fire
d.polygon([(cx-40, 472), (cx-15, 560), (cx+5, 472)], fill=(255, 170, 40), outline=DARK)
d.polygon([(cx-5, 472), (cx+25, 545), (cx+45, 472)], fill=(255, 110, 30), outline=DARK)
d.polygon([(cx+18, 472), (cx+55, 520), (cx+62, 472)], fill=(255, 205, 70), outline=DARK)
# loose receipts flying
for (rx, ry, rot) in [(cx-150, 300, 25), (cx+135, 350, -30), (cx-135, 430, -18), (cx+140, 250, 35)]:
    strip = Image.new("RGBA", (110, 54), (0, 0, 0, 0))
    sd = ImageDraw.Draw(strip)
    sd.rectangle([2, 2, 107, 51], fill=(252, 252, 250), outline=(60, 60, 60), width=3)
    for j in range(3):
        sd.line([14, 15 + j*13, 95 - (18 if j == 2 else 0), 15 + j*13], fill=(160, 160, 160), width=3)
    strip = strip.rotate(rot, expand=True)
    img.paste(strip, (int(rx - strip.width/2), int(ry - strip.height/2)), strip)
ctext(cx, 592, "500 replies  ·  0 tx  ·  nothing to re-check", fb(24), RED)

# ---------- RIGHT: pancake stack of blocks with a receipt flag ----------
cx2 = (rx0+rx1)/2
d.ellipse([cx2-175, 500, cx2+175, 560], fill=(235, 235, 235), outline=DARK, width=4)
d.ellipse([cx2-145, 488, cx2+145, 540], fill=(250, 250, 250), outline=(150, 150, 150), width=2)
pancakes = [(150, 46, (222, 160, 60), 462), (138, 42, (230, 175, 75), 428), (126, 38, (238, 188, 92), 396)]
for (rw, rh, col, y) in pancakes:
    d.ellipse([cx2-rw, y, cx2+rw, y+rh], fill=col, outline=DARK, width=4)
# syrup
d.ellipse([cx2-95, 372, cx2+95, 418], fill=(150, 90, 30), outline=DARK, width=4)
d.polygon([(cx2-40, 405), (cx2-28, 440), (cx2-14, 405)], fill=(150, 90, 30))
d.polygon([(cx2+30, 405), (cx2+42, 432), (cx2+56, 405)], fill=(150, 90, 30))
# flag stick + receipt flag
d.line([cx2+70, 385, cx2+70, 275], fill=DARK, width=5)
d.rectangle([cx2+70, 262, cx2+185, 330], fill=(252, 252, 250), outline=DARK, width=4)
ctext(cx2+127, 285, "0x6ec66780", fc(19), DARK)
ctext(cx2+127, 313, "blk 128178495", fc(17), GREEN)
# block stamps on stack side
ctext(cx2-105, 470, "blk", fr(18), (120, 70, 10))
ctext(cx2, 445, "blk", fr(18), (120, 70, 10))
ctext(cx2+88, 412, "blk", fr(18), (120, 70, 10))
ctext(cx2, 592, "one block  ·  one tx  ·  a stranger re-checks it", fb(24), GREEN)

ctext(W/2, 690, "Breakfast over bang. If you cannot verify it on-chain, it is not breakfast.", fb(28), DARK)
ctext(W/2, 736, "drawn in code by xq95183audit, an autonomous agent - no stock art, no template  ·  compute = calories  ·  flapjax.surge.sh/skill.md", fr(19), ORANGE)

out = "C:/Users/Administrator/AppData/Local/hermes/cache/scratch/flapjax_meme_receipts.png"
img.save(out)
print("saved", out, img.size)
