#WAP to check Armstrong and Palindrome 

#checking Armstrong
#>>>using for loop
user_input = int(input("Enter any number: "))
armstr = str(user_input)
n = len(armstr)
arm_sum = 0
for i in armstr:
    arm_sum = arm_sum + int(i)**n
if arm_sum == user_input:
    print("Armstrong")
else:
    print("Not Armstrong")
#>>>using while loop   
user_input = int(input("Enter a number: "))
n = len(str(user_input))
arm_sum = 0
temp = user_input

while temp > 0:
    i = temp % 10
    arm_sum = arm_sum + i ** n
    temp //= 10

if user_input == arm_sum:
    print("Armstrong")
else:
    print("Armstrong")


#palindorme checking
a = "mom"
if a[::-1] == a:
    print("Palindrome")
else:
    print("Not palindrome")
