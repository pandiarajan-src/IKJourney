"""
Given an integer array nums sorted in non-decreasing order, 
    return an array of the squares of each number sorted in non-decreasing order.

Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Example 2:
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]

Constraints:
1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.
 

Follow up: Squaring each element and sorting the new array is very trivial, 
    could you find an O(n) solution using a different approach?
"""

import unittest

def sorted_squares_brute_force(nums: list[int]) -> list[int]:
    """
        Time Complexity: O(n log n)
        Space Complexity: O(n)
    """
    result = []
    for num in nums:
        result.append(num * num)
    result.sort()
    return result


def sorted_squares_map(nums: list[int]) -> list[int]:
    """
        Time Complexity: O(n log n)
        Space Complexity: O(n)
    """
    return sorted(list(map(lambda x: x * x, nums)))


def sorted_squares_using_two_pointers(nums: list[int]) -> list[int]:
    """
        Time Complexity: O(n)
        Space Complexity: O(1)
    """
    left, right = 0, len(nums) - 1
    result = [0] * len(nums)
    for i in range(len(nums) - 1, -1, -1):
        if abs(nums[left]) > abs(nums[right]):
            result[i] = nums[left] * nums[left]
            left += 1
        else:
            result[i] = nums[right] * nums[right]
            right -= 1
    return result


class TestSquaresOfSortedArray(unittest.TestCase):
    """
        Test Squares of a sorted array problem
    """
    def test_squares_of_sorted_array_brute_force(self):
        """
            Test sorted_squares_brute_force method
        """
        self.assertEqual(sorted_squares_brute_force([-4,-1,0,3,10]), [0,1,9,16,100])
        self.assertEqual(sorted_squares_brute_force([-7,-3,2,3,11]), [4,9,9,49,121])

    def test_squares_of_sorted_array_map(self):
        """
            Test sorted_squares_brute_force method
        """
        self.assertEqual(sorted_squares_map([-4,-1,0,3,10]), [0,1,9,16,100])
        self.assertEqual(sorted_squares_map([-7,-3,2,3,11]), [4,9,9,49,121])


    def test_sorted_squares_using_two_pointers(self):
        """
            Test sorted_squares_using_two_pointers method
        """
        self.assertEqual(sorted_squares_using_two_pointers([-4,-1,0,3,10]), [0,1,9,16,100])
        self.assertEqual(sorted_squares_using_two_pointers([-7,-3,2,3,11]), [4,9,9,49,121])


if __name__ == "__main__":
    unittest.main()