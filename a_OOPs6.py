#........ static method ...........

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


sambhu = Employee("Sambhu",10000,"Student")
chetan = Employee("Chetan",5000,"Instructor")
shubham = Employee.from_str("Shubham-12000-Clerk")


# print(shubham.salary)                   #  12000
shubham.printgood("sambhu")
