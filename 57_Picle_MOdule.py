import pickle
#......pickling.......

# books = ["Java","CPP","OS","DMGT","DSA"]
# file = "MyBooks.pkl"
# fileobj = open(file,'wb')
# pickle.dump(books,fileobj)
# fileobj.close()

#....depickling......

file = "MyBooks.pkl"
fileobj = open(file,'rb')
books = pickle.load(fileobj)
print(books)
print(type(books))
