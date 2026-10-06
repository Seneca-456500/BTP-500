#
#   Author: Catherine Leung
#   These are the unit tests for functions and classes of lab 3.
#   To use this, run: `python lab3_tester.py`

import unittest
from lab3 import DoublyLinked, Sentinel

class Lab3TestCase(unittest.TestCase):
	"""These are the test cases for functions and classes of a1"""
	
	def test_init_(self):
		my_list = DoublyLinked()
		self.assertEqual(my_list.get_front(), None)
		self.assertEqual(my_list.get_back(), None)
 
	def test_push_front(self):
		my_list = DoublyLinked()
		my_list.push_front(1)
		self.assertNotEqual(my_list.get_front(), None)
		self.assertNotEqual(my_list.get_back(), None)
		self.assertEqual(my_list.get_front().get_data(), 1)
		self.assertEqual(my_list.get_back().get_data(), 1)

		my_list.push_front(5)
		self.assertEqual(my_list.get_front().get_data(), 5)
		self.assertEqual(my_list.get_back().get_data(), 1)
		self.assertEqual(my_list.get_front().get_next().get_data(), 1)
		self.assertEqual(my_list.get_back().get_previous().get_data(), 5)


		my_list.push_front(3)
		self.assertEqual(my_list.get_front().get_data(), 3)
		self.assertEqual(my_list.get_back().get_data(), 1)
		self.assertEqual(my_list.get_front().get_next().get_data(), 5)
		self.assertEqual(my_list.get_front().get_next().get_next().get_data(), 1)
		self.assertEqual(my_list.get_front().get_next().get_previous().get_data(), 3)
		self.assertEqual(my_list.get_back().get_previous().get_data(), 5)

		my_list.push_front(15)
		self.assertEqual(my_list.get_front().get_data(), 15)
		self.assertEqual(my_list.get_back().get_data(), 1)
		self.assertEqual(my_list.get_front().get_next().get_data(), 3)
		self.assertEqual(my_list.get_front().get_next().get_next().get_data(), 5)
		self.assertEqual(my_list.get_front().get_next().get_previous().get_data(), 15)
		self.assertEqual(my_list.get_back().get_previous().get_data(), 5)


 
	def test_push_back(self):
		my_list = DoublyLinked()
		my_list.push_back(1)
		self.assertEqual(my_list.get_front().get_data(), 1)
		self.assertEqual(my_list.get_back().get_data(), 1)

		my_list.push_back(5)
		self.assertEqual(my_list.get_front().get_data(), 1)
		self.assertEqual(my_list.get_back().get_data(), 5)
		self.assertEqual(my_list.get_front().get_next().get_data(), 5)
		self.assertEqual(my_list.get_back().get_previous().get_data(), 1)


		my_list.push_back(3)
		self.assertEqual(my_list.get_front().get_data(), 1)
		self.assertEqual(my_list.get_back().get_data(), 3)
		self.assertEqual(my_list.get_front().get_next().get_data(), 5)
		self.assertEqual(my_list.get_back().get_previous().get_data(), 5)
		self.assertEqual(my_list.get_back().get_previous().get_previous().get_data(), 1)
		self.assertEqual(my_list.get_back().get_previous().get_next().get_data(), 3)

		my_list.push_back(15)
		self.assertEqual(my_list.get_front().get_data(), 1)
		self.assertEqual(my_list.get_back().get_data(), 15)
		self.assertEqual(my_list.get_front().get_next().get_data(), 5)
		self.assertEqual(my_list.get_back().get_previous().get_data(), 3)
		self.assertEqual(my_list.get_back().get_previous().get_previous().get_data(), 5)
		self.assertEqual(my_list.get_back().get_previous().get_next().get_data(), 15)


	def test_pop_front(self):
		my_list = DoublyLinked()
		my_list.push_front(15)
		my_list.push_back(24)
		my_list.push_front(31)
		my_list.push_back(9)


		rc = my_list.pop_front()
		self.assertEqual(rc, 31)
		self.assertEqual(my_list.get_front().get_data(), 15)
		self.assertEqual(my_list.get_front().get_next().get_data(), 24)
		self.assertEqual(my_list.get_front().get_next().get_next().get_data(), 9)
		self.assertEqual(my_list.get_back().get_data(), 9)
		self.assertEqual(my_list.get_back().get_previous().get_data(), 24)
		self.assertEqual(my_list.get_back().get_previous().get_previous().get_data(), 15)


		rc = my_list.pop_front()
		self.assertEqual(rc, 15)
		self.assertEqual(my_list.get_front().get_data(), 24)
		self.assertEqual(my_list.get_front().get_next().get_data(), 9)
		self.assertEqual(my_list.get_back().get_data(), 9)
		self.assertEqual(my_list.get_back().get_previous().get_data(), 24)


		rc = my_list.pop_front()
		self.assertEqual(rc, 24)
		self.assertEqual(my_list.get_front().get_data(), 9)
		self.assertEqual(my_list.get_back().get_data(), 9)


		rc = my_list.pop_front()
		self.assertEqual(rc, 9)
		self.assertEqual(my_list.get_front(), None)
		self.assertEqual(my_list.get_back(), None)

		with self.assertRaises(IndexError) as cm:
			rc = my_list.pop_front()
		self.assertEqual(str(cm.exception), 'pop_front() used on empty list')

 
	def test_pop_back(self):
		my_list = DoublyLinked()
		my_list.push_front(15)
		my_list.push_back(24)
		my_list.push_front(31)
		my_list.push_back(9)



		rc = my_list.pop_back()
		self.assertEqual(rc, 9)
		self.assertEqual(my_list.get_front().get_data(), 31)
		self.assertEqual(my_list.get_front().get_next().get_data(), 15)
		self.assertEqual(my_list.get_front().get_next().get_next().get_data(), 24)
		self.assertEqual(my_list.get_back().get_data(), 24)
		self.assertEqual(my_list.get_back().get_previous().get_data(), 15)
		self.assertEqual(my_list.get_back().get_previous().get_previous().get_data(), 31)


		rc = my_list.pop_back()
		self.assertEqual(rc, 24)
		self.assertEqual(my_list.get_front().get_data(), 31)
		self.assertEqual(my_list.get_front().get_next().get_data(), 15)
		self.assertEqual(my_list.get_back().get_data(), 15)
		self.assertEqual(my_list.get_back().get_previous().get_data(), 31)


		rc = my_list.pop_back()
		self.assertEqual(rc, 15)
		self.assertEqual(my_list.get_front().get_data(), 31)
		self.assertEqual(my_list.get_back().get_data(), 31)


		rc = my_list.pop_back()
		self.assertEqual(rc, 31)
		self.assertEqual(my_list.get_front(), None)
		self.assertEqual(my_list.get_back(), None)

		with self.assertRaises(IndexError) as cm:
			rc = my_list.pop_back()
		self.assertEqual(str(cm.exception), 'pop_back() used on empty list')







	def test_sentinel_init_(self):
		my_list = Sentinel()
		self.assertEqual(my_list.get_front(), None)
		self.assertEqual(my_list.get_back(), None)
 
	def test_sentinel_push_front(self):
		my_list = Sentinel()
		my_list.push_front(1)
		self.assertNotEqual(my_list.get_front(), None)
		self.assertNotEqual(my_list.get_back(), None)
		self.assertEqual(my_list.get_front().get_data(), 1)
		self.assertEqual(my_list.get_back().get_data(), 1)

		my_list.push_front(5)
		self.assertEqual(my_list.get_front().get_data(), 5)
		self.assertEqual(my_list.get_back().get_data(), 1)
		self.assertEqual(my_list.get_front().get_next().get_data(), 1)
		self.assertEqual(my_list.get_back().get_previous().get_data(), 5)


		my_list.push_front(3)
		self.assertEqual(my_list.get_front().get_data(), 3)
		self.assertEqual(my_list.get_back().get_data(), 1)
		self.assertEqual(my_list.get_front().get_next().get_data(), 5)
		self.assertEqual(my_list.get_front().get_next().get_next().get_data(), 1)
		self.assertEqual(my_list.get_front().get_next().get_previous().get_data(), 3)
		self.assertEqual(my_list.get_back().get_previous().get_data(), 5)

		my_list.push_front(15)
		self.assertEqual(my_list.get_front().get_data(), 15)
		self.assertEqual(my_list.get_back().get_data(), 1)
		self.assertEqual(my_list.get_front().get_next().get_data(), 3)
		self.assertEqual(my_list.get_front().get_next().get_next().get_data(), 5)
		self.assertEqual(my_list.get_front().get_next().get_previous().get_data(), 15)
		self.assertEqual(my_list.get_back().get_previous().get_data(), 5)


 
	def test_sentinel_push_back(self):
		my_list = Sentinel()
		my_list.push_back(1)
		self.assertEqual(my_list.get_front().get_data(), 1)
		self.assertEqual(my_list.get_back().get_data(), 1)

		my_list.push_back(5)
		self.assertEqual(my_list.get_front().get_data(), 1)
		self.assertEqual(my_list.get_back().get_data(), 5)
		self.assertEqual(my_list.get_front().get_next().get_data(), 5)
		self.assertEqual(my_list.get_back().get_previous().get_data(), 1)


		my_list.push_back(3)
		self.assertEqual(my_list.get_front().get_data(), 1)
		self.assertEqual(my_list.get_back().get_data(), 3)
		self.assertEqual(my_list.get_front().get_next().get_data(), 5)
		self.assertEqual(my_list.get_back().get_previous().get_data(), 5)
		self.assertEqual(my_list.get_back().get_previous().get_previous().get_data(), 1)
		self.assertEqual(my_list.get_back().get_previous().get_next().get_data(), 3)

		my_list.push_back(15)
		self.assertEqual(my_list.get_front().get_data(), 1)
		self.assertEqual(my_list.get_back().get_data(), 15)
		self.assertEqual(my_list.get_front().get_next().get_data(), 5)
		self.assertEqual(my_list.get_back().get_previous().get_data(), 3)
		self.assertEqual(my_list.get_back().get_previous().get_previous().get_data(), 5)
		self.assertEqual(my_list.get_back().get_previous().get_next().get_data(), 15)


	def test_sentinel_pop_front(self):
		my_list = Sentinel()
		my_list.push_front(15)
		my_list.push_back(24)
		my_list.push_front(31)
		my_list.push_back(9)


		rc = my_list.pop_front()
		self.assertEqual(rc, 31)
		self.assertEqual(my_list.get_front().get_data(), 15)
		self.assertEqual(my_list.get_front().get_next().get_data(), 24)
		self.assertEqual(my_list.get_front().get_next().get_next().get_data(), 9)
		self.assertEqual(my_list.get_back().get_data(), 9)
		self.assertEqual(my_list.get_back().get_previous().get_data(), 24)
		self.assertEqual(my_list.get_back().get_previous().get_previous().get_data(), 15)


		rc = my_list.pop_front()
		self.assertEqual(rc, 15)
		self.assertEqual(my_list.get_front().get_data(), 24)
		self.assertEqual(my_list.get_front().get_next().get_data(), 9)
		self.assertEqual(my_list.get_back().get_data(), 9)
		self.assertEqual(my_list.get_back().get_previous().get_data(), 24)


		rc = my_list.pop_front()
		self.assertEqual(rc, 24)
		self.assertEqual(my_list.get_front().get_data(), 9)
		self.assertEqual(my_list.get_back().get_data(), 9)


		rc = my_list.pop_front()
		self.assertEqual(rc, 9)
		self.assertEqual(my_list.get_front(), None)
		self.assertEqual(my_list.get_back(), None)

		with self.assertRaises(IndexError) as cm:
			rc = my_list.pop_front()
		self.assertEqual(str(cm.exception), 'pop_front() used on empty list')

 
	def test_sentinel_pop_back(self):
		my_list = Sentinel()
		my_list.push_front(15)
		my_list.push_back(24)
		my_list.push_front(31)
		my_list.push_back(9)



		rc = my_list.pop_back()
		self.assertEqual(rc, 9)
		self.assertEqual(my_list.get_front().get_data(), 31)
		self.assertEqual(my_list.get_front().get_next().get_data(), 15)
		self.assertEqual(my_list.get_front().get_next().get_next().get_data(), 24)
		self.assertEqual(my_list.get_back().get_data(), 24)
		self.assertEqual(my_list.get_back().get_previous().get_data(), 15)
		self.assertEqual(my_list.get_back().get_previous().get_previous().get_data(), 31)


		rc = my_list.pop_back()
		self.assertEqual(rc, 24)
		self.assertEqual(my_list.get_front().get_data(), 31)
		self.assertEqual(my_list.get_front().get_next().get_data(), 15)
		self.assertEqual(my_list.get_back().get_data(), 15)
		self.assertEqual(my_list.get_back().get_previous().get_data(), 31)


		rc = my_list.pop_back()
		self.assertEqual(rc, 15)
		self.assertEqual(my_list.get_front().get_data(), 31)
		self.assertEqual(my_list.get_back().get_data(), 31)


		rc = my_list.pop_back()
		self.assertEqual(rc, 31)
		self.assertEqual(my_list.get_front(), None)
		self.assertEqual(my_list.get_back(), None)

		with self.assertRaises(IndexError) as cm:
			rc = my_list.pop_back()
		self.assertEqual(str(cm.exception), 'pop_back() used on empty list')










if __name__ == '__main__':
	unittest.main()
