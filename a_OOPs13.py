#### Diamond problem


class A :
    def method(self):
        print("I am from class A")
class B(A) :
    pass
class C(A) :
    pass
class D(B,C) :
    pass

a = A()
b = B()
c = C()
d = D()

d.method()                         #  I am from class A