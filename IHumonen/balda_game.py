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
		letters[10 + j] = first_word[j]
	redraw(field)
	but.destroy()
	lab.destroy()
	lab_1 = Label(fra1, text=" Введите букву в строку, затем двойным кликом левой мышью выберите клетку для неё. \n  Выделите своё слово(клик левой клавишей мыши - начало и конец выделения) ", font="Arial 12")
	lab_1.pack()
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


def start_or_end_marking(event):
	x = event.x
	y = event.y
	x = x // size * size
	y = y // size * size
	number = x // size + y // size * cells
	if mode[0] == 'mark':		
		mode[0] = 'none'
#		if current_word in dictionary:
		redraw(field)
	else:
		if letters[number] != ' ':
			mode[0] = 'mark'

def making_mark(x, y, colour):
	x_1 = x + size
	y_1 = y + size
	field.create_line(x, y, x_1, y, fill = colour)
	field.create_line(x, y, x, y_1, fill = colour)
	field.create_line(x_1, y, x_1, y_1, fill = colour)
	field.create_line(x, y_1, x_1, y_1, fill = colour)
def put_letter(event):
	x = event.x
	y = event.y
	x = x // size * size
	y = y // size * size
	number = x // size + y // size * cells
	current_letter[0] = ent.get()
	surroundings = True
	if 0 < number < 4:
		if letters[number + 1] == ' ' and letters[number - 1] == ' ' and letters[number + cells] == ' ':
			surroundings = False
	if 20 < number < 24:
		if letters[number + 1] == ' ' and letters[number - 1] == ' ' and letters[number - cells] == ' ':
			surroundings = False
	if 0 == number:
		if letters[number + 1] == ' ' and letters[number + cells] == ' ':
			surroundings = False
	if 4 == number:
		if letters[number - 1] == ' ' and letters[number + cells] == ' ':
			surroundings = False
	if 20 == number:
		if letters[number + 1] == ' ' and letters[number - cells] == ' ':
			surroundings = False
	if 24 == number:
		if letters[number - 1] == ' ' and letters[number - cells] == ' ':
			surroundings = False	
	if current_letter[0].isalpha() and len(current_letter[0]) == 1 and surroundings:
		letters[number] = current_letter[0]
		redraw(field)
		making_mark(x, y, 'green')
		ent.delete(0, END)



root = Tk()
root_2 = Tk()

tex = Text(root_2,width=20,
		font="Verdana 12",
		wrap=WORD)
#scr = Scrollbar(root_2,command=tex.yview)
#scr.pack() 
tex.pack()

ent = Entry(root, width=20, bd=5, fg = 'blue')

side=250
size = 50
cells = side // size
letters = [ ' ' for x in range (25)]
mode = ['none']
current_letter = [' ']


field = tkinter.Canvas(width=side, height=side, bg = 'white')
field.pack()

redraw(field)




field.bind('<Double-Button-1>', put_letter )
field.bind('<Motion>', mark)
field.bind('<Button-1>', start_or_end_marking)





























fra1 = Frame(root, width=500, height=200, bg="white", bd = 20)
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
root_2.mainloop()