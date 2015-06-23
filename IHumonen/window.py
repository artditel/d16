import random
from tkinter import *
import tkinter
def OK_event(event):
	OK(root)
def OK(root):
	x = random.randrange(800)
	y = random.randrange(600)
	space = '+' + str(x) + '+' + str(y)
	root.geometry(space)
	

	
root = Tk()
root.protocol('WM_DELETE_WINDOW', OK_event('WM_DELETE_WINDOW'))
c = tkinter.Canvas(root, width = 200, height  = 200, bg = 'white')
c.create_text(100, 100, text = 'Дурында', font = 'Arial 12')
root.bind('<Motion>', OK_event)
c.pack()
c.mainloop()
root.mainloop()
