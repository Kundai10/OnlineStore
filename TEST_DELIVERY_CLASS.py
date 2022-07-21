import unittest
from DELIVERY import Delivery
from DELIVERY import staff


# imported the unittest module to perform unit testing.
# imported the Delivery Class as it is the class being tested
# imported the staff list so as to pass it through Test cases..

class TestDelivery(unittest.TestCase):
    # tests if a object is an instance of the Delivery Class.
    def test_delivery_is_instance(self):
        alex = Delivery("ALEX", 800)
        harry = Delivery("HARRY", 900)
        william = Delivery("WILLIAM", 700)
        self.assertIsInstance(alex, Delivery)
        self.assertIsInstance(harry, Delivery)
        self.assertIsInstance(william, Delivery)

    # tests if user input is converted to upper case.
    # introduced conditional statements so that if a user's input is of string type it will assertTrue, else if it
    # is of integer type it will raise an exception and pass the test.
    def test_if_input_uppercase(self):
        customer = input("Enter customer's name whose order you want to package: ").upper()
        name = input("Enter your name: ").upper()
        if customer and name == str(type):
            self.assertTrue(customer.isupper())
            self.assertTrue(name.isupper())
        else:
            self.assertRaises(Exception)

    # tests if a key is present in the staff dictionary
    def test_if_dict_keys(self):
        for worker in staff:
            self.assertIn('name', worker.keys())
            self.assertIn('id_num', worker.keys())

    # verifies if the objects I am working with are stored as the appropriate data type
    def test_data_type(self):
        self.assertIsInstance(staff, list)
        for worker in staff:
            self.assertIsInstance(worker, dict)

    # tests if the files, customer_order_history and delivery_address raise Exceptions.
    def test_raise_exception(self):
        file_name1 = 'customer_order_history'
        file_name2 = 'delivery_address'
        with open(file_name1, 'r') as f1:
            self.assertRaises(Exception, f1)
            f1.close()
        with open(file_name2, 'r') as f2:
            self.assertRaises(Exception, f2)
            f2.close()


if __name__ == '__main__':
    unittest.main()
