#....Exercise-8......
import os

def soldier(path,list,ext):
    os.chdir(path)
    ls = os.listdir(path)
    i = 1
    for item in ls:
     if item in list:
      continue
     elif item.__contains__("."):
            if item.endswith(f"{ext}"):
                os.rename(f"{item}", f"{i}.{item}")
                i += 1
            else:
                cap = item.capitalize()
                os.rename(f"{item}", f"{cap}")



#........Program start here........

print("Enter path to Prettify that :",end=" ")
while True :
    path = input()
    if os.path.exists(path) :
        print(os.listdir(path))
        break
    else:
        print("Please Enter valid Path :",end=" ")
print("Enter number of important files :",end=" ")
inp1 = int(input())
list = []
i = 0
for item in range(inp1):
    print(f"Enter important file name {i+1} :",end=" ")
    inp = input()
    list.append(inp)
    i+=1
print("Enter file Extension for Prettify :",end=" ")
ext = input()
print("Soldier Called...")
soldier(path,list,ext)
ls = os.listdir(path)
print(ls)
#.....end........

#  ....OUTPUT.....
# Enter path to Prettify that : d://Soldier
# ['a_oops1.py', 'a_oops2.py', 'a_oops3.py', 'cbvcb.txt', 'important.jpg', 'newsambhu1.jpg', 'originals', 'stock-photo.jpg']
# Enter number of important files : 2
# Enter important file name 1 : important.jpg
# Enter important file name 2 : cbvcb.txt
# Enter file Extension for Prettify : .jpg
# Soldier Called...
# ['1.newsambhu1.jpg', '2.stock-photo.jpg', 'A_oops1.py', 'A_oops2.py', 'A_oops3.py', 'cbvcb.txt', 'important.jpg', 'originals']

