"""
Author: Goat
prints all the factors of a positive integer, all the numbers that divide
evenly into a number are it's factors.
Version: 1
Date: 07/06/2016
reduced processing time by limiting the search to half of the number
Version: 2
Date: 09/06/2016
"""


def Factors(x):
    for i in range(1, int((x / 2) + 1)):
        if x % i == 0:
            print(i)
    print(x)

while True:
    choice = input("Do you want to get the factors of a number? (yes/no)")
    if choice == "yes":
        while True:
            try:
                x = int(input("Please Enter a Positive Integer: "))
                # if the number is positive
                if x > 0:
                    Factors(x)
                    break
                else:
                    print("try entering a positive integer not a negative one.")
            except ValueError:
                print("You entered an invalid number.")
    if choice == "no":
        break
    if choice != "no" and choice != "yes":
        print("Invalid input, enter yes or no.")