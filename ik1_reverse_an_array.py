"""
Reverse An Array
Reverse a given list of numbers.

Example One
input: [50, 35, 78, 66, 17]
Output: [17, 66, 78, 35, 50]

Example Two
input: [50, 40, 30, 20]
Output: [20, 30, 40, 50]

Notes
=====
Modify the input array in-place and return the modified array.
Constraints:

1 <= size of the input array <= 106
0 <= any element of the input array <= 106
"""

import unittest

def reverse_array(nums: list[int]) -> list[int]:
    """
    Args:
     nums(list_int32)
    Returns:
     list_int32
    """
    # Option #1
    # One line built in solution
    # nums.reverse()

    # Option #2
    # Using slicing
    # nums = nums[::-1]

    # Option #3
    # Using default brute force technique with for
    # result = []
    # for index in range(len(nums)-1, -1, -1):
    #     result.append(nums[index])
    # nums = result

    # Optoin #4
    # Using for loop but with reversed index
    # nums = [num for num in reversed(nums)]
    nums = [reversed(nums)]

    return nums

class TestReverseArray(unittest.TestCase):
    """Tesing Reverse array method implementation"""
    def test_reverse_array(self):
        """Test reverse array method implementatio both positive and negative cases"""
        self.assertEqual(reverse_array([50, 40, 30, 20]), [20, 30, 40, 50])
        self.assertListEqual(reverse_array([50, 35, 78, 66, 17]), [17, 66, 78, 35, 50])
        self.assertListEqual(reverse_array([11]), [11])
        self.assertListEqual(reverse_array([]), [])


if __name__ == "__main__":
    unittest.main()
