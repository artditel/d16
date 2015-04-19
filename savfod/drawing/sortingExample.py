#how to write sort
def sorted_by_x(points):
    return sorted(points)

def get_y(p):
    return p[1]

def sorted_by_y(points):
    return sorted(points, key=get_y)

def sorted_by_x_big_first(points):
    return sorted(points, reverse=True)


#visualizing
import tkinter
import time

MAX_LEN = 5
WIDTH = 5

BEFORE_DRAWING = 0
DRAWING_X_SORTED = 1
DRAWING_Y_SORTED = 2
DRAWING_X_REVERSE_SORTED = 3
status = BEFORE_DRAWING

points = []
drawn_points = 0

sleep_time = 1

def visualize_points():
    print ("Called")
    global drawn_points
    global points
    global canvas
    if drawn_points == 0:
        canvas.delete(*canvas.find_all())

    if drawn_points != MAX_LEN:
        x, y = points[drawn_points]
        canvas.create_oval(x - WIDTH, y - WIDTH, x + WIDTH, y + WIDTH, fill = "black")
        drawn_points += 1
        time.sleep(0.3)
        canvas.after(1, visualize_points)

    else:
        drawn_points = 0
        time.sleep(0.3)
        canvas.after(1, visualize_sorting)

def visualize_sorting():
    global status
    status += 1
    global points
    if status == DRAWING_X_SORTED:
        points = sorted_by_x(points)
    elif status == DRAWING_Y_SORTED:
        points = sorted_by_y(points)
    elif status == DRAWING_X_REVERSE_SORTED:
        points = sorted_by_x_big_first(points)
    elif status > DRAWING_X_REVERSE_SORTED:
        status = BEFORE_DRAWING
        canvas.delete(*canvas.find_all())
        points = []
        return

    visualize_points()

def onMouseClick(event):
    x, y = event.x, event.y
    points.append((x,y))
    event.widget.create_oval(x - WIDTH, y - WIDTH, x + WIDTH, y + WIDTH, fill = "black")
    if len(points) >= MAX_LEN:
        visualize_sorting()

canvas = tkinter.Canvas()
canvas.pack()
canvas.bind("<Button-1>", onMouseClick)
canvas.mainloop()





