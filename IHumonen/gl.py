a, b = map(int, input().split())
graph=[]
graphm=[]
v=[]
lengths=[]
for i in range (b):
	x=input().split()
	x1=[int(x[0]), int(x[1])]
	graph.append(x1)
for i in range(a):
	y=[]
	v.append(y)
	graphm.append(y)
	for k in range (a):
		w=[]
		graphm[i].append(w)
		x=[i, k]
		if x in graph:
			graphm[i][k].append(1)
		else:
			graphm[i][k].append(0)
def poisk(i):
	global length
	if v[i]==1:
		length=(-1)
		return
	for k in range(a):
		if graphm[i][k]==1:
			length+=1
			v[i].append(1)
			poisk(k)
for i in range(a):
	length=0
	poisk(i)
	if length != (-1):
		lengths.append(length)
print(lengths)
print(len(lengths))