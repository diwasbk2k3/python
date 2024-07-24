#pickling and unpickling

#pickling: used to convert python object into byte steam
import pickle
l = [1, 2, 3, 4, 5]
with open ("pkl.txt", "wb") as f:
    pickle.dump(l,f)

#unpickling: used to conver byte steam back to python object.
import pickle
with open("pkl.txt", "rb") as f:
    d = pickle.load(f)
    print(d)