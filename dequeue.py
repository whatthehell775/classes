class Dequeue():
	def __init__(self):
		self.items = []
	def isEmpty(self):
		return self.items==[]
	def addFront(self,item):
		self.items.append(item)
	def addRear(self):
		self.items.insert(0,item)
	def removeFront(self):
		self.items.pop()
	def removeRear(self):
		self.items.pop(0)
	def size(self):
		return len(self.items)
	def __str__(self):
		return str(self.items)
	def __repr__(self):
		return str(self.items)
