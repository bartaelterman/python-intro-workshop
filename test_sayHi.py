from unittest import TestCase
from ex8_CodeToTest import *

class TestSayHi(TestCase):
    def test_sayHi(self):
        result = sayHi()
        self.assertEquals('Hello World', result)