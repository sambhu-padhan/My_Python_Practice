##....Multiple inheritance....
# .....inhertance..........


class Employee :
    bonus_salary = 200
    var = 10
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
class Player :
    No_of_games = 4
    var = 25
    def __init__(self,name,game):
        self.name = name
        self.game = game
    def printdetails(self):
        return f"Name is {self.game}, Salary is {self.salary} and role is {self.game}"
class CoolProgrammer(Player,Employee) :
    # var = 12
    language = "c++"
    def printlanguage(self):
        print(self.language)

sambhu = Employee("Sambhu",10000,"Student")
chetan = Employee("Chetan",5000,"Instructor")

shubham = Player("Shubham",["Cricket"])
karan = CoolProgrammer("Karan",["Football"])
# karan.printlanguage()                       # c++
# det = karan.printDetails()
# print(det)                                  #   Name is Karan, Salary is 7000 and role is CoolProgrammer
print(karan.var)                    # 25
