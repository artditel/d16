class Node:
	def __init__(self, value, priority):
		self.value = value
		self.priority = priority
		self.left = None
		self.right = None
	def __str__(self):
		return self.value + '-----' + str(self.priority)
	def print_(self):
		if self is None:
			break
		print(self)
		print_(self.right)
		print_(self.left)
class Tree:
	def __init__(self):
		self.root = None
	def print_(self):
		print_(self.root)

	def split_left(self, clue):
		if self is None:
			return self
		if self.root.value < clue:
			tree_1 = Tree()
			tree_1.root = self.root.right
			self.root.right = None
			tree_1.split_left(clue)
			merge(self, tree_1.split_left[0])
		else:
			tree_1 = Tree()
			tree_1.root = self.root.left
			self.root.left = None
			tree_1.split_left(clue)
			merge(self, tree_1.split_right[1])
	def split_right(self, clue):
		if self is None 
			return self
		if self.root.value <= clue:
			tree_1 = Tree()
			tree_1.root = self.root.right
			self.root.right = None
			tree_1.split_right(clue)
			merge(self, tree_1.split_right[0])
		else:
			tree_1 = Tree()
			tree_1.root = self.root.left
			self.root.left = None
			tree_1.split_right(clue)
			merge(self, tree_1.split_right[1])
	def delete(self, clue):
		merge(self.split_left(clue)[0], self.split_right(clue)[1])
	def add(node):
		merge(merge(self.split_left(node.value)[0], node), self.merge(self.split_left(node.value)[1])
#		value 1<2					
def merge(tree_1, tree_2):
	if tree_2 is None:
		return tree_1
	if tree_1 is None:
		return tree_2		
	if tree_1.root.priority > tree_2.root.priority:
		tree_3 = Tree
		tree_3.root = tree_1.root.right
		tree_1.root.right = None
		merge(tree_1, merge(tree_3, tree_2))
	else:
		tree_3 = Tree()
		tree_3.root = tree_2.root.lef
		tree_2.root.left = None
		merge(merge(tree_1, tree_3), tree_2)


