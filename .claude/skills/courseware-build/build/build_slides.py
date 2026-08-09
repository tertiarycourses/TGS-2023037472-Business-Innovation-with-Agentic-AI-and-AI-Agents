#!/usr/bin/env python3
"""Generate the Digital Transformation and Business Innovation with GenAI course
slide deck (all-white Tertiary house style).

Design helpers are the same set used by the tertiary-course-slides skill that
produced the n8n reference deck (cover, section, content, two_col, cards3,
big_statement, step_slide, test_slide, brk). Content is driven entirely by
course_data.py + data_domainN.py so the deck stays 100% aligned with the LP,
LG and labs.

House rule: the deck is VISUAL. Detailed step-by-step instructions live in the
Learner Guide and the labs/ files — the slides carry only the lab objective,
what the learner builds and the verification, never the numbered steps.
"""
import os, sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import course_data as C
from data_domain1 import DOMAIN1
from data_domain2 import DOMAIN2
from data_domain3 import DOMAIN3
ACTIVITIES = DOMAIN1 + DOMAIN2 + DOMAIN3

def _find_repo(start):
    """Locate the course repo (a dir containing both courseware/ and labs/).
    Env COURSE_REPO overrides. Keeps the build working wherever the skill lives."""
    env = os.environ.get("COURSE_REPO")
    if env and os.path.isdir(env):
        return env
    d = start
    for _ in range(8):
        d = os.path.dirname(d)
        if os.path.isdir(os.path.join(d, "courseware")) and os.path.isdir(os.path.join(d, "labs")):
            return d
    return os.path.dirname(os.path.dirname(HERE))
REPO = _find_repo(HERE)
ASSETS = os.path.join(os.path.dirname(HERE), "assets")   # co-located with the skill

# ---------------- palette (matches reference) ----------------
BLUE=RGBColor(0x1F,0x6F,0xEB); TEAL=RGBColor(0x10,0xB9,0x81); AMBER=RGBColor(0xF5,0x9E,0x0B)
INK=RGBColor(0x16,0x1B,0x26); GREY=RGBColor(0x5B,0x63,0x72); LIGHT=RGBColor(0xF5,0xF8,0xFC)
WHITE=RGBColor(0xFF,0xFF,0xFF); LINE=RGBColor(0xE2,0xE8,0xF0); VIOLET=RGBColor(0x7C,0x3A,0xED)

prs=Presentation(); prs.slide_width=Inches(13.333); prs.slide_height=Inches(7.5)
SW,SH=prs.slide_width,prs.slide_height
BLANK=prs.slide_layouts[6]

def slide(): return prs.slides.add_slide(BLANK)
def rect(s,x,y,w,h,color,line=None):
    sp=s.shapes.add_shape(1,x,y,w,h); sp.fill.solid(); sp.fill.fore_color.rgb=color
    if line is None: sp.line.fill.background()
    else: sp.line.color.rgb=line; sp.line.width=Pt(1)
    sp.shadow.inherit=False; return sp
def oval(s,x,y,w,h,color):
    sp=s.shapes.add_shape(9,x,y,w,h); sp.fill.solid(); sp.fill.fore_color.rgb=color
    sp.line.fill.background(); sp.shadow.inherit=False; return sp
def txt(s,x,y,w,h,runs,align=PP_ALIGN.LEFT,anchor=MSO_ANCHOR.TOP,space=4):
    tb=s.shapes.add_textbox(x,y,w,h); tf=tb.text_frame; tf.word_wrap=True; tf.vertical_anchor=anchor
    for i,line in enumerate(runs):
        p=tf.paragraphs[0] if i==0 else tf.add_paragraph()
        p.alignment=align; p.space_after=Pt(space)
        for t,sz,col,bold in line:
            r=p.add_run(); r.text=t; r.font.size=Pt(sz); r.font.bold=bold
            r.font.color.rgb=col; r.font.name="Arial"
    return tb
def bullets(s,x,y,w,h,items,size=18,color=INK,gap=10,mcolor=BLUE):
    tb=s.shapes.add_textbox(x,y,w,h); tf=tb.text_frame; tf.word_wrap=True
    for i,it in enumerate(items):
        p=tf.paragraphs[0] if i==0 else tf.add_paragraph(); p.space_after=Pt(gap)
        lvl=it[1] if isinstance(it,tuple) else 0
        text=it[0] if isinstance(it,tuple) else it
        r=p.add_run(); r.text=("•  " if lvl==0 else "–  ")+text
        r.font.size=Pt(size if lvl==0 else size-2); r.font.color.rgb=color if lvl==0 else GREY
        r.font.name="Arial"; r.font.bold=(lvl==0 and isinstance(it,tuple) and len(it)>2 and it[2])
    return tb

PAGE={"n":0}
def footer(s):
    PAGE["n"]+=1
    txt(s,Inches(0.4),Inches(7.05),Inches(7.5),Inches(0.35),
        [[(f"{C.SHORT_TITLE}  ·  {C.COURSE_CODE}",9,GREY,False)]])
    txt(s,Inches(5.0),Inches(7.05),Inches(3.3),Inches(0.35),
        [[("© 2026 Tertiary Infotech Academy Pte Ltd",9,GREY,False)]],align=PP_ALIGN.CENTER)
    txt(s,Inches(12.4),Inches(7.05),Inches(0.6),Inches(0.35),
        [[(str(PAGE["n"]),9,GREY,False)]],align=PP_ALIGN.RIGHT)
def head(s,title,kicker=None,kcolor=BLUE):
    """Slide header. Long titles are auto-shrunk so a second line never renders
    on top of the divider rule."""
    rect(s,0,0,SW,SH,WHITE); rect(s,0,0,Inches(0.28),Inches(1.55),kcolor)
    if kicker: txt(s,Inches(0.85),Inches(0.5),Inches(11.6),Inches(0.4),[[(kicker,14,kcolor,True)]])
    tsz=29 if len(title)<=52 else (25 if len(title)<=68 else 22)
    txt(s,Inches(0.85),Inches(0.86),Inches(11.9),Inches(0.82),[[(title,tsz,INK,True)]])
    rect(s,Inches(0.85),Inches(1.7),Inches(11.63),Inches(0.02),LINE)
    return s
def _logo(name):
    p=os.path.join(ASSETS,name)
    return p if os.path.exists(p) else None

# ---------------- slide templates ----------------
def cover():
    s=slide(); rect(s,0,0,SW,SH,WHITE)
    rect(s,0,0,SW,Inches(0.22),BLUE); rect(s,0,Inches(7.28),SW,Inches(0.22),TEAL)
    org=_logo("tertiary-infotech-logo.png")
    if org: s.shapes.add_picture(org,Inches(0.85),Inches(0.7),height=Inches(1.05))
    # course badge (top-right) — WSQ / GenAI course badge
    badge=_logo("course-badge.png")
    if badge:
        s.shapes.add_picture(badge,Inches(10.05),Inches(0.6),width=Inches(2.5))
    else:
        rect(s,Inches(10.95),Inches(0.72),Inches(1.6),Inches(1.0),BLUE)
        txt(s,Inches(10.95),Inches(0.84),Inches(1.6),Inches(0.5),[[("GenAI",20,WHITE,True)]],align=PP_ALIGN.CENTER)
        txt(s,Inches(10.95),Inches(1.30),Inches(1.6),Inches(0.4),[[("WSQ · 2 DAYS",8,WHITE,True)]],align=PP_ALIGN.CENTER)
    txt(s,Inches(0.9),Inches(2.3),Inches(12),Inches(0.6),[[("COURSE SLIDES  ·  WSQ",16,BLUE,True)]])
    txt(s,Inches(0.9),Inches(2.85),Inches(12.0),Inches(1.9),[[(C.TITLE,40,INK,True)]])
    rect(s,Inches(0.92),Inches(4.75),Inches(2.4),Inches(0.06),TEAL)
    txt(s,Inches(0.9),Inches(5.05),Inches(12),Inches(1.4),
        [[(f"WSQ Course Code: {C.COURSE_CODE}",16,GREY,False)],
         [("Conducted by Tertiary Infotech Academy Pte Ltd  ·  UEN 201200696W",14,GREY,False)]],space=6)
    txt(s,Inches(0.9),Inches(6.5),Inches(12),Inches(0.4),[[(f"Version {C.VERSION}  ·  {C.VERSION_DATE}",12,GREY,False)]])
    txt(s,Inches(0.9),Inches(6.85),Inches(12),Inches(0.34),[[("© 2026 Tertiary Infotech Academy Pte Ltd. All rights reserved.  ·  www.tertiarycourses.com.sg",10,GREY,False)]])

def section(kicker,title,n,sub=""):
    s=slide(); rect(s,0,0,SW,SH,WHITE); rect(s,0,0,Inches(0.28),SH,BLUE)
    rect(s,Inches(0.85),Inches(2.5),Inches(0.14),Inches(2.0),TEAL)
    txt(s,Inches(1.25),Inches(2.55),Inches(11),Inches(0.6),[[(kicker,18,BLUE,True)]])
    txt(s,Inches(1.25),Inches(3.0),Inches(11.4),Inches(1.6),[[(title,40,INK,True)]])
    if sub: txt(s,Inches(1.27),Inches(4.55),Inches(11),Inches(0.8),[[(sub,16,GREY,False)]])
    txt(s,Inches(10.0),Inches(0.7),Inches(2.8),Inches(1.6),[[(n,72,RGBColor(0xE2,0xE8,0xF0),True)]],align=PP_ALIGN.RIGHT)
    footer(s)
def content(title,items,kicker=None,size=20):
    s=head(slide(),title,kicker); bullets(s,Inches(0.85),Inches(1.95),Inches(11.6),Inches(4.9),items,size=size); footer(s); return s
def two_col(title,left,right,kicker=None,lhead="",rhead=""):
    s=head(slide(),title,kicker)
    rect(s,Inches(0.85),Inches(1.95),Inches(5.7),Inches(4.7),LIGHT); rect(s,Inches(6.95),Inches(1.95),Inches(5.55),Inches(4.7),LIGHT)
    if lhead: txt(s,Inches(1.1),Inches(2.15),Inches(5.2),Inches(0.4),[[(lhead,16,BLUE,True)]])
    if rhead: txt(s,Inches(7.2),Inches(2.15),Inches(5.0),Inches(0.4),[[(rhead,16,TEAL,True)]])
    bullets(s,Inches(1.1),Inches(2.7),Inches(5.2),Inches(3.8),left,size=16)
    bullets(s,Inches(7.2),Inches(2.7),Inches(5.05),Inches(3.8),right,size=16,mcolor=TEAL); footer(s); return s
