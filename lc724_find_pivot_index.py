"""
Given an array of integers nums, calculate the pivot index of this array.
The pivot index is the index where 
    the sum of all the numbers strictly to the left of the index 
    is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, 
    then the left sum is 0 because there are no elements to the left. 
    This also applies to the right edge of the array.
    Return the leftmost pivot index. 

If no such index exists, return -1.

Example 1:
Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11

Example 2:
Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.
Example 3:

Input: nums = [2,1,-1]
Output: 0
Explanation:
The pivot index is 0.
Left sum = 0 (no elements to the left of index 0)
Right sum = nums[1] + nums[2] = 1 + -1 = 0
 
Constraints:
1 <= nums.length <= 104
-1000 <= nums[i] <= 1000
 
Note: This question is the same as 1991: 
    https://leetcode.com/problems/find-the-middle-index-in-array/
"""

import unittest

def pivot_index_by_bruteforces(nums: list[int]) -> int:
    """
        Brute Force Solution
    """
    for index in range(0, len(nums)):
        left_sum = sum(nums[:index])
        right_sum = sum(nums[index+1:])
        if left_sum == right_sum:
            return index

    return -1


# better solution
def pivot_index_by_totality_sum(nums: list[int]) -> int:
    """
        Find the sum of entire list and subtract left sum value until find an index
    """
    summation = sum(nums)
    left_sum = 0
    for i, x in enumerate(nums):
        if left_sum == (summation - left_sum - x):
            return i
        left_sum += x
    return -1




class TestPivotIndex(unittest.TestCase):
    """
       Test the `pivot_index_of an array` problem.
    """
    def test_pivot_index_by_bruteforces(self):
        """
            This function tests the `pivot_index_by_bruteforces` function
            by asserting the expected output against the actual output.
            It tests various input scenarios and verifies that the function
            returns the correct pivot index.
        """
        self.assertEqual(pivot_index_by_bruteforces([1, 7, 3, 6, 5, 6]), 3)
        self.assertEqual(pivot_index_by_bruteforces([1, 2, 3]), -1)
        self.assertEqual(pivot_index_by_bruteforces([2, 1, -1]), 0)
        self.assertEqual(pivot_index_by_bruteforces([]), -1)
        self.assertEqual(pivot_index_by_bruteforces([1]), 0)
        self.assertEqual(pivot_index_by_bruteforces([1, -1, 1]), 0)


    def test_pivot_index_by_totality_sum(self):
        """
            This function tests the `pivot_index_by_totality_sum` function
            by asserting the expected output against the actual output.
            It tests various input scenarios and verifies that the function
            returns the correct pivot index.
        """
        self.assertEqual(pivot_index_by_totality_sum([1, 7, 3, 6, 5, 6]), 3)
        self.assertEqual(pivot_index_by_totality_sum([1, 2, 3]), -1)
        self.assertEqual(pivot_index_by_totality_sum([2, 1, -1]), 0)
        self.assertEqual(pivot_index_by_totality_sum([]), -1)
        self.assertEqual(pivot_index_by_totality_sum([1]), 0)
        self.assertEqual(pivot_index_by_totality_sum([1, -1, 1]), 0)


if __name__ == '__main__':
    unittest.main()
