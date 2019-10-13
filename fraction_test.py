import math
import time
import unittest
from fraction import Fraction


class FractionTest(unittest.TestCase):
    """Test the methods and constructor of the Fraction class. """

    def test_init(self):
        self.assertEqual(0, Fraction(0))
        self.assertEqual(88, Fraction(88))
        self.assertEqual(10, Fraction(10, 1))
        self.assertEqual(112, Fraction(112, 1))
        self.assertTrue(math.isnan(Fraction(0, 0)))
        self.assertEqual(math.inf, Fraction(1, 0))
        self.assertEqual(-math.inf, Fraction(-1, 0))
        with self.assertRaises(ValueError):
            Fraction(8, 0)
            Fraction(-9, 0)
            Fraction(11, -0)
            Fraction(0.1, 0.8)
            Fraction(3.14, 3.14)

    def test_str(self):
        f = Fraction(3, -1)
        self.assertEqual("-3", f.__str__())
        f = Fraction(0, 5)
        self.assertEqual("0", f.__str__())
        f = Fraction(0, 100)
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
        f = Fraction(10, 1)
        self.assertEqual("10", f.__str__())

        f = Fraction(0, 0)
        self.assertEqual("nan", f.__str__())
        f = Fraction(1, 0)
        self.assertEqual("inf", f.__str__())
        f = Fraction(-1, 0)
        self.assertEqual("-inf", f.__str__())

    def test_add(self):
        self.assertTrue(Fraction(3, 4) == Fraction(1, 12) + Fraction(2, 3))
        self.assertTrue(Fraction(-1, 16) == Fraction(1, 16) + Fraction(-2, 16))
        self.assertTrue(Fraction(-8, 9) == Fraction(-7, 9) + Fraction(-1, 9))
        self.assertTrue(Fraction(-8, 28) == Fraction(7, -28) + Fraction(1, -28))
        self.assertTrue(math.inf == Fraction(10, 112) + Fraction(1, 0))
        self.assertTrue(-math.inf == Fraction(10, 112) + Fraction(-1, 0))

    def test_sub(self):
        self.assertTrue(Fraction(-1, 16) == Fraction(1, 16) - Fraction(2, 16))
        self.assertTrue(Fraction(-8, 9) == Fraction(-7, 9) - Fraction(1, 9))
        self.assertTrue(Fraction(-8, 28) == Fraction(7, -28) - Fraction(1, 28))
        self.assertTrue(Fraction(10, 112) == Fraction(10, 112) - Fraction(0))
        self.assertTrue(Fraction(10, 112) == Fraction(10, 112) - 0)

    def test_mul(self):
        self.assertEqual(Fraction(0), Fraction(-5, 9) * Fraction(0, 6))
        self.assertEqual(Fraction(5, 6), Fraction(1, 6)*Fraction(5, 1))
        self.assertEqual(Fraction(-5, 49), Fraction(1, 7) * Fraction(-5, 7))
        self.assertEqual(Fraction(20, 54), Fraction(-5, 9) * Fraction(-4, 6))
        self.assertEqual(-math.inf, Fraction(1, 0) * Fraction(-1, 0))
        self.assertEqual(math.inf, Fraction(-1, 0) * Fraction(-1, 0))

    def test_neg(self):
        self.assertEqual(Fraction(-7, 8), -Fraction(7, 8))
        self.assertEqual(Fraction(10, -16), -Fraction(10, 16))
        self.assertEqual(Fraction(9, 10), -Fraction(-9, 10))
        self.assertEqual(Fraction(10, 112), -Fraction(-10, 112))
        self.assertEqual(-math.inf, -Fraction(1, 0))
        self.assertEqual(math.inf, -Fraction(-1, 0))
        # Double negation
        self.assertEqual(math.inf, -(-Fraction(1, 0)))

    def test_lt(self):
        self.assertTrue(Fraction(-1, 2) > Fraction(-2, 3))
        self.assertTrue(Fraction(8, 8) < Fraction(9, 8))
        self.assertTrue(Fraction(-112, 112) < 0)
        self.assertTrue(Fraction(-10, 10) < Fraction(1))
        self.assertTrue(Fraction(-15, 16) < Fraction(15, 16))
        self.assertTrue(Fraction(27, 28) < Fraction(28, 29))

    def test_gt(self):
        self.assertTrue(Fraction(1, 2) > Fraction(1, 4))
        self.assertTrue(Fraction(4, 5) > Fraction(3, 4))
        self.assertTrue(Fraction(-4, 5) > Fraction(-5, 6))
        self.assertTrue(Fraction(5, 9) > Fraction(1, 3))
        self.assertTrue(Fraction(10, 112) > Fraction(-10, 112))
        self.assertTrue(Fraction(10, 112) > Fraction(10, -112))
        self.assertTrue(Fraction(8) > Fraction(-8))
        self.assertTrue(Fraction(3, 2) > 0)

    def test_from_str(self):
        self.assertEqual(Fraction(1, 8), Fraction.from_str("1/8"))
        self.assertEqual(1, Fraction.from_str("112/112"))
        self.assertEqual(math.inf, Fraction.from_str("1/0"))
        self.assertEqual(-math.inf, Fraction.from_str("-1/0"))
        self.assertTrue(math.isnan(Fraction.from_str("0/0")))

    def test_eq(self):
        one = Fraction(1)
        f = Fraction(1, 2)
        g = Fraction(-40, -80)
        h = Fraction(10000, 20001)  # not quite 1/2
        i = Fraction(0, 3)
        j = Fraction(0, 6)
        k = Fraction(10, 10)
        self.assertTrue(f == g)
        self.assertTrue(f.__eq__(g))  # same thing
        self.assertFalse(f == h)
        self.assertFalse(f.__eq__(h))
        self.assertTrue(i == j)
        self.assertTrue(i.__eq__(j))
        self.assertTrue(one == k)
        self.assertTrue(one.__eq__(k))
        self.assertTrue(one == 1)
