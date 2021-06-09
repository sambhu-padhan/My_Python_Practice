# Functions in Python
# doc string in Python

"""
x = 10
y = 12
z = sum((x,y))                      # Built-in Function
print(z)                            #  22
"""

def Fun1(a,b) :
    print("Hello you are in function1 :", a+b)             #  Hello you are in function1 : 4


def fun2(a,b) :
    """This is a function which will calculate average of two numbers
            this function does not work for three numbers."""
    avg = (a+b)/2
    print(avg)                                             #  2.0
    return avg

x = fun2(1,3)
print(x)                                                   #  2.0
print(fun2.__doc__)                                        # This is a function which will calculate average of two numbers

