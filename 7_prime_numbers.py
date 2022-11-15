import unittest
from typing import List


# Given a sequence of numbers return only
# the prime ones. Prime numbers are the ones
# that are divisible only by 1 and themselves


class Solution:
    def prime_numbers(self, seq: List[int]) -> List[int]:
        pass


class Test(unittest.TestCase):
    test_cases = [
        ([*range(2, 100)],
            [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])
    ]

    test_functions = [
        Solution().prime_numbers
    ]

    def test_funcs(self):
        for input_, expected in self.test_cases:
            for func in self.test_functions:
                output = func(input_)
                assert output == expected, \
                    f'\nFailed for input {input_}\nYour output: {output}\nCorrect output: {expected}'


if __name__ == "__main__":
    unittest.main()