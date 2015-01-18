A = True
while A == True:
	try:
		r = input()
		list = open(r, "r")
		A = False
	except:
		print("Enter filename again")
end = []
for line in list:
	line = line.strip()
	line = int(line)
	end.append(line)

b = len(end)
end = sorted(end)
try:
	print(end[b - 1], end[b - 2],  end[b - 3], end[b - 4], end[b - 5], end[b - 6], end[b - 7], end[b - 8], end[b - 9], end[b - 10])
except: 
	print("Takih elementov ne sushestvuet")
