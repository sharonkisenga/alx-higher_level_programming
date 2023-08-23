#!/usr/bin/python3
"""make test rectangles"""


import unittest
import contextlib
import importlib
import models.base
import models.rectangle


Rect = models.rectangle.Rectangle


class rectangle_tests(unittest.TestCase):
    """test for rectangle"""
    def setUp(self):
        """test rectangle"""
        importlib.reload(models.base)
        importlib.reload(models.rectangle)

    def test_TooFewArgs(self):
        """test rectangle"""
        err = "missing heigt arg fool"
        with self.assertRaises(TypeError, msg=err):
            Rect(1)

    def def test_TooManyArgs(self):
        """test rectangle"""
        err = "too many arguments man"
        with self.assertRaises(TypeError, msg=err):
            Rect(1, 1, 1, 1, 1, 1)

    def test_Area(self):
        """test test rectangle"""
         testrect = Rect(7, 6)
        with self.subTest():
            self.assertEqual(testrect.area(), 42)
        testrect.width = 4
        testrect.height = 5
        with self.subTest():
            self.assertEqual(testrect.area(), 20)
