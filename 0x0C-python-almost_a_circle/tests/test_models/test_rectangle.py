#!/usr/bin/python3
'''Module Rectangle'''

import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle
from contextlib import redirect_stdout

class TestRectangle(unittest.TestCase):
    '''Tests to Base'''

    def test_None_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 25)
    def test_to_dictionary_out(self):
        m = Rectangle(101, 22, 11, 89, 5)
        c = {'x': 11, 'y': 89, 'id': 5, 'height': 22, 'width': 101}
        self.assertDictEqual(c, m.to_dictionary())

    def test_to_dictionary_no(self):
        m1 = Rectangle(1, 3, 11, 8, 6)
        m2 = Rectangle(6, 8, 11, 3, 1)
        m2.update(**m1.to_dictionary())
        self.assertNotEqual(m1, m2)

    def test_to_dictionary_arg(self):
        r = Rectangle(10, 20, 6, 1, 2)
        with self.assertRaises(TypeError):
            r.to_dictionary(1)

if __name__ == "__main__":
    unittest.main()
