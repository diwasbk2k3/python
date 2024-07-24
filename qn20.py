#four possible combination of try - except - finally

#try - except - finally 
n = int(input("Enter any number: "))
try:
    10/n
except:
    print("Error!")
finally:
    print("Finally executed!")



#try - except - finally with Exception
n = int(input("Enter any number: "))
try:
    10/n
except Exception as e:
    print("Error!", e)
finally:
    print("Finally executed!")


#try-finally with nested try-except
n = int(input("Enter any number: "))
try:
    try:
        10/n
    except Exception as e:
        print("Error", e)
finally:
    print("Finally executed!")