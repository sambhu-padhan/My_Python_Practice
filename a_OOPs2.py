class Employee :
    bonus_salary = 2000
    pass

sambhu = Employee()
chetan = Employee()

sambhu.name = "Sambhu"
sambhu.salary =10000
sambhu.role = "student"

chetan.name = "Chetan"
chetan.salary = 5000
chetan.role = "Instructor"

# print(sambhu.salary)                    # 10000
#
# print(Employee.bonus_salary)            #  2000
# print(chetan.bonus_salary)              #  2000
# print(sambhu.bonus_salary)              #  2000

#by using class name , we can change the value of Bonus_salary only...............

# chetan.bonus_salary = 5000                 #   Here a new instance of  bonus_salary will be created.so
# print(chetan.bonus_salary)          # 5000
# print(Employee.bonus_salary)        # 2000
# print(sambhu.bonus_salary)          # 2000
# Employee.bonus_salary = 5000
# print(sambhu.bonus_salary)          # 5000

sambhu.bonus_salary = 1000
print(sambhu.__dict__)                #  {'name': 'Sambhu', 'salary': 10000, 'role': 'student', 'bonus_salary': 1000}
print(Employee.__dict__)            # {'__module__': '__main__', 'bonus_salary': 2000, '__dict__': <attribute '__dict__' of 'Employee' objects>, '__weakref__': <attribute '__weakref__' of 'Employee' objects>, '__doc__': None}
