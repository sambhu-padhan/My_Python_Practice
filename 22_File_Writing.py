#......file writing in python.......

# f = open("Sambhu.txt", "w")
# f.write("harry bhai bahut achche hein \n")
#
#
#
# f = open("Sambhu.txt", "a")
# f.write("harry bhai bahut achche hein \n")
# a = f.write("Sambhu dost bahut achcha hein \n")
# print(a)                                                    # 31
#

# handle read and write both


f = open("Sambhu.txt", "r+")
print(f.read())                                                 #  harry bhai bahut achche hein
f.write("thank you.")
f.close()