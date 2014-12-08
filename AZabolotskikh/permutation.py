import itertools
from collections import Counter
class Premutation:
	@classmethod
	def all_permutations_of_length(clazz, n):
		a = [i for i in range(n)]
		for i in itertools.permutations(a):
			yield clazz(i)
	def __init__(self, _):
		if len(set(_)) != len(_):
			raise Exception("not reversible")
		self._ = _
	def __len__(self):
		return len(self._)
	def __eq__(self, _):
		return self._ == _._
	def __str__(self):
		return str(self._)
	def __mul__(self, other):
		if len(self._) != len(other._):
			raise Exception("Different arity")
		_ = [0] * len(self._)
		for i in range(len(self._)):
			_[i] = self._[other._[i] - 1]
		return Premutation(_)
	def printAsSubst(self):
		print ([i+1 for i in range(len(self._))])
		print (self)
	def __neg__(self):
		f = [0] * len(self._)
		for i in range(len(self._)):
			f[self._[i] -1]=i+1
		return Premutation(f)
	def __ne__(self,other):
		return not (self == other)
	def __pow__(self, i):
		if i == 1:
			return self
		if i%2==0:
			return (self*self)**(i/2)
		else:
			return self*((self*self)**((i-1)/2))
	def decompose(self):#TBD
		pass
	def _copy(self):
		return Premutation(self._)
	def decompose_transposition(self):
		cycles = []
		this = self._copy()
		for i in range(len(self)):
			if this._[i] == -1:
				continue;
			else:
				if this._[i] - 1 < i:
					break;
				cycles += [[i+1, this._[i]]]
				this._[i] , this._[this._[i]-1] = this._[this._[i]-1] , this._[i]
		return cycles
	def parity(self):
		a = 0
		for j in range(len(self._)):
			for i in range(j):
				if self._[i] > self._[j]:
					a += 1
		return a%2==0
	def commutes(self, other):
		return self*other == other*self
	def some_relationship(self, b):
		return (-b)*self*b
	def has_relationship(self, b):
		a = map(len, self.decompose())
		b = map(len, self.decompose())
		return Counter(a) == Counter(b)

		

def main():
	a1 = Premutation([4,5,1,3,2])
	a2 = Premutation([2,3,4,5,1])
	print(a1*a2)
	print(a2*a1)
	for i in range(10):
		print (a1**(i+1))
		print (a2**(i+1))
	print ("inverse")
	print (-a1, -a2)
	print ("parity")
	print (a1.parity(), a2.parity())
	print ("equality")
	print(a1==a2)
	print ("commutes")
	print(a1.commutes(a2))
	print("order")
		#print(a1.order(), a2.order())
	print ("pow 10kkk")
	print(a1 ** (10**10), a2 ** (10**10))
	print(a1.decompose_transposition(), a2.decompose_transposition())







main()