''' A company decided to give bonus to employee according to the following criteria
    Time period of service                 Bonus
    more than 10 yrs                         10%
    >=6 and <=10 yrs                        8%
    less than 6 yrs                         5%
Write a program to calculate the bonnus of the employee
'''

service_period = int(input("Enter your service period: "))

if service_period>10:
    bp = 10
elif (service_period>=6):
    bp = 8
elif (service_period<6):
    bp = 5
print("Your bonus percentage:", bp)