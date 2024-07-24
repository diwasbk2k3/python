#issuperset, issubset, and disjoint method

a = {1, 2, 3, 4, 5}
b = {1, 2, 3}
c = {10}

print(a.issuperset(b))
print(a.issubset(a))
print(a.isdisjoint(c))