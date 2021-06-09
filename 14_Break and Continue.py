


"""
i = 1
while (i<45) :
    print(i, end = " ")
    i = i+1
"""
"""
i = 0
while(True) :
    if i+1>5 :
        continue
    print(i, end =" ")                                      #   0 1 2 3 4 
    if(i == 44):
        break
    i = i+1
"""
"""
i = 1
while(True) :
    if i<5 :
        i = i + 1
        continue
    print(i, end =" ")                # 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44
    if(i == 44):
        break
    i = i+1
"""



while(True) :
    print("Enter your number : ",end  = "")
    x = int(input())
    if(x<100) :
        print("Try again..")
        continue
    else :
        print("Congratulations, You have entered greater number.")
        break


"""  output

Enter your number :  12
Enter your number :  111
Congratulations, You have entered greater number.

"""