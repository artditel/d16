import tkinter
WIDTH,HEIGHT=21,21
FPS = 300
move_number=0
square=23
def f(x):
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    return True
class Ball:
    def __init__(self,x,y):
        self.x=x
        self.y=y
def draw_field(canvas,game):
    if move_number==0:
        for i in range(0,WIDTH):
            canvas.create_line(i*square,0,i*square,HEIGHT*square, width=1)
            canvas.create_line(0,i*square,WIDTH*square,i*square, width=1)
    for i in game:
        if f(move_number+41):
            canvas.create_rectangle(i.x-square/2,i.y-square/2,i.x+square/2,i.y+square/2, fill='green')
        else:
            canvas.create_rectangle(i.x-square/2,i.y-square/2,i.x+square/2,i.y+square/2, fill='red')
        canvas.create_text(i.x,i.y,text=(str(move_number+41) if square>20 else None))
def make_move(game):
    global Game
    global move_number
    for i in game:
        v=V[move_number]
        i.x+=v[0]*square
        i.y+=v[1]*square
        move_number+=1
if __name__ == "__main__":
    c = tkinter.Canvas(width=WIDTH*square-2, height=HEIGHT*square-2)
    c.pack()
    c.focus_set()
def loop():
    global Game
    draw_field(c, Game)
    if move_number<(WIDTH+1)*(HEIGHT+1):
       make_move(Game)
    c.after(1000// FPS, loop)
V,q=[],0
for i in range(1,100):
    if q==0:
        for j in range(i):
            V.append((1,0))
        for j in range(i):
            V.append((0,1))
    if q==1:
        for j in range(i):
            V.append((-1,0))
        for j in range(i):
            V.append((0,-1))
    q=(q+1)%2
A=Ball(WIDTH//2*square+square/2,HEIGHT//2*square+square/2)
Game = [A]
loop()
c.mainloop()
