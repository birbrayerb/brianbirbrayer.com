# Generates public/og.png (1200x630) for link previews. Run: python3 scripts/make-og.py
from PIL import Image, ImageDraw, ImageFont, ImageFilter
G="/usr/share/fonts/truetype/sand-box/google/Geist/Geist-VariableFont_wght.ttf"
M="/usr/share/fonts/truetype/sand-box/google/Geist Mono/GeistMono-VariableFont_wght.ttf"
def f(p,s,w):
    ft=ImageFont.truetype(p,s)
    try: ft.set_variation_by_axes([w])
    except Exception: pass
    return ft
W,H=1200,630
img=Image.new("RGB",(W,H),"#09090b")
glow=Image.new("RGB",(W,H),"#09090b"); g=ImageDraw.Draw(glow)
g.ellipse((700,-250,1350,350),fill="#0f5e45"); g.ellipse((-200,380,450,900),fill="#1e3a8a")
img=Image.blend(img,glow.filter(ImageFilter.GaussianBlur(160)),0.7)
d=ImageDraw.Draw(img)
for x in range(0,W,40):
    for y in range(0,H,40): d.point((x,y),fill="#27272a")
d.rounded_rectangle((60,60,W-60,H-60),radius=28,outline="#27272a",width=2)
for i,c in enumerate(["#f87171","#fbbf24","#34d399"]): d.ellipse((96+i*30,92,112+i*30,108),fill=c)
d.text((W-96,100),"brianbirbrayer.com",font=f(M,24,400),fill="#71717a",anchor="rm")
d.text((100,180),"~/birbs $ whoami",font=f(M,34,500),fill="#34d399")
d.text((96,232),"Brian Birbrayer",font=f(G,104,700),fill="#fafafa")
t=f(G,48,600); d.text((100,370),"Full Stack Developer",font=t,fill="#34d399")
d.text((100,442),"C#/.NET · GitHub & Azure DevOps · AI/ML",font=f(M,30,400),fill="#d4d4d8")
d.text((100,500),"B.S. Computer Science · Milwaukee School of Engineering",font=f(G,26,400),fill="#a1a1aa")
img.save("public/og.png",optimize=True)
