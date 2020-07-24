'''
Given an integer, n, perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 10, print Weird
If n is even and greater than 20, print Not Weird
'''

import random

n = random.randint(1,100)
print(n)

if n%2 == 1:
    print("Weird")
elif 2<=n<=5 and n%2 == 0:
    print("Not Weird")
elif 6<=n<=20 and n%2 == 0:
    print("Weird")
elif n>20:
    print("Not Weird")
