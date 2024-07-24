#WAP to find the sum of a given number 

#using for loop
n = int(input("Enter any number: "))
sum = 0
for i in range(len(str(n))):
    r = n%10
    n = n//10 
    sum = sum + r
print("Sum of given number is: ", sum )

#using while loop 
n = int(input("Enter any number: "))
sum = 0
while n>0:
    r = n%10 
    n = n//10
    sum = sum + r
print("Sum of given number is: ", sum )
