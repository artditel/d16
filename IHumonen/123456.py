# 1=стена, 2=энергия, 3=жизнь, 4=враг, 5=герой, 0=пустo
def rectangle(x, y, colour, c):
	c.create_rectangle(x*CELL_SIZE, y*CELL_SIZE, x*CELL_SIZE+CELL_SIZE, y*CELL_SIZE+CELL_SIZE, fill = colour)
def do_field(field, side, c):
	for i in range(side):
		for k in range(side):
			if field[i][k]==1:
				rectangle(i, k, black, c)
			if field[i][k]==2:
				rectangle(i, k, yellow, c)
			if field[i][k]==3:
				rectangle(i, k, green, c)
			if field[i][k]==4:
				rectangle(i, k, red, c)
			if field[i][k]==5:
				rectangle(i, k, pink, c)
			if field[i][k]==0:
				rectangle(i, k, white, c)
class gnome_hero:
	def __init__(self):
		self.strenght=100
		self.life=3
		self.x=SIDE//2
		self.y=self.x
	def energy(self):
		self.strenght+=10
	def hp(self):
		if self.life < 5:
			self.life+=1
	def move_up(self):
		new=self.y+1
		if field[self.x][new]==2:
			Thorin_Eikinskjaldi.energy()
		if field[self.x][new]==3:
			Thorin_Eikinskjaldi.life()
		if field[self.x][new]!=1:
			field[self.x][self.y]=0
			self.y=new
			field[self.x][self.y]=5
	def move_down(self):
		new=self.y-1
		if field[self.x][new]==2:
			Thorin_Eikinskjaldi.energy()
		if field[self.x][new]==3:
			Thorin_Eikinskjaldi.life()		
		if field[self.x][new]!=1:
			field[self.x][self.y]=0
			self.y=new
			field[self.x][self.y]=5
	def move_right(self):
		new=self.x+1
		if field[new][self.y]==2:
			Thorin_Eikinskjaldi.energy()
		if field[new][self.y]==3:
			Thorin_Eikinskjaldi.life()
		if field[new][self.y]!=1:
			field[self.x][self.y]=0
			self.x=new
			field[self.x][self.y]=5
	def move_left(self):
		new=self.x-1
		if field[new][self.y]==2:
			Thorin_Eikinskjaldi.energy()
		if field[new][self.y]==3:
			Thorin_Eikinskjaldi.life()
		if field[new][self.y]!=1:
			field[self.x][self.y]=0
			self.x=new
			field[self.x][self.y]=5
def up(event):
	c=event.widget
	Thorin_Eikinskjaldi.up()
	do_field(field, SIDE, c)
def down(event):
	c=event.widget
	Thorin_Eikinskjaldi.down()
	do_field(field, SIDE, c)
def left(event):
	c=event.widget
	Thorin_Eikinskjaldi.left()
	do_field(field, SIDE, c)
def right(event):
	c=event.widget
	Thorin_Eikinskjaldi.right()
	do_field(field, SIDE, c)
white='white'
pink='pink'
black='black'
green='green'
red='red'
yellow='yellow'
import tkinter 
SIDE=500
field=[]
CELL_SIZE=10
c = tkinter.Canvas(width=SIDE, height=SIDE)
c.pack()
Thorin_Eikinskjaldi=gnome_hero()
for i in range (SIDE):
	empty=[]
	field.append(empty)
	for k in range (SIDE):
		empty1=[0]
		wall=[1]
		if i==0 or i==(SIDE-1) or k==0 or k==(SIDE-1):
			field[i].append(wall)
		else:
			field[i].append(empty1)
do_field(field, SIDE, c)
c.bind('<Up>', up)
c.bind('<Down>', down)
c.bind('<Left>', left)
c.bind('<Right>', right)
c.mainloop()