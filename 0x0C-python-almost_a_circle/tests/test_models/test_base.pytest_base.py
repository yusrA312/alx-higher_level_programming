#!/usr/bin/python3
'''Module for Base unit tests.'''
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
class TestBase(unittest.TestCase):
    '''Tests the Base class.'''

    def SetUp(self):
        Base._Base__nb_objects = 0
        pass

    def TDown(self):
        pass

    def test_Cons(self):
        '''Tests.'''
        with self.assertRaises(TypeError) as X:
            Base.__init__()
        m = "__init__() missing argument: 'self'"
        self.assertEqual(str(X.exception), m)

    def test_D_2(self):
        '''Tests.'''
        with self.assertRaises(TypeError) as Xe:
            Base.__init__(self, 1, 2)
        M = "__init__() takes from 1 to 2 positional arguments but 3 \
were given"
        self.assertEqual(str(Xe.exception), M))