def cards3(title,cards,kicker):
    """1-3 equal cards spanning the content width. Never emits an empty card."""
    s=head(slide(),title,kicker)
    cards=[c for c in cards[:3] if c and c[2]]
    n=max(1,len(cards)); X0=Inches(0.85); TOTW=Inches(11.63); gap=Inches(0.35)
    cw=int((TOTW-gap*(n-1))/n)
    for i,c in enumerate(cards):
        x=int(X0+(cw+gap)*i); col=c[0]
        rect(s,x,Inches(1.95),cw,Inches(4.7),LIGHT); rect(s,x,Inches(1.95),cw,Inches(0.12),col)
        txt(s,x+Inches(0.25),Inches(2.2),cw-Inches(0.5),Inches(0.6),[[(c[1],19,col,True)]])
        bullets(s,x+Inches(0.25),Inches(2.95),cw-Inches(0.5),Inches(3.4),c[2],size=14,mcolor=col,gap=9)
    footer(s); return s
def big_statement(line1,line2,kicker,color=BLUE):
    s=slide(); rect(s,0,0,SW,SH,WHITE); rect(s,0,0,Inches(0.28),SH,color)
    txt(s,Inches(1.1),Inches(2.2),Inches(11),Inches(0.5),[[(kicker,16,color,True)]])
    txt(s,Inches(1.1),Inches(2.8),Inches(11.3),Inches(2.4),[[(line1,38,INK,True)]])
    if line2: txt(s,Inches(1.12),Inches(4.9),Inches(11),Inches(1.2),[[(line2,20,GREY,False)]])
    footer(s); return s
