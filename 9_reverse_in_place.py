import unittest
from typing import List


# Given an array, reverse the array in place
# In place means without creating a new array (space complexity O(1))
# Credit: Marijn Haverbeke


class Solution:
    def reverse_in_place(self, arr: List[int]) -> None:
        pass


class Test(unittest.TestCase):
    test_cases = [
        ([1, 2, 3, 4], [4, 3, 2, 1]),
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1])
    ]

    test_functions = [
        Solution().reverse_in_place
    ]

    def test_funcs(self):
        for input_, expected in self.test_cases:
            for func in self.test_functions:
                func(input_)
                assert input_ == expected, \
                    f'\nFailed for input {input_}\nYour output: {input_}\nCorrect output: {expected}'


if __name__ == "__main__":
    unittest.main()