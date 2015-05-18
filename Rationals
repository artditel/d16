class Rationals():
    def __init__(self, m, n):
        self.m = m
        self.n = n

    def add(self, arg):
        x = self.m*arg.n + self.n*arg.m
        y = self.n*arg.n
        return(x, y)

    def multiple(self, arg):
        x = self.m*arg.m
        y = self.n*arg.n
        return(x, y)

    def divide(self, arg):
        x = self.m*arg.n
        y = self.n*arg.m
        return(x, y)

#-------------

x = 1
a = 0
while x < 1000:
    a += 1/(x*(x+1))
    x += 1

print (a)
