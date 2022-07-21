class Product:
    def __init__(self, name, price, quantity, sales):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.sales = sales


# these are Product objects

cake1 = Product("vanilla", 30, 20, 10)
cake2 = Product("chocolate", 40, 12, 10)
cake3 = Product("lemon", 50, 12, 10)
cake4 = Product("strawberry", 20, 15, 10)
# the Product objects have been converted into a dictionary by using the __dict__.
cakes = [cake1.__dict__,
         cake2.__dict__,
         cake3.__dict__,
         cake4.__dict__]
# The product class contains the cakes being sold by the store.
