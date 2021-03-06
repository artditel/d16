from PIL import Image
from PIL import ImageOps
from PIL import ImageTk
import tkinter
import math
import time


photo = input("Choose a photo:")



if photo != '':
	i = Image.open(photo)
	image = i.convert('L')
	invert_image = ImageOps.invert(image)
	invert_image = ImageOps.autocontrast(invert_image)
	final_image = invert_image.resize((28,28),Image.LANCZOS)
	#final_image = ImageOps.mirror(resized_image)
	final_image = ImageOps.autocontrast(final_image)
	final_image.show()
	photo_array = [list(final_image.getdata()), None]

#for x in range(len(train_data)):
# 	i = Image.frombytes('L', (28,28), bytes(train_data[x])) #kaggle data into an image
# 	i.show()
# from collections import namedtuple


#изменить функцию поиска замкнутых пространств, изменить distance, сделать окошко, 2 режима работы(демонстрация и распознавание)


im_width = 28
im_height = 28
 
data = []

K = 30



start = time.clock()

with open('train.csv') as train_file:
	for line in train_file:
		l = list(map(int,line.strip().split(',')))
		this_pic=[l[1:], l[0]]
		data.append(this_pic) 

print("train.csv parsed in", time.clock() - start)

start = time.clock()

"""
with open('test.csv') as test_file:
	for line in test_file:
		l = list(map(int,line.strip().split(',')))
		this_pic = [l,None]
		data.append(this_pic)
print("test.csv parsed in", time.clock() - start)
"""


def feature1(array):
	min_y=im_height
	max_y=0
	min_x=im_width
	max_x=0
	for x in range(len(array)):
		if array[x] >= 90:
			if x//im_height<=min_y:
				min_y=x//im_height
			if x//im_height	>=max_y:
				max_y=x//im_height
			if x%im_height<=min_x:
				min_x=x%im_height
			if x%im_height>=max_x:
				max_x=x%im_height
	k = (max_x-min_x)/(max_y-min_y)
	return(k)


def two_dimensional_array(array):
	a=[]
	for x in range(im_height):
		b=[]
		for y in range(im_width*x, im_width*(x + 1)):
			b.append(array[y])
		a.append(b)	
	return(a)


