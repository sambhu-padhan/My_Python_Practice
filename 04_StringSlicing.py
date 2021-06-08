# String Slicing..................
# Syntax---print(mystr[srart:end:skip])

                                                                            # OUTPUT
mystr= "Sambhu is a bad boy."
print(mystr)                                                                # Sambhu is a bad boy.
print(mystr[0:20])                                                          # Sambhu is a bad boy.
print(len(mystr))                                                           # 20
print(mystr[0])                                                             # S
print(mystr[5:10])                                                          # u is
print(mystr[0:20:2])                                                        # Smh sabdby
print(mystr[::])                                                            # sambhu is bad boy.

# print(mystr[-4:-1:0])                                                       # ValueError: slice step cannot be zero
print(mystr[-8:20:1])                                                       # bad boy.
print(mystr[-8:20:2])                                                       # bdby


print(mystr.endswith("boy"))                                                # False
print(mystr.endswith("boy."))                                               # True

mystr= "sambhu is a bad boy."
print(mystr.capitalize())                                                   # Sambhu is a bad boy.
print(mystr.count("a"))                                                     # 3
print(mystr.count(" "))                                                     # 4
