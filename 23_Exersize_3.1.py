# Exersize 3.1   ......Q.I COMPLETED THIS EXERSIZE WITH WRONG WAY.....SO TRY AGAIN WITH ACCURACY
# ......Pattern Printing........
# Input = integer n
# Boolean  = True or False
# True n=5
# *
# * *
# * * *
# * * * *
# False n=5
# * * * *
# * * *
# * *
# *

print("Please Enter a number :",end = " ")
num = int (input())
print(num)
x = 1
if num == 5 :
    print("True, Number is equal to 5..\n")
    while x < num :
        print(x * "* ")
        x = x + 1

else :
     print("False, Number is not equal to 5.\n")
     x = 4
     while x >= 1 :
         print(x * "* ")
         x = x-1


"""OUTPUT
Please Enter a number : 12
12
False, Number is not equal to 5.

* * * * 
* * * 
* * 
* 

"""