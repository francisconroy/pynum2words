from unittest import TestCase

from util.integer_to_thousand_groups import integer_to_thousand_groups


class Tests(TestCase):
    def test_integer_to_thousand_groups(self):
        self.assertListEqual([123, 456, 789], integer_to_thousand_groups(123456789))
        self.assertListEqual([1], integer_to_thousand_groups(1))
        self.assertListEqual([12], integer_to_thousand_groups(12))
        self.assertListEqual([12, 1], integer_to_thousand_groups(12001))
