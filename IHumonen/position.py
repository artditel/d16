sum = 0
k = 0
wins1 = 0
wins2 = 0
draws = 0
with open ('position_scores.txt') as f:
	for line in f:
		cols = line.rstrip().split('\t')
		print(cols[1], '\t', cols[2])
		sum += int(cols[1])
		k += 1
		if cols[2] == '0-1':
			wins2 += 1
		else:
			if cols[2] == '1-0':
				wins1 += 1
			else:
				draws += 1
print('wins1 =', wins1, 'wins2 =', wins2, 'draws =', draws) 
print(sum/k)
def decision_stump(array):
	array0=[]
	array1=[]
	stump_left=0
	stump_right=0
	errors_left=0
	errors_right=0
	for i in range (len(array)):
		array0.append(array[i][0])
		array1.append(array[i][1])
	d = dict(zip(array0, array1))
	print(d)
	array0.sort()
	print(array0)
# 1 right
	for i in range (len(array0)):
		errors = 0
		for k in range(len(array0)):
			if d[array0[k]] == 1 and k <= i:
				errors+=1
			if d[array0[k]] == 0 and k > i:
				errors+=1
		if i == 0:
			errors_right = errors 
		else: 
			if errors <= errors_right:
				errors_right = errors
				stump_right = array0[i]
# 1 left
	for i in range (len(array0)):
		errors = 0
		for k in range(len(array0)):
			if d[array0[k]] == 0 and k < i:
				errors+=1
			if d[array0[k]] == 1 and k >= i:
				errors+=1
		if i == 0:
			errors_left = errors 
		else:	
			if errors <= errors_left:
				errors_left = errors
				stump_left = array0[i]
	if errors_left > errors_right:
		a = [stump_right, '1 right']
		return a 
	if errors_left <= errors_right:
		a = [stump_left, '1 left']
		return a
array=[(34, 1), (67, 0), (56, 1), (123, 0), (62, 1)] 
print (decision_stump(array))
qwertyuiop = input()


