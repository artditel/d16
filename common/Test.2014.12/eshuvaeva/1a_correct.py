a = []
file1 = str(input())
f_read = open(file1, 'r')
for line in f_read.readlines():
	line = line.strip()
	a.append(int(line))
print(max(a))
	

	