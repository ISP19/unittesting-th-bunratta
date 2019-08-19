import unittest
from .listutil import *


class UniqueFnTest(unittest.TestCase):
    def test_single_list_single_ele(self):
        self.assertEqual([5], unique([5]))
        self.assertEqual([4], unique([4]))
        self.assertEqual([1], unique([1]))

    def test_single_list_repetitive(self):
        self.assertEqual(['b', 'a'], unique(["b", "a", "a",
                                             "b", "b", "b",
                                             "a", "a"]))

    def test_non_list(self):
        try:
            self.assertRaises(InvalidTypeException, unique("str"))
        except:
            pass


if __name__ == "__main__":
    unittest.main()
