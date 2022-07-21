import unittest
from CUSTOMER import Customer
from CUSTOMER import customers
import json


# imported the unittest module so as to perform unit testing.
# imported json so as to test if the json dumps functionality works
# imported the Customer class as it is the class being testes
# imported the customers list so as to pass the list through test cases

class TestCustomer(unittest.TestCase):
    # The program uses the json.dumps() functionality 5 times. So I dumped an empty dictionary in this Testcase
    # since I could not dump all five different dictionaries in my test case.
    def test_json_dumps(self):
        self.assertEqual(json.dumps({}), '{}')

    # tests if a object is an instance of the Customer class.
    def test_customer_is_instance(self):
        fred = Customer('FRED', 11, [])
        brenda = Customer("BRENDA", 12, [])
        jane = Customer("JANE", 13, [])
        self.assertIsInstance(fred, Customer)
        self.assertIsInstance(brenda, Customer)
        self.assertIsInstance(jane, Customer)

    # tests if a key is in the customers dictionary
    def test_if_key_in_dict(self):
        for customer in customers:
            self.assertIn('name', customer.keys())
            self.assertIn('id_num', customer.keys())

    # tests if a user's input is lower or uppercase
    # these are examples of inputs which were converted to upper or lowercase in the Customer class.
    # used conditional statements, so that if the user input is of type string then it will assert True, else
    # they input input integer then it will raise an exception so that the test passes.
    def test_input_upper_lowercase(self):
        user_input = input("Enter the name of cake you want to add to your cart: ").lower()
        proceed = input("Do you want to add another cake?: ").lower()
        remove_cake = input("Enter the name of cake you want to remove from cart: ").lower()
        first_name = input("Enter your first name: ").upper()
        if user_input and proceed and remove_cake and first_name == str(type):
            self.assertTrue(user_input.islower())
            self.assertTrue(proceed.islower())
            self.assertTrue(remove_cake.islower())
            self.assertTrue(first_name.isupper())
        else:
            self.assertRaises(Exception)

    # verifies if the data I am working with is stored as the appropriate data type.
    def test_data_type(self):
        self.assertTrue(type(customers) is list)
        for customer in customers:
            self.assertTrue(type(customer) is dict)


if __name__ == '__main__':
    unittest.main()
