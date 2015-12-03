import math
import random

def func(x):
	a = math.cos(math.pi * 2**20  * x)
	return x*a*a


def otrez(a,b):
	c= 0
	for i in range(n):
		n_x = random.uniform(a,b)
		n_y = random.uniform(0,1)
		if func(n_x) >= n_y:
			c+=1
	return c
for i in range(21):
	n = 2**i

	print(otrez(0,1)*1/n)
