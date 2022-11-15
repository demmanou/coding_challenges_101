import unittest


# Given two words as input,
# find and return if the words are an anagram
# of one another


class Solution:
    def is_anagram(self, word_a: str, word_b: str) -> bool:
        pass


class Test(unittest.TestCase):
    test_cases = [
        (('bored', 'robed'), True),
        (('elbow', 'below'), True),
        (('dog', 'cat'), False) 
    ]

    test_functions = [
        Solution().is_anagram
    ]

    def test_funcs(self):
        for input_, expected in self.test_cases:
            for func in self.test_functions:
                output = func(*input_)
                assert output == expected, \
                    f'Failed for input {input_}. Your output: {output}. Correct output: {expected}'


if __name__ == "__main__":
    unittest.main()
