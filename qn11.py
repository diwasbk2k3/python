#WAP to find the factorial of a given number.

#using for loop
n = int(input("Enter any number: "))
fact = 1
for i in range(1, n+1):
    fact = fact * i

print(f"Factorial of {n} is {fact}")

#using while loop 
n = int(input("Enter any number: "))
fact = 1
i = 1 
while i<=n:
    fact = fact*i
    i = i + 1
print(f"Factorial of {n} is {fact}")