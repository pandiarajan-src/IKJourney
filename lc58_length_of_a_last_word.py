"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal 
substring
 consisting of non-space characters only.

 

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
 

Constraints:

1 <= s.length <= 104
s consists of only English letters and spaces ' '.
There will be at least one word in s.
"""

import unittest

def length_of_last_word_default(s: str) -> int:
    """
        By default implementation
        Time complexity: O(n), where n is the length of the input string s. 
            This is because the algorithm needs to iterate through the entire string
        Space Complexity: O(n) as well, 
            because it creates a new string by stripping whitespace 
            and splitting the original string into words
    """
    return len(s.strip().split(" ")[-1])


def length_of_last_word_by_reverse_search(s:str) -> int:
    """
        By reverse search
        Time complexity: O(n), where n is the length of the input string s. 
            This is because the algorithm needs to iterate through the entire string
        Space Complexity: O(1), 
            because it does not create any additional data structures 
            that scale with the input size. 
            It only uses a fixed amount of space to store variables.
    """
    s = s.strip()
    for i in range(len(s)-1, 0, -1):
        if s[i] == " ":
            return len(s[i+1:])
    return len(s)


class TestLengthOfLastWord(unittest.TestCase):
    """
        function correctly calculates the length of the last word in the string "Hello World".
        It asserts that the function returns the value 5, 
        which is the length of the last word "World".
    """
    def test_length_of_lastword_default(self):
        """
        Test the `length_of_last_word_default` function by asserting
        """
        self.assertEqual(length_of_last_word_default("Hello World"), 5)
        self.assertEqual(length_of_last_word_default("   fly me   to   the moon  "), 4)
        self.assertEqual(length_of_last_word_default("luffy is still joyboy"), 6)
        self.assertEqual(length_of_last_word_default("     "), 0)
        self.assertEqual(length_of_last_word_default(""), 0)
        self.assertEqual(length_of_last_word_default("a"), 1)
        self.assertEqual(length_of_last_word_default("hi"), 2)


    def test_length_of_lastword_by_reverse_search(self):
        """
        Test the `length_of_last_word_default` function by asserting
        """
        self.assertEqual(length_of_last_word_by_reverse_search("Hello World"), 5)
        self.assertEqual(length_of_last_word_by_reverse_search("   fly me   to   the moon  "), 4)
        self.assertEqual(length_of_last_word_by_reverse_search("luffy is still joyboy"), 6)
        self.assertEqual(length_of_last_word_by_reverse_search("     "), 0)
        self.assertEqual(length_of_last_word_by_reverse_search(""), 0)
        self.assertEqual(length_of_last_word_default("a"), 1)
        self.assertEqual(length_of_last_word_default("hi"), 2)



if __name__ == "__main__":
    unittest.main()
