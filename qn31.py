''' Suppose you have login.txt and registration.txt in your current directory.
    Copy the contents of login.txt in registration.txt
'''

with open("login.txt","r") as f1:
    data = f1.read()
    
with open("registration.txt","w") as f2:
    f2.write(data)