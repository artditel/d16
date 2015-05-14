import tkinter
c = tkinter.Canvas(width = 1500, height = 1500)
c.pack()
p = 1
length = 10
size = 10
for x in range(0, 150, 1):
	for y in range(0, 100, 1):
		c.create_rectangle( length + x * size , length + y * size, length + x * size - size,length +  y * size - size, fill = "saddle brown")
def paint(i, j):
		c.create_rectangle(i + size/2, j + size/2, i - size/2, j - size/2, fill = 'white')
for i in board:
	if c[i] == 1:
		paint(ro_x, ro_y)

c.mainloop()
