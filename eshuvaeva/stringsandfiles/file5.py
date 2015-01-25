A = True
def func(a):
	j = a[::-1]
	return j
while A == True:
	try:
		file1 = str(input())
		file2 = str(input())
		k = []
		f_read = open(file1, 'r')
		f_read1 = open(file2, 'w')
		for line in f_read.readlines():
			line = line.strip()
			s = line.split()
			for j in s:
				f_read1.writelines(j)
				k.append(j)
		f_read.close()
		f_read1.close()
		A = False
		print("Ну, видишь, родной, ты тоже на что-то способен.")
	except:
		print("Ты больной, убогий, недееспособный лопух. Ещё попытка:")

k = sorted(k,key = func)
print(k)
