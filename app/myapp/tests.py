from django.test import TestCase

from myapp.utils import add, subtract

# Create your tests here.


class CalcTests(TestCase):

    def test_add_numbers(self):
        """ Test to add numbers """
        self.assertEqual(add(1, 5), 6)

    def test_sub_numbers(self):
        """ Test to subtract numbers """
        self.assertEqual(subtract(5, 11), 6)
