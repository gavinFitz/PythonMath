"""
Author: Goat
Prints out the multiplication table of a number entered by the user up to 12.
input: integer
output: example:    1 * 1 = 1
                    2 * 1 = 2
                    .....
                    12 * 1 = 12
Version: 1
Date: 07/06/2016
"""


def MULT_Table(x, y):
    for i in range(1, y + 1):
        print("{0} x {1:.4f} = {2:.4f}".format(i, x, x * i))


while True:
    try:
        choice = input("Do you want to create a multiplication table? (yes/no)")
        if choice == "yes":
            while True:
                try:
                    x = float(input("Please enter a number whose multiplication table you want: "))
                    y = int(input("Please enter a number limiting the length of the table: "))
                    MULT_Table(x, y)
                    break
                except ValueError:
                    print("You entered an invalid number")
        if choice == "no":
            break
        if choice != "yes" and choice != "no":
            print("Invalid input")
    except ValueError:
        print("Invalid input")
