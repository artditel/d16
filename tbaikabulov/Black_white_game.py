width=int(input("input a width of field, please: "))
height=int(input("input a height of field, please: "))
W,H=width,height
import tkinter
WIDTH=W*50
HEIGHT=H*50
c = tkinter.Canvas(width=WIDTH, height=HEIGHT)
c.pack()
c.focus_set()

moves=[(2,2),(1,0),(1,2)]
A=[[0]*(W) for i in range(H)]
A[0][0]=2
c.create_rectangle(0,0,50,50,fill='black')
for h in range(H):
    for w in range(W):
        if not (w==0 and h==0):
            A[h][w]=2
            c.create_rectangle(w*50,h*50,(w+1)*50,(h+1)*50,fill='black')
            for i in moves:
                if w-i[0]>=0 and h-i[1]>=0:
                    if A[h-i[1]][w-i[0]]==2:
                        A[h][w]=1
                        c.create_rectangle(w*50,h*50,(w+1)*50,(h+1)*50,fill='white')
c.create_rectangle(WIDTH-50,HEIGHT-50,WIDTH,HEIGHT,fill='red')
c.mainloop()
