#   .......loops in Python....
"""                                                                            #  OUTPUTS
list1 = ["Harry", "Larry", "Carry", "marie"]
#print(list1)                                                                #  ['Harry', 'Larry', 'Carry', 'marie']
list1 = [ ["Harry", 1], ["Larry", 2], ["Carry", 3], ["marie", 4]]
print(list1)

dict1 = dict(list1)
print(dict1)                                                        #  {'Harry': 1, 'Larry': 2, 'Carry': 3, 'marie': 4}

#for item , Lollypop in list1 :
#   print(item,Lollypop)
for item , Lollypop in dict1.items() :
    print(item,Lollypop)

   output
Harry 1
Larry 2
Carry 3
marie 4
"""

items = [int, float, "Harry", 5,3,23,6,22,11,4,12,55,64]
for item in items :
    if str(item).isnumeric() and item>6 :
        print(item)

"""  output
23
22
11
12
55
64
"""