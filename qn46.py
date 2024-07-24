#string formatting
name = "diwas"
age = 20
print("My name is %s and I'm %d years old" %(name, age))
print(f"My name is {name} and I'm {age} years old")


#named index
print("My name is {name} and I'm {age} years old".format(name="diwas", age=20))

#numbered index
print("My name is {0} and I'm {1} years old".format("diwas", 20))

#empty place holders
print("My name is {} and I'm {} years old".format("diwas", 20))