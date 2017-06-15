class Node():

	def __init__(self, data):
		self.data = data
		self.nextNode = None
		self.previousNode = None

	def appendNext(self, node):
		self.nextNode = node

	def prependPrevious(self, node):
		self.previousNode = node

	def next(self):
		return self.nextNode

	def prev(self):
		return self.previousNode

	def getData(self):
		return self.data

class LinkedList():
	
	def __init__(self, other_linked_list = None):
		self.len = 0
		if other_linked_list:
			for k in range(other_linked_list.size()):
				node = other_linked_list.getFirst()
				self.append(node)

	def size(self):
		return self.len

	def append(self, node):
		if self.size() == 0:
			self.head = node
			self.tail = node
			node.appendNext(node)
			node.prependPrevious(node)
			self.len += 1
		else:
			self.head.appendNext(node)
			node.prependPrevious(self.head)
			self.head = node
			self.len += 1

	def pop(self):
		node = self.head

		if self.head.prev():
			self.head.prev().appendNext(None)
		self.head = self.head.prev()

		return node

	def getFirst(self):
		node = self.tail

		if self.tail.next():
			self.tail.next().prependPrevious(None)
		
		self.tail = self.tail.next()

		return node
