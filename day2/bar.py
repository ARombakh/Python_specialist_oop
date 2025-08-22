
class Bar:
	def __init__(self, a, b):
		self.a = a
		self.b = b
	def __str__(self):
		return f'{self.a}:{self.b}'
	
	def __add__(self, other):
		return Bar(self.a + other.a, self.b + other.b)
		
	def __eq__(self, other):
		res = False
		if type(other) is Bar:
			if self.a == other.a and self.b == other.b: res = True
		return res
	
	# def __ne__(self, other):
	# 	res = True
	# 	if type(other) is Bar:
	# 		if not (self.a == other.a and self.b == other.b): res = False
	# 	return res

	def __ne__(self, other):
		return not self.__eq__(other)