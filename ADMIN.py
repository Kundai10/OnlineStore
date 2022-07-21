from PRODUCT import cakes


# TO RUN CODE IN THIS FILE, PLEASE RUN THE CODE IN THE W13_A5_Q2_RUN_THIS_FILE, FILE AND INPUT 2.
# imported the cakes variable which contained a list of dictionaries from the Product objects.

class Admin:
    def __init__(self, name, id_num):
        self.name = name
        self.id_num = id_num

    # this method allows a user to add new products to the shop, ie, the list of dictionaries.
    @staticmethod
    def add_new_product():
        cake_flavour = input("Cake Flavour ")
        price = input("Price ")
        pieces = input("Pieces ")
        quantity = input("Quantity ")
        sales = input("Sales ")
        new_cake = {"cake_flavour": cake_flavour, "Price": price, "Pieces": pieces, "Quantity": quantity,
                    "Sales": sales}
        cakes.append(new_cake)
        print("PRODUCT ADDED SUCCESSFULLY. BELOW ARE ALL THE CAKES PRESENT IN STORE.")
        print(cakes)

    # this method allows a user to remove an object from the list of dictionaries, ie, the shop
    @staticmethod
    def remove_product():
        cake_name = input("Enter cake name to be removed: ").lower()
        for cake in cakes:
            if cake.get("name") == cake_name:
                cakes.remove(cake)
                print("PRODUCT REMOVED SUCCESSFULLY. BELOWS ARE ALL PRODUCTS IN STORE.")
                print(cakes)
                break

        else:
            print("Product unavailable.")
            print("SEE PRODUCTS IN STORE:")
            print(cakes)


# the methods above are static methods because there are more than one object and each object is able to perform the
# same functionalities, so it was convenient to call the method using the Class name instead of the objects' name
# these are Admin class objects
admin1 = Admin("SMITH", 2345)
admin2 = Admin("BROWN", 2346)
admin3 = Admin("BARKER", 2347)
admins = [admin1.__dict__,
          admin2.__dict__,
          admin3.__dict__]


# this function enables a user to read the customer reviews made by the customers.
# it first checks if the file has any contents inside by using the len() function, and it prints the appropriate
# feedback depending on whether there is content in the file or not.
def read_reviews():
    try:
        print("BELOW ARE THE CUSTOMER REVIEWS. \n THE CUSTOMER IDENTITIES ARE ANONYMOUS.")
        reviews = 'shop_reviews'
        with open(reviews, 'r') as file_name:
            lines = file_name.read()
        if len(lines) > 0:
            print(lines)
        else:
            print("NO REVIEWS HAVE BEEN WRITTEN YET.")
    # included a try, finally clause so that even if the program encounters an error, the file would be closed.
    finally:
        file_name.close()



# the admin_menu method controls the whole flow of the program in this file.
# the admin first logs in and then prompted to perform the action they want.
def admin_menu():
    print("WELCOME EMPLOYEE\n   ")
    print("TO BEGIN PLEASE LOGIN.")
    name = input("Input your name: ").upper()
    id_num = int(input("Enter your 4 digit employee identification number: "))
    for admin in admins:
        # if user input matches the information of Admin class instances then they are granted access.
        if name == admin['name'] and id_num == admin['id_num']:
            print(f"\n WELCOME TO THE INVENTORY PORTAL, {name}. \n YOU CAN ADD OR REMOVE PRODUCTS IN SHOP.")
            break
    else:
        print("Invalid entries")
        exit()
    while True:
        print(''', 
        Enter 1 to add a new product to the store
        Enter 2 to remove a product from the store
        Enter 3 to read customer reviews
        Enter 4 to view all cakes in store.
        Enter 5 to exit the program.
        ''')
        # wrapped the bottom code in try, except clauses so as to prevent the program from crashing when the user
        # inputs a string instead of a integer.
        try:
            user_input = int(input("Which method do you want to perform?: "))
            if user_input == 1:
                Admin.add_new_product()
            elif user_input == 2:
                Admin.remove_product()
            elif user_input == 3:
                read_reviews()
            elif user_input == 4:
                print(cakes)
            elif user_input == 5:
                print("You have exited the shop.")
                exit()
            else:
                print("Invalid choice")
                exit()
        except ValueError:
            print("Please enter a number.")
