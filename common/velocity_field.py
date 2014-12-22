import tkinter
import math
import random

FPS = 24 #frames per second, i.e. how many step do you have in one second
STEPS_PER_SECOND = 500 #how many steps do you have in one second
WIDTH = 500
HEIGHT = 500
RADIUS = 20
PARTS = 20
SCALE = 0.1

class Vector:
    #https://github.com/artditel/d16/blob/master/tbaikabulov/Vector3.py
    def __init__(self,x,y):
            self.x=x
            self.y=y
    def __add__(self,other):
        return Vector(self.x+other.x,self.y+other.y)
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    def __mul__(self,k):
        return Vector(self.x*k,self.y*k)
    def proj(self,a):
        cos=abs(math.cos(a))
        sin=abs(math.sin(a))
        return Vector( (self.x*cos-self.y*sin)*cos,(self.x*cos-self.y*sin)*sin)
    def __abs__(self):
        return (self.x**2+self.y**2)**0.5
    def __pow__(self,k):
        return Vector(self.x**k,self.y**k)
    def __str__(self):
        return "x:%f, y:%f" % (self.x, self.y)

class State:
    def __init__(self, velocity_function):
        self.start_random()
        self.velocity_function = velocity_function

    def start_random(self):
        self.pos = Vector(random.uniform(-1, 1), random.uniform(-1, 1))  #-1

    def make_step(self, time_interval):
        self.pos += self.velocity_function(self.pos) * time_interval
        if abs(self.pos.x) > 1 or abs(self.pos.y) > 1:
            #ball outside the field
            self.start_random()

class Drawer:
    def __init__(self, canvas, width=WIDTH, height=HEIGHT):
        self.canvas = canvas
        self.width = width
        self.height = height
        self.parts = PARTS
        self.objects_to_delete = []

    def draw_arc(self, from_xy, to_xy):
        diff = to_xy - from_xy
        perpendicular = Vector(-diff.y, diff.x)
        self.draw_line(from_xy, to_xy)
        self.draw_line(to_xy, from_xy + diff*0.75 + perpendicular*0.25)
        self.draw_line(to_xy, from_xy + diff*0.75 - perpendicular*0.25)

    def draw_line(self, vec1, vec2):
        self.canvas.create_line(vec1.x, vec1.y, vec2.x, vec2.y, fill="green")

    def change_coordinates(self, normed_vec):
        center = Vector(self.width/2, self.height/2)
        return center + Vector(self.width * normed_vec.x / 2, self.height * normed_vec.y / 2)

    def draw_arcs(self, velocity_function):
        for i in range(1, self.parts):
            for j in range(1, self.parts):
                start = Vector(-1 + 2 * i / self.parts, -1 + 2 * j / self.parts)
                end = start + velocity_function(start) * SCALE
                self.draw_arc(self.change_coordinates(start), self.change_coordinates(end))


    def draw_snowflake(self, normed_vec):
        def draw_snowflake_part(ids, start, angle, length, recursion_depth):
            diff = Vector(length*math.cos(angle), length*math.sin(angle))
            end = start + diff
            ids.append(self.canvas.create_line(start.x, start.y, end.x, end.y))
            if recursion_depth > 0:
                for i in (-1, 1):
                    new_angle = angle + math.pi * i / 3
                    draw_snowflake_part(ids, start + diff * 0.5, new_angle, length * 0.4, recursion_depth - 1)
                    draw_snowflake_part(ids, start + diff * 0.75, new_angle, length * 0.2, recursion_depth - 1)

        start = self.change_coordinates(normed_vec)
        ids = []
        for i in range(6):
            angle = math.pi * i / 3
            draw_snowflake_part(ids, start, angle, RADIUS, 2)
        return ids

    def redraw(self, state):
        canvas.delete(*self.objects_to_delete)
        self.objects_to_delete = []

        circ_id = self.draw_snowflake(state.pos)
        self.objects_to_delete += circ_id



class Game:
    def __init__(self, canvas):
        def velocity_function(vec):
            f_x = -math.sin(3 * vec.y)
            f_y = math.cos(3 * vec.x)
            return Vector(f_x, f_y)
        self.canvas = canvas
        self.state = State(velocity_function)
        self.drawer = Drawer(canvas)
        self.drawer.draw_arcs(velocity_function)

    def loop(self):
        self.state.make_step(1 / (STEPS_PER_SECOND /  FPS))
        self.drawer.redraw(self.state)
        self.canvas.after(1000 // FPS, self.loop)


canvas = tkinter.Canvas(width=WIDTH, height=HEIGHT)
canvas.pack()
game = Game(canvas)
game.loop()
canvas.mainloop()
