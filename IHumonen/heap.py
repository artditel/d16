class BinaryHeap:
	def __init__(self):
		self.array = []
	def __str__(self):
		return self.array
	def push(self, x):
		self.array.append(x)
		push_(x, self.array) 
	def pop(self):
		a = self.array[0]
		del self.array[0]
		pop_(self.array[0], self.array)
		return a
def push_(x, array):
	i = (array.index(x) - 1)//2
	if i >= 0 and x > array[i]:
		a = array[i] 
		array[i] = x
		array[array.index(x)] = a
		push_(x, array)	
def pop_(x, array):
	i_1 = (array.index(x))*2 + 1
	i_2 = (array.index(x))*2 + 2
	i = max(i_1, i_2)
	if i <= len(array) and x < array[i]:
		a = array[i] 
		array[i] = x
		array[array.index(x)] = a
		pop_(x, array)	
HEAP = BinaryHeap()
HEAP.push(2)
HEAP.push(3)
HEAP.push(4)
HEAP.push(5)
print(HEAP)
HEAP.pop()	
print(HEAP)