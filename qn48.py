#descending order using for loop
a = [1,5,3,4,8,9,6,7]
a.sort()
b = []
for i in list(reversed(a)):
    b.append(i)
print(b)

