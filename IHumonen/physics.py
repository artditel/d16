import tkinter
import math
FPS = 24 
c=tkinter.Canvas(width=500, height=300)
c.pack()
r=5
vx=30
g=100
state = {'x':10, 'y':20, 'vy':0}
def make_step(state, time_interval):
    global vx
    global g
    if state['x'] <  200:
        state['x']=state['x']+vx*time_interval 
        state['y']=state['y']
    else:
        state['x']=state['x']+vx*time_interval
        state['vy']+=g*time_interval
        state['y']=state['y']+state['vy']*time_interval
def redraw(c, state):
    c.delete(*c.find_all())
    c.create_rectangle(0, 25, 200, 30, fill='yellow')
    c.create_oval(state['x']- r, state['y']-r, state['x']+r, state['y']+r, fill ='blue')
def loop():
    global state
    make_step(state, 1 / FPS)
    global c
    redraw(c, state)
    c.after(1000 // FPS, loop)
    
loop()
c.mainloop()