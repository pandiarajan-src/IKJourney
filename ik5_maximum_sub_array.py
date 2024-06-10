"""
Maximum Sum Subarray

Given a list of integers, find the sum of a non-empty subarray that has the largest sum.

Example One
input: [2, -6, 3, 4, -5]
Output: 7

Example Two
input: [-7, -9, -3, -5]
Output:-3

Notes

A subarray is an array composed of a contiguous block of the original array's elements.

Constraints:
1 <= length of the given list <= 105
-104 <= elements of list <= 104
"""
import unittest

def maximum_subarray(nums: list[int]) -> int:
    """
        Time Complexity: O(n)
        Space Complexity: O(1)
    """
    max_sum = nums[0]
    current_sum = 0
    for num in nums:
        if current_sum < 0:
            current_sum = 0
        current_sum += num
        max_sum = max(max_sum, current_sum)
    return max_sum

class TestMaximumSubArray(unittest.TestCase):
    """
        Test case for the `maximum subarray` problem.
    """

    def test_maximum_subarray(self):
        """
            Test case for the `maximum subarray` problem.
        """
        self.assertEqual(maximum_subarray([2, -6, 3, 4, -5]), 7)
        self.assertEqual(maximum_subarray([-7, -9, -3, -5]), -3)

if __name__ == "__main__":
    unittest.main()