#nested function 

def outer_function():
    print("Outer function ")
    def inner_function():
        print("Inner function ")
    inner_function()
outer_function()