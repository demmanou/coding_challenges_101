import unittest
from typing import List


# Given a list of numbers as an input, 
# return a dictionary with the frequency 
# each number is seen at in the list


class Solution:
    def number_count(self, numbers: List[int]) -> list:
        pass


class Test(unittest.TestCase):
    test_cases = [
        ([5, 5, 10, 2, 1, 0, -5, 1],
        {5: 2, 10: 1, 2: 1, 1: 2, 0: 1, -5: 1})
    ]

    test_functions = [
        Solution().number_count
    ]

    def test_funcs(self):
        for input_, expected in self.test_cases:
            for func in self.test_functions:
                assert func(input_) == expected, 'Failed!'


if __name__ == "__main__":
    unittest.main()
