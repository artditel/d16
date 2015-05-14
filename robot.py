import tkinter
c = tkinter.Canvas(width = 1500, height = 1500)
c.pack()
p = 1
length = 10
size = 10
for x in range(0, 150, 1):
	for y in range(0, 100, 1):
		c.create_rectangle( length + x * size , length + y * size, length + x * size - size,length +  y * size - size, fill = "saddle brown")

c.mainloop()
