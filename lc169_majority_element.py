"""
Given na aray nums of size n, return the majority element.

    The majority element is the element that appears more than n/2 times. 
    You may assume that the majority element always exists ni the array.

Example 1:
Input: nums = (3,2,3] Output: 3

Example 2:
Input: nums = (2,2,1,1,1,2,21 Output: 2

Constraints:
• 12 nun. +%01
• -109<=nums[i]<=109
"""

import unittest
# import math


def majority_element_by_sorting(nums: list[int]) -> int:
    """
        Given an array nums of size n, return the majority element.
        Algorithm: Sorting
        Time Complexity: O(nlogn) to sort the object
        Space Complexity: O(1) - no new data structures are created
    """
    nums.sort()
    return nums[len(nums) // 2]


def majority_element_by_hashmap(nums: list[int]) -> int:
    """
        Given an array nums of size n, return the majority element.
        Algorithm:
        Time Complexity: O(n) 
            The method iterates over each element in the input array nums once. 
        Space Complexity: O(n)
            he size of the hash map is at most n (since there are n unique elements in the array),
    """
    hash_map = {}
    for num in nums:
        if num in hash_map:
            hash_map[num] += 1
        else:
            hash_map[num] = 1
    # for num, nums_count in hash_map.items():
    #     if nums_count >= math.floor(len(nums)/2):
    #         return num
    return max(hash_map, key=hash_map.get)


class TestMajorityElement(unittest.TestCase):
    """
        Test the `majority_element` function
    """
    def test_majority_element_by_sorting(self):
        """
        Test the `majority_element_by_sorting` function
        """
        self.assertEqual(majority_element_by_sorting([3, 2, 3]), 3)
        self.assertEqual(majority_element_by_sorting([2, 2, 1, 1, 1, 2, 2]), 2)


    def test_majority_element_by_hashmap(self):
        """
        Test the `majority_element_by_sorting` function
        """
        self.assertEqual(majority_element_by_hashmap([3, 2, 3]), 3)
        self.assertEqual(majority_element_by_hashmap([2, 2, 1, 1, 1, 2, 2]), 2)


if __name__ == "__main__":
    unittest.main()
