class Premutation:
	def __init__(self, _):
		if len(set(_)) != len(_):
			raise Exception("not reversible")
		self._ = _
	def __eq__(self, _):
		return self._ == _._
	def __str__(self):
		return str(self._)
	def __mul__(self, other):
		if len(self._) != len(other._):
			raise Exception("Different arity")
		_ = [0] * len(self._)
		for i in range(len(self._)):
			_[i] = self._[other._[i] - 1]
		return Premutation(_)


def test():
	print("Ok" if Premutation([1,2,3,4]) * Premutation([2,3,1,4]) == Premutation([2,3,1,4]) else "Failed")
	print("Ok" if Premutation([2,3,1,4]) * Premutation([4,3,2,1]) == Premutation([4,1,3,2]) else "Failed")
	try:
		Premutation([2,2])
	except:
		print("Ok")
	else:
		print("Failed")
	try:
		Premutation([2,3,1,4]) * Premutation([4,1])
	except:
		print("Ok")
	else:
		print("Failed")
test()