"""
Sample tests

"""
from django.test import SimpleTestCase

from app import calc

class ClacTests(SimpleTestCase):

	def test_add_numbers(self):
		res = calc.add(5, 6)

		self.assertEquals(res, 11)

	def test_subtract_numbers(self):
		res = calc.subtract(10, 15)

		self.assertEqual(res, 5)

