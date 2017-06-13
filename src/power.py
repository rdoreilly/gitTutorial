""" This is a script that calculates one number to the power of another """
import math, sys

def to_the_power(x,y):
    """ return x to the power of y"""
    return x**y

def square_root(x):
    return math.sqrt(x)

x = int(sys.argv[1])
y = int(sys.argv[2])

result = to_the_power(x,y)

print ("{0} to the power of {1} is {2}".format(x,y,result))
print ("The square root of {0} {1}".format(x,square_root(x))) #
