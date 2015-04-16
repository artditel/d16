
def is_prime (n):
	k = n
	b = 2
	while k > b:
		if n % b == 0:
			return False
		else:
			k = n//b
		b = b + 1
	return True

def test_is_prime ():
	if is_prime (4) == True:
		return False
	if is_prime (13) == False:
		return False
	if is_prime (2) == False:
		return False
	if is_prime (216) == True:
		return False
	if is_prime (49) == True:
		return False
	if is_prime (11) == False:
		return False
	return True
	
def walk(x , y , SIZE):
	#insider programm, used by cells and not to be an element of the spiral.py
	if x + y > SIZE - 2:
		if y - x > -1:
			return x+1 , y
	if x + y > SIZE - 1:
		if y - x < 1:
			return x , y-1
	if x + y < SIZE:
		if y - x < 0:
			return x-1 , y
	if x + y < SIZE-1:
		if y - x > -1:
			return x , y+1

def cells(n , k):
	x = k//2
	y = k//2
	X = k//2
	Y = k//2
	cells = []
	ind = n
	while ind < k**2 + n:
		cells.append((X-x , Y-y , ind))
		ind += 1
		x , y = walk(x , y , k)
	return cells
