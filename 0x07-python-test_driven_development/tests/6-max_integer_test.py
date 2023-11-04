#!/usr/bin/python3

"""
This is a unnitest code for the max_integer(list=[]) function
"""

import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """
    class TestMaxInteger for running test cases on the inented module
    """
    def test_regular_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
