import tkinter

is_drawing = False
previous_point = (0, 0)


def start_drawing(event):
    global is_drawing
    is_drawing = True
    global previous_point
    previous_point = event.x, event.y

def stop_drawing(event):
    global is_drawing
    is_drawing = False

def draw(event):
    if is_drawing:
        current_point = event.x, event.y
        global previous_point
        event.widget.create_line(previous_point[0], previous_point[1], current_point[0], current_point[1])
        previous_point = current_point


c = tkinter.Canvas()
c.pack()
c.bind("<Button-1>", start_drawing)
c.bind("<ButtonRelease-1>", stop_drawing)
c.bind("<Motion>", draw)

c.mainloop()

