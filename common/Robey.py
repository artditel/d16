import tkinter
SIZE = int(input())
c = tkinter.Canvas(width = SIZE * 50, height = SIZE * 50)
c.pack()
p = 1
length = 50
size = 50
for x in range(0, SIZE, 1):
	for y in range(0, SIZE, 1):
		c.create_rectangle( length + x * size , length + y * size, length + x * size - size, length +  y * size - size, fill = "saddle brown")


a = [0] * SIZE
board = [a[:] for i in range(SIZE)]

ro_x = int(input())
ro_y = SIZE - int(input())
countey = 0



def reader(file):
	f_read = open(file, 'r')
	reader = []
	global countey
	for line in f_read.readlines():
		line = line.strip()
		reader.append(line)
		countey += 1
	f_read.close()
	return(reader)

rade = reader("commands.txt")

#the following uses global ro_x and ro_y coordinates and the board list of 0 and 1, where a 1 cell is painted and 0 is not;
#it returns new ro_x and ro_y coordinates and changes the colour of a cell if needed

def inpey(k):
	global ro_x
	global ro_y
	global SIZE
	global board
	x = ro_x
	y = ro_y
	commey = rade[k-1]

	if commey == "left":
		if x:
			x = x - 1
		else:
			x = SIZE - 1

	if commey == "right":
		if SIZE - x - 1:
			x = x + 1
		else:
			x = 0

	if commey == "up":
		if y:
			y = y - 1
		else:
			y = SIZE - 1

	if commey == "down":
		if SIZE - y - 1:
			y = y + 1
		else:
			y = 0

	if commey == "paint":
		board[x][y] = 1 - board[x][y]

	return(x , y)


#for i in range(countey):
#	ro_x , ro_y = inpey(i+1)


def paint(x, y):
		c.create_rectangle(length + x * size , length + y * size, length + x * size - size, length +  y * size - size, fill = "black")

for k in range(countey):
	ro_x , ro_y = inpey(k+1)
	for i in range(SIZE):
		for j in range(SIZE):
			c.create_rectangle(length + i * size , length + j * size, length + i * size - size, length +  j * size - size, fill = "saddle brown")
			if board[i][j]:
				paint(i , j)
	c.create_oval(length + ro_x * size , length + ro_y * size, length + ro_x * size - size, length +  ro_y * size - size, fill = "white")
	print(board)


c.mainloop()
