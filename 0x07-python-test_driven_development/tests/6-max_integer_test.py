#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    """
    Class of unittest
    """

    def test_variousFunction(self):
        """
        Test normal cases
        """
        self.assertEqual(max_integer([1, 2]), 2)

    def test_sameSearch(self):
        """
        Test same num search
        """
        self.assertEqual(max_integer([1, 1, 1]), 1)

    def test_negativeSearch(self):
        """
        Test negative search
        """
        self.assertEqual(max_integer([-5, -2, -3]), -2)

    def test_ranNumSearch(self):
        """
        Test ran search
        """
        self.assertEqual(max_integer([-5, 2, 5]), 5)

    def test_Error(self):
        """
        Test error cases
        """
        with self.assertRaises(TypeError):
            max_integer(True)

    def test_Error_2(self):
        """
        Test error cases
        """
        with self.assertRaises(TypeError):
            max_integer(4, 2, 1, 2)

    def test_Error_3(self):
        """
        Test error cases
        """
        with self.assertRaises(TypeError):
            max_integer("Melkin", 1)

    def test_Error_4(self):
        """
        Test error cases
        """
        with self.assertRaises(TypeError):
            max_integer("", "")


if __name__ == '__main__':
    unittest.main()
