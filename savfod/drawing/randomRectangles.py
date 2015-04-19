import tkinter
import random

WIDTH = 1200
HEIGHT = 800
H_COUNT = 100
W_COUNT = 100

canvas = tkinter.Canvas(width=WIDTH, height=HEIGHT)
canvas.pack()
for i in range(W_COUNT):
    for j in range(H_COUNT):
        color = "#"+("%06x"%random.randint(0,16777215))
        canvas.create_rectangle(WIDTH/W_COUNT * i, HEIGHT/H_COUNT * j, WIDTH/W_COUNT * (i + 1), HEIGHT/H_COUNT * (j + 1), fill=color)
canvas.mainloop()
