L = []
f_read = open("a.txt", 'r')
for line in f_read:
	L.append(int(line))
print(max(L))