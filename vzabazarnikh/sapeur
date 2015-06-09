import tkinter
import random










def pol_param():
    size = 50	
    a = 8
    b = 8
    n = 10
    return [size, a, b, n]





def perevod(a, v, d):
    f = a*v + d
    return f




def sozd_bomb(a, b, n):
    m = []
    for x in range(n):
        k = (random.randrange(a * b))
        while k in m:
            k = (random.randrange(a * b))
        m.append (k)
    return m



def prov(m, f):
    if f in m:
        return 1
    else:
        return 0






def sh_kl(m, f, a):
    if f in m:
        return(9)
    c = prov (m, (f + 1)) + prov (m, (f - 1)) + prov (m, (f + a)) + prov (m, (f - a)) + prov (m, (f + a + 1)) + prov (m, (f + 1 - a)) + prov (m, (f - 1 - a)) + prov (m, (f - 1 + a))
    return c




def sh_znach(m, a, b):
    pole = []
    for i in range(b):
        pole.append([0; 0; 0] * a)
    for x in range(a):
        for y in range(b):
            pole[x][y][0] = sh_kl(m, perevod(a, x, y), a)
    pole.append(0)
    return pole





def right_click(a, b, pole, k):
    if pole[-1] == 0:
        if pole[b][a][1] == 0:
            if pole[b][a][2] == 0:
                pole[b][a][2] = 1
            else:
                pole[b][a][2] = 0
        paint(pole)
    return (pole)



def left_click(a, b, pole, k):
    if pole[-1] == 0:
        if pole[b][a][2] == 0:
            pole[b][a][1] = 0
        paint(pole)
        if pole[b][a][0] == 9:
            pole[-1] = 1
    return (pole)







def LClick(x, y, size, pole, k):
    x, y = event.x, event.y
    b = y//size
    a = x//size
    left_click(a, b, pole)

    

    

def RClick(event, size, pole, k):
    x, y = event.x, event.y
    b = y//size
    a = x//size
    right_click(a, b, pole)












size = dan[0]
dan = pol_param()
m = sozd_bomb(dan[1], dan[2], dan[3])

canvas = tkinter.Canvas()
canvas.pack()
pole = sh_znach(m, dan[1], dan[2])
canvas.bind("<Button-2>", lambda evt: RClick(evt, size, pole))
canvas.bind("<Button-1>", lambda evt: LClick(evt, size, pole))
canvas.mainloop()



















print(m)

print(pole)
