#
#   Author: Catherine Leung
#   These are the unit tests for the MinHeap class
#   To use this, run: python test_lab-05.py

import unittest
from lab5 import MinHeap

class MinHeapTestCase(unittest.TestCase):
	"""These are the test cases for the MinHeap class"""
	
	def test_init_empty(self):
		my_heap = MinHeap()
		self.assertTrue(my_heap.is_empty())
		self.assertEqual(my_heap.size(), 0)

	def test_init_with_list(self):
		my_list = [5, 3, 7, 1, 9, 2]
		my_heap = MinHeap(my_list)
		self.assertFalse(my_heap.is_empty())
		self.assertEqual(my_heap.size(), 6)
		self.assertEqual(my_heap.min(), 1)

	def test_is_empty(self):
		my_heap = MinHeap()
		self.assertTrue(my_heap.is_empty())
		
		my_heap.push(5)
		self.assertFalse(my_heap.is_empty())
		
		my_heap.pop()
		self.assertTrue(my_heap.is_empty())

	def test_size_empty(self):
		my_heap = MinHeap()
		self.assertEqual(my_heap.size(), 0)

	def test_size_after_push(self):
		my_heap = MinHeap()
		my_heap.push(5)
		self.assertEqual(my_heap.size(), 1)
		
		my_heap.push(3)
		self.assertEqual(my_heap.size(), 2)
		
		my_heap.push(7)
		self.assertEqual(my_heap.size(), 3)

	def test_size_after_pop(self):
		my_heap = MinHeap()
		my_heap.push(5)
		my_heap.push(3)
		my_heap.push(7)
		self.assertEqual(my_heap.size(), 3)
		
		my_heap.pop()
		self.assertEqual(my_heap.size(), 2)
		
		my_heap.pop()
		self.assertEqual(my_heap.size(), 1)

	def test_push_single_element(self):
		my_heap = MinHeap()
		my_heap.push(5)
		self.assertEqual(my_heap.min(), 5)
		self.assertEqual(my_heap.size(), 1)

	def test_push_multiple_elements(self):
		my_heap = MinHeap()
		my_heap.push(5)
		self.assertEqual(my_heap.min(), 5)
		
		my_heap.push(3)
		self.assertEqual(my_heap.min(), 3)
		
		my_heap.push(7)
		self.assertEqual(my_heap.min(), 3)
		
		my_heap.push(1)
		self.assertEqual(my_heap.min(), 1)
		
		my_heap.push(9)
		self.assertEqual(my_heap.min(), 1)


	def test_push_negative_values(self):
		my_heap = MinHeap()
		my_heap.push(5)
		my_heap.push(-3)
		my_heap.push(7)
		self.assertEqual(my_heap.min(), -3)
		self.assertEqual(my_heap.size(), 3)

	def test_min_single_element(self):
		my_heap = MinHeap()
		my_heap.push(42)
		self.assertEqual(my_heap.min(), 42)

	def test_min_multiple_elements(self):
		my_heap = MinHeap()
		my_heap.push(10)
		my_heap.push(20)
		my_heap.push(5)
		my_heap.push(15)
		self.assertEqual(my_heap.min(), 5)

	def test_min_does_not_remove(self):
		my_heap = MinHeap()
		my_heap.push(5)
		my_heap.push(3)
		my_heap.push(7)
		
		self.assertEqual(my_heap.min(), 3)
		self.assertEqual(my_heap.size(), 3)
		self.assertEqual(my_heap.min(), 3)


	def test_pop_single_element(self):
		my_heap = MinHeap()
		my_heap.push(5)
		rc = my_heap.pop()
		self.assertEqual(rc, 5)
		self.assertTrue(my_heap.is_empty())

	def test_pop_multiple_elements_in_order(self):
		my_heap = MinHeap()
		my_heap.push(5)
		my_heap.push(3)
		my_heap.push(7)
		my_heap.push(1)
		my_heap.push(9)
		
		self.assertEqual(my_heap.pop(), 1)
		self.assertEqual(my_heap.pop(), 3)
		self.assertEqual(my_heap.pop(), 5)
		self.assertEqual(my_heap.pop(), 7)
		self.assertEqual(my_heap.pop(), 9)
		self.assertTrue(my_heap.is_empty())

	def test_pop_maintains_heap_property(self):
		my_heap = MinHeap()
		my_heap.push(10)
		my_heap.push(20)
		my_heap.push(5)
		my_heap.push(15)
		my_heap.push(30)
		
		rc = my_heap.pop()
		self.assertEqual(rc, 5)
		self.assertEqual(my_heap.min(), 10)
		
		rc = my_heap.pop()
		self.assertEqual(rc, 10)
		self.assertEqual(my_heap.min(), 15)



	def test_pop_until_empty(self):
		my_heap = MinHeap()
		my_heap.push(3)
		my_heap.push(1)
		my_heap.push(2)
		
		self.assertEqual(my_heap.pop(), 1)
		self.assertEqual(my_heap.size(), 2)
		self.assertFalse(my_heap.is_empty())
		
		self.assertEqual(my_heap.pop(), 2)
		self.assertEqual(my_heap.size(), 1)
		self.assertFalse(my_heap.is_empty())
		
		self.assertEqual(my_heap.pop(), 3)
		self.assertEqual(my_heap.size(), 0)
		self.assertTrue(my_heap.is_empty())

	def test_init_with_unsorted_list(self):
		my_list = [9, 5, 6, 2, 3, 7, 1, 4, 8]
		my_heap = MinHeap(my_list)
		self.assertEqual(my_heap.size(), 9)
		self.assertEqual(my_heap.min(), 1)
		
		sorted_result = []
		while not my_heap.is_empty():
			sorted_result.append(my_heap.pop())
		self.assertEqual(sorted_result, 
			[1, 2, 3, 4, 5, 6, 7, 8, 9])

	def test_init_with_single_element_list(self):
		my_list = [42]
		my_heap = MinHeap(my_list)
		self.assertEqual(my_heap.size(), 1)
		self.assertEqual(my_heap.min(), 42)


	def test_init_list_not_modified(self):
		my_list = [5, 3, 7, 1, 9]
		original_list = my_list.copy()
		my_heap = MinHeap(my_list)
		self.assertEqual(my_list, original_list)

	def test_mixed_operations(self):
		my_heap = MinHeap()
		my_heap.push(10)
		my_heap.push(5)
		self.assertEqual(my_heap.min(), 5)
		
		my_heap.push(3)
		self.assertEqual(my_heap.pop(), 3)
		
		my_heap.push(7)
		my_heap.push(1)
		self.assertEqual(my_heap.min(), 1)
		
		self.assertEqual(my_heap.pop(), 1)
		self.assertEqual(my_heap.pop(), 5)
		self.assertEqual(my_heap.size(), 2)

	def test_init_list_push_pop_complex(self):
		my_list = [25, 20, 15, 30]
		my_heap = MinHeap(my_list)
		self.assertEqual(my_heap.size(), 4)
		self.assertEqual(my_heap.min(), 15)
		
		# Push new items - some will be removed, some won't
		my_heap.push(10)
		self.assertEqual(my_heap.size(), 5)
		self.assertEqual(my_heap.min(), 10)
		
		my_heap.push(5)
		self.assertEqual(my_heap.size(), 6)
		self.assertEqual(my_heap.min(), 5)
		
		my_heap.push(35)
		self.assertEqual(my_heap.size(), 7)
		self.assertEqual(my_heap.min(), 5)
		
		my_heap.push(12)
		self.assertEqual(my_heap.size(), 8)
		self.assertEqual(my_heap.min(), 5)
		
		# Remove 10 items (more than the 4 initial + 4 added = 8 total)
		# This tests that we remove both original and newly added items
		self.assertEqual(my_heap.pop(), 5)
		self.assertEqual(my_heap.size(), 7)
		
		self.assertEqual(my_heap.pop(), 10)
		self.assertEqual(my_heap.size(), 6)
		
		self.assertEqual(my_heap.pop(), 12)
		self.assertEqual(my_heap.size(), 5)
		
		self.assertEqual(my_heap.pop(), 15)
		self.assertEqual(my_heap.size(), 4)
		
		self.assertEqual(my_heap.pop(), 20)
		self.assertEqual(my_heap.size(), 3)
		
		self.assertEqual(my_heap.pop(), 25)
		self.assertEqual(my_heap.size(), 2)
		
		self.assertEqual(my_heap.pop(), 30)
		self.assertEqual(my_heap.size(), 1)
		
		self.assertEqual(my_heap.pop(), 35)
		self.assertEqual(my_heap.size(), 0)
		self.assertTrue(my_heap.is_empty())

	def test_large_heap(self):
		my_heap = MinHeap()
		for i in range(100, 0, -1):
			my_heap.push(i)
		
		self.assertEqual(my_heap.size(), 100)
		self.assertEqual(my_heap.min(), 1)
		
		for i in range(1, 101):
			self.assertEqual(my_heap.pop(), i)
		
		self.assertTrue(my_heap.is_empty())


if __name__ == '__main__':
	unittest.main()
