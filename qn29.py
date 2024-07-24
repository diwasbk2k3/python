#read, and readline
with open("diwas.txt", 'r') as f:

    d = f.read()
    print(d)

    d1 = f.readline()
    print(d1)

    d2 = f.readline()
    print(d2)


#readlines
with open("diwas.txt", 'r') as f:

    d3 = f.readlines()
    print(d3)