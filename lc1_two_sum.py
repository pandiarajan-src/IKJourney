"""
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

"""

import unittest


def two_sum_brute_force(nums: list[int], target: int) -> tuple[int, int]:
    """
    Returns the indices of two numbers in the list that sum up to the target.

    This function takes in a list of integers `nums` and an integer `target`,
    and returns a tuple of two indices `i` and `j` such that `nums[i] + nums[j] == target`. 
    If no such indices exist, it returns `-1, -1`.

    Algorithm Used: Brute Force
    Time Complexity: O(n^2)
        because it needs to traverse each element of the list nums twice
    Space Complexity: O(1)
        because it only uses a constant amount of space to store the indices i and j
        and the temporary variables i_num and j_num.
    """
    for i, i_num in enumerate(nums):
        for j, j_num in enumerate(nums[i+1:], start=i+1):
            if i_num + j_num == target:
                return i, j
    return -1, -1


def two_sum_using_two_pointers(nums: list[int], target: int) -> tuple[int, int]:
    """Two sum using two pointers
    Algorithm Used: Two Pointers
    Time Complexity: O(n)
        because it needs to traverse the list only once
    Space Complexity: O(1)
        because it only uses a constant amount of space to store the indices i and j
    """
    # Sort the number before proceed with the two pointers algorithm
    nums.sort()

    left, right = 0, len(nums) - 1
    while left < right:
        if nums[left] + nums[right] > target:
            right -= 1
        elif nums[left] + nums[right] < target:
            left += 1
        else:
            return left, right
    return -1, -1


class TestTwoSumBruteForce(unittest.TestCase):
    """
        Test case for the `two sum` problem.
        This test case verifies the behavior of the `two sum` problem
        by checking the correctness of its output for various input scenarios.

        The function takes in a list of integers `nums` and a target integer `target`,
        and returns a tuple of two indices `i` and `j` such that `nums[i] + nums[j] == target`.
        If no such indices exist, it returns `-1, -1`.

        The test cases cover the following scenarios:

        1. Test case 1: Two unique indices with a valid sum.
           - Input: `nums = [2, 7, 11, 15]`, `target = 9`
           - Expected output: `(0, 1)`

        2. Test case 2: Two unique indices with an invalid sum.
           - Input: `nums = [2, 7, 11, 15]`, `target = 17`
           - Expected output: `(-1, -1)`

        3. Test case 3: No indices with a valid sum.
           - Input: `nums = [2, 7, 11, 15]`, `target = 30`
           - Expected output: `(-1, -1)`

        4. Test case 4: Empty list.
           - Input: `nums = []`, `target = 9`
           - Expected output: `(-1, -1)`

        5. Test case 5: Single element list.
           - Input: `nums = [5]`, `target = 10`
           - Expected output: `(-1, -1)`

        6. Test case 6: List with duplicate elements.
           - Input: `nums = [2, 7, 11, 11, 15]`, `target = 16`
           - Expected output: `(1, 4)`

        7. Test case 7: List with negative numbers.
           - Input: `nums = [-1, 0, 1, 2, 3]`, `target = 0`
           - Expected output: `(0, 4)`    
    """

    def test_two_sum_brute_force(self) -> None:
        """
        This test case is part of the unit tests for the `two_sum_brute_force` function.
        """
        # Test case 1: Two unique indices with a valid sum
        self.assertTupleEqual(two_sum_brute_force([2, 7, 11, 15], 9), (0, 1))

        # Test case 2: Two unique indices with an invalid sum
        self.assertTupleEqual(two_sum_brute_force([2, 7, 11, 15], 17), (0, 3))

        # Test case 3: No indices with a valid sum
        self.assertTupleEqual(two_sum_brute_force(
            [2, 7, 11, 15], 30), (-1, -1))

        # Test case 4: Empty list
        self.assertTupleEqual(two_sum_brute_force([], 9), (-1, -1))

        # Test case 5: Single element list
        self.assertTupleEqual(two_sum_brute_force([5], 10), (-1, -1))

        # Test case 6: List with duplicate elements
        self.assertTupleEqual(two_sum_brute_force(
            [2, 7, 11, 11, 15], 16), (-1, -1))

        # Test case 7: List with negative numbers
        self.assertTupleEqual(two_sum_brute_force([-1, 0, 1, 2, 3], 0), (0, 2))

    def test_two_sum_two_pointers(self) -> None:
        """
            This test case is part of the unit tests for the `two_sum_using_two_pointers` function.
        """

        # Test case 1: Two unique indices with a valid sum
        self.assertTupleEqual(two_sum_using_two_pointers([2, 7, 11, 15], 9), (0, 1))

        # Test case 2: Two unique indices with an invalid sum
        self.assertTupleEqual(two_sum_using_two_pointers([2, 7, 11, 15], 17), (0, 3))

        # Test case 3: No indices with a valid sum
        self.assertTupleEqual(two_sum_using_two_pointers(
            [2, 7, 11, 15], 30), (-1, -1))

        # Test case 4: Empty list
        self.assertTupleEqual(two_sum_using_two_pointers([], 9), (-1, -1))

        # Test case 5: Single element list
        self.assertTupleEqual(two_sum_using_two_pointers([5], 10), (-1, -1))

        # Test case 6: List with duplicate elements
        self.assertTupleEqual(two_sum_using_two_pointers(
            [2, 7, 11, 11, 15], 16), (-1, -1))

        # Test case 7: List with negative numbers
        self.assertTupleEqual(two_sum_using_two_pointers([-1, 0, 1, 2, 3], 0), (0, 2))

if __name__ == '__main__':
    unittest.main()
