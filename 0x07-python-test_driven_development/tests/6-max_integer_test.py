#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxIntegerFunction(unittest.TestCase):
    def test_empty_list(self):
        result = max_integer([])
        self.assertIsNone(result, None)

    def test_positive_numbers(self):
        result = max_integer([1, 3, 5, 2, 4])
        self.assertEqual(result, 5)

    def test_negative_numbers(self):
        result = max_integer([-1, -3, -5, -2, -4])
        self.assertEqual(result, -1)

    def test_mixed_numbers(self):
        result = max_integer([-1, 3, -5, 2, -4])
        self.assertEqual(result, 3, "Should return the maximum number in the list")

    def test_duplicate_numbers(self):
        result = max_integer([5, 5, 5, 5, 5])
        self.assertEqual(result, 5)

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            max_integer([1, 'a', 3, 2])

    def test_strings_representing_numbers(self):
        result = max_integer(['10', '25', '5'])
        self.assertEqual(result, 25, "Should return the maximum number from strings representing numbers")

    def test_floats_mixed_with_integers(self):
        result = max_integer([1.5, 2, 3, 1])
        self.assertEqual(result, 3, "Should return the maximum number with floats mixed with integers")

    def test_float(self):
        """Test with a list of mixed ints and floats: should return the max"""
        l = [3, 4.5, 2]
        result = max_integer(l)
        self.assertEqual(result, 4.5)

    def test_single_element_list(self):
        result = max_integer([7])
        self.assertEqual(result, 7, "Should return the only element in the list")

    def test_none(self):
        """Test with a None as parameter: should raise a TypeError"""
        with self.assertRaises(TypeError):
            max_integer(None)
        # self.assertRaises(TypeError, max_integer, None)

    def test_regular(self):
        """Test with a regular list of ints: should return the max result"""
        l = [1, 2, 3, 4, 5]
        result = max_integer(l)
        self.assertEqual(result, 5)

    def test_strings(self):
        """Test with a list of strings: should return the first string"""
        l = ["hi", "hello"]
        result = max_integer(l)
        self.assertEqual(result, "hi")

    def test_not_list(self):
        """Test with a parameter that's not a list: should raise a TypeError"""
        self.assertRaises(TypeError, max_integer, 7)

    def test_unique(self):
        """Test with a list of one int: should return the value of this int"""
        l = [45]
        result = max_integer(l)
        self.assertEqual(result, 45)


if __name__ == '__main__':
    unittest.main()
