'''
2.	Write a class called Product. The class should have fields called name, amount, and price, holding the product’s
name, the number of items of that product in stock, and the regular price of the product. There should be a method
get_price that receives the number of items to be bought and return a the cost of buying that many items, where the
regular price is charged for orders of less than 10 items, a 10% discount is applied for orders of between 10 and 99
items, and a 20% discount is applied for orders of 100 or more items. There should also be a method called make_purchase
that receives the number of items to be bought and decrease amount by that much.
'''


class Product:
    def __init__(self, name, amount, price):
        self.name = name
        self.amount = amount
        self.price = price

    def get_price(self):
        global quantity
        global product

        product = input("Enter a Product you want to buy: ")
        quantity = eval(input("Enter the amount you want to buy: "))

        if quantity < 10:
            cost = quantity*self.price
            print("The cost to buy " + str(quantity) + product + " is " + str(cost))

        if 10 < quantity < 99:
            self.price = self.price*0.9
            cost = quantity*self.price
            print("The cost to buy " + str(quantity) + product + " is " + str(cost))

        if quantity > 100:
            self.price = self.price*0.8
            cost = quantity*self.price
            print("The cost to buy " + str(quantity) + product + " is " + str(cost))

    def make_purchase(self):
        self.amount = self.amount - quantity
        print("The amount of " + product + " left is " + str(self.amount))




