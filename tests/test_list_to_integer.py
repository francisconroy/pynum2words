from unittest import TestCase

from util.list_to_integer import list_to_integer


class Tests(TestCase):
    def test_with_valid_integer_lists(self):
        self.assertEqual((True, 123), list_to_integer([1, 2, 3]))
        self.assertEqual((True, 23), list_to_integer([0, 2, 3]))
        self.assertEqual((True, 231), list_to_integer([2, 3, 1]))
        self.assertEqual((True, -231), list_to_integer([-2, 3, 1]))

    def test_with_empty_list(self):
        self.assertEqual(False, list_to_integer([])[0])

    def test_with_no_args(self):
        self.assertEqual(False, list_to_integer()[0])

    def test_with_lists_of_other(self):
        self.assertEqual(False, list_to_integer([1, "d", 3])[0])

    def test_with_multiple_negatives(self):
        self.assertEqual(False, list_to_integer([-1, -1, 2])[0])
        self.assertEqual(False, list_to_integer([-1, -1, -2])[0])
