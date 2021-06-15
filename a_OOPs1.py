# OOPs start
# classes - Template
class student :
    pass

sambhu = student()
chetan = student()

# print(sambhu,chetan)                   # <__main__.student object at 0x0062A028> <__main__.student object at 0x0062A040>

sambhu.name = "Sambhu"
sambhu.std = 12
sambhu.section = 1
print(sambhu.name,sambhu.section)           # Sambhu 1
chetan.subjects = ["English","Sambalpuri"]
print(chetan.subjects)                      # ['English', 'Sambalpuri']
