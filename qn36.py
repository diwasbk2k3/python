#Recursion
def factorial(n):
    if n==0: #Base Case
        return 1
    else:
        return n*factorial(n-1) # Recursive Case
    
result = factorial(5)
print(result)
