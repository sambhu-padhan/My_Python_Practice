#  seek(),tell() and more on python files

# f = open("Sambhu.txt")
# # print(f.tell())                             # 0
# # print(f.readline())                         # harry bhai bahut achche hein
# # print(f.tell())                             # 31
# # print(f.readline())                         # thank you.
# # print(f.tell())                             # 43
# # # print(f.readline())

f = open("Sambhu.txt")
# print(f.tell())
print(f.readline())                           # harry bhai bahut achche hein
# print(f.tell())
f.seek(0)                                     # harry bhai bahut achche hein
print(f.readline())
f.seek(13)
print(f.readline())                           # hut achche hein
# print(f.tell())

f.close()
