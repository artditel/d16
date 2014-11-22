import tkinter
import math
import sys

VECS_COUNT = 7
LEN = 100

WIDTH = 800
HEIGHT = 800

c = tkinter.Canvas(width=WIDTH, height=HEIGHT)
c.pack()

vecs = []
for i in range(VECS_COUNT):
    vecs.append((LEN * math.cos(math.pi * 2 / VECS_COUNT * i), LEN * math.sin(math.pi * 2 / VECS_COUNT * i)))

def for_seq(seq, i, func):
    if i < len(seq):
        seq[i] = 0
        for_seq(seq, i + 1, func)
        seq[i] = 1
        for_seq(seq, i + 1, func)

    else:
        func(seq)

def print_them(canvas, vecs, seq, fill = 'black'):
    vec = WIDTH/2 + sum(vecs[i][0] for i in range(VECS_COUNT) if seq[i]),  HEIGHT/2 + sum(vecs[i][1] for i in range(VECS_COUNT) if seq[i])
    for i in range(VECS_COUNT):
        if not seq[i]:
           canvas.create_line(vec[0], vec[1], vec[0] + vecs[i][0], vec[1] + vecs[i][1], fill=fill )

for_seq([0]*VECS_COUNT, 0, lambda x: print_them(c, vecs, x))
print_them(c, vecs, [0]*VECS_COUNT, 'red')

c.mainloop()



