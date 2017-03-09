class Node():

	def __init__(self, data):
		self.data = data

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
				node = other_linked_list.head
				for i in range(k):
					node = node.next()
				if self.size() == 0:
					self.tail = node
					self.head = node
				else:
					self.head.append(node)


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
		self.head.prev().appendNext(self.tail)
		self.head = self.head.prev()
		return node