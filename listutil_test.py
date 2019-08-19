import unittest
from .listutil import *
from .listutil_test_data import HUGE_LIST_1


class UniqueFnTest(unittest.TestCase):
    def test_single_list_single_ele(self):
        self.assertEqual([5], unique([5]))
        self.assertEqual([4], unique([4]))
        self.assertEqual([1], unique([1]))

    def test_single_list_repetitive(self):
        self.assertEqual(['b', 'a'], unique(["b", "a", "a",
                                             "b", "b", "b",
                                             "a", "a"]))

    def test_single_list_huge(self):
        # 1000 random items with some repetitive items
        self.assertListEqual(sorted(list(range(0, 23))), sorted(unique(HUGE_LIST_1)))

    def test_non_list(self):
        try:
            self.assertRaises(InvalidTypeException, unique("str"))
        except:
            pass


if __name__ == "__main__":
    unittest.main()
