#  operator overloading
#  render method


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
    def __add__(self, other):
        return self.salary + other.salary
    def __truediv__(self, other):
        return self.salary / self.salary
    def __repr__(self):
        return f"Employee({self.name},{self.salary},{self.role})"
    # def __str__(self):
    #     return f"Name is {self.name}, Salary is {self.salary} and role is {self.role}"

emp1 = Employee("Sambhu",4,"Programmer")
emp2 = Employee("Azad",5,"Cleaner")

# print(emp1+emp2)                    #  105
# print(emp1/emp2)                    #  1.0
# print(emp2)                         #  Name is Azad, Salary is 5 and role is Cleaner
# print(emp2)                         #  Employee(Azad,5,Cleaner)
# print(emp2)                         #  Name is Azad, Salary is 5 and role is Cleaner
print(str(emp2))                      # Employee(Azad,5,Cleaner)