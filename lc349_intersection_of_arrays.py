"""
349. Intersection of Two Arrays
Easy

Given two integer arrays nums1 and nums2, return an array of their intersection
. Each element in the result must be unique and you may return the result in any order.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.

Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
"""

import unittest

def intersection_by_bruteforce(nums1: list[int], nums2: list[int]) -> list[int]:
    """
        Traverse both arrays
        The time complexity of this function is O(n^2) 
            because it needs to traverse both nums1 and nums2 to find the intersection. 
        The space complexity is O(n) 
            because the size of the result list can grow up to the size 
            of the smaller of nums1 and nums2.
    """
    result = []

    # input validation
    if nums1 is None or nums2 is None:
        return result

    # traverse both arrays
    for num in nums1:
        if num in nums2 and num not in result:
            result.append(num)
    return result

def intersection_by_list_comprehension(nums1: list[int], nums2: list[int]) -> list[int]:
    """
        Using list comprehension
    """
    result = set(x for x in nums1 if x in nums2)
    return list(sorted(result))

def intersection_by_set(nums1: list[int], nums2: list[int]) -> list[int]:
    """
        Using set
        The time complexity of the intersection_by_set function is O(n + m), 
            where n is the length of nums1 and m is the length of nums2. 
            This is because creating a set from a list is O(n) 
            and finding the intersection of two sets is O(m).

        The space complexity of the intersection_by_set function is O(n + m), 
        where n is the length of nums1 and m is the length of nums2. 
        This is because creating a set from a list is O(n) 
        and finding the intersection of two sets is O(m). 
        The result list is O(k), where k is the size of the intersection.

        Note that the time and space complexity can be improved to O(n + m) and O(k) 
        respectively if we use a hash table instead of a set.
    """
    if not nums1 or not nums2:
        return []
    set1 = set(nums1)
    set2 = set(nums2)
    return list(sorted(set1.intersection(set2)))

def intersection_by_hash(nums1: list[int], nums2: list[int]) -> list[int]:
    """
        Using hash table
        The time complexity of the intersection_by_hash function is O(n + m), 
            where n is the length of nums1 and m is the length of nums2. 
            This is because creating a hash table from a list is O(n) 
            and finding the intersection of two hash tables is O(m).

        The space complexity of the intersection_by_hash function is O(n + m), 
        where n is the length of nums1 and m is the length of nums2. 
        This is because creating a hash table from a list is O(n) 
        and finding the intersection of two hash tables is O(m). 
        The result list is O(k), where k is the size of the intersection.
    """
    if not nums1 or not nums2:
        return []
    hash_table = {}
    for num in nums1:
        hash_table[num] = True
    result = []
    for num in nums2:
        if num in hash_table and num not in result:
            result.append(num)
    return sorted(result) # hash table doesn't keep the order

def intersection_by_two_pointers(nums1: list[int], nums2: list[int]) -> list[int]:
    """
        Using Two pointers, 
        one pointer to one list and another pointer to another list 
    """
    result = []

    # Input validation
    if not nums1 or not nums2:
        return result

    # sort the list before using two pointers
    nums1.sort()
    nums2.sort()

    # two pointers
    i, j = 0, 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            if not result or result[-1] != nums1[i]:
                result.append(nums1[i])
            i += 1
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            j += 1

    return result

class TestIntersectionOfArrays(unittest.TestCase):
    """
        Test the intersection of arrays problem.

        This function tests the intersection of arrays problem with different input
        combinations and asserts the expected result.
    """
    def test_intersection_of_arrays_by_set(self):
        """
            This function test intersection of arrays using set logic
        """
        self.assertEqual(intersection_by_set([1, 2, 2, 1], [2, 2]), [2])
        self.assertEqual(intersection_by_set([4, 9, 5], [9, 4, 9, 8, 4]), [4, 9])
        self.assertEqual(intersection_by_set([], [1, 2, 3]), [])
        self.assertEqual(intersection_by_set([1, 2, 3], []), [])
        self.assertEqual(intersection_by_set([1, 2, 3], [4, 5, 6]), [])
        self.assertEqual(intersection_by_set([1, 2, 3], [1, 2, 3]), [1, 2, 3])

    def test_intersection_of_arrays_by_bruteforce(self):
        """
            This function test intersection of arrays with brute force
        """
        self.assertEqual(intersection_by_bruteforce([1, 2, 2, 1], [2, 2]), [2])
        self.assertEqual(intersection_by_bruteforce([4, 9, 5], [9, 4, 9, 8, 4]), [4, 9])
        self.assertEqual(intersection_by_bruteforce([], [1, 2, 3]), [])
        self.assertEqual(intersection_by_bruteforce([1, 2, 3], []), [])
        self.assertEqual(intersection_by_bruteforce([1, 2, 3], [4, 5, 6]), [])
        self.assertEqual(intersection_by_bruteforce([1, 2, 3], [1, 2, 3]), [1, 2, 3])

    def test_intersection_of_arrays_by_two_pointers(self):
        """
            This function test intersection of arrays using two pointers logic
        """
        self.assertEqual(intersection_by_two_pointers([1, 2, 2, 1], [2, 2]), [2])
        self.assertEqual(intersection_by_two_pointers([4, 9, 5], [9, 4, 9, 8, 4]), [4, 9])
        self.assertEqual(intersection_by_two_pointers([], [1, 2, 3]), [])
        self.assertEqual(intersection_by_two_pointers([1, 2, 3], []), [])
        self.assertEqual(intersection_by_two_pointers([1, 2, 3], [4, 5, 6]), [])
        self.assertEqual(intersection_by_two_pointers([1, 2, 3], [1, 2, 3]), [1, 2, 3])

    def test_intersection_of_arrays_by_has_table(self):
        """
            This function test intersection of arrays using hash table logic
        """
        self.assertEqual(intersection_by_hash([1, 2, 2, 1], [2, 2]), [2])
        self.assertEqual(intersection_by_hash([4, 9, 5], [9, 4, 9, 8, 4]), [4, 9])
        self.assertEqual(intersection_by_hash([], [1, 2, 3]), [])
        self.assertEqual(intersection_by_hash([1, 2, 3], []), [])
        self.assertEqual(intersection_by_hash([1, 2, 3], [4, 5, 6]), [])
        self.assertEqual(intersection_by_hash([1, 2, 3], [1, 2, 3]), [1, 2, 3])

    def test_intersection_of_arrays_by_list_comprehension(self):
        """
            This function test intersection of arrays using hash table logic
        """
        self.assertEqual(intersection_by_list_comprehension([1, 2, 2, 1], [2, 2]), [2])
        self.assertEqual(intersection_by_list_comprehension([4, 9, 5], [9, 4, 9, 8, 4]), [4, 9])
        self.assertEqual(intersection_by_list_comprehension([], [1, 2, 3]), [])
        self.assertEqual(intersection_by_list_comprehension([1, 2, 3], []), [])
        self.assertEqual(intersection_by_list_comprehension([1, 2, 3], [4, 5, 6]), [])
        self.assertEqual(intersection_by_list_comprehension([1, 2, 3], [1, 2, 3]), [1, 2, 3])

if __name__ == '__main__':
    unittest.main()
