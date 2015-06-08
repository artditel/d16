from tkinter import *
import tkinter

def redraw(canvas):
	for i in range(0, side, size):
		for k in range(0, side, size):
			canvas.create_rectangle(i, k, i+size, k+size, outline = 'blue')
	for x in range(len(letters)):
		canvas.create_text(x%cells * size + size//2, x //cells * size + size//2, text = letters[x])

def starter(event):
	first_word = ent.get()
	for j in range(5):
		field.create_text(j*size+size//2, 2*size+size//2, text=first_word[j])
		letters[10 + j] = first_word[j]
	but.destroy()
	lab.destroy()
	ent.delete(0, END)

def mark(event):
	field = event.widget
	x = event.x
	y = event.y
	x = x // size * size
	y = y // size * size
	number = x // size + y // size * cells
	if mode[0] == 'mark' and letters[number] != ' ':
		making_mark(x, y, 'red')


def start_marking(event):
	x = event.x
	y = event.y
	x = x // size * size
	y = y // size * size
	number = x // size + y // size * cells
	if mode[0] == 'mark':		
		mode[0] = 'none'
		redraw(field)
		ent.delete(0, END)
	else:
		redraw(field)
		if letters[number] == ' ':
			letters[number] = ent.get()[0]
			redraw(field)
			making_mark(x, y, 'green')
			mode[0] = 'mark'

def making_mark(x, y, colour):
	x_1 = x + size
	y_1 = y + size
	field.create_line(x, y, x_1, y, fill = colour)
	field.create_line(x, y, x, y_1, fill = colour)
	field.create_line(x_1, y, x_1, y_1, fill = colour)
	field.create_line(x, y_1, x_1, y_1, fill = colour)
def put_letter(event):
	current_letter = ent.get()
	
	redraw(field)

root = Tk()

ent = Entry(root, width=20, bd=5, fg = 'blue')

side=250
size = 50
cells = side // size
letters = [ ' ' for x in range (25)]
mode = ['none']


field = tkinter.Canvas(width=side, height=side, bg = 'white')
field.pack()

redraw(field)

ent = Entry(root, width=20, bd=5, fg = 'blue')



field.bind('<Motion>', mark)
field.bind('<Button-1>', start_marking)





























fra1 = Frame(root, width=500, height=100, bg="white", bd = 20)
fra2 = Frame(root, width=300, height=200, bg="white", bd = 20)


but = Button(fra2)
but['text'] = 'Начать игру'
but['bg'] = 'blue'
but['fg'] = 'yellow'


but.bind("<Button-1>",starter)

lab = Label(fra1, text=" Введите первое слово (из пяти букв) ", font="Arial 18")


 




fra1.pack()
fra2.pack()

ent.pack()
but.pack()
lab.pack()
field.mainloop()
root.mainloop()