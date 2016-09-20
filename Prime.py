"""
Author: Goat
determines if a number is a prime
Version: 1
Date: 09/08/2016
"""


def IsPrime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


print("Enter a number to see if it is a prime, or enter END to stop the program.")
while True:
    x = input("Enter an integer: ")
    if x == "END":
        break
    else:
        if IsPrime(int(x)):
            print("Is a prime.")
        else:
            print("Not a prime.")
