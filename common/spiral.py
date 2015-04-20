n=int(input())
k=int(input())
w=1366
h=768

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
	
def give_me_colour(self_seq):
	for j in self_seq:
		number = j[2]
		a = 0
	for i in range(number):
		if number//(i + 1) == number/(i + 1):                                
			a += 1
		if a > 2:
			j[2] = "Red"
		else:
			j[2] = "Green"
		return(self_seq)   
		
def test_give_me_colour():
	assert(give_me_colour([[1, 1, 24]]) == [[1, 1, "Red"]])
	assert(give_me_colour([[1, 1, 1], [1, 1, 3], [1, 1, 5], [1, 1, 15], [1, 1, 32]]) == ([[1, 1, "Green"], [1, 1, "Green"], [1, 1, "Green"], [1, 1, "Red"], [1, 1, "Red"]]))
	assert(give_me_colour([[1, 1, 86], [1, 1, 3], [1, 1, 23], [1, 1, 56], [1, 1, 465]]) == ([[1, 1, "Red"], [1, 1, "Green"], [1, 1, "Green"], [1, 1, "Red"], [1, 1, "Red"]]))
	assert(give_me_colour([[1, 1, 24], [1, 1, 58], [1, 1, 94], [1, 1, 20], [1, 1, 36]]) == ([[1, 1, "Red"], [1, 1, "Red"], [1, 1, "Red"], [1, 1, "Red"], [1, 1, "Red"]]))
	assert(give_me_colour([[1, 1, 7], [1, 1, 3], [1, 1, 37], [1, 1, 3], [1, 1, 82]]) == ([[1, 1, "Green"], [1, 1, "Green"], [1, 1, "Green"], [1, 1, "Green"], [1, 1, "Red"]]))
	assert(give_me_colour([[1, 1, 28], [1, 1, 94], [1, 1, 59], [1, 1, 3], [1, 1, 58]]) == ([[1, 1, "Red"], [1, 1, "Red"], [1, 1, "Green"], [1, 1, "Green"], [1, 1, "Red"]]))
	assert(give_me_colour([[1, 1, 48], [1, 1, 85], [1, 1, 6], [1, 1, 56], [1, 1, 97]]) == ([[1, 1, "Red"], [1, 1, "Red"], [1, 1, "Red"], [1, 1, "Red"], [1, 1, "Green"]]))           

def get_coordinate(width, height, k, i, j):
	size = width/k
	x1 = width/2 + i * size
	y1 = height/2 - (j + 1) * size
	x2 = x1 + size
	y2 = y1 + size

	return (x1, y1, x2, y2)
	
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

def cell_sequence(n , k):
	#By Me
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
	
def test_cells():
	if not cell_sequence(1 , 7)[3] == (0 , 1 , 4):
		return 1
	elif not cell_sequence(3 , 5)[5] == (1 , 0 , 8):
		return 2
	elif not cell_sequence(11 , 11)[9] == (-2 , -1 , 20):
		return 3
	else:
		return True

def draw_and_halt(width,height,k,ar):
	cell_num = 0
	for x in range(0, k * (width//k), (width//k)):
		for y in range(0, k * (height//k),(height//k)):
			cd = get_cordinate(width,height,k,x,y)
			c.create_rectangle( cd[0] , cd[1],cd[2],  cd[3], fill = ar[cell_num[2]])
			cell_num = cell_num+1
	
cs=cell_sequence(n,k)
ar=give_me_colour(cs)
draw(w,h,k,ar)

