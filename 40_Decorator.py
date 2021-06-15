# def function1() :
#     print("subscribe now")
# fun2 = function1
# del function1
# fun2()

# def funcreat(num) :
#     if num==0 :
#         return print                            # <built-in function print>
#     if num==1 :
#         return sum
# a = funcreat(1)
# print(a)                                # <built-in function sum>

# def executor(func) :
#     func("this")
#
# executor(print)                             # this

def dec1(func1) :
    def nowexe() :
        print("Execute now")
        func1()
        print("Executed")
    return nowexe()

@dec1
def who_is_harry() :
    print("Harry is a good boy")

# who_is_harry = dec1(who_is_harry)
who_is_harry()