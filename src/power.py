def to_the_power(x,y=2):
    result=x
    for i in range(0,y):
        result = result * x
    return result
x = 6 #
y = 5
print ("{0} to the power of {1} is: ".format(x,y,to_the_power(x,y)))
print ("The End")
