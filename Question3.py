'''
Write a class called Investment with fields called principle and interest. The constructor should set the values of
those fields. There should be a method called value_after that returns the value of the investment after n years. The
formulae for this is p(1+i)n, where p is the principle, and i is the interest rate. It should also use the special
method __str__ so that priniting the object will result in something like below:

Principal - $1000.00, Interest rate – 5.12%
'''

class Investment:
    def __init__(self,principle,interest):
        self.principle = principle
        self.interest = interest

    def __str__(self):
        return 'Principle - ${self.principle}, Interest rate - {self.interest}'.format(self=self)

    def value_after(self, year):
        rate = self.principle*((1 + self.interest)**year)
        return rate








