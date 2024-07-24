my_dict = {"a":"diwas","age":20}
value = my_dict.pop("a")
print(my_dict)
print("Value: ", value)

#popitem
my_dict = {"a":"diwas","age":20,"address":"gulmi"}
key, value= my_dict.popitem()
print(my_dict)
print("Key Value: ",key, value)