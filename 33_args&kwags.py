#  *args....**quarqs


# def function_name_print(a,b,c,d) :
#     print(a,b,c,d)
#
# function_name_print("Harry","Sambhu","Rohan","Prteek")                      # Harry Sambhu Rohan Prteek
# function_name_print("Harry","Sambhu","Rohan","Prteek","Ram")            # TypeError: function_name_print() takes 4 positional
#
def functionargs(normal,*args,**kwargs) :
    print(normal)
    for item in args :
        print(item)
    for key, value in kwargs.items() :
        print(f"{key} is a {value}")

      # print(args)
arguments = ["Harry","Sambhu","Rohan","Prteek","Ram"]
normal = "Hello friends :"
kw = {"Harry":"chicken","Sambhu":"mutton","Rohan":"paneer","Prteek":"Egg"}

functionargs(normal,*arguments,**kw)


""""OUTPUT

Hello friends :
Harry
Sambhu
Rohan
Prteek
Ram
Harry is a chicken
Sambhu is a mutton
Rohan is a paneer
Prteek is a Egg

"""