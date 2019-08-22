import math
import time
import unittest
from fraction import Fraction


class FractionTest(unittest.TestCase):
    """Test the methods and constructor of the Fraction class. """

    #TODO: Constructor test
    def test_init(self):
        pass

    def test_str(self):
        f = Fraction(3, -1)
        self.assertEqual("-3", f.__str__())
        f = Fraction(0, 5)
        self.assertEqual("0", f.__str__())
        f = Fraction(60, 90)
        self.assertEqual("2/3", f.__str__())
        f = Fraction(1500, 60)
        self.assertEqual("25", f.__str__())
        f = Fraction(1500, 90)
        self.assertEqual("50/3", f.__str__())
        f = Fraction(-80, 20)
        self.assertEqual("-4", f.__str__())
        f = Fraction(36, -60)
        self.assertEqual("-3/5", f.__str__())
        # Constructor should provide default denominator = 1
        f = Fraction(99)
        self.assertEqual("99", f.__str__())

    # TODO Write tests for __init__, __eq__, +, *.
    # Here is an example, but you must add more test cases.  
    # The test requires that your __eq__ is correct.
    def test_add(self):
        # 3/4 = 2/3 + 1/12
        self.assertAlmostEqual(Fraction(3, 4), Fraction(1, 12) + Fraction(2, 3))

    def test_mul(self):
        self.assertEqual(Fraction(5, 6), Fraction(1, 6)*Fraction(5, 1))
        self.assertEqual(Fraction(-5, 49), Fraction(1, 7) * Fraction(-5, 7))
        self.assertEqual(Fraction(20, 54), Fraction(-5, 9) * Fraction(-4, 6))
        self.assertEqual(-1, (Fraction(1, 0) * Fraction(-1, 0)).numerator)
        self.assertEqual(1, (Fraction(-1, 0) * Fraction(-1, 0)).numerator)

    def test_eq(self):
        f = Fraction(1,2)
        g = Fraction(-40, -80)
        h = Fraction(10000, 20001)  # not quite 1/2
        i = Fraction(0, 3)
        j = Fraction(0, 6)
        self.assertTrue(f == g)
        self.assertTrue(f.__eq__(g))  # same thing
        self.assertFalse(f == h)
        self.assertFalse(f.__eq__(h))
        self.assertTrue(i == j)
        self.assertTrue(i.__eq__(j))
        #TODO write more tests using other cases.
        # Consider special values like 0, 1/0, -1/0
