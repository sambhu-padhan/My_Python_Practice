#   ......self...and...__init__....
#  ...Constructor....

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


sambhu = Employee("Sambhu",10000,"Student")
chetan = Employee("Chetan",5000,"Instructor")

#   here we can change the class variable by outside variable
sambhu.change_bonusSalary(100)
print(sambhu.bonus_salary)      # 100

