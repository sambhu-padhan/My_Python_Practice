import json

data = '{"var1":"Sambhu","var2":40}'
print(data)         #{"var1":"Sambhu","var2":40}
parsed = json.loads(data)
print(parsed)       # {'var1': 'Sambhu', 'var2': 40}

data2 = {"Channel Name":"life",
         "Source":['youtube','google','gaming'],
         "Income":5000,
         "isSambhu":False}     #False==false

jscomp = json.dumps(data2)
print(jscomp)               #{"Channel Name": "life", "Source": ["youtube", "google", "gaming"], "Income": 5000, "isSambhu": false}