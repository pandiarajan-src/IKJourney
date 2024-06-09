"""
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. 
The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.
Note that s may contain leading or trailing spaces or multiple spaces between two words. 
The returned string should only have a single space separating the words. 
Do not include any extra spaces.

 
Example 1:
Input: s = "the sky is blue"
Output: "blue is sky the"

Example 2:
Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.

Example 3:
Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between 
    words to a single space in the reversed string.
 

Constraints:

1 <= s.length <= 104
s contains English letters (upper-case and lower-case), digits, and spaces ' '.
There is at least one word in s.
 

Follow-up: If the string data type is mutable in your language, 
    can you solve it in-place with O(1) extra space?
"""

import unittest

def reverse_words_in_string(sentense: str) -> str:
    """
        Reverse the word of the string in pythonic way
        Time Complexity: O(n), 
            where n is the length of the input string. 
            This is because the function iterates through the string 
            once to split it into words and then again to reverse the list of words.
        Space complexity: O(n), 
            where n is the length of the input string. 
            This is because the function creates a new list of words, 
            which can be up to n characters long.
    """
    sentense = sentense.strip()
    word_list = [word for word in sentense.split(" ") if len(word.strip()) > 0]
    return " ".join(reversed(word_list))

def reverse_words_in_string_using_dequeue(sentense: str) -> str:
    """
        Reverse the word of using dequeue
        Time Complexity: O(n), 
            where n is the length of the input string. 
            This is because the function iterates through 
            the string once to split it into words and then again to reverse the list of words.
        Space Complexity: O(n), 
            where n is the length of the input string. 
            This is because the function creates a new list of words, 
            which can be up to n characters long
    """
    sentense = sentense.strip()
    dequeue = list()
    search_start = sentense.find(" ", 0, len(sentense) - 1)
    prev_search_end = 0
    while  search_start != -1:
        item = sentense[prev_search_end:search_start].strip()
        if len(item) > 0:
            dequeue.insert(0, item)
        prev_search_end = search_start + 1
        search_start = sentense.find(" ", prev_search_end, len(sentense) - 1)

    last_word = sentense[prev_search_end:len(sentense)].strip()
    if len(last_word) > 0:
        dequeue.insert(0, last_word)

    return " ".join(dequeue)



class TestReverseWordInAString(unittest.TestCase):
    """
        Unit test for Test ReveseWord in a string
    """
    def test_reverse_word_in_string(self) -> None:
        """
        test method test_reverse_word_in_string
        """
        self.assertEqual(reverse_words_in_string("the sky is blue"), "blue is sky the")
        self.assertEqual(reverse_words_in_string("  hello world  "), "world hello")
        self.assertEqual(reverse_words_in_string("a good   example"), "example good a")
        self.assertEqual(reverse_words_in_string("hi"), "hi")
        self.assertEqual(reverse_words_in_string(" "), "")
        self.assertEqual(reverse_words_in_string("   "), "")


    def test_reverse_words_in_string_using_dequeue(self) -> None:
        """
        test method test_reverse_word_in_string
        """
        self.assertEqual(
            reverse_words_in_string_using_dequeue("the sky is blue"), "blue is sky the"
            )
        self.assertEqual(
            reverse_words_in_string_using_dequeue("  hello world  "), "world hello"
            )
        self.assertEqual(
            reverse_words_in_string_using_dequeue("a good   example"), "example good a"
            )
        self.assertEqual(reverse_words_in_string_using_dequeue("hi"), "hi")
        self.assertEqual(reverse_words_in_string_using_dequeue(" "), "")
        self.assertEqual(reverse_words_in_string_using_dequeue("    "), "")        


if __name__ == "__main__":
    unittest.main()
