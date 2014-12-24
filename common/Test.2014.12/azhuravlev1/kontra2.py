class Ratio:
	def __init__(self,k,s):
		felf.x1=k;self.x2=s
	def __add__(self,other):
		n=self.x2*other.x2
		m=self.x1*other.x2+self.x2*self.x1
		return(ratio(m,n))
