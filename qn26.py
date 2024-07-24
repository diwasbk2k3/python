'''
Accept the no of days and calculate the library charge.

    Till 5 days:        Rs 2/day
    6 to 10 days:       Rs 3/day
    11 to 15 days:      Rs 4/day
    After 15 days:      Rs 5/day

'''
no_of_days = int(input("Enter the number of days: "))

if no_of_days<=5:
    charge = 2
elif no_of_days>5 and no_of_days<=10:
    charge = 3
elif no_of_days>=11 and no_of_days<=15:
    charge = 4
else:
    charge = 5
    
total_charge = no_of_days*charge
print("Total fine: ", total_charge)


