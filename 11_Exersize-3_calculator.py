# ......Exersize 2 - Faulty Calculator........
# Design a calcolator which will correctly solove all the problems
# except the following ones :
#             45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Your program should take opaerator and the two numbers as input from and then return the result.


types = ["*","+","-","/"]
list1 = [{"*","-","+","/"}]
#print(type(numbers))
print(types)

print("Choose your Calculation Operator :", end  = "\t")
ctype = input()
if  ctype in types :
    if ctype == "+" :
       print("Enter first number :", end = "\t")
       x = int(input())
       print("Enter second number :", end = "\t")
       y = int(input())
       if x==56 and y==9 :
           print("\t\t\t56 + 9 = 77")
       else :
           print("\t\t\t",x,"+",y ,"=", x+y)

    elif ctype == "*" :
       print("Enter first  number :", end = "\t")
       x = int(input())
       print("Enter second number :", end = "\t")
       y = int(input())
       if x==45 and y==3 :
           print("\t\t\t45 * 3 = 555")
       else :
           print("\t\t\t", x ,"*", y, "=" ,x*y)

    elif ctype == "-" :
       print("Enter first  number :", end = "\t")
       x = int(input())
       print("Enter second number :", end = "\t")
       y = int(input())
       print("\t\t\t",x,"-",y ,"=", x-y)

    elif ctype == "/" :
       print("Enter first number :", end = "\t")
       x = int(input())
       print("Enter second number :", end = "\t")
       y = int(input())
       if x==56 and y==6 :
           print("\t\t\t56 / 6 = 4")
       else :
           print("\t\t\t",x,"/",y ,"=", x/y)
else :
  print("Please enter valid symbol from the above list.")
  print("Choose your Calculation Operator :", end="\t")
  ctype = input()



"""  output

['*', '+', '-', '/']
Choose your Calculation Operator :	/
Enter first number :	12
Enter second number :	4
			 12 / 4 = 3.0

"""

#  @Sambhu Padhan