# Find execution time
# local time,current time

import time
# initial = time.time()
# print(initial)                          # 1622633956.379167
#
# k = 0
# while(k<5) :
#     print("This is Sambhu.")
#     k+=1
# print("while loop took ",initial,"seconds")                 # while loop took  1622634228.8804457 seconds
#
# initial2 = time.time()
# for i in range(5) :
#     print("this is Sambhu.")
# print("for loop took ",initial2,"seconds")                  # while loop took  1622634228.8804457 seconds

local_time = time.asctime(time.localtime(time.time()))
print(local_time)                                           # Wed Jun  2 17:15:43 2021
