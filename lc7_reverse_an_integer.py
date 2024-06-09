"""
Given a signed 32-bit integer x, return x with its digits reversed.
    If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], 
    then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21

"""

import unittest
import math


def reverse_an_integer_using_string_method(num: int) -> int:
    """
    Reverse an integer using string
    Algorithm used: String conversion reverse
    Time Complexity: O(n) - where n is the number of digits in the input integer
    Space Complexity: O(n) - This is because the function creates a new string
                        to store the reversed digits of the input integer.
    """
    len_of_int = len(str(abs(num)))
    resultant_sign = -1 if num < 0 else 1 if num > 0 else 0
    if resultant_sign == 0:
        return resultant_sign
    str_num = str(abs(num))
    result = ""
    for i in range(len_of_int):
        result += str_num[-1:]
        str_num = str_num[:-1]
    result = int(result)
    result = 0 if result > 2**31 - 1 else result
    return result * resultant_sign


def reverse_an_integer_math(num: int) -> int:
    """
    Using mathematical logrithm method
    Algorithm used: Math log and div mod
    Time Complexity: O(n) - where n is the number of digits in the input integer
    Space Complexity: O(1) - it does not use any additional data structures or variables
                        to store the reversed integer
    """
    resultant_sign = -1 if num < 0 else 1 if num > 0 else 0
    if resultant_sign == 0:
        return resultant_sign
    num = abs(num)
    len_of_int = int(math.log10(abs(num))) + 1
    result = 0
    for i in range(len_of_int):
        # add the result into the last digit of integer * 10 ^ length of integer-1
        result += (num % 10) * (10 ** (len_of_int - (i + 1)))
        num = num // 10
    result = 0 if result > 2**31 - 1 else result
    return result * resultant_sign


def reverse_an_integer_using_divmod(num: int) -> int:
    """
    Using divmod method
    Algorithm used: Math div and mod
    Time Complexity: O(n) - where n is the number of digits in the input integer
    Space Complexity: O(1) - it does not use any additional data structures or variables
                        to store the reversed integer    
    """
    # base case if num is 0 return the same
    if num == 0:
        return num
    sign = -1 if num < 0 else 1
    sign = [1, -1][num < 0]
    result, num = 0, abs(num)
    while num:
        num, mod = divmod(num, 10)
        result = result * 10 + mod
        if result > 2**31 - 1:
            return 0
    return result * sign


class TestReverseAnInteger(unittest.TestCase):
    """
    Test Reverse An Integer from string with various method
    """

    def test_reverse_an_integer_using_string_method(self) -> None:
        """
        Using string method for reversing
        """
        self.assertEqual(reverse_an_integer_using_string_method(321), 123)
        self.assertEqual(reverse_an_integer_using_string_method(-321), -123)
        self.assertEqual(reverse_an_integer_using_string_method(21), 12)
        self.assertEqual(reverse_an_integer_using_string_method(3), 3)
        self.assertEqual(reverse_an_integer_using_string_method(40), 4)
        self.assertEqual(reverse_an_integer_using_string_method(240), 42)
        self.assertEqual(reverse_an_integer_using_string_method(404), 404)
        self.assertEqual(reverse_an_integer_using_string_method(0), 0)

    def test_reverse_an_integer_using_math_log_method(self) -> None:
        """
        Using string method for reversing
        """
        self.assertEqual(reverse_an_integer_math(321), 123)
        self.assertEqual(reverse_an_integer_math(-321), -123)
        self.assertEqual(reverse_an_integer_math(21), 12)
        self.assertEqual(reverse_an_integer_math(3), 3)
        self.assertEqual(reverse_an_integer_math(40), 4)
        self.assertEqual(reverse_an_integer_math(240), 42)
        self.assertEqual(reverse_an_integer_math(404), 404)
        self.assertEqual(reverse_an_integer_math(0), 0)

    def test_reverse_an_integer_using_divmod_method(self) -> None:
        """
        Using string method for reversing
        """
        self.assertEqual(reverse_an_integer_using_divmod(321), 123)
        self.assertEqual(reverse_an_integer_using_divmod(-321), -123)
        self.assertEqual(reverse_an_integer_using_divmod(21), 12)
        self.assertEqual(reverse_an_integer_using_divmod(3), 3)
        self.assertEqual(reverse_an_integer_using_divmod(40), 4)
        self.assertEqual(reverse_an_integer_using_divmod(240), 42)
        self.assertEqual(reverse_an_integer_using_divmod(404), 404)
        self.assertEqual(reverse_an_integer_using_divmod(0), 0)


if __name__ == "__main__":
    unittest.main()
