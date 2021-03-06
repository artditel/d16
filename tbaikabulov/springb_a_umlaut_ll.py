import tkinter
import sys
import random
import math
from collections import namedtuple

WIDTH=1200
HEIGHT=600
FPS = 100
# MASS = [2,30]
# MASS = [2,3]
# MASS = [2,3]
# MASS = [2,3]
m=MASS
HOLE_FILL='black'
FIELD_COLOR='green'
BORDER_COLOR='dark green'
HOLE_RADIUS=[33,24]
r=17
R=[25,25]
V=[2,-10]
ktr=0
a=[-ktr,-ktr,-ktr,-ktr,-ktr,-ktr,-ktr,-ktr]
v=V
xmax0=0
xmax1=WIDTH
hline0=HEIGHT*0.75
hline1=HEIGHT*0.66
stick=False
l=200
angle=90
bort=50

FILL=['red','blue','white','brown','yellow','orange','grey']
FILL1=['red','white','white','white','white','white','red']
fill=FILL1

HOLES=[]
def wend(event):
    global stick
    global v
    l=stick
    if l==True:
        stick=False
    if l==False:
        stick=True
def draw_field(canvas,lgame):
    canvas.delete(*canvas.find_all())
    canvas.create_rectangle(0,0,WIDTH, HEIGHT, fill=BORDER_COLOR)
    canvas.create_rectangle(10,10,WIDTH-10, HEIGHT-50, fill=FIELD_COLOR)
    for i in range(len(HOLES)):
        canvas.create_oval(HOLES[i][0],HOLES[i][1],HOLES[i][2],HOLES[i][3],fill=HOLE_FILL)
    for i in range(0,len(lgame)):
        canvas.create_oval(
            lgame[i][0]-R[i],
            HEIGHT-bort-2*R[i],
            lgame[i][0]+R[i],
            HEIGHT-bort,
            fill=fill[i])
    canvas.create_line(xmax0,hline0,0,hline0, fill='red')
    canvas.create_line(xmax1,hline1,WIDTH,hline1, fill='white')
def distance (x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5
def make_move(lgame):
    global R
    global v
    global xmax1
    global xmax0
    angle0=lgame[0][2]
    angle1=lgame[1][2]
    positionx0=lgame[0][0]
    positiony0=lgame[0][1]
    positionx1=lgame[1][0]
    positiony1=lgame[1][1]
    if positionx1<xmax1:
        xmax1=positionx1
    if positionx0>xmax0:
        xmax0=positionx0
    if not(10+R[0]<positionx0+v[0]<WIDTH-R[0]-10):
        v[0]=-v[0]
    if not(10+R[1]<positionx1+v[1]<WIDTH-R[1]-10):
        v[1]=-v[1]
    if not( abs(positionx0-positionx1)>(2*((R[0]*R[1])**0.5))+1):
        m0, m1 = MASS[0], MASS[1]
        u0=(2*m[1]*v[1]+v[0]*(m[0]-m[1]))/(m[0]+m[1])
        u1=(2*m[0]*v[0]+v[1]*(m[1]-m[0]))/(m[0]+m[1])
        v[0]=u0
        v[1]=u1
    if stick:
        R[1]+=0.1
    positionx0+=v[0]
    positionx1+=v[1]
    return [[positionx0, positiony0, angle0, True],
            [positionx1, positiony1,angle1, True]]
if __name__ == "__main__":
    c = tkinter.Canvas(width=WIDTH-2, height=HEIGHT-2)
    c.pack()
    c.focus_set()
c.bind('<Button-1>',wend)
def loop():
    global lgame
    draw_field(c, lgame)
    lgame = make_move(lgame)
    c.after(1000 // FPS, loop)
lgame = [[bort/5+R[0],HEIGHT-bort-R[0], 0,True],
         [WIDTH-bort/5-R[1],HEIGHT-bort-R[1], 0,True]]
loop()
c.mainloop()
