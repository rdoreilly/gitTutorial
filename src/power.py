""" This is a script that calculates one number to
    power of another
"""

def to_the_power(x,y):
#    result = x
#    for i in range(1,y):
#        result = result * x
    return x**y

x = 2
y = 5 #
result = to_the_power(x,y)
print ("This birthday I will be {0} to the power of {1} which makes me: {2}".format(x,y,result))

x = 2
y = 6 #

print ("Next year I will be: {2}".format(x,y,(to_the_power(x,y) - (result - 1))))



print ("The End")
