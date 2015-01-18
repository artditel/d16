def f():
	try:
		name = "file.txt"
		lenght = 6
		a=0
		with open(name, 'r') as f_read:
			for line in f_read:
				words = line.split()
			for word in words:
				x = len(word)
				if x == lenght:
					a = a + 1
		print(a)
	except:
		f()
		print("File not found. Try another name, please.")
f()
