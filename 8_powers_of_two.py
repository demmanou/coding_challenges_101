import unittest


# Given a number (float or integer!), find out if it's a valid power of two
# A number is considered to be a valid power of two, if there is a 
# number such, that when raised to the power of 2, is equal to the the first number
# For example, 8 is a valid power of two since 2^3 == 8. 0.25 is a valid power of two
# since 2^(-2) == 0.25


class Solution:
    def power_of_two(self, num: float) -> bool:
        pass


class Test(unittest.TestCase):
    test_cases = [
        (8, True),
        (6, False),
        (-1, False),
        (0, False),
        (0.25, True),
        (0.5, True),
        (0.125, True),
        (0.15, False)
    ]

    test_functions = [
        Solution().power_of_two
    ]

    def test_funcs(self):
        for input_, expected in self.test_cases:
            for func in self.test_functions:
                output = func(input_)
                assert output == expected, \
                    f'\nFailed for input {input_}\nYour output: {output}\nCorrect output: {expected}'


if __name__ == "__main__":
    unittest.main()
