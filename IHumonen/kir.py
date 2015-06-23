import tkinter
import sys
import random
 
from collections import namedtuple

WIDTH=1200
HEIGHT=800
FPS = 1000
global key
Point = namedtuple("Point", ["x", "y"])
VAL  = []
W = 15
H = 10
def draw_field(canvas):
    global cell_width
    global cell_height
    cell_width = WIDTH // W
    cell_height = HEIGHT // H
    def draw_cell(point):
        canvas.create_rectangle(
            cell_width * point.x,
            cell_height * point.y,
            cell_width * (point.x + 1),
            cell_height * (point.y + 1))

    canvas.delete(*canvas.find_all())
    for i in range(W):
        for j in range(H):
            draw_cell(Point(i, j))

    canvas.create_rectangle(
            cell_width * 0,
            cell_height * H//2,
            cell_width * (0 + 1),
            cell_height * (H//2 + 1),
            fill= 'green')
    canvas.create_rectangle(
            cell_width * W-2,
            cell_height * H//2,
            cell_width * (W-1),
            cell_height * (H//2 + 1),
            fill= 'green')
def starter(event):
    for i in range(H):
        vs = []
        for j in range(W):
            vs.append(0)
        VAL.append(vs)
        print(VAL)
        VAL[H//2][0] = 1
        VAL[H//2][W-1] = 1        

root = tkinter.Tk()
c = tkinter.Canvas(root, width=WIDTH, height=HEIGHT)
draw_field(c)

def choose1(event):
    getx = event.x
    gety = event.y
    cx = getx // cell_width
    cy = gety // cell_height 
    VAL[cy][cx] = 1
    c.create_rectangle(
            cell_width * cx,
            cell_height * cy,
            cell_width * (cx + 1),
            cell_height * (cy + 1),
            fill= 'green')

def choose2(event):
    getx = event.x
    gety = event.y
    cx = getx // cell_width
    cy = gety // cell_height 
    VAL[cy][cx] = 2
    c.create_rectangle(
            cell_width * cx,
            cell_height * cy,
            cell_width * (cx + 1),
            cell_height * (cy + 1),
            fill= 'red')
c.bind('<Button-1>', choose1)
c.bind('<Button-3>', choose2)

def key_press(event):
    if event.keysym == "Return":
        '''def obxod(t,x,y):
            k = 0
            oiu = []
            if VAL[y+1][x] == 1:
                obxod(t,x,y+1)
                k+=1
            if VAL[y-1][x] == 1:
                obxod(t,x,y-1)
                k+=1
            if VAL[y][x+1] == 1:
                obxod(t,x+1,y)
                k+=1`xx`
            if k > 1 and t == 0:

                mass.append'''


but = tkinter.Button(root)
but['text'] = 'Start'
but['bg'] = 'blue'
but['fg'] = 'yellow'
but.pack(side = 'right')
but.bind("<Button-1>", starter)

c.bind("<Key>", key_press)
c.pack()
c.focus_set()
root.mainloop()
c.mainloop()