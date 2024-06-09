"""
Given an integer array nums, 
    return true if any value appears at least twice in the array, 
    and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
 
Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""

import unittest

def contains_duplication_builtin_set(nums: list[int]) -> bool:
    """
        Check if the given list contains any duplicate elements.
        Time Complexity: O(n) 
            This is because the method converts the list to a set, 
            which is an unordered collection of unique elements. 
            Converting a list to a set takes linear time in the size of the list.
        Space Compleixty: O(n)
            This is because the method creates a new set, 
            which requires additional memory to store the unique elements.
    """
    nums_set = set(nums)
    if len(nums) == len(nums_set):
        return False
    return True


def contains_duplication_bruteforce(nums: list[int]) -> bool:
    """
        Check if the given list contains any duplicate elements.
        Time complexity: O(n^2)
            This is because the method uses nested loops 
            to compare each element with every other element in the list, 
            resulting in a quadratic time complexity.
        Space complexity: O(1), 
            since it does not use any additional 
            data structures or memory beyond the input list itself.
    """
    for i, num in enumerate(nums):
        if num in nums[i+1:]:
            return True
    return False


class TestContainsDuplication(unittest.TestCase):
    """
        Check if the given list contains any duplicate elements using different test methods.
    """
    def test_contains_duplication(self):
        """
            Check if the given list contains any duplicate elements.
        """
        # Test case: List with duplicate elements
        self.assertTrue(contains_duplication_builtin_set([1, 2, 3, 1]))

        # Test case: List with no duplicate elements
        self.assertFalse(contains_duplication_builtin_set([1, 2, 3, 4]))

        # Test case: Empty list
        self.assertFalse(contains_duplication_builtin_set([]))

        # Test case: Empty list
        self.assertTrue(contains_duplication_builtin_set([1,1,1,3,3,4,3,2,4,2]))

        # Test case: List with negative numbers
        self.assertTrue(contains_duplication_builtin_set([-1, -1, -2, -1, -2, -3]))

        # Test case: List with large numbers
        self.assertTrue(contains_duplication_builtin_set([1000, 1000, 2000, 2000, 3000, 3000]))

        # Test case: List with one element
        self.assertFalse(contains_duplication_builtin_set([1]))

        # Test case: List with all elements the same
        self.assertTrue(contains_duplication_builtin_set([1, 1, 1, 1, 1, 1]))


    def test_contains_duplication_bruteforce(self):
        """
            Check if the given list contains any duplicate elements.
        """
        # Test case: List with duplicate elements
        self.assertTrue(contains_duplication_bruteforce([1, 2, 3, 1]))

        # Test case: List with no duplicate elements
        self.assertFalse(contains_duplication_bruteforce([1, 2, 3, 4]))

        # Test case: Empty list
        self.assertFalse(contains_duplication_bruteforce([]))

        # Test case: Empty list
        self.assertTrue(contains_duplication_bruteforce([1,1,1,3,3,4,3,2,4,2]))

        # Test case: List with negative numbers
        self.assertTrue(contains_duplication_bruteforce([-1, -1, -2, -1, -2, -3]))

        # Test case: List with large numbers
        self.assertTrue(contains_duplication_bruteforce([1000, 1000, 2000, 2000, 3000, 3000]))

        # Test case: List with one element
        self.assertFalse(contains_duplication_bruteforce([1]))

        # Test case: List with all elements the same
        self.assertTrue(contains_duplication_bruteforce([1, 1, 1, 1, 1, 1]))


if __name__ == "__main__":
    unittest.main()
