import tkinter
import sys
import random
import math
import par
def distance (x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5  
WIDTH=800
HEIGHT=900
w,h=WIDTH,HEIGHT/2
FPS = 100
g=1
G=0
ko=1/100
HOLE_FILL='black'
FIELD_COLOR='lime green'
BORDER_COLOR='dark green'
def  S(a,b,c):
    p=(a+b+c)/2
    return (p*(p-a)*(p-b)*(p-c))**0.5
def distancel(x1,y1,x2,y2,x,y):
    return S( ((x-x1)**2+(y-y1)**2)**0.5,((x2-x1)**2+(y2-y1)**2)**0.5,((x-x2)**2+(y-y2)**2)**0.5)/((x2-x1)**2+(y2-y1)**2)**0.5
class Vector:
    def __init__(self,x,y):
            self.x=x
            self.y=y
    def __add__(self,other):
        return Vector(self.x+other.x,self.y+other.y)
    def __mul__(self,k):
        return Vector(self.x*k,self.y*k)
    def proj(self,a):
        cos=abs(math.cos(a))
        sin=abs(math.sin(a))
        return Vector( (self.x*cos-self.y*sin)*cos,(self.x*cos-self.y*sin)*sin)
    def __abs__(self):
        return (self.x**2+self.y**2)**0.5
class Ball:
    force=Vector(0,0)
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
    def E(self):
        return (self.v.x**2+self.v.y**2)*self.m/2
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
            return (self.b1.distance(self.b2)- self.length)*bool(self.b1.distance(self.b2)- self.length>0)*0.1
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
    for b in game:
        canvas.create_oval(b.x-b.R,b.y-b.R,b.x+b.R,b.y+b.R, fill=b.fill)
    for s in Spring:
        canvas.create_line(s.b1.x,s.b1.y,s.b2.x,s.b2.y,width=3,fill='dim gray')
    for r in Rope:
        while r.b1.distance(r.b2)>=r.length:
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
def change(v0,m0,v1,m1):
    u0=(2*m1*v1+v0*(m0-m1))*(1/(m0+m1))
    u1=(2*m0*v0+v1*(m1-m0))*(1/(m0+m1))
    return(u0,u1)
def make_move(game,c):
    global Game
    global k
    global G
    print(1)
    for r in Rope:
        if r.b1.distance(r.b2)>r.length and 1==0:
            r.b1.force += r.b1.vec_to(r.b2) * r.force()
            r.b2.force += r.b1.vec_to(r.b1) * r.force()    
    for i in game:
        i.force+=Vector(0,g)
        if not i.R<i.x+i.v.x*ko<WIDTH-i.R:
            pass
            i.v+=Vector(-2*i.v.x,0)
        if not i.R<i.y+i.v.y*ko<HEIGHT-i.R:
            pass
            i.v+=Vector(0,-2*i.v.y)
    print(2)
    for s in Spring:
        s.b1.force += s.b1.vec_to(s.b2) * s.force()
        s.b2.force += s.b1.vec_to(s.b1) * s.force() 
    for sp in Spoke:
        for j in sp.Balls:
            if 1==0:
                j.force+=j.vec_to_line(sp.x1,sp.y1,sp.x2,sp.y2)
    for b1 in game:
        for b2 in game:
            if b1!=b2 and 1==0:
                b1.force += b1.vec_to(b2) * G * b1.m * b2.m *(1/ (b1.distance(b2) ** 2))
                b2.force += b2.vec_to(b2) * G * b2.m * b1.m *(1/ (b2.distance(b1) ** 2))                
                if b1.distance(b2)<b1.R+b2.R:
                    b1.force += (b1.vec_to(b2)+b1.normal_distance(b2)*-1 )*(1/10)
                    b2.force += (b1.vec_to(b1)+b2.normal_distance(b1)*-1  )*(1/10)                  
    for b in game:
        b.v+=b.force*ko
        b.force=Vector(0,0)
        b.x+=b.v.x*ko
        b.y+=b.v.y*ko
    #print(sum([b.E() for b in game]))
if __name__ == "__main__":
    c = tkinter.Canvas(width=WIDTH, height=HEIGHT)
    c.pack()
    c.focus_set()
def loop():
    global Game
    draw_field(c, Game)
    for i in range(int(1/ko)):
        pass
        make_move(Game,c)
    c.after(1000// FPS, loop)
A=Ball(400,300,             Vector(-1,3),1,40,'orange')
B=Ball(500,200,             Vector(1,0),1,30,'red')
C=Ball(350,h/2,             Vector(1,1),1,40,'white')
D=Ball(w/2,h/4,             Vector(1,1),5,20,'orange')
E=Ball(w/2-70,h/2+50,       Vector(1,1),3,20,'black')
F=Ball(w/2,h/2,             Vector(1,1),2,6,'yellow')
I=Ball(w/2,h/2-200,         Vector(1,1),1,6,'red')
Spoke1=Spoke(0,300,1000,300,[A])
Rope1=Rope(200,A,B)
Spoke=[Spoke1]
Spring=[]
Rope=[Rope1]
Game = [A,B]
loop()
c.mainloop()