import math
PALETTE=[BLUE,TEAL,VIOLET,AMBER]
def tile_grid(title,items,kicker=None,cols=2,size=15,icons=None,accent=BLUE):
    """Grid of light panels, each with a coloured icon/number badge + text.
    items: list of strings (or (title,caption) tuples). Much richer than a bullet list."""
    s=head(slide(),title,kicker,kcolor=accent)
    n=len(items); rows=math.ceil(n/cols)
    X0=Inches(0.85); Y0=Inches(1.95); TOTW=Inches(11.63); AREAH=Inches(4.78)
    gx=Inches(0.3); gy=Inches(0.26)
    cw=int((TOTW-gx*(cols-1))/cols); ch=int((AREAH-gy*(rows-1))/rows)
    bd=Inches(0.6)
    for i,it in enumerate(items):
        r=i//cols; c=i%cols
        x=int(X0+(cw+gx)*c); y=int(Y0+(ch+gy)*r); col=PALETTE[i%len(PALETTE)]
        rect(s,x,y,cw,ch,LIGHT); rect(s,x,y,Inches(0.1),ch,col)
        oval(s,x+Inches(0.28),int(y+ch/2-bd/2),bd,bd,col)
        ic=icons[i] if icons else str(i+1)
        txt(s,x+Inches(0.28),int(y+ch/2-bd/2),bd,bd,[[(ic,19,WHITE,True)]],align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
        tx=x+Inches(1.08); tw=cw-Inches(1.32)
        if isinstance(it,tuple):
            txt(s,tx,int(y+Inches(0.14)),tw,int(ch-Inches(0.2)),
                [[(it[0],size+2,INK,True)],[(it[1],size-2,GREY,False)]],anchor=MSO_ANCHOR.MIDDLE,space=3)
        else:
            txt(s,tx,int(y+Inches(0.1)),tw,int(ch-Inches(0.16)),[[(it,size,INK,False)]],anchor=MSO_ANCHOR.MIDDLE)
    footer(s); return s
def flow_h(title,steps,kicker=None,color=BLUE):
    """Horizontal numbered flow: coloured chips connected by chevrons."""
    s=head(slide(),title,kicker,kcolor=color)
    n=len(steps); X0=Inches(0.85); TOTW=Inches(11.63); gap=Inches(0.34)
    cw=int((TOTW-gap*(n-1))/n); y=Inches(2.55); ch=Inches(3.15); bd=Inches(0.82)
    for i,st in enumerate(steps):
        x=int(X0+(cw+gap)*i)
        rect(s,x,y,cw,ch,LIGHT); rect(s,x,y,cw,Inches(0.1),color)
        oval(s,int(x+cw/2-bd/2),int(y+Inches(0.42)),bd,bd,color)
        txt(s,int(x+cw/2-bd/2),int(y+Inches(0.42)),bd,bd,[[(str(i+1),30,WHITE,True)]],align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
        txt(s,x+Inches(0.16),int(y+Inches(1.55)),cw-Inches(0.32),int(ch-Inches(1.7)),[[(st,14,INK,False)]],align=PP_ALIGN.CENTER)
        if i<n-1:
            txt(s,int(x+cw-Inches(0.04)),int(y+ch/2-Inches(0.3)),int(gap+Inches(0.08)),Inches(0.6),
                [[("▶",15,color,True)]],align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
    footer(s); return s
def trainer_slide(kicker,name,role,rows,initials,accent=BLUE):
    """Profile-card layout: avatar badge + name/role panel on the left, labelled
    info tiles on the right. rows: list of (LABEL, value); blank value → fill-in line."""
    s=head(slide(),"About the Trainer",kicker,kcolor=accent)
    lx=Inches(0.85); lw=Inches(3.65)
    rect(s,lx,Inches(1.95),lw,Inches(4.7),LIGHT); rect(s,lx,Inches(1.95),lw,Inches(0.12),accent)
    bd=Inches(1.7); ax=int(lx+(lw-bd)/2)
    oval(s,ax,Inches(2.5),bd,bd,accent)
    txt(s,ax,Inches(2.5),bd,bd,[[(initials,44,WHITE,True)]],align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
    txt(s,lx+Inches(0.15),Inches(4.55),lw-Inches(0.3),Inches(0.6),[[(name,21,INK,True)]],align=PP_ALIGN.CENTER)
    txt(s,lx+Inches(0.15),Inches(5.2),lw-Inches(0.3),Inches(1.2),[[(role,13,GREY,False)]],align=PP_ALIGN.CENTER)
    rx=Inches(4.9); rw=Inches(7.6); ry=Inches(1.95); rh=Inches(4.7)
    n=len(rows); gy=Inches(0.2); th=int((rh-gy*(n-1))/n)
    for i,(label,val) in enumerate(rows):
        y=int(ry+(th+gy)*i); col=PALETTE[i%len(PALETTE)]
        rect(s,rx,y,rw,th,LIGHT); rect(s,rx,y,Inches(0.1),th,col)
        vruns=[(val,14,INK,False)] if val else [("____________________________________________",13,LINE,False)]
        txt(s,rx+Inches(0.32),y,rw-Inches(0.6),th,
            [[(label.upper(),11,col,True)],vruns],anchor=MSO_ANCHOR.MIDDLE,space=3)
    footer(s); return s
def stat_band(title,stats,kicker=None,color=BLUE):
    """Big-number band: 3-4 headline figures with captions. Highly visual."""
    s=head(slide(),title,kicker,kcolor=color)
    n=len(stats); X0=Inches(0.85); TOTW=Inches(11.63); gap=Inches(0.3)
    cw=int((TOTW-gap*(n-1))/n); y=Inches(2.35); ch=Inches(2.5)
    for i,(big,cap) in enumerate(stats):
        x=int(X0+(cw+gap)*i); col=PALETTE[i%len(PALETTE)]
        rect(s,x,y,cw,ch,LIGHT); rect(s,x,y,cw,Inches(0.1),col)
        txt(s,x+Inches(0.2),int(y+Inches(0.5)),cw-Inches(0.4),Inches(1.0),
            [[(big,40,col,True)]],align=PP_ALIGN.CENTER)
        txt(s,x+Inches(0.2),int(y+Inches(1.6)),cw-Inches(0.4),Inches(0.8),
            [[(cap,13,GREY,False)]],align=PP_ALIGN.CENTER)
    footer(s); return s

def compare(title,lhead,litems,rhead,ritems,kicker=None,lcolor=BLUE,rcolor=TEAL):
    """Two coloured columns with header chips — for A vs B concept slides."""
    s=head(slide(),title,kicker)
    for x,w,hd,items,col in ((Inches(0.85),Inches(5.7),lhead,litems,lcolor),
                             (Inches(6.78),Inches(5.7),rhead,ritems,rcolor)):
        rect(s,x,Inches(1.95),w,Inches(4.7),LIGHT); rect(s,x,Inches(1.95),w,Inches(0.62),col)
        txt(s,x,Inches(1.95),w,Inches(0.62),[[(hd,17,WHITE,True)]],
            align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
        bullets(s,x+Inches(0.3),Inches(2.85),w-Inches(0.6),Inches(3.5),items,size=15,mcolor=col,gap=11)
    footer(s); return s

def layers(title,rows,kicker=None,color=BLUE):
    """Stacked architecture layers — each a full-width band with label + detail."""
    s=head(slide(),title,kicker,kcolor=color)
    n=len(rows); X0=Inches(0.85); W=Inches(11.63); Y0=Inches(1.95)
    gy=Inches(0.14); rh=int((Inches(4.78)-gy*(n-1))/n)
    for i,(name,detail) in enumerate(rows):
        y=int(Y0+(rh+gy)*i); col=PALETTE[i%len(PALETTE)]
        rect(s,X0,y,W,rh,LIGHT); rect(s,X0,y,Inches(0.1),rh,col)
        rect(s,X0+Inches(0.3),y+int(rh/2-Inches(0.22)),Inches(2.45),Inches(0.44),col)
        txt(s,X0+Inches(0.3),y+int(rh/2-Inches(0.22)),Inches(2.45),Inches(0.44),
            [[(name.upper(),11,WHITE,True)]],align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
        txt(s,X0+Inches(3.0),y,W-Inches(3.35),rh,[[(detail,14,INK,False)]],anchor=MSO_ANCHOR.MIDDLE)
    footer(s); return s

def activity_overview(tag,title,desc,build,services,kicker):
    """Lab overview. The 'You'll build' text is measured so the Tools line is
    pushed below it — a 3-line deliverable used to overprint the tools line."""
    s=head(slide(),title,kicker,kcolor=TEAL)
    rect(s,Inches(0.85),Inches(1.85),Inches(1.7),Inches(0.5),TEAL)
    txt(s,Inches(0.85),Inches(1.9),Inches(1.7),Inches(0.4),[[(tag,16,WHITE,True)]],align=PP_ALIGN.CENTER)
    dsz=21 if len(desc)<210 else 18
    txt(s,Inches(0.85),Inches(2.5),Inches(11.7),Inches(1.7),[[(desc,dsz,INK,False)]])
    # size the panel to the deliverable text so nothing collides
    bsz=17 if len(build)<150 else 15
    CPL=int(11.0*96/(bsz*0.70))          # measured bold-Arial chars-per-line
    blines=max(1,-(-len(build)//CPL))
    bh=Inches(0.34)*blines
    panel_y=Inches(4.32); panel_h=max(Inches(2.0),Inches(1.05)+bh)
    if panel_y+panel_h>Inches(6.85): panel_y=Inches(6.85)-panel_h
    rect(s,Inches(0.85),panel_y,Inches(11.7),panel_h,LIGHT)
    txt(s,Inches(1.1),panel_y+Inches(0.18),Inches(11),Inches(0.34),[[("You'll build",13,BLUE,True)]])
    txt(s,Inches(1.1),panel_y+Inches(0.55),Inches(11.2),bh,[[(build,bsz,INK,True)]])
    txt(s,Inches(1.1),panel_y+Inches(0.6)+bh,Inches(11.2),Inches(0.42),
        [[("Tools:  ",12,GREY,True),(services,12,GREY,False)]])
    footer(s); return s
def step_slide(kicker,act_title,n,total,text,cmd=""):
    s=head(slide(),act_title,kicker,TEAL)
    oval(s,Inches(0.85),Inches(2.5),Inches(1.4),Inches(1.4),TEAL)
    txt(s,Inches(0.85),Inches(2.74),Inches(1.4),Inches(0.9),[[(str(n),38,WHITE,True)]],align=PP_ALIGN.CENTER)
    txt(s,Inches(0.95),Inches(1.95),Inches(11),Inches(0.4),[[(f"STEP {n} OF {total}",13,GREY,True)]])
    txt(s,Inches(2.55),Inches(2.4),Inches(10.1),Inches(1.3),[[(text,23,INK,False)]],anchor=MSO_ANCHOR.MIDDLE)
    if cmd:
        rect(s,Inches(2.55),Inches(4.15),Inches(10.1),Inches(0.95),RGBColor(0x0B,0x12,0x20))
        txt(s,Inches(2.8),Inches(4.28),Inches(9.7),Inches(0.7),[[("$ "+cmd,13,RGBColor(0x9C,0xDC,0xFE),False)]],anchor=MSO_ANCHOR.MIDDLE)
    footer(s); return s
def test_slide(act_title,text,kicker):
    s=head(slide(),act_title,kicker,TEAL)
    rect(s,Inches(0.85),Inches(2.3),Inches(11.7),Inches(2.6),RGBColor(0xE8,0xF7,0xEE))
    txt(s,Inches(1.2),Inches(2.6),Inches(11),Inches(0.5),[[("✅  Test it",20,RGBColor(0x12,0x7A,0x3E),True)]])
    txt(s,Inches(1.2),Inches(3.3),Inches(11),Inches(1.4),[[(text,18,INK,False)]]); footer(s); return s
def brk(kind,dur,color=AMBER):
    s=slide(); rect(s,0,0,SW,SH,WHITE)
    rect(s,0,0,SW,Inches(0.22),color); rect(s,0,Inches(7.28),SW,Inches(0.22),color)
    rect(s,Inches(5.4),Inches(2.35),Inches(2.53),Inches(0.1),color)
    txt(s,0,Inches(2.75),SW,Inches(1.2),[[(kind,48,INK,True)]],align=PP_ALIGN.CENTER)
    txt(s,0,Inches(4.05),SW,Inches(0.8),[[(dur,22,color,True)]],align=PP_ALIGN.CENTER); PAGE["n"]+=1

# ---------------- rich visual components (reference-deck style) ----------------
def rrect(s,x,y,w,h,color,line=None):
    """Rounded rectangle — softer card look used by the reference deck."""
    sp=s.shapes.add_shape(5,x,y,w,h); sp.fill.solid(); sp.fill.fore_color.rgb=color
    if line is None: sp.line.fill.background()
    else: sp.line.color.rgb=line; sp.line.width=Pt(1.25)
    sp.shadow.inherit=False
    try: sp.adjustments[0]=0.06
    except Exception: pass
    return sp

def journey(title,items,kicker=None,note=None,cols=2):
    """Two-column numbered journey list — the 'Connected Labs' pattern.
    items: list of (badge, name, caption)."""
    s=head(slide(),title,kicker)
    n=len(items); rows=(n+cols-1)//cols
    X0=Inches(0.85); TOTW=Inches(11.63); gx=Inches(0.3)
    cw=int((TOTW-gx*(cols-1))/cols)
    AREAH=Inches(4.25) if note else Inches(4.78)
    gy=Inches(0.1); rh=int((AREAH-gy*(rows-1))/rows)
    for i,(badge,name,cap) in enumerate(items):
        c=i//rows; r=i%rows
        x=int(X0+(cw+gx)*c); y=int(Inches(1.95)+(rh+gy)*r); col=PALETTE[i%len(PALETTE)]
        rrect(s,x,y,cw,rh,LIGHT,line=RGBColor(0xE6,0xEC,0xF4))
        bd=min(rh-Inches(0.12),Inches(0.46))
        bw=max(bd,Inches(0.5))          # wide enough for two digits
        rrect(s,x+Inches(0.14),int(y+rh/2-bd/2),bw,bd,col)
        tb=txt(s,x+Inches(0.14),int(y+rh/2-bd/2),bw,bd,[[(badge,12,WHITE,True)]],
               align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
        tb.text_frame.word_wrap=False   # never wrap a 2-digit lab number
        tx=x+Inches(0.78); tw=cw-Inches(0.98)
        txt(s,tx,y,tw,rh,[[(name,12.5,INK,True)],[(cap,10,GREY,False)]],
            anchor=MSO_ANCHOR.MIDDLE,space=1)
    if note:
        y=Inches(6.35)
        rrect(s,X0,y,TOTW,Inches(0.62),WHITE,line=BLUE)
        txt(s,X0+Inches(0.3),y,TOTW-Inches(0.6),Inches(0.62),
            [[(note,14,INK,True)]],anchor=MSO_ANCHOR.MIDDLE)
    footer(s); return s

def step_cards(title,cards,kicker=None,note=None,ntitle=None):
    """Row of 3-4 rounded step cards with a coloured left rail + numbered badge,
    optionally над a callout box. cards: list of (heading, body)."""
    s=head(slide(),title,kicker)
    n=len(cards); X0=Inches(0.85); TOTW=Inches(11.63); gap=Inches(0.28)
    cw=int((TOTW-gap*(n-1))/n); y=Inches(2.15); ch=Inches(2.9) if note else Inches(4.3)
    for i,(hd,body) in enumerate(cards):
        x=int(X0+(cw+gap)*i); col=PALETTE[i%len(PALETTE)]
        rrect(s,x,y,cw,ch,LIGHT,line=RGBColor(0xE6,0xEC,0xF4))
        rect(s,x,y+Inches(0.06),Inches(0.075),ch-Inches(0.12),col)
        bd=Inches(0.5)
        oval(s,x+Inches(0.3),y+Inches(0.3),bd,bd,col)
        txt(s,x+Inches(0.3),y+Inches(0.3),bd,bd,[[(str(i+1),15,WHITE,True)]],
            align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
        txt(s,x+Inches(0.95),y+Inches(0.3),cw-Inches(1.2),Inches(0.6),[[(hd,14,col,True)]])
        txt(s,x+Inches(0.32),y+Inches(1.0),cw-Inches(0.6),ch-Inches(1.2),
            [[(body,11.5,INK,False)]])
    if note:
        ny=Inches(5.3)
        rrect(s,X0,ny,TOTW,Inches(1.5),LIGHT,line=RGBColor(0xDC,0x26,0x26))
        if ntitle:
            txt(s,X0+Inches(0.3),ny+Inches(0.16),TOTW-Inches(0.6),Inches(0.34),
                [[(ntitle,12,RGBColor(0xDC,0x26,0x26),True)]])
        txt(s,X0+Inches(0.3),ny+Inches(0.55),TOTW-Inches(0.6),Inches(0.85),
            [[(note,12.5,INK,False)]])
    footer(s); return s

def pipeline_flow(title,stages,kicker=None,note=None):
    """The course production pipeline as a connected chevron ribbon.
    stages: list of (label, tools)."""
    s=head(slide(),title,kicker)
    n=len(stages); X0=Inches(0.85); TOTW=Inches(11.63)
    gap=Inches(0.16); cw=int((TOTW-gap*(n-1))/n)
    y=Inches(2.3); ch=Inches(2.5)
    for i,(label,tools) in enumerate(stages):
        x=int(X0+(cw+gap)*i); col=PALETTE[i%len(PALETTE)]
        rrect(s,x,y,cw,ch,LIGHT,line=RGBColor(0xE6,0xEC,0xF4))
        rrect(s,x,y,cw,Inches(0.42),col)
        txt(s,x,y,cw,Inches(0.42),[[("STAGE %d"%(i+1),10,WHITE,True)]],
            align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
        txt(s,x+Inches(0.12),y+Inches(0.55),cw-Inches(0.24),Inches(0.95),
            [[(label,12.5,INK,True)]],align=PP_ALIGN.CENTER)
        txt(s,x+Inches(0.12),y+Inches(1.55),cw-Inches(0.24),Inches(0.85),
            [[(tools,9.5,GREY,False)]],align=PP_ALIGN.CENTER)
        if i<n-1:
            txt(s,int(x+cw-Inches(0.02)),int(y+ch/2-Inches(0.22)),int(gap+Inches(0.04)),Inches(0.44),
                [[("▶",11,col,True)]],align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
    if note:
        ny=Inches(5.35)
        rrect(s,X0,ny,TOTW,Inches(1.35),WHITE,line=BLUE)
        txt(s,X0+Inches(0.35),ny,TOTW-Inches(0.7),Inches(1.35),
            [[(note,13,INK,False)]],anchor=MSO_ANCHOR.MIDDLE)
    footer(s); return s

def link_grid(title,items,kicker=None,cols=3,accent=None):
    """Grid of tool cards where the URL is a REAL clickable hyperlink.
    items: list of (tool, url, caption)."""
    accent=accent or TEAL
    s=head(slide(),title,kicker,kcolor=accent)
    n=len(items); rows=math.ceil(n/cols)
    X0=Inches(0.85); TOTW=Inches(11.63); gx=Inches(0.26); gy=Inches(0.22)
    cw=int((TOTW-gx*(cols-1))/cols); ch=int((Inches(4.78)-gy*(rows-1))/rows)
    for i,(tool,url,cap) in enumerate(items):
        r=i//cols; c=i%cols
        x=int(X0+(cw+gx)*c); y=int(Inches(1.95)+(ch+gy)*r); col=PALETTE[i%len(PALETTE)]
        rrect(s,x,y,cw,ch,LIGHT,line=RGBColor(0xE6,0xEC,0xF4))
        rect(s,x,y+Inches(0.05),Inches(0.07),ch-Inches(0.1),col)
        txt(s,x+Inches(0.28),y+Inches(0.1),cw-Inches(0.56),Inches(0.32),[[(tool,12.5,INK,True)]])
        # clickable URL — shortened display text so it never runs past the card
        disp=url.replace("https://","").replace("http://","").rstrip("/")
        if len(disp)>34: disp=disp[:33]+"…"
        tb=s.shapes.add_textbox(x+Inches(0.28),y+Inches(0.42),cw-Inches(0.56),Inches(0.3))
        tf=tb.text_frame; tf.word_wrap=True; p=tf.paragraphs[0]
        run=p.add_run(); run.text=disp
        run.font.size=Pt(9.5); run.font.name="Arial"; run.font.color.rgb=BLUE
        run.font.underline=True
        run.hyperlink.address=url if url.startswith("http") else "https://"+url
        txt(s,x+Inches(0.28),y+Inches(0.74),cw-Inches(0.56),ch-Inches(0.82),
            [[(cap,9.5,GREY,False)]])
    footer(s); return s

def callout(s,y,text,title=None,color=None,h=None):
    """Bordered callout box, reference-deck style."""
    color=color or BLUE
    h=h or Inches(1.1)
    rrect(s,Inches(0.85),y,Inches(11.63),h,WHITE,line=color)
    if title:
        txt(s,Inches(1.2),y+Inches(0.13),Inches(11),Inches(0.32),[[(title,11.5,color,True)]])
        txt(s,Inches(1.2),y+Inches(0.5),Inches(11),h-Inches(0.62),[[(text,12.5,INK,False)]])
    else:
        txt(s,Inches(1.2),y,Inches(11),h,[[(text,13,INK,False)]],anchor=MSO_ANCHOR.MIDDLE)

def split_visual(title,left_head,left_items,right_head,right_items,kicker=None,
                 lcolor=None,rcolor=None,note=None):
    """Two panels of small labelled chips — richer than a bullet two-column."""
    lcolor=lcolor or BLUE; rcolor=rcolor or TEAL
    s=head(slide(),title,kicker)
    H=Inches(4.0) if note else Inches(4.7)
    for x,w,hd,items,col in ((Inches(0.85),Inches(5.7),left_head,left_items,lcolor),
                             (Inches(6.78),Inches(5.7),right_head,right_items,rcolor)):
        rrect(s,x,Inches(1.95),w,H,LIGHT,line=RGBColor(0xE6,0xEC,0xF4))
        rrect(s,x,Inches(1.95),w,Inches(0.55),col)
        txt(s,x,Inches(1.95),w,Inches(0.55),[[(hd,14,WHITE,True)]],
            align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
        n=len(items); y0=Inches(2.68); rh=int((H-Inches(0.85))/max(n,1))
        for i,it in enumerate(items):
            yy=int(y0+rh*i)
            oval(s,x+Inches(0.3),int(yy+rh/2-Inches(0.11)),Inches(0.22),Inches(0.22),col)
            txt(s,x+Inches(0.68),yy,w-Inches(1.0),rh,[[(it,12,INK,False)]],anchor=MSO_ANCHOR.MIDDLE)
    if note: callout(s,Inches(6.15),note,color=BLUE,h=Inches(0.72))
    footer(s); return s

# ---------------- visual admin components (no bullet walls) ----------------
def qr_glyph(s,x,y,size,color=INK):
    """Draw a simple QR-code glyph so the attendance slide is visual, not a bullet list."""
    rect(s,x,y,size,size,WHITE,line=LINE)
    m=int(size/9); pad=m
    for (cx,cy) in ((0,0),(6,0),(0,6)):   # three finder patterns
        fx=int(x+pad+cx*m); fy=int(y+pad+cy*m)
        rect(s,fx,fy,m*3,m*3,color)
        rect(s,int(fx+m*0.85),int(fy+m*0.85),int(m*1.3),int(m*1.3),WHITE)
    for (cx,cy) in ((4,2),(5,3),(4,4),(6,4),(3,5),(5,5),(6,6),(4,6),(2,4),
                    (6,2),(3,3),(5,7),(7,5),(2,6),(6,8),(8,6),(4,8)):
        rect(s,int(x+pad+cx*m),int(y+pad+cy*m),m,m,color)

def attendance_slide():
    """TRAQOM digital attendance — QR panel + 3-step flow (visual, per house rules)."""
    s=head(slide(),"Digital Attendance (Mandatory)","TRAQOM · SSG DIGITAL ATTENDANCE")
    rect(s,Inches(0.85),Inches(1.95),Inches(3.5),Inches(4.7),LIGHT)
    rect(s,Inches(0.85),Inches(1.95),Inches(3.5),Inches(0.12),BLUE)
    qr_glyph(s,Inches(1.55),Inches(2.45),Inches(2.1))
    txt(s,Inches(0.95),Inches(4.75),Inches(3.3),Inches(0.5),
        [[("Scan the SSG QR code",15,INK,True)]],align=PP_ALIGN.CENTER)
    txt(s,Inches(0.95),Inches(5.25),Inches(3.3),Inches(1.2),
        [[("Displayed by your trainer from the SSG portal at AM, PM and Assessment.",12,GREY,False)]],
        align=PP_ALIGN.CENTER)
    rows=[("AM","Scan at the start of each training day."),
          ("PM","Scan again after the lunch break."),
          ("ASSESSMENT","Scan before the final assessment begins."),
          ("75%","Minimum attendance required for funding and certification.")]
    rx=Inches(4.75); rw=Inches(7.73); ry=Inches(1.95); rh=Inches(4.7)
    n=len(rows); gy=Inches(0.22); th=int((rh-gy*(n-1))/n)
    for i,(label,val) in enumerate(rows):
        y=int(ry+(th+gy)*i); col=PALETTE[i%len(PALETTE)]
        rect(s,rx,y,rw,th,LIGHT); rect(s,rx,y,Inches(0.1),th,col)
        rect(s,rx+Inches(0.3),int(y+th/2-Inches(0.22)),Inches(1.55),Inches(0.44),col)
        txt(s,rx+Inches(0.3),int(y+th/2-Inches(0.22)),Inches(1.55),Inches(0.44),
            [[(label,12,WHITE,True)]],align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
        txt(s,rx+Inches(2.1),y,rw-Inches(2.45),th,[[(val,15,INK,False)]],anchor=MSO_ANCHOR.MIDDLE)
    footer(s); return s

def lms_slide():
    """Download Course Material — browser mock of lms-tms + numbered download flow."""
    s=head(slide(),"Download Your Course Material","COURSE PORTAL · LMS / TMS")
    bx,by,bw,bh=Inches(0.85),Inches(1.95),Inches(6.6),Inches(4.15)
    rect(s,bx,by,bw,bh,WHITE,line=LINE)
    rect(s,bx,by,bw,Inches(0.42),RGBColor(0xEE,0xF2,0xF7))   # browser chrome
    for i,c in enumerate((RGBColor(0xFF,0x5F,0x57),RGBColor(0xFE,0xBC,0x2E),RGBColor(0x28,0xC8,0x40))):
        oval(s,int(bx+Inches(0.18)+i*Inches(0.24)),int(by+Inches(0.13)),Inches(0.16),Inches(0.16),c)
    rect(s,int(bx+Inches(1.05)),int(by+Inches(0.09)),int(bw-Inches(1.35)),Inches(0.25),WHITE,line=LINE)
    txt(s,int(bx+Inches(1.2)),int(by+Inches(0.07)),int(bw-Inches(1.5)),Inches(0.28),
        [[("https://lms-tms.tertiaryinfotech.com",10,BLUE,False)]],anchor=MSO_ANCHOR.MIDDLE)
    txt(s,int(bx+Inches(0.3)),int(by+Inches(0.62)),int(bw-Inches(0.6)),Inches(0.4),
        [[("My Courses  ›  ",11,GREY,False),(C.SHORT_TITLE[:44],11,INK,True)]])
    files=[("Trainer Slides (PPT)",BLUE),("Learner Slides (PDF)",TEAL),
           ("Learner Guide (PDF)",VIOLET),("Lesson Plan (PDF)",AMBER)]
    for i,(name,col) in enumerate(files):
        fy=int(by+Inches(1.15)+i*Inches(0.66))
        rect(s,int(bx+Inches(0.3)),fy,int(bw-Inches(0.6)),Inches(0.54),LIGHT)
        rect(s,int(bx+Inches(0.3)),fy,Inches(0.08),Inches(0.54),col)
        txt(s,int(bx+Inches(0.55)),fy,Inches(3.6),Inches(0.54),[[(name,12,INK,False)]],anchor=MSO_ANCHOR.MIDDLE)
        rect(s,int(bx+bw-Inches(1.55)),int(fy+Inches(0.11)),Inches(1.15),Inches(0.32),col)
        txt(s,int(bx+bw-Inches(1.55)),int(fy+Inches(0.11)),Inches(1.15),Inches(0.32),
            [[("Download",10,WHITE,True)]],align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
    steps=[("1","Sign in to lms-tms.tertiaryinfotech.com with the email you registered with."),
           ("2","Open My Courses and select this course."),
           ("3","Download the slides, Learner Guide and Lesson Plan."),
           ("4","Keep them open — the assessment is open book.")]
    rx=Inches(7.75); rw=Inches(4.73)
    for i,(num,tx_) in enumerate(steps):
        y=int(Inches(1.95)+i*Inches(1.07)); col=PALETTE[i%len(PALETTE)]
        rect(s,rx,y,rw,Inches(0.92),LIGHT); rect(s,rx,y,Inches(0.1),Inches(0.92),col)
        oval(s,int(rx+Inches(0.3)),int(y+Inches(0.24)),Inches(0.44),Inches(0.44),col)
        txt(s,int(rx+Inches(0.3)),int(y+Inches(0.24)),Inches(0.44),Inches(0.44),
            [[(num,15,WHITE,True)]],align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
        txt(s,int(rx+Inches(0.92)),y,rw-Inches(1.2),Inches(0.92),[[(tx_,12,INK,False)]],anchor=MSO_ANCHOR.MIDDLE)
    txt(s,Inches(7.75),Inches(6.25),Inches(4.73),Inches(0.4),
        [[("Portal: https://lms-tms.tertiaryinfotech.com",11,BLUE,True)]])
    footer(s); return s

def briefing_slide():
    """Briefing for Assessment — do / don't tile grid instead of a bullet wall."""
    s=head(slide(),"Briefing for Assessment","BEFORE YOU START",kcolor=AMBER)
    cols=[(TEAL,"DO",["Place phones and bags under the table or on the floor.",
                      "Use a black or blue pen for hard-copy answers.",
                      "Read every question fully before answering.",
                      "Hand in your script when time is called."]),
          (RGBColor(0xDC,0x26,0x26),"DON'T",["No photos or recording of assessment scripts.",
                      "No discussion with other candidates.",
                      "No liquid paper or correction tape.",
                      "No unapproved materials on the desk."])]
    for i,(col,hd,items) in enumerate(cols):
        x=Inches(0.85)+i*Inches(5.93); w=Inches(5.7)
        rect(s,x,Inches(1.95),w,Inches(4.7),LIGHT); rect(s,x,Inches(1.95),w,Inches(0.62),col)
        txt(s,x,Inches(1.95),w,Inches(0.62),[[(hd,17,WHITE,True)]],
            align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
        for j,it in enumerate(items):
            y=int(Inches(2.78)+j*Inches(0.92))
            oval(s,int(x+Inches(0.32)),int(y+Inches(0.16)),Inches(0.34),Inches(0.34),col)
            txt(s,int(x+Inches(0.32)),int(y+Inches(0.16)),Inches(0.34),Inches(0.34),
                [[("✓" if i==0 else "✕",13,WHITE,True)]],align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
            txt(s,int(x+Inches(0.85)),y,w-Inches(1.15),Inches(0.7),[[(it,13,INK,False)]],anchor=MSO_ANCHOR.MIDDLE)
    footer(s); return s

def assessment_slide(kicker="FINAL ASSESSMENT"):
    """Assessment — instrument tiles (WA + Practical Performance) instead of bullets."""
    s=head(slide(),"Assessment",kicker,kcolor=VIOLET)
    cards=[(BLUE,"WRITTEN ASSESSMENT","WA · SAQ","1 hour · open book\nShort-answer questions on the course knowledge (K1–K6)."),
           (TEAL,"PRACTICAL PERFORMANCE","PP","1 hour · open book\nThree hands-on tasks using generative AI tools (A1–A6).")]
    for i,(col,hd,tag,body) in enumerate(cards):
        x=Inches(0.85)+i*Inches(5.93); w=Inches(5.7)
        rect(s,x,Inches(1.95),w,Inches(2.75),LIGHT); rect(s,x,Inches(1.95),w,Inches(0.12),col)
        rect(s,int(x+Inches(0.35)),Inches(2.35),Inches(1.5),Inches(0.44),col)
        txt(s,int(x+Inches(0.35)),Inches(2.35),Inches(1.5),Inches(0.44),
            [[(tag,13,WHITE,True)]],align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
        txt(s,int(x+Inches(0.35)),Inches(2.95),w-Inches(0.7),Inches(0.5),[[(hd,18,INK,True)]])
        txt(s,int(x+Inches(0.35)),Inches(3.5),w-Inches(0.7),Inches(1.1),[[(body,13,GREY,False)]])
    facts=[("Open book","Slides, Learner Guide and approved materials only."),
           ("Competent","You must pass BOTH instruments to be assessed Competent."),
           ("75% attendance","Required for assessment eligibility and funding."),
           ("Appeal","An appeal process is available if required.")]
    for i,(hd,body) in enumerate(facts):
        x=int(Inches(0.85)+(i%2)*Inches(5.93)); y=int(Inches(4.95)+(i//2)*Inches(0.88)); w=Inches(5.7)
        rect(s,x,y,w,Inches(0.74),LIGHT); rect(s,x,y,Inches(0.1),Inches(0.74),PALETTE[i%len(PALETTE)])
        txt(s,int(x+Inches(0.3)),y,Inches(1.8),Inches(0.74),
            [[(hd,13,PALETTE[i%len(PALETTE)],True)]],anchor=MSO_ANCHOR.MIDDLE)
        txt(s,int(x+Inches(2.1)),y,w-Inches(2.4),Inches(0.74),[[(body,12,INK,False)]],anchor=MSO_ANCHOR.MIDDLE)
    footer(s); return s

def support_slide():
    """Support — contact card grid instead of a bullet list."""
    s=head(slide(),"Support","WE'RE HERE TO HELP",kcolor=TEAL)
    txt(s,Inches(0.85),Inches(1.95),Inches(11.6),Inches(0.5),
        [[("If you have any enquiries during or after the class, please contact us.",17,GREY,False)]])
    cards=[(BLUE,"EMAIL","enquiry@tertiaryinfotech.com"),
           (TEAL,"TELEPHONE","+65 6100 0613"),
           (VIOLET,"WEBSITE","www.tertiarycourses.com.sg"),
           (AMBER,"LMS / TMS","lms-tms.tertiaryinfotech.com")]
    for i,(col,hd,val) in enumerate(cards):
        x=int(Inches(0.85)+(i%2)*Inches(5.93)); y=int(Inches(2.75)+(i//2)*Inches(2.0)); w=Inches(5.7)
        rect(s,x,y,w,Inches(1.75),LIGHT); rect(s,x,y,w,Inches(0.1),col)
        txt(s,int(x+Inches(0.4)),int(y+Inches(0.35)),w-Inches(0.8),Inches(0.4),[[(hd,12,col,True)]])
        txt(s,int(x+Inches(0.4)),int(y+Inches(0.8)),w-Inches(0.8),Inches(0.7),[[(val,19,INK,True)]])
    footer(s); return s

def recap_slide(code,items):
    """Topic recap — K/A chip tiles instead of a bullet wall."""
    s=head(slide(),f"Recap — Topic {code}","TOPIC RECAP",kcolor=TEAL)
    n=len(items); Y0=Inches(1.95); gy=Inches(0.16)
    rh=int((Inches(4.78)-gy*(n-1))/n)
    for i,(code_,body) in enumerate(items):
        y=int(Y0+(rh+gy)*i); col=PALETTE[i%len(PALETTE)]
        rect(s,Inches(0.85),y,Inches(11.63),rh,LIGHT); rect(s,Inches(0.85),y,Inches(0.1),rh,col)
        rect(s,Inches(1.15),int(y+rh/2-Inches(0.19)),Inches(1.15),Inches(0.38),col)
        txt(s,Inches(1.15),int(y+rh/2-Inches(0.19)),Inches(1.15),Inches(0.38),
            [[(code_,11,WHITE,True)]],align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
        txt(s,Inches(2.55),y,Inches(9.7),rh,[[(body,13,INK,False)]],anchor=MSO_ANCHOR.MIDDLE)
    footer(s); return s

# ============================================================ BUILD
cover()

# ---------------- ADMIN ----------------
section("COURSE ADMINISTRATION","Welcome & Housekeeping","")
attendance_slide()
trainer_slide("YOUR TRAINER · GENERAL","Your Trainer","General Trainer template —\nto be completed by the trainer",
 [("Name",""),("Title / Designation",""),("Qualifications",""),
  ("Areas of expertise",""),("Training & industry experience",""),("Contact","")],
 initials="?",accent=GREY)
trainer_slide("YOUR TRAINER",C.TRAINER,"Principal Trainer\nTertiary Infotech Academy Pte Ltd",
 [("Role","Principal Trainer, Tertiary Infotech Academy Pte Ltd"),
  ("Certification","Generative AI, digital transformation and data analytics — 20+ years in technology and innovation."),
  ("Delivers","WSQ courses on generative AI, business innovation, automation and data science."),
  ("Founder","Founder and lead instructor at Tertiary Infotech / Tertiary Courses.")],
 initials="AA",accent=BLUE)
content("Let's Know Each Other",[
 "Your name, organisation and role.",
 "Which generative AI tools you already use, and what for.",
 "One business problem in your organisation you would like GenAI to solve.",
 "What you want to be able to do by the end of Day 2."],kicker="ICE-BREAKER")
tile_grid("Ground Rules",[
 "Set your mobile phone to silent mode.","Participate actively — no question is too small.",
 "Mutual respect: agree to disagree.","One conversation at a time.",
 "Be punctual; return from breaks on time.","75% attendance is required."],
 kicker="HOUSEKEEPING",cols=2,size=15)
lms_slide()

# Skills Framework
tile_grid("Skills Framework — Business Innovation",[
 ("TSC Title",C.TSC_TITLE),("TSC Code",C.TSC_CODE),
 ("Proficiency","Level 5 — evaluate, design and manage business innovation."),
 ("Assessment","Written Assessment (SAQ) + Practical Performance (PP), both open book.")],
 kicker="SKILLS FRAMEWORK FOR ICT",cols=2,size=15,accent=VIOLET)
def tsc_slide():
    """Abilities vs Knowledge — code chip + text, sized to fit six rows a side."""
    s=head(slide(),"Skills Framework — Abilities & Knowledge",C.TSC_CODE)
    for x,w,hd,items,col in ((Inches(0.85),Inches(5.7),"ABILITIES (A1–A6)",C.TSC_ABILITIES,BLUE),
                             (Inches(6.78),Inches(5.7),"KNOWLEDGE (K1–K6)",C.TSC_KNOWLEDGE,TEAL)):
        rect(s,x,Inches(1.95),w,Inches(4.7),LIGHT); rect(s,x,Inches(1.95),w,Inches(0.5),col)
        txt(s,x,Inches(1.95),w,Inches(0.5),[[(hd,14,WHITE,True)]],
            align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
        y0=Inches(2.58); rh=int((Inches(3.95))/len(items))
        for i,it in enumerate(items):
            code,_,body=it.partition(": ")
            y=int(y0+rh*i)
            rect(s,x+Inches(0.22),y+int(rh/2-Inches(0.15)),Inches(0.42),Inches(0.3),col)
            txt(s,x+Inches(0.22),y+int(rh/2-Inches(0.15)),Inches(0.42),Inches(0.3),
                [[(code,10,WHITE,True)]],align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
            txt(s,x+Inches(0.76),y,w-Inches(1.0),rh,[[(body,11,INK,False)]],anchor=MSO_ANCHOR.MIDDLE)
    footer(s); return s
tsc_slide()

# Learning outcomes + outline
tile_grid("Learning Outcomes",[
 ("LO1 — Evaluate opportunities","Investigate GenAI business strategies and identify viable opportunities compatible with organisational objectives."),
 ("LO2 — Design and plan","Develop action plans for business innovation with GenAI and design digital architectures across the business."),
 ("LO3 — Implement and manage","Manage business innovation and facilitate information flow among stakeholders to review success and grow ideas.")],
 kicker="WHAT YOU'LL ACHIEVE",cols=1,size=15)
# ---- THE PIPELINE: what the whole course builds, shown up front ----
pipeline_flow("The Course Pipeline — One Idea, End to End",[
 ("Research the idea","Perplexity\nNotebookLM"),
 ("Evaluate & score","Chat assistant\nSheets"),
 ("Design Thinking\n+ Canvas","DT Studio · BMC Studio\n(group activities)"),
 ("Script the video","ChatGPT · Gemini\nCopilot 365"),
 ("Voice + music","ElevenLabs\nSuno"),
 ("Produce the video","Kling · CapCut"),
 ("Pitch & automate","Gamma · n8n")],
 kicker="THE JOURNEY · STAGES 1–7",
 note="You choose ONE business idea in Lab 3 and carry it through every lab to the end of the course. "
      "Each lab consumes what the previous one produced — nothing is rebuilt from scratch. The course "
      "finishes by automating this entire pipeline as an agentic workflow with a human review gate.")

journey("Eighteen Connected Labs",[
 ("1","Predictive vs Generative AI","Same data, two framings"),
 ("2","Map the GenAI Tool Landscape","Four modalities, hands-on"),
 ("3","Research Your Idea","Perplexity + NotebookLM"),
 ("4","Evaluate & Prioritise","Weighted scoring rubric"),
 ("5","Design Thinking Sprint","GROUP · DT Studio"),
 ("6","Business Model Canvas","GROUP · BMC Studio"),
 ("7","Digital Architecture","Five layers + governance"),
 ("8","Script the Video","Three assistants compared"),
 ("9","AI Voiceover","ElevenLabs, 60 seconds"),
 ("10","AI Soundtrack","Suno, licence checked"),
 ("11","Produce the Video","Kling + CapCut, captioned"),
 ("12","Business Presentation","Gamma, video embedded"),
 ("13","Risk-Assess the Pipeline","Your own assets"),
 ("14","Guardrails & AI Ethics","8 principles, 4 guardrail types"),
 ("15","Action Plan","90 days, go/no-go"),
 ("16","Measure Success","Baseline + counter-metric"),
 ("17","Stakeholder Comms","Map, policy, idea intake"),
 ("18","CAPSTONE — Agentic Workflow","Automated, human-reviewed")],
 kicker="WHAT YOU'LL BUILD",cols=2,
 note="Eighteen labs, each reusing the one before it. Nothing is rebuilt from scratch.")

link_grid("Your AI Toolkit — Research, Thinking & Text",[
 ("Perplexity","https://www.perplexity.ai","Research with cited sources · Lab 3"),
 ("NotebookLM","https://notebooklm.google.com","Reason over your documents · Lab 3"),
 ("ChatGPT","https://chat.openai.com","Drafting and challenge · Labs 1, 4, 8"),
 ("Google Gemini","https://gemini.google.com","Current web context · Lab 8"),
 ("Copilot 365","https://copilot.microsoft.com","Business documents · Lab 8"),
 ("DT Studio","https://alfredang.github.io/designthinking/","Design Thinking · Lab 5"),
 ("BMC Studio","https://alfredang.github.io/bcm/","Business Model Canvas · Lab 6")],
 kicker="ALL FREE TIERS · SIGN UP BEFORE LAB 1  (1 OF 2)",cols=2,accent=TEAL)
link_grid("Your AI Toolkit — Voice, Video & Automation",[
 ("ElevenLabs","https://elevenlabs.io","Text-to-speech voiceover · Lab 9"),
 ("Suno","https://suno.com","AI background music · Lab 10"),
 ("Kling AI","https://klingai.com","Text-to-video scenes · Lab 11"),
 ("CapCut","https://www.capcut.com","Edit, caption, export · Lab 11"),
 ("Gamma","https://gamma.app","AI presentations · Lab 12"),
 ("n8n","https://n8n.io","Agentic workflows · Lab 18")],
 kicker="ALL FREE TIERS · SIGN UP BEFORE LAB 1  (2 OF 2)",cols=2,accent=VIOLET)

cards3("Course Outline",[
 (BLUE,"Topic 1",["Predictive vs generative AI","The GenAI tool landscape","Business value of GenAI","Investigating opportunities","Evaluating and prioritising"]),
 (TEAL,"Topic 2",["Business Model Canvas","Design Thinking with GenAI","Digital architecture design","Integrating GenAI tools","Building the action plan"]),
 (VIOLET,"Topic 3",["Implementation best practices","Legal, ethical & security issues","Measuring and reviewing success","Stakeholder communication","The AIM framework"])],
 kicker="THREE TOPICS · 18 CONNECTED LABS")
two_col("Lesson Plan — 2 Days, 8 hours/day",[
 (f"Day 1 — {C.DAY_THEMES[1]}",0),
 ("Digital attendance (AM) · Introductions · Outcomes",1),
 ("Topic 1: Introduction to Business Innovation and GenAI",1),
 ("Labs 1–4: compare AI types, tool map, research your idea, score it",1),
 ("Topic 2 begins: Design Thinking and the Business Model Canvas",1),
 ("Labs 5–7: DT Studio sprint, BMC Studio canvas, digital architecture",1)],
 [(f"Day 2 — {C.DAY_THEMES[2]}",0),
 ("Topic 2 continues: the content production pipeline",1),
 ("Labs 8–12: script, voiceover, soundtrack, video, presentation",1),
 ("Topic 3: Implementing, governing and automating",1),
 ("Labs 13–18: risk, guardrails & ethics, plan, KPIs, comms, CAPSTONE",1),
 ("Revision · TRAQOM survey · Final Assessment (WA + PP)",1)],
 kicker="SCHEDULE",lhead="Day 1",rhead="Day 2")
briefing_slide()
assessment_slide()
flow_h("Assessment Flow",[
 "TRAQOM survey — scan the QR code on the LMS",
 "Assessment digital attendance — scan the SSG QR",
 "Sit WA (SAQ) then the PP — open book",
 "Submit your answers on the LMS",
 "Sign the Assessment Summary Record"],kicker="ON ASSESSMENT DAY")

# ---------------- TOPICS + ACTIVITIES ----------------
TOPIC_ACTS = {t["num"]: [a for a in ACTIVITIES if a["topic"]==t["num"]] for t in C.TOPICS}
CARD_COLORS=[BLUE,TEAL,VIOLET]

# ---- extra visual concept slides per topic (highly visual, no step-by-step) ----
def topic1_concepts():
    stat_band("Generative AI — The Market Opportunity",[
     ("$1.3T","Projected generative AI market by 2032"),
     (">35%","Compound annual growth rate"),
     ("70%","Of organisations piloting or deploying GenAI")],
     kicker="WHY NOW",color=BLUE)
    compare("Predictive AI vs Generative AI","PREDICTIVE AI",
     ["Scores, ranks and forecasts.","Learns from labelled historical data.",
      "Output: a number, class or probability.","Churn scoring, demand forecast, fraud detection.",
      "Mature — in production for a decade."],
     "GENERATIVE AI",
     ["Creates new content.","Learns patterns from very large corpora.",
      "Output: text, image, audio, video, code.","Drafting, design, summarising, conversation.",
      "Fast-moving — new capability every quarter."],
     kicker="K1 · THE SHIFT")
    flow_h("How Generative AI Works",[
     "Pre-train a foundation model on a very large corpus",
     "Align it with human feedback so answers are useful and safe",
     "Learner writes a prompt describing the task and context",
     "Model predicts the most likely next token, repeatedly",
     "Output is generated, then reviewed by a human"],kicker="UNDER THE HOOD",color=VIOLET)
    tile_grid("The Four Business Value Levers",[
     ("Revenue growth","Faster product development, new revenue channels, personalised offers at scale."),
     ("Cost & productivity","Worker augmentation in drafting, summarising, coding and support; long-term talent optimisation."),
     ("Risk mitigation","Broader, deeper visibility of data improves pattern recognition and early risk detection."),
     ("Sustainability","Supports regulatory compliance and embeds sustainability into design and decisions.")],
     kicker="WHERE THE VALUE COMES FROM",cols=2,size=15,accent=TEAL)
    tile_grid("The Generative AI Tool Landscape",[
     ("Text","ChatGPT · Gemini · Claude · Copilot · Perplexity"),
     ("Image","Firefly · Designer · Canva · Leonardo · Midjourney"),
     ("Speech & voice","ElevenLabs · Descript · TTS and voice cloning"),
     ("Music","Suno · Udio · AIVA · Soundraw"),
     ("Video","Sora · Runway · Kling · CapCut · Veed"),
     ("Digital human","HeyGen · D-ID · Synthesia · Descript"),
     ("3D models","Luma AI · Meshy · Spline · Tripo"),
     ("Office productivity","Microsoft 365 Copilot · Google Workspace Gemini"),
     ("Data & analysis","Code interpreter · Copilot in Excel · BI assistants"),
     ("IP & legal","Patent and trademark search · contract review assistants")],
     kicker="K1 · TEN MODALITIES",cols=2,size=12,accent=VIOLET)
    tile_grid("Use Cases Across Industries",[
     ("Food & beverage","McCormick used AI with IBM to develop new flavour combinations under its ONE platform."),
     ("Media & entertainment","Script development, storyboarding, dubbing, de-ageing and localised content at scale."),
     ("Public safety","Analysing historical incident data to allocate resources proactively — with strict oversight."),
     ("Financial services","Client reporting, KYC summarisation, adviser copilots and fraud narrative generation."),
     ("Healthcare","Clinical note-taking, patient communication drafting and research summarisation."),
     ("Retail & e-commerce","Product descriptions, personalised campaigns and conversational shopping assistants.")],
     kicker="K2 · REAL-WORLD ADOPTION",cols=2,size=13)
    tile_grid("Evaluating a GenAI Opportunity",[
     ("Business value","How much revenue, cost or risk does it actually move?"),
     ("Feasibility","Can it be built and adopted with the capability we have?"),
     ("Data readiness","Does the data exist, and are we permitted to use it?"),
     ("Risk","What is the legal, ethical, security and reputational exposure?"),
     ("Strategic fit","Does it advance a stated organisational objective?"),
     ("Decision","Score, weight, rank — then defend the top two and the discards.")],
     kicker="A2 · THE SCORING RUBRIC",cols=2,size=14,accent=AMBER)

def topic2_concepts():
    tile_grid("Business Planning Methodologies for Innovation",[
     ("Business Model Canvas","Nine blocks describing how the organisation creates, delivers and captures value."),
     ("Value Proposition Canvas","Matches customer jobs, pains and gains to your products and services."),
     ("Design Thinking","Empathise, Define, Ideate, Prototype, Test — human-centred and iterative."),
     ("Lean experimentation","Identify the riskiest assumption and test it cheaply before committing.")],
     kicker="K3 · STRUCTURE FOR INNOVATION",cols=2,size=15)
    link_grid("BMC Studio — Your Canvas Ed-Tool",[
     ("Design Thinking Studio","https://alfredang.github.io/designthinking/","5 stages · empathy map · voting — Lab 5"),
     ("BMC Studio","https://alfredang.github.io/bcm/","Nine blocks · Strategyzer prompts — Lab 6"),
     ("One owner creates","Share the Canvas ID","Team joins by link or QR code"),
     ("Everyone edits live","Real-time sticky notes","See teammates' initials as they work"),
     ("Nine blocks guided","Strategyzer prompts built in","Each block asks the right question"),
     ("Tag and prioritise","Category · priority · status","Vote on the riskiest assumptions"),
     ("Capture for Lab 12","Screenshot or share link","Goes straight into your pitch deck")],
     kicker="K3 · GROUP ACTIVITIES · LABS 5–6",cols=3,accent=VIOLET)
    step_cards("Six Rules for a Good Business Model Canvas",[
     ("Be specific","'Busy working parents in Singapore with children aged 4–8' beats 'families'. A vague segment produces a vague everything-else."),
     ("Make it testable","If no evidence could disprove a block, it is a slogan, not a business model. Write what would prove you wrong."),
     ("Keep it consistent","Revenue must come from the segment you named, through the channel you listed, using the resources you have."),
     ("3–5 items per block","A canvas crammed with everything says nothing. Force the prioritisation.")],
     kicker="K3 · CANVAS GUIDELINES  (1 OF 2)")
    step_cards("Six Rules for a Good Business Model Canvas",[
     ("Customer language","Write what the customer would say, not internal jargon. If they would not recognise the pain, you have not found it."),
     ("Hypothesis, not plan","Mark what is ASSUMED versus EVIDENCED. Then test the three riskiest assumptions within two weeks.")],
     kicker="K3 · CANVAS GUIDELINES  (2 OF 2)",
     ntitle="THE MOST COMMON FAILURE",
     note="Accepting the AI's first draft. A chat assistant writes a confident, generic canvas in seconds — it reads well "
          "and says nothing specific to your market. Feed it your Lab 3 research, then REWRITE at least four blocks with "
          "what only you know. The canvas is where your research becomes a business model, not where the AI guesses one.")
    tile_grid("The AI-Powered Business Model Canvas",[
     ("Customer segments","Cluster and profile segments from your own data."),
     ("Value propositions","Draft and stress-test alternative propositions fast."),
     ("Channels","Generate channel-specific content at scale."),
     ("Customer relationships","Assistants and personalised follow-up at every touchpoint."),
     ("Revenue streams","Model pricing scenarios and bundle options."),
     ("Key resources","Identify the data, models and skills actually required."),
     ("Key activities","Automate drafting, research, analysis and reporting."),
     ("Key partners","Map vendors, model providers and integration partners."),
     ("Cost structure","Estimate licence, inference, integration and change costs.")],
     kicker="K3 · NINE BLOCKS, AI-ASSISTED",cols=3,size=12,accent=TEAL)
    flow_h("Design Thinking with Generative AI",[
     "EMPATHISE — draft personas and interview guides, then talk to real users",
     "DEFINE — converge on one 'How might we' problem statement",
     "IDEATE — diverge to twenty ideas, then converge to three",
     "PROTOTYPE — generate concepts, copy, visuals and mockups quickly",
     "TEST — put it in front of users and measure what actually happens"],
     kicker="K3 · HUMAN-CENTRED, AI-ACCELERATED",color=TEAL)
    layers("Digital Architecture for a GenAI Solution",[
     ("Application","Where the user works — chat window, intranet, Teams, or an existing business system."),
     ("Orchestration","Prompts, retrieval, workflow automation and agent logic that connect data to the model."),
     ("Model","The foundation model or AI service — and whether your data leaves your tenancy when it is called."),
     ("Data","Source systems, documents and records — with owner, sensitivity and permission recorded."),
     ("Governance","Access control, human review points, logging, audit and prohibited-data rules across all layers.")],
     kicker="K4 · FIVE LAYERS",color=VIOLET)
    tile_grid("Four Integration Patterns",[
     ("Chat assistant","A general assistant for staff productivity. Fastest to adopt, lowest integration cost."),
     ("RAG over documents","Grounds answers in your own content so responses cite the organisation's truth."),
     ("Workflow automation","GenAI embedded as a step inside an existing business process."),
     ("Autonomous agent","Plans and executes multi-step tasks with tools — highest value, highest oversight need.")],
     kicker="K4 · CHOOSING THE PATTERN",cols=2,size=15,accent=AMBER)
    # ---- the content production pipeline (Labs 7-11) ----
    pipeline_flow("The Content Production Pipeline",[
     ("Script","ChatGPT · Gemini\nCopilot 365"),
     ("Storyboard","6 scenes\nvisual direction"),
     ("Voiceover","ElevenLabs\n~150 words"),
     ("Soundtrack","Suno\ninstrumental"),
     ("Video scenes","Kling AI\n~5s per clip"),
     ("Assemble","CapCut\ncaptions + export"),
     ("Present","Gamma\nvideo embedded")],
     kicker="K4 · LABS 8–12",
     note="Each stage consumes the previous one's output. The script sets the pace of the whole video — "
          "get it to 150 words and 60 seconds before you generate a single asset.")
    split_visual("Prompting the Three Text Assistants",
     "WHAT EACH IS BEST AT",
     ["ChatGPT — most creative; strongest hooks and taglines.",
      "Gemini — most current; can pull live web context.",
      "Copilot 365 — most business-appropriate; reads your own M365 documents.",
      "Run the SAME brief through all three, then combine the best parts."],
     "WHAT MAKES A PROMPT WORK",
     ["Give it a ROLE: 'You are a marketing copywriter.'",
      "State the AUDIENCE, the ONE message and the desired action.",
      "Specify FORMAT and LENGTH: '60 seconds, mark the timing.'",
      "Ask it to CHALLENGE you — assistants agree far too readily."],
     kicker="K4 · TEXT TOOLS · LAB 8",
     note="150 words ≈ 60 seconds of natural speech. Read the script aloud with a stopwatch before you go further.")
    step_cards("Voice, Music and Video — The Craft Tips",[
     ("Voiceover · ElevenLabs","Punctuation IS direction: a comma is a short pause, an ellipsis a beat. Write numbers and acronyms as they should be SAID ('twenty twenty-six', 'A-I'). Lower stability = more emotion, higher = steadier."),
     ("Music · Suno","Use Instrumental mode — lyrics fight the voiceover. Describe genre, mood, instruments and BPM. Never prompt 'in the style of <artist>'. Music sits 15–20 dB UNDER the voice."),
     ("Video · Kling","Name the subject, setting, camera move and lighting. Keep motion simple — hands, text and fast movement are where clips break. Reuse the same style words across scenes for consistency."),
     ("Assembly · CapCut","Lay the voiceover down FIRST, then cut visuals to it. Auto-caption, then PROOFREAD — 80% of social video is watched muted.")],
     kicker="K4 · AUDIO & VIDEO TOOLS · LABS 9–11",
     ntitle="BEFORE YOU PUBLISH ANYTHING",
     note="Check the free-tier licence of every generated asset. Free tiers are frequently non-commercial or watermarked, "
          "and voice cloning requires written consent from the person whose voice it is.")
    tile_grid("From Design to Action Plan",[
     ("Milestone","What is delivered, and by when."),
     ("Owner","A named role accountable for the outcome."),
     ("Resource","People, budget, licences and data access required."),
     ("Dependency","What must happen first, and who is blocking."),
     ("Risk & mitigation","What could derail it, and the control that prevents it."),
     ("Go / no-go","The numbers at week 12 that justify scaling, pausing or stopping.")],
     kicker="A4 · WHAT A VIABLE PLAN CONTAINS",cols=3,size=13)

def topic3_concepts():
    tile_grid("Implementation Best Practices",[
     ("Start narrow","One high-value use case with a measurable baseline beats ten pilots that prove nothing."),
     ("Human in the loop","Keep a review point wherever the output carries legal, financial or reputational weight."),
     ("Measure the baseline first","You cannot claim an improvement you never measured before the change."),
     ("Design for adoption","Train, communicate honestly about job impact, and make the tool easier than the old way."),
     ("Scale what works","Promote only the pilots that hit their go criteria; retire the rest without blame."),
     ("Iterate the loop","Assess, implement, manage — then reassess as models and regulation change.")],
     kicker="K5 · WHAT ACTUALLY WORKS",cols=2,size=14)
    compare("Legal & Copyright Considerations","THE CONTESTED GROUND",
     ["Training data — Getty Images v Stability AI and related suits.",
      "Authorship — the US Copyright Office holds purely AI-generated work unprotectable.",
      "Likeness and voice cloning consent.",
      "AI-generated music and derivative-work claims."],
     "WHAT TO DO",
     ["Read the vendor terms on commercial use and ownership.",
      "Keep a human contribution record for creative work.",
      "Obtain written consent for any real person's likeness or voice.",
      "Disclose AI-generated content where regulation or policy requires."],
     kicker="K6 · LEGAL",lcolor=AMBER,rcolor=TEAL)
    tile_grid("AI Ethics — The Principles",[
     ("Transparency","Users know when AI is used and how."),
     ("Fairness","No unjustified bias against any group."),
     ("Safety","The system behaves within intended bounds."),
     ("Explainability","Decisions can be understood and justified."),
     ("Privacy","Personal data is protected and minimised."),
     ("Security","The system resists misuse and attack."),
     ("Responsibility","A named human owns each AI outcome."),
     ("Auditability","Decisions are logged and reviewable.")],
     kicker="K6 · ETHICS",cols=2,size=14,accent=VIOLET)
    tile_grid("Singapore's AI Governance Landscape",[
     ("Model AI Governance Framework","IMDA's practical guidance on deploying AI responsibly, including for generative AI."),
     ("AI Verify","A testing framework and toolkit for validating AI system behaviour against governance principles."),
     ("PDPA","Consent, purpose limitation, retention and protection obligations for any personal data used."),
     ("Sector regulation","MAS, MOH and other regulators add sector-specific expectations on top of the baseline.")],
     kicker="K6 · GOVERNANCE IN SINGAPORE",cols=2,size=14,accent=BLUE)
    tile_grid("Security Risks in GenAI Adoption",[
     ("Prompt injection","Hostile instructions hidden in content the model reads, hijacking its behaviour."),
     ("Data leakage","Confidential material pasted into a public model and retained outside your control."),
     ("Shadow AI","Staff using unapproved tools with company data, invisible to IT and compliance."),
     ("Access control","Assistants inheriting broad permissions and exposing data users should not see."),
     ("Hallucination","Confident, fluent output that is simply wrong — dangerous without a review step."),
     ("Vendor & supply chain","Model, plugin and connector dependencies you do not control.")],
     kicker="K6 · SECURITY",cols=2,size=14,accent=AMBER)
    tile_grid("Measuring and Reviewing Success",[
     ("Adoption","Active users, tasks completed, share of the team using it weekly."),
     ("Efficiency","Cycle time and effort per task, against the pre-AI baseline."),
     ("Quality","Accuracy, rework rate and human-review pass rate."),
     ("Cost","Licence and inference cost per task versus the cost it replaced."),
     ("Business outcome","Revenue, retention, satisfaction or risk reduction actually moved."),
     ("Counter-metric","The measure that would reveal harm — errors, complaints, rework.")],
     kicker="A5 · THE KPI SET",cols=2,size=14,accent=TEAL)
    # ---- guardrails, ethics in practice, and the agentic capstone ----
    step_cards("Four Types of Guardrail",[
     ("INPUT","What may never enter a prompt: personal data, customer records, unreleased financials, credentials, client-identifying material. Define which tools are approved for which data classification."),
     ("PROCESSING","Prompt-injection defence: treat all retrieved or uploaded content as UNTRUSTED, never let retrieved text change the system instruction, and restrict which tools an agent may call."),
     ("OUTPUT","Before anything is published: facts verified against a source, licence terms confirmed, brand and tone reviewed, AI disclosure applied where required."),
     ("HUMAN-IN-THE-LOOP","A named person approves wherever output is customer-facing, carries legal or financial weight, or cannot be reversed.")],
     kicker="K6 · SECURITY GUARDRAILS · LAB 14",
     ntitle="THE RULE THAT MATTERS MOST",
     note="Put the human gate BEFORE the expensive, irreversible steps. Approving the script costs nothing; "
          "discovering the problem after the video is generated and published costs credits, money and reputation.")
    split_visual("AI Ethics — From Principle to Practice",
     "THE PRINCIPLE",
     ["Transparency — users know when AI is used.",
      "Fairness — no unjustified bias against any group.",
      "Privacy — personal data protected and minimised.",
      "Responsibility — a named human owns each outcome.",
      "Auditability — decisions are logged and reviewable."],
     "WHAT IT LOOKS LIKE IN YOUR PIPELINE",
     ["Every AI-generated video carries an on-screen AI label.",
      "Run the same prompt with two demographic framings and compare.",
      "No customer data ever enters a public tool. Ever.",
      "The approver's name is recorded on every published asset.",
      "Every workflow run is logged: input, output, approver, time."],
     kicker="K6 · ETHICS PRINCIPLES · LAB 14",lcolor=VIOLET,rcolor=TEAL,
     note="A principle without an observable behaviour is decoration. Write each one as something you could audit.")
    pipeline_flow("The Capstone — An Agentic Workflow with Human Review",[
     ("Idea submitted","n8n form\ntrigger"),
     ("Research agent","web search\ncited sources"),
     ("Evaluation agent","scoring rubric\nJSON verdict"),
     ("Canvas + script","chained agents\nstructured output"),
     ("HUMAN REVIEW","approve · reject\nrequest changes"),
     ("Assets generated","voice · music\nvideo"),
     ("Logged & delivered","audit row\n+ notification")],
     kicker="LAB 18 · AUTOMATING THE WHOLE PIPELINE",
     note="The workflow PAUSES at the human gate and only continues on approval — a rejection routes back to the "
          "script agent without spending a single video credit. A gate that cannot stop the process is not a gate.")
    flow_h("The AIM Framework for Implementing GenAI",[
     "ASSESS — investigate opportunities, evaluate viability and fit, pick the top use case",
     "IMPLEMENT — design the architecture, plan the pilot, build with governance from day one",
     "MANAGE — measure against baseline, review, communicate, and feed new ideas back in"],
     kicker="K5 · THE OPERATING LOOP",color=BLUE)
    tile_grid("Facilitating Stakeholder Information Flow",[
     ("Map the stakeholders","Plot influence against interest — sponsors, staff, IT, legal, customers."),
     ("Tailor the message","Executives need outcomes; affected staff need honesty about job impact."),
     ("Publish an AI use policy","Approved tools, prohibited data, disclosure rules and where to get help."),
     ("Build a community of practice","A channel and a monthly session where people share what worked."),
     ("Create an idea intake","A simple form so anyone can propose a use case."),
     ("Triage consistently","Score every submitted idea with the same rubric so the pipeline stays fair.")],
     kicker="A6 · KEEPING IDEAS FLOWING",cols=2,size=14,accent=VIOLET)

TOPIC_CONCEPTS = {1: topic1_concepts, 2: topic2_concepts, 3: topic3_concepts}

for t in C.TOPICS:
    section(f"TOPIC {t['code']}", t["title"], t["code"], t["subtitle"])
    # headline concept grid straight from the single source
    tile_grid(f"Key Concepts — Topic {t['code']}", t["concepts"],
              kicker=f"{t['weighting']} · WHAT THIS TOPIC COVERS", cols=2, size=13)
    # the rich visual concept deck for this topic
    TOPIC_CONCEPTS[t["num"]]()
    acts=TOPIC_ACTS[t["num"]]
    # card summary of the labs in this topic — split into at most 3 EVEN, NON-EMPTY
    # groups so no placeholder "—" tile and no degenerate "Labs 15–15" range appears.
    ncards=min(3,len(acts))
    base,extra=divmod(len(acts),ncards)
    groups=[];i=0
    for gi in range(ncards):
        n=base+(1 if gi<extra else 0)
        groups.append(acts[i:i+n]); i+=n
    cards=[]
    for gi,g in enumerate(groups):
        label=f"Lab {g[0]['num']}" if len(g)==1 else f"Labs {g[0]['num']}–{g[-1]['num']}"
        cards.append((CARD_COLORS[gi], label, [a["title"] for a in g]))
    cards3(f"Hands-On Labs — Topic {t['code']}", cards, kicker="WHAT YOU'LL DO")
    # per activity — overview + verification ONLY.
    # Step-by-step instructions live in the Learner Guide and labs/, never on a slide.
    for a in acts:
        activity_overview(f"LAB {a['num']}", a["title"], a["desc"], a["build"], a["services"],
                          kicker=f"TOPIC {t['code']} · HANDS-ON")
        test_slide(a["title"], a["test"], kicker=f"LAB {a['num']} · VERIFY")
    # topic recap — K/A chip tiles (visual), one row per lab objective
    recap_items=[]
    for a in acts:
        codes,_,body=a["objective"].partition(" — ")
        recap_items.append((codes.strip(), body.strip().capitalize() or a["title"]))
    recap_slide(t["code"], recap_items)

# ---------------- CLOSE ----------------
section("WRAP-UP","Course Summary & Next Steps","")
tile_grid("What You Achieved",[
 ("LO1 — Evaluated opportunities","Compared predictive and generative AI, mapped the tool landscape, researched real case studies and scored a prioritised opportunity register."),
 ("LO2 — Designed and planned","Built an AI-powered Business Model Canvas, ran a Design Thinking sprint, designed a five-layer digital architecture, shipped an AI assistant and a GenAI video."),
 ("LO3 — Implemented and managed","Produced a 90-day action plan, assessed legal/ethical/security risk, debated a real dilemma, built a KPI dashboard and a stakeholder communication plan.")],
 kicker="LEARNING OUTCOMES",cols=1,size=14)
big_statement("Start narrow. Measure the baseline. Govern from day one.",
 "The organisations that win with generative AI are not the ones with the most pilots — they are the ones that measured, governed and scaled the few that worked.",
 "THE TAKEAWAY",color=BLUE)
content("Your Next 30 Days",[
 "Take your top-ranked opportunity from Lab 4 and socialise it with your sponsor.",
 "Measure the pre-AI baseline for that task before you change anything.",
 "Run the 90-day pilot plan from Lab 15 with the go/no-go criteria you defined.",
 "Publish the one-page AI use policy from Lab 17 so staff know what is permitted.",
 "Set up the idea intake and triage new use cases with the Lab 4 rubric."],kicker="NEXT STEPS")
tile_grid("Recommended Follow-On Courses", C.RECOMMENDED,
 kicker="CONTINUE YOUR LEARNING",cols=1,size=14,accent=TEAL)
support_slide()
# END SEQUENCE (house rule): Assessment → Assessment Flow → Digital Attendance → Thank You
assessment_slide("WRAP-UP")
flow_h("Assessment Flow",[
 "TRAQOM survey — scan the QR code on the LMS",
 "Assessment digital attendance — scan the SSG QR",
 "Sit WA (SAQ) then the PP — open book",
 "Submit your answers on the LMS",
 "Sign the Assessment Summary Record"],kicker="ON ASSESSMENT DAY")
attendance_slide()
big_statement("Thank You!","You can now evaluate, design, implement and govern business innovation with generative AI in your own organisation.","SEE YOU AT THE NEXT COURSE",color=TEAL)

OUT=os.path.join(REPO,"courseware",f"{C.SHORT_TITLE}-{C.VERSION}.pptx")
prs.save(OUT)
print(f"Saved {OUT}  ({len(prs.slides.__iter__.__self__._sldIdLst)} slides)")
