import unittest

from fibonacci import fibonacci


class Lab1TestCase(unittest.TestCase):
    
    def test_fibonacci(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(3), 2)
        self.assertEqual(fibonacci(7), 13)
        self.assertEqual(fibonacci(11), 89)
        self.assertEqual(fibonacci(14), 377)
        self.assertEqual(fibonacci(17), 1597)


if __name__ == '__main__':
    unittest.main()