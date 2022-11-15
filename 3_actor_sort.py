import unittest
from typing import List


# Given a list of actor names in (first, last name) pairs,
# return a list with the same pairs, sorted by descending 
# alphabetical order of the actors' last names


class Solution:
    def actor_sort(self, actors: List[tuple]) -> list:
        pass


class Test(unittest.TestCase):
    test_cases = [
        ([('John', 'Wayne'), ('Charlton', 'Heston'), ('Sean', 'Connery'), ('Robert', 'Redford'), ('Alain', 'Delon')],
            [('John', 'Wayne'), ('Robert', 'Redford'), ('Charlton', 'Heston'), ('Alain', 'Delon'), ('Sean', 'Connery')])
    ]

    test_functions = [
        Solution().actor_sort
    ]

    def test_funcs(self):
        for input_, expected in self.test_cases:
            for func in self.test_functions:
                assert func(input_) == expected, 'Failed!'


if __name__ == "__main__":
    unittest.main()
