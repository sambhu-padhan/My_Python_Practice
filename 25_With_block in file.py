# ....Using with block to open python files.....
#  BY USING WITH WE CAN IGNORE THE CLOSE FUNCTION AND ALL.


with open("Sambhu.txt") as f :
    # a = f.read(4)
    # print(a)                                # harr
    a = f.read()
    print(a)

""" OUTPUT
harry bhai bahut achche hein 
thank you.
More line
Add more lines.
"""

f = open("Sambhu.txt", "rt")
print(f.readlines())                    # ['harry bhai bahut achche hein \n', 'thank you.\n', 'More line\n', 'Add more lines.\n']
print(f.readline())                       # harry bhai bahut achche hein

# f.close()