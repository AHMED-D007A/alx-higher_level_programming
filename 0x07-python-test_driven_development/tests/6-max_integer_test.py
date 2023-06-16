#!/usr/bin/python3
"""
Unittest for max_integer(list)
"""
import unittest
max_integer = __import__("6-max_integer").max_integer

class TestingMaxInteger(unittest.TestCase):
    def test_void(self):
        self.assertIsNone(max_integer())

    def test_no_1(self):
        self.assertEqual(max_integer([0]), 0)

    def test_no_2(self):
        self.assertEqual(max_integer([i for i in range(10)]), 9)
        self.assertEqual(max_integer([5, 15, 25, 20]), 25)

    def test_no_3(self):
        self.assertEqual(max_integer([-9, -14, -33, -3]), -3)

    def test_None_integer(self):
        self.assertEqual(max_integer([True, False]), True)
        self.assertEqual(max_integer(["ahmed", "mamdouh"]), "mamdouh")
        self.assertEqual(max_integer([8.0, 9.1, 10.2]), 10.2)
