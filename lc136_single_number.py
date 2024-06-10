"""
Given a non-empty array of integers nums, 
    every element appears twice except for one. 
    Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1
 

Constraints:

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.
"""
import unittest

def single_number_using_xor(nums: list[int]) -> int:
    """
    Returns the single number in the list.

    Algorithm used: XOR
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    result = 0
    for num in nums:
        result ^= num
    return result


def single_number_using_two_pointers(nums: list[int]) -> int:
    """
    Returns the single number in the list.

    Algorithm used: Loop
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if len(nums) == 1:
        return nums[0]

    nums.sort()
    first, second = 0, 1
    while second < len(nums):
        if nums[first] == nums[second]:
            first += 2
            if second + 2 < len(nums):
                second += 2
            else:
                return nums[second+1]
            continue
        else:
            return nums[first]
    return 0


def single_number_brute_force(arr):
    """
    Returns the single number in the list.

    Algorithm used: Brute Force
    Time Complexity: O(n log n)
    Space Complexity: O(1)
    """
    arr.sort()
    for index in range(0, len(arr), 2):
        if index == len(arr)-1:
            return arr[index]
        if arr[index] != arr[index+1]:
            return arr[index]
    return 0



class TestSingleNumber(unittest.TestCase):
    """
        Test the `single_number` function
    """
    def test_single_number_xor(self):
        """
        Test the `single_number_using_xor` function
        """
        self.assertEqual(single_number_using_xor([2,2,1]), 1)
        self.assertEqual(single_number_using_xor([4,1,2,1,2]), 4)
        self.assertEqual(single_number_using_xor([1]), 1)

    def test_single_number_two_pointers(self):
        """
        Test the `single_number_using_two_pointers` function
        """
        self.assertEqual(single_number_using_two_pointers([2,2,1]), 1)
        self.assertEqual(single_number_using_two_pointers([4,1,2,1,2]), 4)
        self.assertEqual(single_number_using_two_pointers([1]), 1)

    def test_single_number_brute_force(self):
        """
        Test the `single_number_brute_force` function
        """
        self.assertEqual(single_number_brute_force([2,2,1]), 1)
        self.assertEqual(single_number_brute_force([4,1,2,1,2]), 4)
        self.assertEqual(single_number_brute_force([1]), 1)


if __name__ == "__main__":
    unittest.main()
