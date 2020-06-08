#!/usr/bin/python3
"""Unittest for Square class"""

import json
from os import path
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquareClass(unittest.TestCase):
    """This class is for testing the Square class"""

    @classmethod
    def setUpClass(cls):
        """Set up instances for all tests"""
        Base._Base__nb_objects = 0
        cls.s1 = Square(4)
        cls.s2 = Square(8, 2)
        cls.s3 = Square(16, 2, 3)
        cls.s4 = Square(32, 2, 4, 10)
        cls.s5 = Square(64, 2, 5, None)

    def test_id_validation(self):
        """Test to check id's"""

        self.assertEqual(self.s1.id, 1)
        self.assertEqual(self.s2.id, 2)
        self.assertEqual(self.s3.id, 3)
        self.assertEqual(self.s4.id, 10)
        self.assertEqual(self.s5.id, 4)

    def test_y_getter(self):
        """Test to check getter function of y"""

        self.assertEqual(self.s1.y, 0)
        self.assertEqual(self.s2.y, 0)
        self.assertEqual(self.s3.y, 3)
        self.assertEqual(self.s4.y, 4)
        self.assertEqual(self.s5.y, 5)

    def test_x_getter(self):
        """"Test to check getter function of x"""

        self.assertEqual(self.s1.x, 0)
        self.assertEqual(self.s2.x, 2)
        self.assertEqual(self.s3.x, 2)
        self.assertEqual(self.s4.x, 2)
        self.assertEqual(self.s5.x, 2)

    def test_size_getter(self):
        """"Test to check getter function of size"""

        self.assertEqual(self.s1.size, 4)
        self.assertEqual(self.s2.size, 8)
        self.assertEqual(self.s3.size, 16)
        self.assertEqual(self.s4.size, 32)
        self.assertEqual(self.s5.size, 64)

    def test_area(self):
        """Test to check area function"""

        self.assertEqual(self.s1.area(), 16)
        self.assertEqual(self.s2.area(), 64)
        self.assertEqual(self.s3.area(), 256)
        self.assertEqual(self.s4.area(), 1024)
        self.assertEqual(self.s5.area(), 4096)

    def test_str(self):
        """Test to check area function"""

        self.assertEqual(str(self.s1), "[Square] (1) 0/0 - 4")
        self.assertEqual(str(self.s2), "[Square] (2) 2/0 - 8")
        self.assertEqual(str(self.s3), "[Square] (3) 2/3 - 16")
        self.assertEqual(str(self.s4), "[Square] (10) 2/4 - 32")
        self.assertEqual(str(self.s5), "[Square] (4) 2/5 - 64")

    @classmethod
    def tearDownClass(cls):
        """class method called after tests have run"""

        pass


if __name__ == "__main__":
    unittest.main()
