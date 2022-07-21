from ADMIN import Admin


# The Delivery class only inherits the constructor from the Admin class.
# TO RUN THE CODE IN THIS FILE, PLEASE RUN THE W13_A5_Q2_RUN_THIS_FILE, FILE AND INPUT 3.
class Delivery(Admin):
    def __init__(self, name, id_num):
        super().__init__(name, id_num)

    @staticmethod
    def customer_orders():
        # first we read the file.
        print("SEE ALL CUSTOMERS' ORDER HISTORY BELOW:")
        file_name = 'customer_order_history'
        with open(file_name, 'r') as f:
            lines = f.read()

        # the len function checks the length of the contents of the file.
        # the program only prints the file contents if there is something inside, else, it tells the user that no orders have been made.

        if len(lines) > 0:
            print(lines)
            customer = input("Enter customer's name whose order you want to package: ").upper()
            # to check if user input is in the file contents
            if customer in lines:
                address = 'delivery_address'
                with open(address, 'r') as b:
                    read_file = b.read()
                    print(f"The customer's address is: \n {read_file}")
                # to check if user input is also in the second file"s contents
                # if the user's input is in both files, it confirms there is a match, if not, it lets the user know.
                if customer in read_file:
                    print("THERE IS A MATCH. YOU CAN PACKAGE THEIR ORDER.")
                else:
                    print("THERE IS NO MATCH. PLEASE SELECT ANOTHER CUSTOMER")

            else:
                print("Customer name unidentified.")
        else:
            print("THERE ARE NO ORDERS TODAY.")


# the methods above are static methods because there are more than one object and each object is able to perform the
# same functionalities, so it was convenient to call the method using the Class name instead of the objects' name
staff1 = Delivery("ALEX", 800)
staff2 = Delivery("HARRY", 900)
staff3 = Delivery("WILLIAM", 700)
staff = [staff1.__dict__,
         staff2.__dict__,
         staff3.__dict__]


# this function controls the flow of the program in this file.

def delivery_menu():
    print("WELCOME TO THE DELIVERY PORTAL, EMPLOYEE.\n TO BEGIN LOGIN BELOW.")
    name = input("Enter your name: ").upper()
    id_num = int(input("Enter your 3 digit employee identification number: "))
    for worker in staff:
        # if user input matches the Delivery class instances then they are granted access.
        if name == worker['name'] and id_num == worker['id_num']:
            print(f"WELCOME, {name}.\nCHOOSE WHICH CUSTOMER ORDER TO PACKAGE.")
            break
    else:
        print("Invalid entries.")
        exit()
    # the customers_orders function is called using the class name.
    Delivery.customer_orders()
    choice = input("Do you want to handle another customer's order? ").lower()
    if choice == "yes":
        Delivery.customer_orders()
    elif choice == "no":
        print("You have exited the program.")
    else:
        print("Invalid choice.")
