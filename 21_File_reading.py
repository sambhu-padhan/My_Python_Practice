# # file reading in python
#
# i = open("Sambhu.txt", "rt")
# content = i.read(344)
# print(content)                                 # Sambhu is a bad boy.
#
# content = i.read(344)
# print(content)                                 # Sambhu is very intelligent.
#
#
# content = i.read(344)
# print("1", content)                                 # 1
# content = i.read(344)
# print("2", content)                                 # 2
#
# i.close()
#
# i = open("Sambhu.txt", "rt")
# content = i.read(344)
# print("1", content)                                 # 1 Sambhu is a bad boy.
#                                                     # Sambhu is very intelligent.
# content = i.read(344)
# print("2", content)                                 # 2                   # ignore all


i = open("Sambhu.txt", "rt")
# content = i.read()

# for line in content :
#     print(line)

# for line in i :
#     print(line, end = "")                       # Sambhu is a bad boy.
                                                 # Sambhu is very intelligent.


# print(i.readline())                               # Sambhu is a bad boy.
# print(i.readline())                               # Sambhu is very intelligent.
print(i.readlines())                                # ['Sambhu is a bad boy.\n', 'Sambhu is very intelligent.\n']
i.close()
