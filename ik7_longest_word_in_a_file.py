"""
    Write a Python program to find the longest word in a file.
"""
import unittest
import os

def longest_word_in_file(file_path: str) -> str:
    """
        Find the longest word in a file
    """
    with open(file_path, "r", encoding="utf-8") as file:
        words = file.read().split()
        # return max(words, key=len) # Option 1
        return sorted(words, key=len, reverse=True)[0] # Option 2


class TestLongestWordInFile(unittest.TestCase):
    """
        Test longest scenarios in a file.
    """

    def setUp(self) -> None:
        """
        Set up the test case by creating a test file.
        """
        self.file_path = "test_file.txt"
        with open(self.file_path, "w", encoding="utf-8") as file:
            file.write("hi hello world, how are you doing? \
                       longest is the longest word in this file")

    def tearDown(self) -> None:
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_longest_word_in_file(self) -> None:
        """
            Test longest_word_in_file
        """
        self.assertEqual(longest_word_in_file(self.file_path), "longest")



if __name__ == "__main__":
    unittest.main()
