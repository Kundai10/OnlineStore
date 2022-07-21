# wrapped the entire program on this file in try, except clauses to prevent the program from crashing when a user
# inputs a string.
# RUN THIS FILE TO RUN THE ENTIRE PROGRAM FOR THE ONLINE SHOP.

try:

    choice = int(
        input("Enter 1 if you are a CUSTOMER. Enter 2 is you are an ADMIN. Enter 3 if you handle DELIVERIES : "))
    if choice == 1:
        from CUSTOMER_PART2 import customer_menu

        customer_menu()
    elif choice == 2:
        from ADMIN import admin_menu

        admin_menu()
    elif choice == 3:
        from DELIVERY import delivery_menu
        delivery_menu()
    else:
        print("Invalid choice.")
except ValueError:
    print("Please enter a number.")