def quater1(array):
	k = 0
	for i in range(im_height // 2):
		for j in range(im_width // 2):
			if array[i][j] >=90:
				k += 1
	return(4 * k / (im_height * im_width))			


def quater2(array):
	k = 0
	for i in range(im_height // 2):
		for j in range(im_width // 2, im_width):
			if array[i][j] >= 90:
				k += 1
	return(4 * k / (im_height * im_width))


def quater3(array):
	k = 0
	for i in range(im_height // 2, im_height):
		for j in range(im_width // 2, im_width):
			if array[i][j] >= 90:
				k += 1
	return(4 * k / (im_height * im_width))


def quater4(array):
	k = 0
	for i in range(im_height // 2, im_height):
		for j in range(im_width // 2):
			if array[i][j] >= 90:
				k += 1
	return(4 * k / (im_height * im_width))


def corner(x,array):
	coordinate_x = x//im_width
	coordinate_y = x%im_height
	if coordinate_x > 0 and coordinate_x < im_width - 1 and coordinate_y > 0 and coordinate_y < im_height-1:
		if array[coordinate_y + 1][coordinate_x + 1] <= 90 and array[coordinate_y + 1][coordinate_x] <= 90 and array[coordinate_y][coordinate_x + 1] <= 90 and array[coordinate_y + 1][coordinate_x - 1] <= 90 and array[coordinate_y - 1][coordinate_x + 1] <= 90:
				return True
		if array[coordinate_y + 1][coordinate_x - 1] <= 90 and array[coordinate_y + 1][coordinate_x] <= 90 and array[coordinate_y][coordinate_x - 1] <= 90 and array[coordinate_y + 1][coordinate_x + 1] <= 90 and array[coordinate_y - 1][coordinate_x - 1] <= 90:
			return True
		if array[coordinate_y - 1][coordinate_x - 1] <= 90 and array[coordinate_y - 1][coordinate_x] <= 90 and array[coordinate_y - 1][coordinate_x + 1] <= 90 and array[coordinate_y][coordinate_x - 1] <= 90 and array[coordinate_y + 1][coordinate_x - 1] <= 90:
			return True
		if array[coordinate_y - 1][coordinate_x + 1] <= 90 and array[coordinate_y][coordinate_x + 1] <= 90 and  array[coordinate_y + 1][coordinate_x + 1] <= 90 and  array[coordinate_y - 1][coordinate_x] <= 90 and  array[coordinate_y - 1][coordinate_x - 1] <= 90:
			return True
		else:
			return False
	else:
		return False


#counting corners
def feature2(array):
	corners = 0
	for x in range(im_width*im_height - 1):
		if corner(x, array) == True:
			corners+=1
	return(corners)


#horizontal lines
def feature3(array):
	abrupt_changes = 0
	for x in range(im_height-1):
		crossing_horizontal_line = 0
		crossing_next_horizontal_line = 0
		for y in range(im_width):
			if array[x][y] >= 50:
				crossing_horizontal_line += 1
			if array[x+1][y] >= 50:
				crossing_next_horizontal_line += 1
		if abs(crossing_next_horizontal_line - crossing_horizontal_line) > 3:
			abrupt_changes += 1
	return(abrupt_changes)


#vertical lines
def feature4(array):
	abrupt_changes = 0
	for y in range(im_width-1):
		crossing_vertical_line = 0
		crossing_next_vertical_line = 0
		for x in range(im_height):
			if array[x][y] >= 50:
				crossing_vertical_line += 1
			if array[x][y+1] >= 50:
				crossing_next_vertical_line += 1
		if abs(crossing_next_vertical_line - crossing_vertical_line) > 3:
			abrupt_changes += 1
	return(abrupt_changes)


def feature5(array):
	max_y = 0
	min_y = im_height
	min_x = im_width
	max_x = 0
	for x in range(im_height):
		for y in range(im_width):
			if array[x][y] >= 90:
				if x > max_y:
					max_y = x
				if x < min_y:
					min_y = x
				if y > max_x:
					max_x = y
				if y < min_x:
					min_x = y
	average_x = (max_x + min_x)/2
	height_of_the_digit = max_y - min_y
	sum_of_x = 0
	for x in range(im_height):
		sum_of_x_in_line = 0
		number_of_pixels_in_line = 0
		if array[x][y] >= 90:
			sum_of_x_in_line += (y - average_x)
			number_of_pixels_in_line += 1
		if number_of_pixels_in_line != 0:	
			sum_of_x += sum_of_x_in_line/number_of_pixels_in_line
	k = sum_of_x/height_of_the_digit
	return k



def dfs(x,y,visited,array):
	visited.add((x,y))
	if x < im_height-1 and array[x + 1][y] <= 90 and (x + 1, y) not in visited:
		dfs(x + 1, y, visited, array)
	if x > 0 and array[x - 1][y] <= 90 and (x - 1, y) not in visited:
		dfs(x - 1, y, visited, array)
	if y > 0 and array[x][y - 1] <= 90 and (x, y - 1) not in visited:
		dfs(x, y - 1, visited, array)
	if y < im_width - 1 and array[x][y + 1] <= 90 and (x, y + 1) not in visited:
		dfs(x, y + 1, visited, array)




def number_of_closed_areas(array):
	visited_pixels=set()
	k = -1
	for x in range(im_height):
		for y in range(im_width):
			if array[x][y] <= 90:
				if (x,y) not in visited_pixels:
					dfs(x,y,visited_pixels,array)
					k += 1
	return k


def vector(array):
	a = two_dimensional_array(array)
	return [feature1(array),
		feature2(a),
		feature3(a),
		feature4(a),
		feature5(a),
		quater1(a),
		quater2(a),
		quater3(a),
		quater4(a),
		number_of_closed_areas(a)]


start = time.clock()
new_data = [vector(x[0]) + [x[1]] for x in data]
print("features calculated in", time.clock() - start)

#5, 6, 3, 3, 5, 4, 4, 4, 4, 8
weight = [5, 6, 3, 3, 5, 4, 4, 4, 4, 8]

def normalize(array, index,weight):
	max_x = max(x[index] for x in array)
	min_x = min(x[index] for x in array)
	for x in array:
		x[index] = (x[index]-min_x)/(max_x-min_x)*weight[index]



def distance(array1,array2):
	return math.sqrt(sum((x-y)**2 for x,y in zip(array1[:-1],array2[:-1])))


def recognize(x,data):
	distances = []
	for y in data:
		if y[-1] != None:
			distances.append((distance(x,y),y[-1]))
	distances.sort(key = lambda x: x[0])
	weight = [K+1-x for x in range(1,K+1)]
	result = [[0,x] for x in range(10)]
	for x in range(K):
		result[distances[x][1]][0] += 1*weight[x]
	result.sort(reverse = True)
	return (result[0][1], result)


# def guessed_pic(x, data):
# 	if x < len(data):
# 		image = Image.frombytes('L', (28,28), bytes(data[x][0]))
# 		big_image = image.resize((500,500))

		

# 		cnv.delete(*cnv.find_all())
# 		image_tk = ImageTk.PhotoImage(image)
# 		cnv.create_image(0, 0, image=image_tk, anchor ='nw')
# 		cnv.after(200, guessed_pic(x+1, data))

# 	else:
# 		print('Done')

# def guessed_digit(x, new_data):
# 	if x < len(data):
# 		ans = new_data[x][-1]
# 		new_data[x][-1] = None
# 		rec = recognize(new_data[x],new_data)[0]
# 		new_data[x][-1] = ans


# 		correct_digit.delete(*correct_digit.find_all())
# 		correct_digit = correct_digit.create_text(text = (rec, ans), font = "Arial 100")
# 		correct_digit.after(200, guessed_digit(x+1, new_data))


# 	else:
# 		print('Done')	


if photo == '':
	for index in range(len(new_data[0])-1):
		normalize(new_data,index,weight)
	guessed = 0

	# window = tkinter.Tk()
	# window.geometry('1000x500+200+200')
	
	# correct_digit = tkinter.Canvas(width = 500, height = 500)
	# cnv = tkinter.Canvas(width = 500, height = 500)
	# guessed_pic(0, data)
	# guessed_digit(0,data)

	# correct_digit.grid(row = 0, column = 0)
	# cnv.grid(row = 0, column = 1, sticky = 'ne')
	
	# window.mainloop()

	for x in range(500):#len(new_data)
		ans = new_data[x][-1]
		new_data[x][-1] = None
		rec = recognize(new_data[x],new_data)[0]
		new_data[x][-1] = ans
		print(ans, rec)
		if ans == rec:
			guessed += 1
		if x!=0:
			print("precent:", guessed/(x+1))

	print("guessed:", guessed, "total:", len(new_data))


else:
	new_photo_array = vector(photo_array[0]) + [photo_array[1]]
	print(new_photo_array)
	for index in range(len(new_photo_array)-1):
		normalize(new_data + [new_photo_array],index,weight)
	print(new_photo_array)
	
	print(recognize(new_photo_array, new_data))

	window = tkinter.Tk()
	window.geometry('900x500+200+200')
	
	image = Image.frombytes('L', (28,28), bytes(photo_array[0]))
	image=image.resize((500,500))
	correct_digit = tkinter.Label(text = recognize(new_photo_array, new_data)[0], padx = 170, font = "Arial 100")
	correct_digit.grid(row = 0, column = 0)
	cnv = tkinter.Canvas(width = 500, height = 500)
	cnv.grid(row = 0, column = 1, sticky = 'ne')
	image_tk = ImageTk.PhotoImage(image)
	image_id = cnv.create_image(0, 0, image=image_tk, anchor ='nw')
	window.mainloop()











