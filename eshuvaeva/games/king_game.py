n = int(input())
m = int(input())
a = []
for i in range(m):
	a.append([])
	for t in range(n):
		a[i].append(0)
a[m-1][0]==2
for i in range(m):
	for g in range(n):
		if (g>3 and a[i][g-3]==2) or (g>3 and a[i-1][g-3]==2) or (g>2 and a[i-2][g-2]==2) or (g>2 and a[i-1][g-1]==2) or a[i-1][g]==2:
			a[i][g] = 1
		else:
			a[i][g] = 2
for i in reversed(a):
    print(i) 
