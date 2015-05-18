import tkinter
WIDTH,HEIGHT=400,400
FPS = 300
move_number=0
x_=0
y_=0
POINTS=[]
LINES=[]
active=True
r=2
FIELD_COLOR='light green'
def getXY(event):
    global x_
    global y_
    global POINTS
    x_,y_=event.x,event.y
    if active:
        POINTS.append([x_,y_,0])
def delete(event):
    global active
    global POINTS
    global LINES
    active=True
    POINTS=[]
    LINES=[]
def find_obol(massiv):
    return massiv
def create(event):
    global active
    global LINES
    active=False
    points=find_obol(POINTS)
    for i in range(0,len(points)):
        LINES.append([points[i][0],points[i][1],points[(i+1)%len(points)][0],points[(i+1)%len(points)][1]])
def angle(point1,point2):
    return (point1[1]-point2[1])/ ((point2[1]-point1[1])**2+(point2[0]-point1[0])**2)**0.
    
        
class Ball:
    def __init__(self,x,y):
        self.x=x
        self.y=y
def draw_field(canvas,game):
    canvas.delete(*canvas.find_all())
    canvas.create_rectangle(5,5,WIDTH-5, HEIGHT-5, fill=FIELD_COLOR)
    for i in POINTS:
        canvas.create_oval(i[0]-r,i[1]-r,i[0]+r,i[1]+r, fill='red' ,width=1)
    for i in LINES:
        canvas.create_line(i[0],i[1],i[2],i[3], fill='red' ,width=1)
def make_move(game):
    global Game
    global move_number
if __name__ == "__main__":
    c = tkinter.Canvas(width=WIDTH-2, height=HEIGHT-2)
    c.pack()
    c.focus_set()
def loop():
    global Game
    draw_field(c, Game)
    c.after(1000// FPS, loop)
A=Ball(WIDTH//2,HEIGHT//2)
Game = [A]
c.bind('<Button-1>',getXY)
c.bind('<Button-3>',delete)
c.bind('<Button-2>',create)
loop()
c.mainloop()
