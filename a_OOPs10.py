#   public,
#   private,
#   protected......
#   name embling

class Employee :
    bonus_salary = 200
    var = 10
    _protect = 111
    __private = 112

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
emp = Employee("Sambhu",300,"Programmer")
print(emp._protect)                      # 111
# print(emp.__private)                     # error
print(emp._Employee__private)           # 112                       # name embling

