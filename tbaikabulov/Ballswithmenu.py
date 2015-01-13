import tkinter
import sys
import random
import math
def distance (x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5
x_=0
y_=0
PAUSE=True
WIDTH=700
HEIGHT=700
w,h=WIDTH,HEIGHT/2
FPS = 100
g=0
G=0
ko=1/10
KO=1/10
activ=0
standart_Rad_of_ball=6
FIELD_COLOR='lime green'
BORDER_COLOR='dark green'
from tkinter import *
root = Tk()
menubar = Menu(root)

class Vector:
    def __init__(self,x,y):
            self.x=x
            self.y=y
    def __add__(self,other):
        if type(other)==Vector:
            return Vector(self.x+other.x,self.y+other.y)
        if type(other)==Ball:
            return Ball(other.x+self.x,other.y+self.y,other.v,other.m,other.fill,other.R)
    def __mul__(self,k):
        return Vector(self.x*k,self.y*k)
    def proj(self,a):
        cos=abs(math.cos(a))
        sin=abs(math.sin(a))
        return Vector( (self.x*cos-self.y*sin)*cos,(self.x*cos-self.y*sin)*sin)
    def __abs__(self):
        return (self.x**2+self.y**2)**0.5
    def __pow__(self,k):
        return Vector(self.x**k,self.y**k)
class Ball:
    force=Vector(0,0)
    impregnability=0
    def __init__(self,x,y,v,m,R,fill):
        self.x=x
        self.y=y
        self.v=v
        self.m=m
        self.fill=fill
        self.R=R
    def vec_to(self,b):
        return Vector(b.x-self.x,b.y-self.y)
    def vec_to_line(self,x1,y1,x2,y2):
        sin=(y2-y1)/distance(x1,y1,x2,y2)
        cos=(x2-x1)/distance(x1,y1,x2,y2)
        s=((y1-y2)*self.x+(x2-x1)*self.y+(x1*y2-y1*x2))/( (x2-x1)**2+(y1-y2)**2)**0.5
        return Vector(s*sin,-s*cos)    
    def distance(self,other):
        return ((self.x-other.x)**2+(self.y-other.y)**2)**0.5
    def distance_next(self,other):
        x1=self.x+self.v.x*ko+self.force.x*(0.5/self.m)*ko
        x2=other.x+other.v.x*ko+other.force.y*(0.5/other.m)*ko
        y1=self.y+self.v.y*ko+self.force.x*(0.5/self.m)*ko
        y2=other.y+other.v.y*ko+other.force.y*(0.5/other.m)*ko        
        return distance(x1,y1,x2,y2) 
    def E(self):
        return (self.v.x**2+self.v.y**2)*self.m/2-self.y*g*self.m
    def normal_distance(self,other):
        sin=(other.y-self.y)/self.distance(other)
        cos=(other.x-self.x)/self.distance(other)
        return Vector( (self.R+other.R)*cos,(self.R+other.R)*sin)
class Spring:
    def __init__(self,l,stiffness,B1,B2):
                self.length=length
                self.stiffness=stiffness
                self.b1=b1
                self.b2=b2
    def force(self):
                return (b1.distance(b2)- self.length) * self.stiffness    
class Rope:
    def __init__(self,length,b1,b2):
            self.length=length
            self.b1=b1
            self.b2=b2
    def force(self):
            return (self.b1.distance(self.b2)- self.length)*bool(self.b1.distance(self.b2)- self.length>0)*0.01
class Spoke:
    def __init__(self,x1,y1,x2,y2,Balls):
                self.x1=x1
                self.y1=y1
                self.x2=x2
                self.y2=y2
                self.Balls=Balls
def draw_field(canvas,game):
    canvas.delete(*canvas.find_all())
    canvas.create_rectangle(0,0,WIDTH, HEIGHT, fill=BORDER_COLOR)
    canvas.create_rectangle(5,5,WIDTH-5, HEIGHT-5, fill=FIELD_COLOR)
    if create_ball_active==True and x_*y_!=0:
        canvas.create_oval(x_-standart_Rad,y_-standart_Rad,x_+standart_Rad,y_+standart_Rad,fill='red')
    for b in game:
        canvas.create_oval(b.x-b.R,b.y-b.R,b.x+b.R,b.y+b.R, fill=b.fill)
    for s in Spring:
        canvas.create_line(s.b1.x,s.b1.y,s.b2.x,s.b2.y,width=3,fill='dim gray')
    for r in Rope:
        if r.b1.distance(r.b2)>=r.length or True:
            canvas.create_line(r.b1.x,r.b1.y,r.b2.x,r.b2.y)
        else:
            if r.b2.x>r.b1.x:
                par.draw_rope(r.b1.x,r.b1.y,r.b2.x,r.b2.y, r.length,canvas)
            if  r.b1.x>r.b2.x:
                par.draw_rope(r.b2.x,r.b2.y,r.b1.x,r.b1.y, r.length,canvas)
    for sp in Spoke:
        canvas.create_line(sp.x1,sp.y1,sp.x2,sp.y2, width=1)
        for j in sp.Balls:
            canvas.create_line(j.x,j.y,j.x+j.vec_to_line(sp.x1,sp.y1,sp.x2,sp.y2).x,j.y+j.vec_to_line(sp.x1,sp.y1,sp.x2,sp.y2).y)
            canvas.create_oval(j.x+j.vec_to_line(sp.x1,sp.y1,sp.x2,sp.y2).x+3,j.y+j.vec_to_line(sp.x1,sp.y1,sp.x2,sp.y2).y+3,j.x+j.vec_to_line(sp.x1,sp.y1,sp.x2,sp.y2).x-3,j.y+j.vec_to_line(sp.x1,sp.y1,sp.x2,sp.y2).y-3)
            c.create_text(100,100,text=str(abs(j.vec_to_line(sp.x1,sp.y1,sp.x2,sp.y2))))
            c.create_text(100,200,text=str(sum([b.E() for b in game])))
def make_move(game,c):
    global activ
    global Game
    global ko
    for r in Rope:
        if r.b1.distance(r.b2)>r.length:
            r.b1.force += r.b1.vec_to(r.b2) * r.force()
            r.b2.force += r.b1.vec_to(r.b1) * r.force()    
    for i in game:
        i.force+=Vector(0,g)
        i.force+=(i.v**2)*(-0.005)
        if not i.R<i.x+i.v.x*ko<WIDTH-i.R:
            pass
            i.v+=Vector(-2*i.v.x,0)
            i.impregnability+=10
        if not i.R<i.y+i.v.y*ko<HEIGHT-i.R:
            pass
            i.v+=Vector(0,-2*i.v.y)
            i.impregnability+=10
    for s in Spring:
        s.b1.force += s.b1.vec_to(s.b2) * s.force()
        s.b2.force += s.b1.vec_to(s.b1) * s.force() 
    for sp in Spoke:
        for j in sp.Balls:
            j.force+=j.vec_to_line(sp.x1,sp.y1,sp.x2,sp.y2)
    for b1 in game:
        for b2 in game:
            if b1!=b2 and b1.impregnability==0 and b2.impregnability==0:
                b1.force += b1.vec_to(b2) * G * b1.m * b2.m *(1/ (b1.distance(b2) ** 2))
                b2.force += b2.vec_to(b2) * G * b2.m * b1.m *(1/ (b2.distance(b1) ** 2))
                if (b1.v+b1).distance(b2.v+b2)<(b1.R+b2.R):
                    activ=2
                if b1.distance(b2)<(b1.R+b2.R):
                    b1.force += (b1.vec_to(b2)+b1.normal_distance(b2)*-1 )*(1/30)
                    b2.force += (b1.vec_to(b1)+b2.normal_distance(b1)*-1  )*(1/30)                  
    for b in game:
        if b.impregnability>0:
            b.impregnability-=1
        b.v+=b.force*ko
        b.force=Vector(0,0)
        b.x+=b.v.x*ko
        b.y+=b.v.y*ko
    if activ>0:
        ko=ko
        activ-=1
    else:
        ko=KO
    #print(sum([b.E() for b in game]))
if __name__ == "__main__":
    c = tkinter.Canvas(width=WIDTH, height=HEIGHT)
    c.pack()
    c.focus_set()
def loop():
    global Game
    draw_field(c, Game)
    if not PAUSE:
        for i in range(int(1/ko)):
            make_move(Game,c)
        #print(create_ball_active,x_,y_)
    c.after(1000// FPS, loop)
A=Ball(400,300,             Vector(-1,3),1,40,'orange')
B=Ball(500,200,             Vector(3,0),1,30,'red')
C=Ball(350,h/2,             Vector(1,-3),1,40,'white')
D=Ball(w/2,h/4,             Vector(4,1),5,20,'orange')
E=Ball(w/2-70,h/2+50,       Vector(1,1),3,20,'black')
F=Ball(w/2,h/2,             Vector(1,1),2,6,'yellow')
I=Ball(w/2,h/2-200,         Vector(1,1),1,6,'red')
Spoke1=Spoke(0,300,1000,300,[A])
Rope1=Rope(200,A,B)
Spoke=[]
Spring=[]
Rope=[]
Game = []
create_ball_active=False
standart_Rad=standart_Rad_of_ball
prGame=[Game,Game]
Undo_index=0
def donothing():
    filewin = Toplevel(root)
    button = Button(filewin, text="Do nothing button")
    button.pack()
def getXY(event):
    global x_
    global y_
    getx=event.x        #координата x сохраняется в переменной getx
    gety=event.y        #y  соответственно в gety
    x_,y_=getx,gety
def create_ball_activ():
    global standart_Rad
    global create_ball_active
    if create_ball_active==True:
        create_ball_active=False
    else:
        create_ball_active=True
    standart_Rad=standart_Rad_of_ball
def Create_Ball(event):
    global Game
    global prGame
    global Undo_index
    if create_ball_active:
        prGame+=[Game]
        Game.append(Ball(event.x,event.y,     Vector(1,1),1,standart_Rad,'red'))
        #create_ball_activ()
        Undo_index=0
def increase_rad(event):
    global standart_Rad
    if create_ball_active and standart_Rad+event.delta/60>1:
        standart_Rad+=event.delta/60
def start_game():
    global PAUSE
    PAUSE=False
def stop_game():
    global PAUSE
    PAUSE=True
def new_game():
    global Game
    Game=[]
def Undo():
    print(1)
    global Game
    global Undo_index
    Undo_index+=1
    print(prGame)
    Game=prGame[-2]
c.bind('<Motion>',getXY)
c.bind('<Button-1>',Create_Ball)
c.bind('<MouseWheel>',increase_rad)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=new_game)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

gamemenu = Menu(menubar, tearoff=0)
gamemenu.add_command(label="Start", command=start_game)
gamemenu.add_command(label="Pause", command=stop_game)
menubar.add_cascade(label="Game", menu=gamemenu)



editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=Undo)

editmenu.add_separator()

editmenu.add_command(label="Create Ball", command=create_ball_activ)
editmenu.add_command(label="Create Spoke", command=donothing)
editmenu.add_command(label="Create Rope", command=donothing)
editmenu.add_command(label="Create Spring", command=donothing)

menubar.add_cascade(label="Create odject", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)

root.focus_set() 
loop()
root.mainloop()
c.mainloop()
