""" This is a script that calculates one number to
    power of another
"""

def to_the_power(x,y=2):
    result=x
    for i in range(0,y):
        result = result * x
    return result

x = 2
y = 5 #

print ("{0} to the power of {1} is: ".format(x,y,to_the_power(x,y)))
print ("The End")
