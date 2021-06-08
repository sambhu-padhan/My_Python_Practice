# LIST IN PYTHON.........
                                                                                    #  OUTPUT
grocery = ["Harpic" , "vim bar" , "deodrant" , "Bhindi" , "Lolypop"]
print(grocery)                                                                 # ['Harpic', 'vim bar', 'deodrant', 'Bhindi', 'Lolypop']
grocery = ["Harpic" , "vim bar" , "deodrant" , "Bhindi" , "Lolypop" , 55]
print(grocery)                                                                 # ['Harpic', 'vim bar', 'deodrant', 'Bhindi', 'Lolypop', 55]
print(grocery[4])                                                              # Lolypop
#print(grocery[6])                                                              # IndexError: list index out of range
"""
numbers = [1 , 4 , 5 , 6 , 3]
print(numbers)                                                                # [1, 4, 5, 6, 3]
numbers.sort()
print(numbers)                                                                # [1, 3, 4, 5, 6]    (sorted)
numbers.reverse()
print(numbers)                                                                # [6, 5, 4, 3, 1]
"""

numbers = [1 , 4 , 5 , 6 , 3]
#print(numbers[0:5:2])                                                         # [1, 5, 3]
numbers.append(23)
numbers.append(4)
print(numbers)                                                                 # [1, 4, 5, 6, 3, 23, 4]

numbers.insert(3,111)
print(numbers)                                                                 # [1, 4, 5, 111, 6, 3, 23, 4]

numbers.remove(111)
print(numbers)                                                                 # [1, 4, 5, 6, 3, 23, 4]

numbers.pop()
print(numbers)                                                                 # [1, 4, 5, 6, 3, 23]

numbers[1] = 55
print(numbers)                                                                 # [1, 55, 5, 6, 3, 23]


######..............TUPLE....................***********
#  tuple is immutable.....i.e... value can not be change...

tp = (1,2,3)
print(tp)                                                                       # (1, 2, 3)

# tp[1] = 4
# print(tp)                                                                       # TypeError: 'tuple' object does not support item assignment

a = 2
b = 3
print(a,b)                                                                      # 2 3
temp = a
a = b
b = temp
print(a,b)                                                                      # 3 2

a,b = b,a
print(a,b)                                                                      # 2 3
