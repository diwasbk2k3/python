# variable length argument and keyword length argument

def my_function(*args, **kwargs):

    print("Variable length arguments (*args):", *args)
    print("Keyword  length arguments (*kwargs):", *kwargs)

my_function(1,2,3,a = "diwas", age = 20)