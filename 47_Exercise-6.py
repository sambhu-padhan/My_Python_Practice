ls = []
print("How many values to be stored in the list :",end=" ")
inp = (input())

while inp.isalpha() :
    print("Invalid Keyword....")
    print("How many values to be stored in the list :", end=" ")
    inp = (input())
    if inp.isnumeric()  :
        print("ok")
        break
    else :
        continue

inp = int(inp)
for i in range(inp) :
    print("Enter the values for list :",end=" ")
    inp = (input())
    ls.append(inp)
print(ls)