import unittest2

from Calculator import calc

class TestCalc(unittest2.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(10,20),30,"Should be 30")

    def test_sub(self):
        self.assertEqual(calc.sub(50,10),40,"Should be 40")

    def test_mul(self):
        self.assertEqual(calc.mul(25,2),50,"Should be 50")

    def test_div(self):
        self.assertEqual(calc.div(600,10),60,"Should be 60")