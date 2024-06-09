"""
Given two strings needle and haystack, 
    return the index of the first occurrence of needle in haystack,
    or -1 if needle is not part of haystack.
 

Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.


Example 2:
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

Constraints:
1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.
"""

import unittest

def find_index_by_default_str_find(haystack: str, needle: str) -> int:
    """
    Using built-in function, find returns -1 if not found
        Time Complexity:O(n), where n is the length of the haystack
        Space Complexity: O(1), as it only uses constant space to store the indices
    """
    return haystack.find(needle)


# word search by sliding window
def find_index_from_str(haystack: str, needle: str) -> int:
    """
        Using search mechanism with for a word by word
        Time Complexity: O(n*m),
                where n is the length of the haystack and m is the length of the needle.
        Space Complexity: O(1),
                s it only uses constant space to store the indices.
    """
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i + len(needle)] == needle:
            return i

    return -1


# sliding window
def find_index_from_str_using_sliding_window(haystack: str, needle: str) -> int:
    """
    Using sliding window
    Algorithm Used: Sliding Window
    Time Complexity: O(n*m), 
        where n is the length of the haystack and m is the length of the needle.
    Space Complexity: O(1),
        as it only uses constant space to store the indices
    """
    n = len(haystack)
    m = len(needle)
    for window_start in range(n - m + 1):
        for find_str_index in range(m):
            if haystack[window_start + find_str_index] != needle[find_str_index]:
                break
            if find_str_index == m - 1:
                return window_start
    return -1


class TestFindIndex(unittest.TestCase):
    """
    Find the occurence of a char or string (child) in a parent string
    """
    def test_find_index_by_default_str_find(self) -> None:
        """
        Testing method find_index_by_default_str_find
        """
        self.assertEqual(find_index_by_default_str_find("sadbutsad", "sad"), 0)
        self.assertEqual(find_index_by_default_str_find("sadbutsad", "but"), 3)
        self.assertEqual(find_index_by_default_str_find("leetcode", "leet0"), -1)
        self.assertEqual(find_index_by_default_str_find("interview", "e"),3)
        self.assertEqual(find_index_by_default_str_find("kick start", "start"), 5)
        self.assertEqual(find_index_by_default_str_find("kickstart", "n"), -1)
        self.assertEqual(find_index_by_default_str_find("kickstart", " "), -1)
        self.assertEqual(find_index_by_default_str_find("    ", "n"), -1)


    def test_find_index_from_str(self) -> None:
        """
        Testing method find_index_by_default_str_find
        """
        self.assertEqual(find_index_from_str("sadbutsad", "sad"), 0)
        self.assertEqual(find_index_from_str("sadbutsad", "but"), 3)
        self.assertEqual(find_index_from_str("leetcode", "leet0"), -1)
        self.assertEqual(find_index_from_str("interview", "e"),3)
        self.assertEqual(find_index_from_str("kick start", "start"), 5)
        self.assertEqual(find_index_from_str("kickstart", "n"), -1)
        self.assertEqual(find_index_from_str("kickstart", " "), -1)
        self.assertEqual(find_index_from_str("    ", "n"), -1)

    def test_find_index_from_str_using_sliding_window(self) -> None:
        """
        Testing method find_index_by_default_str_find
        """
        self.assertEqual(find_index_from_str_using_sliding_window("sadbutsad", "sad"), 0)
        self.assertEqual(find_index_from_str_using_sliding_window("sadbutsad", "but"), 3)
        self.assertEqual(find_index_from_str_using_sliding_window("leetcode", "leet0"), -1)
        self.assertEqual(find_index_from_str_using_sliding_window("interview", "e"),3)
        self.assertEqual(find_index_from_str_using_sliding_window("kick start", "start"), 5)
        self.assertEqual(find_index_from_str_using_sliding_window("kickstart", "n"), -1)
        self.assertEqual(find_index_from_str_using_sliding_window("kickstart", " "), -1)
        self.assertEqual(find_index_from_str_using_sliding_window("    ", "n"), -1)

if __name__ == "__main__":
    unittest.main()
