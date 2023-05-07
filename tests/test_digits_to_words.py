from unittest import TestCase

from util.digits_to_words import two_digits_to_words, three_digits_to_words


class Tests(TestCase):
    def test_two_digits_to_words(self):
        self.assertEqual("twenty", two_digits_to_words([2, 0]))
        self.assertEqual("twelve", two_digits_to_words([1, 2]))
        self.assertEqual("one", two_digits_to_words([0, 1]))
        self.assertEqual("thirty", two_digits_to_words([3, 0]))
        self.assertEqual("eighteen", two_digits_to_words([1, 8]))
        self.assertEqual("nineteen", two_digits_to_words([1, 9]))
        self.assertEqual("thirty one", two_digits_to_words([3, 1]))
        with self.assertRaises(ValueError):
            two_digits_to_words(["c"])
        with self.assertRaises(ValueError):
            two_digits_to_words([1, 2, 3], "XX")

    def test_two_digits_to_words_zero(self):
        self.assertEqual("", two_digits_to_words([0]))

    def test_three_digits_to_words(self):
        self.assertEqual("one hundred and twenty seven", three_digits_to_words([1, 2, 7]))
        self.assertEqual("one hundred and thirteen", three_digits_to_words([1, 1, 3]))
        self.assertEqual("one hundred and nineteen", three_digits_to_words([1, 1, 9]))
        self.assertEqual("nine hundred and nineteen", three_digits_to_words([9, 1, 9]))
        self.assertEqual("one hundred", three_digits_to_words([1, 0, 0]))

    def test_three_digits_to_words_zero(self):
        self.assertEqual("", three_digits_to_words([0]))
    def test_three_digits_to_words_single_digit(self):
        self.assertEqual("one", three_digits_to_words([1]))
