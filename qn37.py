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