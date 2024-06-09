"""
Given a string s, 
    return the string after replacing every uppercase letter with the same lowercase letter.

 

Example 1:
Input: s = "Hello"
Output: "hello"

Example 2:
Input: s = "here"
Output: "here"

Example 3:
Input: s = "LOVELY"
Output: "lovely"
 

Constraints:

1 <= s.length <= 100
s consists of printable ASCII characters.
"""
import unittest

def convert_to_lowercase(s: str) -> str:
    """
    Convert a given string in to lower case
    """
    return s.lower()


def to_lower_case_impl(s: str) -> str:
    """
    Do Python implementation of isupper and tolower.

    Args:
        s (str): The input string.

    Returns:
        str: The input string with all uppercase letters converted to lowercase.
    """
    def is_upper_impl(x: str) -> bool:
        """Check if a character is an uppercase letter."""
        return 'A' <= x <= 'Z'

    def to_lower_impl(x: str) -> str:
        """Convert an uppercase letter to lowercase."""
        return chr(ord(x) | 32)

    return ''.join(to_lower_impl(x) if is_upper_impl(x) else x for x in s)




class TestConvertToLowercase(unittest.TestCase):
    """
    Covert lower case test
    """
    def test_convert_to_lowercase(self):
        """
        Test convert_to_lowercase
        """
        self.assertEqual(convert_to_lowercase("Hello"), "hello")
        self.assertEqual(convert_to_lowercase("HELLO"), "hello")
        self.assertEqual(convert_to_lowercase("HELLO WORLD"), "hello world")
        self.assertEqual(convert_to_lowercase(""), "")
        self.assertEqual(convert_to_lowercase("123"), "123")


    def test_convert_to_lowercase_by_own_impl(self):
        """
        Test convert_to_lowercase
        """
        self.assertEqual(to_lower_case_impl("Hello"), "hello")
        self.assertEqual(to_lower_case_impl("HELLO"), "hello")
        self.assertEqual(to_lower_case_impl("HELLO WORLD"), "hello world")
        self.assertEqual(to_lower_case_impl(""), "")
        self.assertEqual(to_lower_case_impl("123"), "123")


if __name__ == "__main__":
    unittest.main()
