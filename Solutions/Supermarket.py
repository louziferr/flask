# Exercise: Classes
# This is a class for managing supermarkets.

class Supermarket:
    # Constructor
    def __init__(self):
        self.stock = dict()     # dict with {item: quantity} to keep track of our stock
        self.money = 0.0        # total money our shop has
        self.prices = dict()    # dict with {item: price} to keep track of our prices

    def add_product(self, product, quantity):
        # function to add a product to the stock
        if product not in self.stock:
            self.stock[product] = 0
        self.stock[product] += quantity

    def set_price(self, product, price):
        # function to set the price of a product
        self.prices[product] = price

    def sell(self, product, quantity):
        # function to sell a certain product
        if product in self.stock:                       # check if product is in stock
            if self.stock[product] >= quantity:         # check if we have enough
                self.stock[product] -= quantity         # we have enough and call sell
                income = self.prices[product]*quantity
                self.money += income                    # add money to our money-attribute
            else:
                # raise Error if we don't have enough
                raise ValueError(f'Not enough in stock ({product}).')
        else:
            # just return, if we don't have the product at all
            return