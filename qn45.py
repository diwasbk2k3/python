#split 
a = "Diwas//IT/Student"
print(a.split("/"))

#join
a = ["Diwas", "IT", "student"]
new = "/".join(a)
print(new)

#maketrans
a ="diwas bishwokarma"
new = a.maketrans("b", "0","s")
print(a.translate(new))