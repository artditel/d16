import time
import math
def n(v,k):
	sum=0
	i=0
	while int(v/k**i)>0:
		sum+=int(v/k**i)
		i+=1
	return sum
def v(s):
	N=int(s[0])
	k=int(s[1])
	begin=0
	end=N+1
	while end-begin>2:
		middle=(end+begin)//2
		if n(middle,k)>=N:
			end=middle+1
		else:
			begin=middle
	return(begin+1)




class obert:
	calls_count=0
	errors=0
	time=0
	def __call__(self,a):
		self.calls_count+=1
		t=time.clock()
		try:
		     b=self.functions[self.f](a)
		     print(1)
		     self.time=time.clock()-t
		     return b
		except:
		     self.errors+=1
		     return 0
	def change(self):
		self.f+=1
	def __init__(self,functions):
		self.functions=functions
		self.f=0
	def print_stat(self):
		print ('% of errors is ' +str(self.errors/self.calls_count))
	def get_time(self):
		return  self.time
for i in range(7,100):
	f = obert([v])
	f((10**i,3))
	print(f.get_time()*100/math.log(10**i))
