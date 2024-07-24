#difference between r+, w+, and a+ mode

# r+ mode is used to read and write>>it does not erase the existing content
# and if the file doesn't exist it will create a new
with open("index.txt","r+") as f:
    f.write("Diwas Bishwokarma")


# w+ mode is used to write and read >> w+ does erase the existing content of the file./Overwrite
# and if the file doesn't exist it will create a new.
with open("index.txt","w+") as f:
    f.write("Softwarica")


# a+ mode is used for appending and reading.
with open("index.txt", "a+") as f:
    f.write("Additional content")
