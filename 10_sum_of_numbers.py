import unittest

# Given a number, return the sum of all positive numbers up to it, 
# itself inclusive
# As a followup, if you haven't already, write a recursive solution


class Solution:
    def sum_of_numbers(self, num: int) -> int:
        pass


class Test(unittest.TestCase):
    test_cases = [
        (5, 15),
        (12, 78),
        (0, 0)
    ]

    test_functions = [
        Solution().sum_of_numbers
    ]

    def test_funcs(self):
        for input_, expected in self.test_cases:
            for func in self.test_functions:
                output = func(input_)
                assert output == expected, \
                    f'\nFailed for input {input_}\nYour output: {output}\nCorrect output: {expected}'


if __name__ == "__main__":
    unittest.main()
