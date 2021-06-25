#  ....Comprehension.....

# ls = []
# for i in range(100) :
#     if i%3 == 0 :
#         ls.append(i)
# ls = [i for i in range(100) if i%3==0]
# print(ls)   #[0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99]

# dict1 = {i:f"item {i}" for i in range(1,1000) if i%100==0}
# print(dict1)      #{100: 'item 100', 200: 'item 200', 300: 'item 300', 400: 'item 400', 500: 'item 500', 600: 'item 600', 700: 'item 700', 800: 'item 800', 900: 'item 900'}
#
# dict2 = {i:f"item {i}" for i in range(6)}
# dict2 = {value:key for key,value in dict2.items()}
# print(dict2)   # {'item 0': 0, 'item 1': 1, 'item 2': 2, 'item 3': 3, 'item 4': 4, 'item 5': 5}
#

dresses = {dress for dress in ["dress1","dress2","dress1","dress2","dress1","dress2"]}
print(type(dresses))        # <class 'set'>
dresses = [dress for dress in ["dress1","dress2","dress1","dress2","dress1","dress2"]]
print(type(dresses))        # <class 'list'>
