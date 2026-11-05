import unittest

from sum_to_goal import sum_to_goal


class TestSumToGoal(unittest.TestCase):

    def test_1(self):
        self.assertEqual(sum_to_goal([1, 2, 3, 4], 5), 4)

    def test_2(self):
        self.assertEqual(sum_to_goal([2, 7, 11, 15], 9), 14)

    def test_3(self):
        self.assertEqual(sum_to_goal([3, 5, 8, 10], 13), 40)

    def test_4(self):
        self.assertEqual(sum_to_goal([1, 5, 9, 12], 20), 60)

    def test_5(self):
        self.assertEqual(sum_to_goal([1, 2, 3, 4], 100), None)

    def test_6(self):
        self.assertEqual(sum_to_goal([], 10), None)


if __name__ == "__main__":
    unittest.main()