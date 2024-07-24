#pyramids in python 

# normal pyramid
print("\nNormal Pyramid")
for i in range(5):
    x = "*"
    x = x*i
    print(f"{x:^10}")

# inverted pyramid
print("\nInverted Pyramid")
for i in range(5):
    x = "*"
    x = x*(5-i)
    print(f"{x:^10}")

# left sided pyrammid
print("\nLeft Sided Pyramid")
for i in range(5):
    x = "*"
    x = x*i
    print(f"{x:<10}")

#right sided pyramid
print("\nRight Sided Pyramid")
for i in range(5):
    x = "*"
    x = x*i
    print(f"{x:>10}")
