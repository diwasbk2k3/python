#raise and assert

#raise:
age = int(input("Enter your age: "))
if age<0:
    raise("Age cannot be negative")
else:
    print("Your age is", age)