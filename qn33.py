# global keyword:
x = 10
def modify_global():
    global x
    x = 20
modify_global()
print(x)


#except keyword:
n = int(input("Enter any number:"))
try:
    d = 10/n
    print(d)
except Exception as e:
    print("Error!", e)


#return keyword:
def sum (a, b):
    return a+b
result = sum(20,10)
print(result)
