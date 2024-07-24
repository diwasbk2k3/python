#unique element(print only unique elements from a list)
a =[1,2,2,2,3,3,3,4,4,4,5,5,5,5]
unique_list = []
for item in a:
    if not item in unique_list:
        unique_list.append(item)
print(unique_list)
