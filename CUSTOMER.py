from PRODUCT import cakes
from ADMIN import Admin
import time
import json


# imported json so that I can be able to append dictionaries to my files.
# it is impossible to append a dictionary to a textfile. To do that, JSON is used.
# imported the time module to so as to use delay the execution of the program with some seconds.
# imported the cakes variable which contained a list of dictionaries from the Product objects.

# the customer class inherits the Admin class constructor.

class Customer(Admin):

    def __init__(self, name, id_num, cart):
        super().__init__(name, id_num)
        self.cart = []

    # introduced an empty list as an attribute so that each customer has their own cart.

    # allows the user to add items to their own cart.
    def add_to_cart(self):

        user_input = input("Enter name of cake you want to add to your cart: ").lower()
        for cake in cakes:
            if cake['name'] == user_input:
                self.cart.append(cake['name'])
                print(f"THE PRODUCTS IN CART ARE \n {self.cart}.")
                proceed = input("Do you want to add another cake?(yes/no): ").lower()
                if proceed == "yes":
                    Customer.add_to_cart(self)
                else:
                    print("CHOOSE WHICH METHOD YOU WANT TO PERFORM NEXT, FROM THE METHODS BELOW")
                break
        else:
            print('Not available')
            print(f"THE PRODUCTS IN CART ARE \n {self.cart}")
            print("CHOOSE WHICH METHOD YOU WANT TO PERFORM NEXT, FROM THE METHODS BELOW")

    # allows user to remove items from their cart
    def remove_cart(self):
        user_input = input("Enter name of cake you want to remove from your cart: ").lower()
        if user_input in self.cart:
            self.cart.remove(user_input)
            print(f"THE PRODUCTS IN CART ARE \n {self.cart}")
            proceed = input("Do you want to remove another cake?(yes/no): ").lower()
            if proceed == "yes":
                Customer.remove_cart(self)
            else:
                print("CHOOSE WHICH METHOD YOU WANT TO PERFORM NEXT, FROM THE METHODS BELOW")
        else:
            print("Invalid choice.")
            print("CHOOSE WHICH METHOD YOU WANT TO PERFORM NEXT, FROM THE METHODS BELOW")

    # calculates how much the bill is, and prompts the user to pay or cancel order
    def generate_bill(self):
        # declared global variable so as to access the bill variable's value which is outside this function.
        global bill
        # counts how many cakes of a particular name are present in the cart.
        vanilla = self.cart.count("vanilla")
        chocolate = self.cart.count("chocolate")
        lemon = self.cart.count("lemon")
        strawberry = self.cart.count("strawberry")
        bill += (vanilla * 30) + (chocolate * 40) + (lemon * 50) + (strawberry * 20)
        print(f"Your total bill is: ${bill}")
        # if the bill is more than 0, then they can either proceed with payment or cancel order
        # otherwise it means that there is nothing in the cart.
        if bill > 0:
            pay_option = input("Enter 1 to PROCEED WITH PAYMENT. Enter 2 to CANCEL ORDER: ")
            if pay_option == "1":
                checkout()
            elif pay_option == "2":
                print("Your order has been cancelled successfully.")
                self.cart.clear()
                print(f"The items in your cart are:{self.cart} and your bill is now $0.")
            else:
                print("invalid choice")
        else:
            print("You have nothing in your cart.")
            exit()


# the bill variable is declared here so that it can be accessed in the generate_bill, checkout and delivery functions
bill = 0
# these are Customer class objects
customer1 = Customer("FRED", 11, [])
customer2 = Customer("BRENDA", 12, [])
customer3 = Customer("JANE", 13, [])
# the customer objects have been converted into a dictionary.
customers = [customer1.__dict__,
             customer2.__dict__,
             customer3.__dict__]


#  function allows user to pay.

