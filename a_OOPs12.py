##  .....Overriding......
##   ....super class...

class A :
    classvar1 = "I am a class var in class A "
    def __init__(self):
        self.var1 = "I am inside class A's constructor"
        self.classvar1 = "Instance variable in class A"
        self.special = "special"
class B(A) :
    classvar1 = "I am in class B"
    def __init__(self):

        self.var1 = "I am inside class B's constructor"
        self.classvar1 = "Instance var in class B"
        super().__init__()
        print(super().classvar1)                        # I am a class var in class A

a = A()
b = B()

print(b.special,b.var1,b.classvar1)            # special I am inside class A's constructor Instance variable in class A