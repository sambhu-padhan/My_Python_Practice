###...Regular Expression.....
#  try these methods--- (match,finditer,compile,search,split)


import re


mystr = '''url = ('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data')
response = requests.get(url)
response_text = response.text
print(response_text)
picklefile = "MyPickle.pkl"
file = open(picklefile,'wb')
12211312_1212
21321332.1231
11111111_2333
33333131_1323
response_pickled = pickle.dump(response_text,file)
file.close()

# file = open(picklefile,'wb')
# pickle.dump(jsonfile,file)

    '''


# patyh = re.compile(r'.pkl')
# patyh = re.compile(r'pi*')
# patyh = re.compile(r'(.){2}')
# patyh = re.compile(r'.pkl')
# patyh = re.compile(r'pkl{1}|text')

#  special sequences
# patyh = re.compile(r'\bfile')                # starting with file
# patyh = re.compile(r'fi\b')                 # ending with fi

patyh = re.compile(r'\d{8}_\d{4}')


matches = patyh.finditer(mystr)
for match in matches :
    print(match)
