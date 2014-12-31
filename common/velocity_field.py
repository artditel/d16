import tkinter
import math
import random

FPS = 50 #frames per second, i.e. how many step do you have in one second
STEPS_PER_SECOND = 1000 #how many steps do you have in one second
WIDTH = 1000
HEIGHT = 600
RADIUS = 10
PARTS = 50
SCALE = 0.1
SNOWFLAKES_COUNT = 30

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
            # self.start_random()
            self.pos.x = (self.pos.x + 1) % 2 - 1
            self.pos.y = (self.pos.y + 1) % 2 - 1

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
        self.canvas.create_line(vec1.x, vec1.y, vec2.x, vec2.y, fill="grey")

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
            ids.append(self.canvas.create_line(start.x, start.y, end.x, end.y, fill="red"))
            if recursion_depth > 0:
                for i in (-1, 1):
                    new_angle = angle + math.pi * i / 3
                    draw_snowflake_part(ids, start + diff * 0.5, new_angle, length * 0.4, recursion_depth - 1)
                    draw_snowflake_part(ids, start + diff * 0.75, new_angle, length * 0.2, recursion_depth - 1)

        start = self.change_coordinates(normed_vec)
        ids = []
        for i in range(6):
            angle = math.pi * i / 3
            draw_snowflake_part(ids, start, angle, RADIUS, 1)
        return ids

    def draw(self, state):
        circ_id = self.draw_snowflake(state.pos)
        self.objects_to_delete += circ_id

    def rm_old(self):
        self.canvas.delete(*self.objects_to_delete)
        self.objects_to_delete = []

    def rm_all(self):
        self.canvas.delete(*self.canvas.find_all())

class RandomFunction:
    def __init__(self):
        self.reinit()

    def reinit(self):
        self.coefs = [random.uniform(-1, 1) for i in range(10)]

    def __call__(self, x, y):
        f_x = self.coefs[0] * x + self.coefs[2] * y + self.coefs[4] + self.coefs[6]*x*y
        f_y = self.coefs[1] * x + self.coefs[3] * y + self.coefs[5] + self.coefs[7]*x*y
        return f_x, f_y

class FixedFunctions:
    def __init__(self):
        self.index = 0

        def f1(x,y):
            return -math.sin(3 * y), math.cos(3 * x)
        def f2(x,y):
            def f(x):
                return 3*(x**3 - 0.5*x)
            return f(y), f(x)
        def f3(x,y):
            def f(x):
                return 3*(x**3 - 0.5*x)
            return -f(y), f(x)

        f4 = lambda x,y: (y, x)
        f5 = lambda x,y: (-y, x)

        self.functions = [f1, f2, f3, f4, f5]

    def __call__(self, x, y):
        return self.functions[self.index % len(self.functions)](x,y)

    def reinit(self):
        self.index += 1

class FunctionFactory:
    def __init__(self):
        self.functions = [RandomFunction(), FixedFunctions()]
        self.func_ind = 0

    def get_function(self):
        return self.functions[self.func_ind % len(self.functions)]

    def change_function_class(self):
        self.func_ind += 1

    def change_function_type(self):
        self.get_function().reinit()

class Game:
    def __init__(self, canvas):
        self.function_factory = FunctionFactory()
        self.init(canvas)

        def change_function_class(event):
            self.function_factory.change_function_class()
            self.on_function_change(event.widget)

        def change_function_type(event):
            self.function_factory.change_function_type()
            self.on_function_change(event.widget)

        def key_press(event):
            global SNOWFLAKES_COUNT
            if event.keysym == "plus":
                SNOWFLAKES_COUNT += 1
            if event.keysym == "minus":
                SNOWFLAKES_COUNT -= 1
            print ("Set %d snowflakes count" % SNOWFLAKES_COUNT)
            self.on_function_change(event.widget)

        canvas.focus_set()
        canvas.bind("<Key>", key_press)
        canvas.bind("<Button-1>", change_function_type)
        canvas.bind("<Button-3>", change_function_class)

    def init(self, canvas):
        velocity_function = self.get_function()
        self.canvas = canvas
        self.states = [State(velocity_function) for x in range(SNOWFLAKES_COUNT)]
        self.drawer = Drawer(canvas)
        self.drawer.draw_arcs(velocity_function)

    def get_function(self):
        func = self.function_factory.get_function()
        def to_vec(pair):
            return Vector(pair[0], pair[1])
        return lambda vec: to_vec(func(math.sin(math.pi * vec.x), math.sin(math.pi * vec.y)))

    def on_function_change(self, canvas):
        self.drawer.rm_all()
        self.init(canvas)

    def loop(self):
        self.drawer.rm_old()
        for state in self.states:
            for i in range(int(STEPS_PER_SECOND / FPS)):
                state.make_step(1 / (STEPS_PER_SECOND))
            self.drawer.draw(state)
        self.canvas.after(1000 // FPS, self.loop)


canvas = tkinter.Canvas(width=WIDTH, height=HEIGHT)
canvas.pack()
game = Game(canvas)
game.loop()
canvas.mainloop()
