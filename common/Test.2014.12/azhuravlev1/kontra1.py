f= open("kontra1.txt","r")
a=[]
for l in f:
	a.append(int(l))
k=0
n=k
m=a[n]
while k<len(a):
	if a[k]>m:
		n=k
	k=k+1
print(a[n])
