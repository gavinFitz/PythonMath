'''
Author: Goat
determines the roots of an inputted quadratic equation
Version: 1
Date: 07/06/2016
'''
def Roots(a, b, c):
    D = (b*b - 4*a*c)**0.5
    x_1 = (-b + D)/(2*a)
    x_2 = (-b - D)/(2*a)
    print('x1: {0}'.format(x_1))
    print('x2: {0}'.format(x_2))

print("Your Quadratic sum should be in the form ax*2 + bx + c.")
print("To Get the roots of the sum: ")
a = float(input('Enter a: '))
b = float(input('Enter b: '))
c = float(input('Enter c: '))
Roots(a, b, c)
