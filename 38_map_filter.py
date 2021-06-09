# map
# filter
# reduce


# numbers = ["3","34","64"]
#
# # for i in range(len(numbers)) :
# #     numbers[i] = int(numbers[i])
# numbers = list(map(int,numbers))
#
# numbers[2] = numbers[2] + 1
# print(numbers[2])                                       # 65

# numbers = list(map(int,numbers))

# def sq(a) :
#     return a*a

 # num = [2,3,4,5,44,1,3,2]
# # square = list(map(sq,num))
# square = list(map(lambda x:x*x,num))
# print(square)                                      # [4, 9, 16, 25, 1936, 1, 9, 4]
# ############################### map #######
# def square(a) :
#     return a*a
# def cube(a) :
#     return a*a*a
# func = [square,cube]
# for i in range(5) :
#     val = list(map(lambda x:x(i),func))
#     print(val)
################################   Filter   ########

# lisi1 = [1,2,34,5,56,3,2,27,8]
#
# def is_greater_5(num):
#     return num>5
#
# gr_than_5 = list(filter(is_greater_5,lisi1))
# print(gr_than_5)                                        # [34, 56, 27, 8]
############################    Reduce    ###################################
from functools import reduce

lisi1 = [1,2,3,4]
num = reduce(lambda x,y:x+y,lisi1)
# num = 0
# for i in lisi1 :
#     num = num + i
print(num)                                      # 10


