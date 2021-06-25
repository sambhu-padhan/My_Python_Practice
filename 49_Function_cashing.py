# #...Function Cashing....
#
# import time
# from functools import lru_cache
#
# @lru_cache(maxsize=20)              #   after 20 values it will skip the time of function
# def some_work(n) :
#     time.sleep(n)
#     return n
#
#
# if __name__ == '__main__':
#     print("NOw running some_work....")
#     some_work(3)
#     print("xxx")
#     some_work(5)
#     print("ccasdc")
#     some_work(6)
#     print("rrrasdsad")
#     some_work(3)
#     print("time skipped and returned suddenly....")

#...........Exercise......................
# main()....q-enter

import time
from functools import lru_cache

print("Enter size of the cache :",end=" ")
inp = int(input())


@lru_cache(maxsize=inp)
def return_value(n) :
    time.sleep(n)
    return n
print("start...")
return_value(5)
print("time not skipped")
return_value(7)
print("tine not skipped")
return_value(5)
print("time skipped")
return_value(5)
print("time skipped")

