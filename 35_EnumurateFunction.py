# enumurate


s1 = ["chawal", "Sabji", "chicken", "Egg"]

i = 1
# for item in s1 :
#     if i%2 is not 0 :
#         print(f"Sambhu please buy {item}")
#     i+=1

for index,item in enumerate(s1) :
    if index%2==0 :
        print(f"Sambhu please buy {item}")


"""OUTPUT

Sambhu please buy chawal
Sambhu please buy chicken

"""
