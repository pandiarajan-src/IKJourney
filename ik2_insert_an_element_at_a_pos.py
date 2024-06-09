"""
Insert An Element At A Specific Position In An Array
Given an array of numbers, insert a given element at the specified position in the array.

Example One
input:
{
"nums": [2, 4, 5, 6, -1],
"element": 3,
"position": 2
}
Output:
[2, 3, 4, 5, 6]

Example Two
input:
{
"nums": [70, 60, 50, -1],
"element": 40,
"position": 4
}
Output:
[70, 60, 50, 40]


Notes
=====
The last element of the array is -1 indicating a blank position.
The given position follows 1-based indexing.
Return the modified array.
Constraints:

2 <= size of the input array <= 106
0 <= elements of the array <= 106
1 <= position <= size of the input array
"""

import unittest

def insert_an_element_at_an_array_position(nums:list[int], pos:int, element:int) -> list[int]:
    """Insert an element at a given position in an array"""
    nums.insert(pos-1, element)
    nums.pop()
    return nums

class TestInsertAnElementAtAnArrayPosition(unittest.TestCase):
    """Test class for a method that insert an element at a given position in an array"""
    def test_insert_an_array_position(self) -> None:
        """Test class for a method that insert an element at a given position in an array"""
        self.assertEqual(
            insert_an_element_at_an_array_position(
                [2, 4, 5, 6, -1], 2, 3), [2, 3, 4, 5, 6]
                )
        self.assertEqual(
            insert_an_element_at_an_array_position(
                [70, 60, 50, -1], 4, 40), [70, 60, 50, 40]
                )

if __name__ == "__main__":
    unittest.main()
