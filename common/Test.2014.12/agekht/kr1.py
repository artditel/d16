f.open("a.txt", "r")
A = []
for i in f:
	A.append(int(i))

x = 0
y = x
z = A[y]

while x < len[A]:
	if A[x] > z:
		y = x
	x += 1

print (A[y])
