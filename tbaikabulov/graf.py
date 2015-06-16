import tkinter
from tkinter import *
w,h=1000,1000
cen=(40,h-40)
r=2
kx=50
ky=13
points= [(0,0),(1.8,3.3),(2.6,8.83),(3.7,11.5),(4.7,14.65),(5.75,18.05),(6.65,19.71),(8.7,29.9),(10.85,37.78),(12.6,42.1),(14.8,49.18),(16.6,58.13)]
points2=[(0,0),(1.0,4.0),(2.05,8.0),(3.05,14.5),(4.0,20.0),(6.0,27.5),(8.1,40.0),(10.0,52.0),(11.9,60.0),(14.0,71.0)]
for i in range(0,len(points)):
    points[i]=points[i][0]*kx,points[i][1]*ky
for i in range(0,len(points2)):
    points2[i]=points2[i][0]*kx,points2[i][1]*ky
print(points2)
c = tkinter.Canvas(width=w, height=h)
c.pack()
c.focus_set()
c.create_rectangle(0,0,w, h, fill='white')
for i in range(0,150):
    c.create_line(0,cen[1]-ky*i,w,cen[1]-ky*i,fill='grey82')
    c.create_line(cen[0]+kx*i,0,cen[0]+kx*i,h,fill='grey82')
c.create_line(cen[0],0,cen[0],h)
c.create_line(0,cen[1],w,cen[1])
c.create_text(cen[0]-10,cen[1]+10,text=str(0),font=('Purisa',10))
c.create_text(w-55,cen[1]-13,text='length, cm',font=('Purisa',12))
c.create_text(cen[0]+23,20,text='angle',font=('Purisa',12))

for i in range(0,len(points)):
    if i!=len(points)-1:
        c.create_line(cen[0]+points[i][0],cen[1]-points[i][1],cen[0]+points[i+1][0],cen[1]-points[i+1][1],width=2,fill='red')
    c.create_oval(cen[0]+points[i][0]-r,cen[1]-points[i][1]-r,cen[0]+points[i][0]+r,cen[1]-points[i][1]+r,fill='red')
    c.create_line(cen[0]+points[i][0],cen[1]-points[i][1],cen[0],cen[1]-points[i][1],fill='grey55')
    c.create_line(cen[0]+points[i][0],h-cen[0],cen[0]+points[i][0],cen[1]-points[i][1]+r,fill='grey55')
    if i!=0:
        c.create_text(cen[0]+points[i][0],cen[1]+9,text=(str(points[i][0]/kx)+'0'*5)[0:4],font=('Purisa',6))
        c.create_text(cen[0]-14,cen[1]-points[i][1],text=(str(points[i][1]/ky)+'0'*5)[0:4],font=('Purisa',6))
        c.create_oval(cen[0]-r,cen[1]-points[i][1]-r,cen[0]+r,cen[1]-points[i][1]+r,fill='black')
        c.create_oval(cen[0]+points[i][0]-r,cen[1]-r,cen[0]+points[i][0]+r,cen[1]+r,fill='black')
points=points2
for i in range(0,len(points)):
    if i!=len(points)-1:
        c.create_line(cen[0]+points[i][0],cen[1]-points[i][1],cen[0]+points[i+1][0],cen[1]-points[i+1][1],width=2,fill='green')
    c.create_oval(cen[0]+points[i][0]-r,cen[1]-points[i][1]-r,cen[0]+points[i][0]+r,cen[1]-points[i][1]+r,fill='red')
    c.create_line(cen[0]+points[i][0],cen[1]-points[i][1],cen[0],cen[1]-points[i][1],fill='grey55')
    c.create_line(cen[0]+points[i][0],h-cen[0],cen[0]+points[i][0],cen[1]-points[i][1]+r,fill='grey55')    
    if i!=0:
        c.create_text(cen[0]+points[i][0],cen[1]-9,text=(str(points[i][0]/kx)+'0'*5)[0:4],font=('Purisa',6))
        c.create_text(cen[0]+14,cen[1]-points[i][1],text=(str(points[i][1]/ky)+'0'*5)[0:4],font=('Purisa',6))
        c.create_oval(cen[0]-r,cen[1]-points[i][1]-r,cen[0]+r,cen[1]-points[i][1]+r,fill='black')
        c.create_oval(cen[0]+points[i][0]-r,cen[1]-r,cen[0]+points[i][0]+r,cen[1]+r,fill='black')
c.mainloop()
