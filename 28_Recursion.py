# .......Recursion in python.......

def factorial(n) :
    fac = 1
    for i in range(n) :
        fac = fac * (i+1)
    return fac
def fact(n) :
    if n == 1 :
        return 1
    fac = n * fact(n-1)
    return fac
print("Enter a Number :",end = " ")
n =  int(input())
x = factorial(n)
y = fact(n)
print("Factorial using Iterative method : ",x)
print("Factorial using Recursion method : ",y)
