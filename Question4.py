
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




