import unittest


# Given a word as an input,
# find and return if the word is a palindrome


class Solution:
    def is_palindrome(self, word: str) -> bool:
        pass


class Test(unittest.TestCase):
    test_cases = [
        ('aabaa', True),
        ('abdf', False), 
    ]

    test_functions = [
        Solution().is_palindrome
    ]

    def test_funcs(self):
        for input_, expected in self.test_cases:
            for func in self.test_functions:
                output = func(input_)
                assert output == expected, \
                    f'Failed for input {input_}. Your output: {output}. Correct output: {expected}'


if __name__ == "__main__":
    unittest.main()
