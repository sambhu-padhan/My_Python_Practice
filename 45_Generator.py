#  Generator in python
#  generator will store the value of less number iteration

def gen(n) :
    for i in range(n) :
        yield i

g = gen(7)
# print(g)                # <generator object gen at 0x01311450>
# print(g.__next__())     # 0
# print(g.__next__())     # 1
# print(g.__next__())     # 2
# print(g.__next__())     # 3
# print(g.__next__())     # 4
# print(g.__next__())     # 5
# print(g.__next__())     # 6
# print(g.__next__())     # StopIteration
#
# for i in g:
#     print(i)                # Same

s = "sambhu"
print(iter(s))      #<str_iterator object at 0x007B0FE8>
ier = iter(s)
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())       # Sambhu will be print one by one chaacter

s = 3232  # here in integer generator cannot work




# for c in s :
#     print(c)            # one by one character


