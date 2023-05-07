from unittest import TestCase

from main import integer_to_text


class Tests(TestCase):
    def test_integer_to_text(self):
        self.assertEqual("one thousand one hundred and twenty seven", integer_to_text(1127))
        self.assertEqual("one hundred billion one hundred and twenty seven", integer_to_text(100000000127))
        self.assertEqual("one hundred trillion one hundred and twenty seven", integer_to_text(100000000000127))
        self.assertEqual("one hundred trillion four hundred and twelve million one hundred and twenty seven", integer_to_text(100000412000127))
