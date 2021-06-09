#  Write a program to check
#  the person is able to drive or not........


print("Enter your age :")
x = int(input())

if 100>x > 18 :
    print("You are Eligible for driving.")
elif x == 18 :
    print("We will think about it.")
else :
    if x>100:
        print("Please enter a supportive age.")
    else :
        print("You have to wait for few years...")
