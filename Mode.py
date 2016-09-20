"""
Author: Goat
determines the mode of an inputted list of numbers
Version: 1
Date: 07/06/2016
"""

def Mode(List):
    from collections import Counter
    counter = Counter(List)
    mode = counter.most_common(1)
    return mode[0][0]

while True:
    execute = input("Do you want to find the mode of a list of numbers? (y/n)")
    if execute == "y":
        List = []
        while True:
            choice = input("Do you want to enter a number? (y/n)")
            if choice == "y":
                try:
                    List.append(float(input("Enter a number: ")))
                except ValueError:
                    print("Invalid Input")
                    List = []
                    break
            if choice == "n":
                print("Thank you")
                if len(List) >= 1:
                    print("The mode is " + str(Mode(List)))
                break
            if choice != "y" and choice != "n":
                print("Invalid input")
    if execute == "n":
        break
    if execute != "n" and execute != "y":
        print("Invalid input")