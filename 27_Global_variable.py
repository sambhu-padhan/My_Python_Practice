# .......Global variable..........

# l =  10
#
# def fun1() :
#     l = 11
#     m = 15
#     print(l,m)
#
# fun1()                                              #  11 15
# # print(m)                                            # NameError: name 'm' is not defined

z = 22
def sambhu() :
    z = 10
    def fun() :
        global z
        z = 40
    print("Before calling fun() :",z)
    fun()
    print("After calling fun()  :",z)
sambhu()
print(z)

"""OUTPUT

Before calling fun() : 10
After calling fun()  : 10
40

"""