
class Rationals():
    def __init__(self, m, n):
        self.m = m
        self.n = n

    def __add__(self, arg):
        x = self.m*arg.n + self.n*arg.m
        y = self.n*arg.n
        z = Rationals(x, y)
        return(z)

    def __mul__(self, arg):
        x = self.m*arg.m
        y = self.n*arg.n
        z = Rationals(x, y)
        return(z)

    def __div__(self, arg):
        x = self.m*arg.n
        y = self.n*arg.m
        z = Rationals(x, y)
        return(z)

#    def __str__(self):


#-------------

x = 1
a = 0
while x < 1000:
    a += 1/(x*(x+1))
    x += 1

print (a)
z1 = Rationals(1,2)
z2 = Rationals(3,4)
z3 = Rationals(5,6)
print(z1+z2+z3)
