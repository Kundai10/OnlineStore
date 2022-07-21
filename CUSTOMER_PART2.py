from CUSTOMER import customers
from CUSTOMER import customer1, customer2, customer3
from PRODUCT import cakes
import json
import time

# TO RUN CODE IN THIS FILE, RUN THE W13_A5_Q2_RUN_THIS_FILE, FILE AND INPUT 1.

# imported json so that I can be able to append dictionaries to my files.
# it is impossible to append a dictionary to a textfile. To do that, JSON is used.
# imported the time module to so as to use delay the execution of the program with some seconds.
# imported the cakes variable which contained a list of dictionaries from the Product objects.
# imported the objects from the CUSTOMER.py file.

# if the user's input to login matches the information in the Customer class instances, then they can shop.
print("WELCOME TO KUDE SHOPS!\n   ")
print("TO BEGIN PLEASE LOGIN")
name = input("Input your first name only: ").upper()
id_num = int(input("Enter your 2 digit password: "))
for customer in customers:
    if name == customer['name'] and id_num == customer['id_num']:
        print(f"\n WELCOME {name}!\n TO BEGIN SHOPPING CHECK THE MENU BELOW.")
        break
else:
    print("Invalid choice.")
    exit()


# this function allows a user to add things to his/her cart.

def add_to_cart():
    if id_num == 11:
        customer1.add_to_cart()
    elif id_num == 12:
        customer2.add_to_cart()
    elif id_num == 13:
        customer3.add_to_cart()
    else:
        print("Invalid choice.")


# this allows a user to remove items from his/her cart.
def remove_cart():
    if id_num == 11:
        customer1.remove_cart()
    elif id_num == 12:
        customer2.remove_cart()
    elif id_num == 13:
        customer3.remove_cart()
    else:
        print("Invalid choice")


# this allows a user to generate bill and then their name, id_number and shopping cart history will be appended to
# their file. Each customer has their own file.
# used JSON because the information being appended is a dictionary.
# the user's shopping history is appended to a file after they have paid their bill or cancelled their order.
# if they quit the program before payment, NOTHING WILL BE APPENDED.
def generate_bill():
    if id_num == 11:
        customer1.generate_bill()
        file_name = 'client1_order_history'
        j = json.dumps(customers[0])
        with open(file_name, 'a+') as f:
            f.write(j)
            f.write(' ')
            f.close()
    elif id_num == 12:
        customer2.generate_bill()
        file_name = 'client2_order_history'
        j = json.dumps([customers[1]])
        with open(file_name, 'a+') as f:
            f.write(j)
            f.write(' ')
            f.close()
    elif id_num == 13:
        customer3.generate_bill()
        file_name = 'client3_order_history'
        j = json.dumps(customers[2])
        with open(file_name, 'a+') as f:
            f.write(j)
            f.write(' ')
            f.close()
    else:
        print("Invalid choice")


# allows a user to view their order history depending on their id_number. Each user has a different file to read.
# the program first checks if there is any information in their files and returns feedback depending on whether the
# file is empty or not.
# introduced the try, finally clause so that even if the program encounters an error, the file will be closed.
def view_order_history():
    print("SEE YOUR ORDER HISTORY BELOW:")
    time.sleep(1)
    if id_num == 11:
        try:
            file_name = 'client1_order_history'
            with open(file_name, 'r') as f:
                lines = f.readlines()
            if len(lines) > 0:
                print(lines)
            else:
                print("Your order history is empty. You haven't made any orders yet.")
        finally:
            f.close()

    elif id_num == 12:
        try:
            file_name = 'client2_order_history'
            with open(file_name, 'r') as f:
                lines = f.readlines()
            if len(lines) > 0:
                print(lines)
            else:
                print("Your order history is empty. You haven't made any orders yet.")
        finally:
            f.close()
    elif id_num == 13:
        try:
            file_name = 'client3_order_history'
            with open(file_name, 'r') as f:
                lines = f.readlines()
            if len(lines) > 0:
                print(lines)
            else:
                print("Your order history is empty. You haven't made any orders yet.")
        finally:
            f.close()

    else:
        print("Invalid choice")


# the user can give a review.
# used JSON since the information being appended is in the form of a dictionary.
def review():
    print("Thank you for shopping with us!\n How would you rate our services please? It helps us improve.")
    print("Input any number between 1-5, with 5 being the best shopping experience and 1 being the least")
    print("YOUR FEEDBACK WILL REMAIN ANONYMOUS.")

    customer_rating = int(input("5/4/3/2/1: "))
    customer_review = input("Please add a comment: ")
    feedback = {'customer_rating': customer_rating, 'customer_comment': customer_review}
    reviews = 'shop_reviews'
    d = json.dumps(feedback)
    with open(reviews, 'a+') as r:
        r.write(d)
        r.write(' ')
        r.close()
    print("Thank you! It helps us improve.")


# this function controls the flow of the program in this file.
def customer_menu():
    while True:
        time.sleep(1)
        print('''\n
        Enter 1 to add items to cart
        Enter 2 to remove items from cart
        Enter 3 to generate bill and proceed to checkout
        Enter 4 to give a review
        Enter 5 to display and see the products in store.
        Enter 6 to view your order history.
        Enter 7 to exit code.
            ''')
        try:
            user_input = int(input("Which method would you want to perform?: "))
            if user_input == 1:
                add_to_cart()
            elif user_input == 2:
                remove_cart()
            elif user_input == 3:
                generate_bill()
                # this appends order history for ALL customers instead of only one. The file will be read by the
                # employees the user's shopping history is appended to a file after they have paid for their goods or
                # cancelled their order. if they quit their program before payment or cancelling their order,
                # NOTHING WILL BE APPENDED TO THE FILE
                file_name = 'customer_order_history'
                j = json.dumps(customers)
                with open(file_name, 'a+') as f:
                    f.write(j)
                    f.write(' ')
                    f.close()
            elif user_input == 4:
                review()
            elif user_input == 5:
                print(cakes)
            elif user_input == 6:
                view_order_history()
            elif user_input == 7:
                print("You have exited the shop.")
                exit()
            else:
                print("Invalid choice")
                exit()
        except ValueError:
            print("Please enter a number.")

