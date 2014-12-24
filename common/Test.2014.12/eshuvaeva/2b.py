class Ratio:
	def __init__(self,A,B):
		self.A = A
		self.B = B
		self.N=str(A)+'/'+str(B)
	def __str__(self):
		return (str(self.N))
	def __add__(self,other):
		return str(Ratio(int(self.A)*int(other.B) + int(self.B)*int(other.A),int(other.B)*int(self.B)))
print(Ratio(1,2) + Ratio(1,3))