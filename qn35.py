#Explain Recursion >> Base Case >> Recursive Case >> Direct and Indirect Recusrion

#Recurion is a programming technique in which a function call itself to solve a problem.

#Base Case:Base Case is a conditon to stop recursion. 
    #It's like a exit point for recursion. 
    #Without recurion the function would call itself repetiadely.
#Recursive Case:
    # Recursive case is a technique in which the function call itself with a modified argument.
    # typically bringing closer to the base case.


#Recursion
def factorial(n):
    if n==0: #Base Case
        return 1
    else:
        return n*factorial(n-1) # Recursive Case
    
result = factorial(5)
print(result)



# odd and even from a list
n =[1,2,3,4,5,6,7,8,9,10]
even_list = []
odd_list = []
for i in n:
    if i%2==0:
        even_list.append(i)
    else:
        odd_list.append(i)
print("Even number list: ", even_list)
print("Odd number list: ", odd_list)



# variable length argument and keyword length argument

def my_function(*args, **kwargs):

    print("Variable length arguments (*args):", *args)
    print("Keyword  length arguments (*kwargs):", *kwargs)

my_function(1,2,3,a = "diwas", age = 20)



#unique element(print only unique elements from a list)
a =[1,2,2,2,3,3,3,4,4,4,5,5,5,5]
unique_list = []
for item in a:
    if not item in unique_list:
        unique_list.append(item)
print(unique_list)



#remove
my_list = [1,2,3,4,5,6]
my_list.remove(3)
print(my_list)


#discard
my_set = {1,2,3,4,5}
my_set.discard(3)
my_set.discard(6)
print(my_set)



#Palindrome
a = input("Enter any words: ")
if a[::-1]==a:
    print("Palindrome")
else:
    print("Not palindrome")



#Extract Odd and Even from the list
a = [1,2,3,4,5,6,7,8,9,10]
even=[]
odd=[]
for i in a:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("Even: ", even)
print("Odd: ", odd)    



#Sum od a list using for and while loop
a = [1,2,3,4,5]
sum = 0
for i in a:
    sum = sum + i
print(sum)

#using while loop
a = [1,2,3,4,5]
sum = 0
i = 0
while i<=len(a):
    sum = sum +i
    i = i+1
print(sum)


#break
for i in range(1, 5):
    if i== 3:
        break
    print(i)

#continue
for i in range(1, 5):
    if i== 3:
        continue
    print(i)
#pass
a = int(input("Enter any number:"))
if a>0:
    print("Positive number:")
else:
    pass

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


#descending order using for loop
a = [1,5,3,4,8,9,6,7]
a.sort()
b = []
for i in list(reversed(a)):
    b.append(i)
print(b)



#nested function 

def outer_function():
    print("Outer function ")
    def inner_function():
        print("Inner function ")
    inner_function()
outer_function()