def checkout():
    user_payment = input("Enter 1 to pay using MOBILE MONEY.Enter 2 to pay using a DEBIT CARD: ")
    if user_payment == "1":
        mobile_num = input("Enter your mobile number: ")
        # the len function checks if the mobile number inputted has 5 digits.
        if len(mobile_num) == 5:
            pay = int(input("Initiate payment of  "))
            if pay == bill:
                print("Processing... ")
                time.sleep(2)
                print("Payment of ", bill, "dollars, successful!")
                delivery()
            else:
                print("Transaction Unsuccessful!\nInsufficient Funds")
        else:
            print("Invalid phone number. Please enter a 5 digit number.")

    elif user_payment == "2":
        card_num = input("Enter your card number: ")
        # the len function checks if the card number inputted has 5 digits.
        if len(card_num) == 5:
            pay = int(input("Initiate payment of: "))
            if pay >= bill:
                print("Processing... ")
                time.sleep(1)
                print("Payment of ", bill, "dollars, successful!")
                delivery()
            else:
                print("Transaction Unsuccessful!\nInsufficient Funds")
        else:
            print("Card number must have 5 figures.")
    else:
        print("invalid choice")


# allows user to enter their location and contact details for delivery facilitation
distributor_remera = {"Name": "Becky", "No_Plate": "6001", "Means": "car", "id_no": "3545"}, {}
distributor_kacykiru = {"Name": "Michael", "No_Plate": "6001", "Means": "car", "id_no": "3545"}, {}
distributor_innovation = {"Name": "Ben", "No_Plate": "6001", "Means": "car", "id_no": "3545"}, {}
distributor_nyabisindu = {"Name": "Belinda", "No_Plate": "6001", "Means": "car", "id_no": "3545"}, {}
distributor_other = {"Name": "Ben", "No_Plate": "6001", "Means": "car", "id_no": "3545"}, {}

distributors = distributor_remera, distributor_innovation, distributor_nyabisindu, distributor_kacykiru, distributor_other


def delivery():
    # declared global bill so as to access the bill variable's value which was declared outside this function.
    global bill

    print("Dear customer, for delivery logistics, please input the following information: ")
    first_name = input("Enter First name only. The one you used to log in: ").upper()
    town = input("Your Town of reception: ")
    apartment_number = input("Apartment Number: ")
    phone_number = input("Phone Number: ")
    customer_location = input("Select location from, Remera, Kacykiru, Nyabisindu, Innovation: ").lower()
    if customer_location == "remera":
        distributor = distributor_remera
    elif customer_location == "innovation":
        distributor = distributor_innovation
    elif customer_location == "nyabisindu":
        distributor = distributor_nyabisindu
    elif customer_location == "kacykiru":
        distributor = distributor_kacykiru
    elif customer_location == "other":
        distributor = distributor_other
    else:
        print("Adjust your location, if not listed, please choose other.")
    import random
    # imported random to generate a random receipt number.
    receipt_num = random.getrandbits(16)
    # the user's receipt will be appended to a file that will be accessed by one of the employees.
    receipt = {"First Name": first_name, "Town ": town, "Apartment_number ": apartment_number,
               "Phone Number ": phone_number}

    file_name = 'delivery_address'
    j = json.dumps(receipt)
    with open(file_name, 'a+') as b:
        b.write(j)
        b.write(" ")
        b.close()

    print("Please wait!Printing your receipt....")

    time.sleep(1)
    print("-----------------------------------------")
    print("\nReceipt No ", receipt_num)
    print("KUDE MUNCHES SHOPPING")
    print("234 Kimironko Street")
    print(receipt)
    print("KUDE is Happy to serve you!")
    print("Amount Paid: ", {bill})
    print(f"Your order will be delivered by, {distributor[0]}")
    print("we are an order away")
    print("\nfor any queries,confirmations or complaints")
    print("         Please contact us through:       ")
    print("         0717266565, kude@gmail.com       ")
    print("------------------------------------------")
