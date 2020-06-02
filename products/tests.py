from django.test import TestCase
from .models import Product

# Create your tests here.
class ProductTests(TestCase):
    """
    Here we'll define the tests that we'll run against our
    Product model
    """

    def test_str(self):
        test_title = Product(title='First product')
        self.assertEqual(str(test_title), 'First product')