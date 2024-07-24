#tell
with open("diwas.txt", "r") as f:
    f.readline()
    t1 = f.tell()
    print(t1)
    f.readline()
    t2 = f.tell()
    print(t2)

#seek
with open("diwas.txt", "r") as f:
    f.seek(5)
    r1 = f.read()
    print(r1)