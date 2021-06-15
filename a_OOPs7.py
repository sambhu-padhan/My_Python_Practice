# .....inhertance..........


class Employee :
    bonus_salary = 200
    def __init__(self,sname,ssalary,srole):
        self.name = sname
        self.salary = ssalary
        self.role = srole

    def printDetails(self):
        return f"Name is {self.name}, Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_bonusSalary(cls,newbonus_salary):
        cls.bonus_salary = newbonus_salary

    @classmethod
    def from_str(cls,string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("This is good " + string)         # This is good sambhu

class Programmer(Employee) :
    def __init__(self,sname,ssalary,srole,languages):
        self.name = sname
        self.salary = ssalary
        self.role = srole
        self.languages = languages

    def printprog(self):
        return f"The Programmer's Name is {self.name}, Salary is {self.salary} and role is {self.role}.The languages are {self.languages}"

sambhu = Employee("Sambhu",10000,"Student")
chetan = Employee("Chetan",5000,"Instructor")

shubham = Programmer("Shubham",6000,"Programmer",["Python"])
karan = Programmer("Karan",7000,"Programmer",["CPP"])

print(karan.printprog())
print(karan.printDetails())