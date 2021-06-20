#  ....setter and property decorator.....

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


hindustani_supporter = Employee("Hindustani", "Supporter")

# print(hindustani_supporter.explain())                       # This Employee is Hindustani Supporter
# print(hindustani_supporter.email())                           # Hindustani.Supporter@codewithSambhu.com
print(hindustani_supporter.email)
hindustani_supporter.fname = "US"
# print(hindustani_supporter.email())                             # US.Supporter@codewithSambhu.com
print(hindustani_supporter.email)

hindustani_supporter.email = "Hindustani.Supporter@codewithSambhu.com"
print(hindustani_supporter.email)                               #  Hindustani.Supporter@codewithSambhu.com

del hindustani_supporter.email                     # AttributeError: can't delete attribute
print(hindustani_supporter.email)