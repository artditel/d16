import math
import random

h= lambda x: (math.cos((math.pi)*(2**20)*x))**2

def trapezoidal_integral(a, b, f, n):
	dx=(b-a)/n
	es=0
	for i in range(n):
		l=(f((i+1)*dx+a)-f(i*dx+a))/2.+f(i*dx+a)
		s=dx*l
		es=es+s
	return es

def MonteCarlo(a, b, f, n):
	c=0; l=0
	for i in range(n):
		u=random.uniform(a, b)
		v=random.uniform(0, 1)
		if f(u)>=v:
			c =c+1
	s=1*1
	return (c/n*s)-(l/n*s)
for i in range (21):
	print(MonteCarlo(0, 1, h, 2**i))
for i in range (21):
	print(trapezoidal_integral(0, 1, h, 2**i))
