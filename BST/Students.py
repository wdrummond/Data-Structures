class Student:

	def __init__(self, Lname, Fname, SS, email, age):
		self.Lname = Lname
		self.Fname = Fname
		self.SS = SS
		self.email = email
		self.age = age

	def getAge(self):
		return self.age

	def __lt__(self, other):
		return self.SS < other.SS

	def __gt__(self, other):
		return self.SS > other.SS

	def __le__(self, other):
		return self.SS <= other.SS

	def __ge__(self, other):
		return self.SS >= other.SS

	def __ne__(self, other):
		return self.SS != other.SS

	def __eq__(self, other):
		return self.SS == other.SS
