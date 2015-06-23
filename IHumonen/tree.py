class Node:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None
	def __str__(self):
		return str(self.value)
	def add(self, node):
		if node.value > self.value:
			if self.right == None:
				self.right = node
			else:
				self.right.add(node)
		else:
			if self.left == None:
				self.left = node
			else:
				self.left.add(node)
	def find(self, node):
		if self.value == node.value:
			return True
		else:
			if node.value > self.value:
				if self.right == None:
					return False
				else:
					return self.right.find(node) 
			else:
				if self.left == None:
					return False 	
				else:
					return self.left.find(node)

class Tree:
	def __init__(self):
		self.root = None					
	def add(self, node):
		if self.root == None:
			self.root = node
		else:
			self.root.add(node)
	def find(self, node):
		if self.root == None:
			return False
		else:
			return self.root.find(node)
	def delete(self, node):
		if self.root.value == node.value:
			if self.root.left == 0 and self.root.right == 0:
				self.root = None
			else:
				if self.root.right == None:
					self.root =  self.root.left
				else:
						self.root = self.root.right
		else:
			
node_1 = Node('Artiom')
node_2 = Node('Kesha')
node_3 = Node('Mathew')
node_4 = Node('Sanya')
node_5 = Node('qwerfcdtygjcvvgyhxvjg')
print(node_2)
tree = Tree()
if tree.find(node_1):
	print('YES')
else:
	print('NO')
tree.add(node_1)
print(tree.root)
if tree.find(node_1):
	print('YES')
else:
	print('NO')
tree.add(node_2)
print(tree.root.right)
tree.add(node_3)
tree.add(node_4)
if tree.find(node_4):
	print('YES')
else:
	print('NO')
if tree.find(node_5):
	print('YES')
else:
	print('NO')
q = input()