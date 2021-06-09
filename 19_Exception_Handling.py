#  try...accept...concept in python

print("Enter first number :",end = " ")
num1 = input()
print("Enter second number :", end = " ")
num2 = input()

try :
    print("The sum of these two numbers is :", int(num1) + int(num2))
except Exception as e :
        print(e)                                                          # invalid literal for int() with base 10: 'a'

print("This line is very important.")


""" OUTPUT
Enter first number : 11
Enter second number : a
invalid literal for int() with base 10: 'a'
This line is very important.
"""