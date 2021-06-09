#  ....Anonymous/Lamda Functions........
#
# def add(a,b) :
#     return a+b

# minus = lambda a, b : a-b
# # def minus(a,b) :
# #     return a-b
# print(minus(4,1))                                     # 3


def a_first(a) :
    return a[1]

# a = [[1,14],[5,6],[8,23]]
# a.sort(key = a_first)
# print(a)                                    #  [[5, 6], [1, 14], [8, 23]]

a = [[1,14],[5,6],[8,23]]
a.sort(key = lambda x  : x[1])
print(a)                                    # [[5, 6], [1, 14], [8, 23]]
