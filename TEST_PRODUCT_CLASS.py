import unittest
from PRODUCT import Product
from PRODUCT import cakes


# Since the Product class had no methods. I managed to only have 3 TestCases.
# imported cakes so as to pass the cakes list through TestCases
# imported Product as it is the class that is being tested.
# imported the unittest module so as to perform unit testing.

class TestProduct(unittest.TestCase):
    # tests if a object is an instance of the Product class
    def test_product_is_instance(self):
        vanilla = Product("vanilla", 30, 20, 10)
        chocolate = Product("chocolate", 40, 12, 10)
        lemon = Product("lemon", 50, 12, 10)
        strawberry = Product("strawberry", 12, 15, 10)
        self.assertIsInstance(vanilla, Product)
        self.assertIsInstance(chocolate, Product)
        self.assertIsInstance(lemon, Product)
        self.assertIsInstance(strawberry, Product)

    # tests is a particular key is present in the dictionary of the Product class
    def test_if_key_in_dict(self):
        for cake in cakes:
            self.assertIn('name', cake.keys())
            self.assertIn('price', cake.keys())
            self.assertIn('quantity', cake.keys())
            self.assertIn('sales', cake.keys())

    # verifies that they data I am working with is stored as the appropriate data type.
    def test_datatype(self):
        self.assertIs(type(cakes), list)
        for cake in cakes:
            self.assertIs(type(cake), dict)


if __name__ == '__main__':
    unittest.main()
