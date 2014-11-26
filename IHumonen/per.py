class Permutation:
	def __init__(self, array):
		self.array=array
	def __str__(self):
		s=' '.join(str(i) for i in self.array)
		a=' '.join(str(i) for i in range(1, len(self.array)+1))
		sa='(' + a + ')' + '\n' + '(' + s + ')'
		return sa
	def __mul__(self, other):
		x=[0 for i in range(len(self.array))]
		for i in range(len(self.array)):
			x[i]=self.array[other.array[i]-1]
		c=Permutation(x)			
		return c
	def invert (self):
		x=[0 for i in range(len(self.array))]
		for i in range(len(self.array)):
			x[self.array[i]-1]=i+1
		c=Permutation(x)
		return c
	def __eq__ (self, other):
		return self.array == other.array
	def __ne__ (self, other):
		return self.array != other.array
	def parity(self):
		sum=0
		for i in range (len(self.array)):
			for k in range (i, len(self.array)):
				if self.array[i] > self.array[k]:
					sum+=1
		return sum%2==0
a=Permutation([4, 5, 1, 3, 2])
b=Permutation([2, 3, 4, 5, 1])
def test_mul(a,b):
	c=a*b
	print(c)
def test_a(a, b):
	c=a.invert()
	print(c)
def test_c(a, b):
	if a==b:
		print ('a=b')
	else:
		print('vahahah')
def  test_b(a):
	if a.parity():
		print('yes')
	else:
		print('no')
test_mul(a, b)
test_a(a, b)
test_b(a)
test_c(a, b)