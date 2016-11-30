import math

def IsPrime(x):
	if x == 2:
		return True
	if x % 2 == 0:
		return False
	s = int(math.sqrt(x))
	for i in range(3, s+1, 2):
		if x % i == 0:
			return False
	return True

class Hashtable:

	def __init__(self, datasize):
		self.mSize = 0
		tablesize = datasize * 2 + 1
		while not IsPrime(tablesize):
			tablesize += 2
		self.mTable = [None] * tablesize

	def Insert(self, item):
		# if self.Exists(item):
		# 	return False
		self.mSize += 1
		index = int(item) % len(self.mTable)
		while self.mTable[index] is not None:
			index += 1
			if index == len(self.mTable):
				index = 0
		self.mTable[index] = item

	def Size(self):
		return self.mSize

	def Exists(self, item):
		index = int(item) % len(self.mTable)
		while self.mTable[index] is not None:
			if self.mTable[index] and self.mTable[index] == item:
				return True
			index += 1
			if index == len(self.mTable):
				index = 0
		return False

	def Delete(self, item):
		if self.Exists(item):
			self.mSize -= 1
			index = int(item) % len(self.mTable)
			while not self.mTable[index] or self.mTable[index] != item:
				index += 1
				if index == len(self.mTable):
					index == 0
			self.mTable[index] = False
			return True
		else:
			return False 

	def Traverse(self, function):
		i = 0 
		age = 0
		while i < len(self.mTable):
			if self.mTable[i]:
				age += function(self.mTable[i])
			i += 1
		return age


	def Retrieve(self, item):
		if self.Exists(item):
			index = int(item) % len(self.mTable)
			while not self.mTable[index] or self.mTable[index] != item:
				index += 1
				if index == len(self.mTable):
					index = 0
			return self.mTable[index]
		return False





