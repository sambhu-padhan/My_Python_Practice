# https://archive.ics.uci.edu/ml/machine-learning-databases/iris/

import requests
import json
import pickle

url = ('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data')
response = requests.get(url)
response_text = response.text
print(response_text)
picklefile = "MyPickle.pkl"
file = open(picklefile,'wb')
response_pickled = pickle.dump(response_text,file)
file.close()

# file = open(picklefile,'wb')
# pickle.dump(jsonfile,file)

