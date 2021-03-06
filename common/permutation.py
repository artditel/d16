class Permutation:
	def __init__(self,A):
		self.A=A
	def f(self,n):
		return self.A[n-1]
	def __str__(self):
		return (str(self.A))
	def __len__(self):
		return len(self.A)
	def __mul__(X,Y):
		A=[]
		for i in range(1,len(X)+1):
			A.append(X.f(Y.f(i)))
		return Permutation(A)
	def __pow__(X,n):
		if n==1:
			return X
		if n%2==0:
			return (X*X)**(n//2)
		else:
			return X**(n-1)*X
	def __eq__(self, other):
		if self.A == other.A:
			return True
		else:
			return False
	def __ne__(self, other):
		if __eq__(self, other) == True:
			return False
		else:
			return True
