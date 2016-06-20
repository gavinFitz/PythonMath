"""
Author: Goat
1) Prints whether the inputted number is even or odd
2) Prints the following nine even/odd numbers
Version: 1
Date: 07/06/2016
"""


def Even_Odd(x):
    i = 9
    a = x
    if x % 2 == 0:
        print("Even")
        while i > 0:
            a += 1
            if a % 2 == 0:
                print(a)
                i -= 1
    else:
        print("Odd")
        while i > 0:
            a += 1
            if a % 2 != 0:
                print(a)
                i -= 1


print("Enter a number to see if it is even or odd, or enter END to stop the program.")
while True:
    x = input("Enter an integer: ")
    if x == "END":
        break
    else:
        try:
            Even_Odd(int(x))
        except ValueError:
            print("Invalid input")
