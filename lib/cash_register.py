#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.total = 0                 # total
        self.discount = discount       # discount
        self.items = []                # list of items
        self.prices = []

    #add item based on price and quanity
    def add_item(self,item,price=0,quantity=1):
        self.item = item
        self.total += price*quantity
        for i in range(quantity):       #loop to add each item added, i is not used
            self.items.append(item)
            self.prices.append(price)
        self.last_transaction = price*quantity
        
    def apply_discount(self):
        if self.discount > 0:
            self.total -= self.total * (self.discount/100)
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        last_item = self.items[:-1]
        self.total -= self.last_transaction
        self.items = last_item