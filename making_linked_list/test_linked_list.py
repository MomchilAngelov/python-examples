import unittest
import linked_list

class TestLinkedListMethod(unittest.TestCase):

	def testNewLinkedListIsEmpty(self):
		ll = linked_list.LinkedList()
		self.assertEqual(ll.size(), 0)

	def testAddNewNodeToLinkedList(self):
		value = 123
		n = linked_list.Node(value)
		ll = linked_list.LinkedList()
		ll.append(n)
		self.assertEqual(ll.size(), 1)

	def testAddNewNodeToLinkedListAndCheckValue(self):
		value = 123
		n = linked_list.Node(value)
		ll = linked_list.LinkedList()
		ll.append(n)
		data = ll.pop()
		self.assertEqual(data.data, value)

	def testMultipleAppends(self):
		value = [123, 234, 345, 456, 567, 678]
		ll = linked_list.LinkedList()
		for k in value:
			n = linked_list.Node(k)
			ll.append(n)

		for k in reversed(value):
			self.assertEqual(k, ll.pop().getData())

	def testCopyTwoLinkedLists(self):
		value = [123, 234, 345, 456, 567, 678]
		ll = linked_list.LinkedList()
		for k in value:
			n = linked_list.Node(k)
			ll.append(n)

		another_linked_list = linked_list.LinkedList(ll);
		another_linked_list.append(linked_list.Node(789))

		for k in reversed(value):
			self.assertEqual(k, ll.pop().getData())

		value.append(789)

		for k in reversed(value):
			self.assertEqual(k, another_linked_list.pop().getData())

unittest.main()