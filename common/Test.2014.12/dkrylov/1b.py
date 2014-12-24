L = []
f_read = open("a.txt", 'r')
for line in f_read:
	L.append(int(line))
for i in range(10):
	if len(L)>0:
		print(max(L))
		L.remove(max(L))