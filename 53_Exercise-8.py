#....Exercise-8......
import os

def soldier(inp):
    os.chdir(inp)
    ls = os.listdir(inp)
    print(ls)
    i = 1
    for item in ls:
        if item.__contains__("."):
            if item.endswith(".jpg"):
                os.rename(f"{item}", f"{i}.{item}")
                i += 1
            elif item.endswith(".txt"):
                pass
            else:
                cap = item.capitalize()
                os.rename(f"{item}", f"{cap}")
        else:
            pass

#........Program start here........

print("Enter path to Prettify that :",end=" ")
while True :
    inp = input()
    if os.path.exists(inp) :
        soldier(inp)
        print("Soldier Called...")
        break
    else:
        print("Please Enter valid Path :",end=" ")
ls = os.listdir(inp)
print(ls)
#.....end........
#  OUTPUT
# Enter path to Prettify that : ASD
# Please Enter valid Path : D://SOLDIER
# ['a_oops1.py', 'a_oops2.py', 'a_oops3.py', 'cbvcb.txt', 'newSambhu.jpg', 'newSambhu1.jpg', 'Originals', 'stock-photo-soldier-on-top-of-the-mountain-with-the-indian-flag-593817638.jpg']
# Soldier Called...
# ['1.newSambhu.jpg', '2.newSambhu1.jpg', '3.stock-photo-soldier-on-top-of-the-mountain-with-the-indian-flag-593817638.jpg', 'A_oops1.py', 'A_oops2.py', 'A_oops3.py', 'cbvcb.txt', 'Originals']
