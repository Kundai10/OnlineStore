import unittest
from ADMIN import Admin
from ADMIN import admins
from PRODUCT import cakes


# imported the unittest module so as to perform Testcases.
# imported the admins list so as to pass the list through test cases.
# imported cakes from product file so that I can test if the append method works well.
# imported the Admin class as it is the class being tested.

class TestAdmin(unittest.TestCase):

    # tests if the file, called shop_reviews, raises an exception.
    def test_exception_handling(self):
        file_name = 'shop_reviews'
        with open(file_name, 'r') as f:
            self.assertRaises(Exception, f)
            f.close()

    # tests if the append functionality works well
    def test_append(self):
        new_cake = {}
        cakes.append(new_cake)
        self.assertEqual(cakes[-1], new_cake)

    # tests if an object is an instance of the Admin class
    def test_admin_is_instance(self):
        smith = Admin("SMITH", 2345)
        brown = Admin("BROWN", 2346)
        barker = Admin("BARKER", 2347)
        self.assertIsInstance(smith, Admin)
        self.assertIsInstance(brown, Admin)
        self.assertIsInstance(barker, Admin)

    # in the admin class, the user's input has only be changed to lower or upper case only twice.
    # please input the name and cake_name to see if the test run.
    # if the user inputs a string(type), it will assert if True, else, the user inputs a integer, it will raise
    # an exception and pass the test

    def test_check_if_input_upper_lower_case(self):
        cake_name = input("Enter cake name to be removed: ").lower()
        name = input("Input your name: ").upper()
        if cake_name == str(type) and name == str(type):
            self.assertTrue(cake_name.islower())
            self.assertTrue(name.isupper())
        else:
            self.assertRaises(Exception)

    # tests if a key exists in the admins dictionary
    def test_if_key_dict(self):
        for admin in admins:
            self.assertIn('name', admin.keys())
            self.assertIn('id_num', admin.keys())

    # tests the data types of the admins list and items inside the list
    def test_data_type(self):
        self.assertIsInstance(admins, list)
        for admin in admins:
            self.assertIsInstance(admin, dict)


if __name__ == '__main__':
    unittest.main()
