# Receive numbers from users and show it.......
"""                                                                        #  OUTPUTS
print("Enter your number : ")
inpnum = input()
print(inpnum)                                                           #  12
print("You entered  :", inpnum * 10)                                    #  12121212121212121212(10 times 12)
#print("you entered :", inpnum + 10)                                    #  Error(TypeError: can only concatenate str (not "int") to str)
print("You entered :", int(inpnum) + 10)                                #  22    (typecasting)

"""



# add two numbers and print them..............

print("Enter 1st number : ")
x = input()
print("Enter 2nd number : ")
y = input()
print("The sum of these two numbers is : ",int(x)+int(y))

""" 
Enter 1st number : 
11
Enter 2nd number : 
12
The sum of these two numbers is :  23
"""