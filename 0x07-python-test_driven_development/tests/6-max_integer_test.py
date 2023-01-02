#!/usr/bin/python3

"""
unittest module for the fuction max-integer
"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_integer(self):
        #test max integer on a list of integers
        self.assertAlmostEqual(max_integer([1, 2, 3]), 3)
    def test_empty_list(self):
        """
        test an empty list passed as arg:
        expect None
        """
        self.assertAlmostEqual(max_integer([]), None)
    def test_non_list(self):
        """
        test TypeError raised when an not a list is passed:
        """
        self.assertRaises(TypeError, max_integer, 1, 2)
