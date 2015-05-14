import tkinter
import math
W=1000
H=1000
STRETCH=10

def draw_graph(function):
	def Coord(x,y):
		return (x+W/2, H/2 - y)
	def Cit(x,y):
		return Coord(STRETCH*x, STRETCH*y)
	# def function(x):
	# 	return x**2
	c = tkinter.Canvas(width=W,height=H)
	c.pack()
	c.create_line(0, W/2, H, W/2)
	c.create_line(H/2, 0, H/2, W)

	for x in range(-500,500):
		c.create_line(Cit(x/10, function(x/10)), Cit((x+1)/10, function((x+1)/10)))
	c.mainloop()

draw_graph(lambda x: 10*math.cos(x) -30* math.sin(x))
draw_graph(function)
