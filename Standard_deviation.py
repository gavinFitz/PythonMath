"""
Author: Goat
determines the standard deviation of an inputted list of numbers
Version: 1
Date: 07/06/2016
"""

def Mean(List):
    s = sum(List)
    l = len(List)
    mean = s / l
    return mean

def Deviation(List):
    mean = Mean(List)
    total = 0
    for j in range(1, len(List)):
        total += (List[j]-mean)**2
    return (total/len(List)-1)**0.5

while True:
    execute = input("Do you want to calculate the standard deviation of a list of numbers? (y/n)")
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
                    print("The standard deviation is " + str(Deviation(List)))
                break
            if choice != "y" and choice != "n":
                print("Invalid input")
    if execute == "n":
        break
    if execute != "n" and execute != "y":
        print("Invalid input")