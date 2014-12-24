class Ratio:
	def __init__(self,A,B):
		self.N=str(A)+'/'+str(B)
	def __str__(self):
		return (str(self.N))
a = Ratio(1,2)
print(a)
