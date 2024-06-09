"""
Count Alphabets

Count the number of alphabets in a given string.

Example One
{
"s": "#aBdj12C"
}
Output:
5


Example Two
{
"s": "123 !@#$"
}
Output:
0

Notes

Constraints:
0 <= length of string <= 104
String contains lower case and upper case English alphabets, 
    digits, and some special characters('!', '@', '#', '$', '*', ' ') only.
"""

import unittest

def count_alphabets(sentense: str) -> int:
    """
    Count Alphabets
    """
    alpha_chars = list(filter(lambda ch: ch.isalpha(), sentense))
    return len(alpha_chars)


class TestCountAlphabets(unittest.TestCase):
    """
    Test count alphabets algorithm
    """
    def test_count_alphabets(self) -> None:
        """
        Default implementation using isalpha
        """
        self.assertEqual(count_alphabets("#aBdj12C"), 5)
        self.assertEqual(count_alphabets("123 !@#$"), 0)
        self.assertEqual(count_alphabets("     "), 0)
        self.assertEqual(count_alphabets("Ran 3 tests in 0.000s"), 11)


if __name__ == "__main__":
    unittest.main()
