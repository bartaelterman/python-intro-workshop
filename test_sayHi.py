from unittest import TestCase
from ex7_CodeToTest import *

__author__ = 'bart_aelterman'


class TestSayHi(TestCase):
    def test_sayHi(self):
        result = sayHi()
        self.assertEquals('Hello World', result)