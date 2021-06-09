# .........F-Strings...........
import math
me  = "Sambhu"
a = 1
a1 = "This is %s"%me
print(a1)                           #  This is Sambhu
a2 = "This is %s %s"%(me,a)
print(a2)                           # This is Sambhu 1

a3 = "this is {1} {0}"
b = a3.format(me,a)
print(b)                            # this is 1 Sambhu

a4 = f"this is {me} {a}"
print(a4)                           # this is Sambhu 1

a5 = f"this is {me}{a}{math.cos(65)}"
print(a5)                               # this is Sambhu1-0.562453851238172

