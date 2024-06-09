"""
Intersection Of Two Arrays
Given two lists of numbers, find their intersection.

Example One
{
"a": [4, 2, 2, 3, 1],
"b": [2, 2, 2, 3, 3]
}
Output:
[2, 2, 3]

Example Two
{
"a": [6, 2, 4],
"b": [1, 5, 3, 7]
}
Output:
[]
Notes

The order of elements in the output list does not matter.
The frequency of any number in the intersection 
    must be equal to the minimum of the frequency of that number in both the given lists.

Constraints:
    1 <= size of the input lists <= 105
    -106 <= any element of the input lists <= 106
"""
import unittest

def intersection_of_arrays(nums1: list[int], nums2: list[int]) -> list[int]:
    """
        By list comprehension
    """
    result = []
    for x in nums1:
        if (x not in result) and (x in nums2):
            x_count_in_nums1 = nums1.count(x)
            x_count_in_nums2 = nums2.count(x)
            times = min(x_count_in_nums1, x_count_in_nums2)
            result.extend([x] * times)
    return result


class TestIntersectionOfArrays(unittest.TestCase):
    """
    Test class
    """
    def test_intersection_of_arrays(self) -> None:
        """
            intersection_of_arrays_by_list_comprehension
        """
        self.assertEqual(intersection_of_arrays(
            [4, 2, 2, 3, 1],[2, 2, 2, 3, 3]), [2, 2, 3]
            )
        self.assertEqual(intersection_of_arrays(
            [6, 2, 4],[1, 5, 3, 7]), []
            )

if __name__ == "__main__":
    unittest.main()
