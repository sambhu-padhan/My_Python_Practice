#   ......self...and...__init__....
#  ...Constructor....

class Employee :
    bonus_salary = 2000
    def __init__(self,sname,ssalary,srole):
        self.name = sname
        self.salary = ssalary
        self.role = srole

    def printDetails(self):
        return f"Name is {self.name}, Salary is {self.salary} and role is {self.role}"

sambhu = Employee("Sambhu",10000,"Student")

# sambhu.name = "Sambhu"
# sambhu.salary =10000
# sambhu.role = "student"
#
# chetan.name = "Chetan"
# chetan.salary = 5000
# chetan.role = "Instructor"

print(sambhu.printDetails())            # Name is Sambhu, Salary is 10000 and role is student
print(sambhu.name)                  # Sambhu
