"""
Samples tests
"""
from django.test import SimpleTestCase

from app import cal

class CalTest(SimpleTestCase):
    
    """Test the cal module."""
    def test_add_numbers(self):
        res = cal.add(5,6)

        self.assertEqual(res,11)

    def test_subtract_numbers(self):
        res = cal.subtract(13,10)

        self.assertEqual(res,3)