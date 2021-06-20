#.....Object Introspection.......
class Employee :
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{self.fname}{self.lname}@codewithSambhu.com"
    def explain(self):
        return f"This Employee is {self.fname} {self.lname}"
    @property
    def email(self):
        if self.fname==None or self.lname==None :
            return f"email is not set, please set it using setter."
        return f"{self.fname}.{self.lname}@codewithSambhu.com"

    @email.setter
    def email(self, string):
        print("Setting now....")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None
skillf = Employee("Skill","F")
# print(skillf.email)
#
# print(type("This is a string"))                     # <class 'str'>
# print(id("This is a string"))                       # 20069936
# print(id("This"))                                   # 21221888 id - not same
o = "this is string"
# print(dir(0))               # ['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']

import inspect
print(inspect.getmembers(skillf))           #[('__class__', <class '__main__.Employee'>), ('__delattr__', <method-wrapper '__delattr__' of Employee object at 0x01410FD0>), ('__dict__', {'fname': 'Skill', 'lname': 'F'}), ('__dir__', <built-in method __dir__ of Employee object at 0x01410FD0>), ('__doc__', None), ('__eq__', <method-wrapper '__eq__' of Employee object at 0x01410FD0>), ('__format__', <built-in method __format__ of Employee object at 0x01410FD0>), ('__ge__', <method-wrapper '__ge__' of Employee object at 0x01410FD0>), ('__getattribute__', <method-wrapper '__getattribute__' of Employee object at 0x01410FD0>), ('__gt__', <method-wrapper '__gt__' of Employee object at 0x01410FD0>), ('__hash__', <method-wrapper '__hash__' of Employee object at 0x01410FD0>), ('__init__', <bound method Employee.__init__ of <__main__.Employee object at 0x01410FD0>>), ('__init_subclass__', <built-in method __init_subclass__ of type object at 0x01429788>), ('__le__', <method-wrapper '__le__' of Employee object at 0x01410FD0>), ('__lt__', <method-wrapper '__lt__' of Employee object at 0x01410FD0>), ('__module__', '__main__'), ('__ne__', <method-wrapper '__ne__' of Employee object at 0x01410FD0>), ('__new__', <built-in method __new__ of type object at 0x542F6B78>), ('__reduce__', <built-in method __reduce__ of Employee object at 0x01410FD0>), ('__reduce_ex__', <built-in method __reduce_ex__ of Employee object at 0x01410FD0>), ('__repr__', <method-wrapper '__repr__' of Employee object at 0x01410FD0>), ('__setattr__', <method-wrapper '__setattr__' of Employee object at 0x01410FD0>), ('__sizeof__', <built-in method __sizeof__ of Employee object at 0x01410FD0>), ('__str__', <method-wrapper '__str__' of Employee object at 0x01410FD0>), ('__subclasshook__', <built-in method __subclasshook__ of type object at 0x01429788>), ('__weakref__', None), ('email', 'Skill.F@codewithSambhu.com'), ('explain', <bound method Employee.explain of <__main__.Employee object at 0x01410FD0>>), ('fname', 'Skill'), ('lname', 'F')]
