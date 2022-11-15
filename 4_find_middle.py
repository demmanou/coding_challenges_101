import unittest
from typing import List


# An unordered sequence of numbers is provided.
# Sort the sequence and return the number at the middle
# If the sequence is one of an odd length, for example 
# [1, 2, 3, 4], the middle one would be 2


class Solution:
    def middle_number(self, numbers: List[int]) -> int:
        pass


class Test(unittest.TestCase):
    test_cases = [
        ([5, 5, 10, 2, 1, 0, -5, 1], 1),
        ([4, 5, 1, 2], 2), 
    ]

    test_functions = [
        Solution().middle_number
    ]

    def test_funcs(self):
        for input_, expected in self.test_cases:
            for func in self.test_functions:
                output = func(input_)
                assert output == expected, \
                    f'Failed for input {input_}. Your output: {output}. Correct output: {expected}'


if __name__ == "__main__":
    unittest.main()
