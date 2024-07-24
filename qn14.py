#Accept a string from the user and calculate the no of digit, space, and letters.
user_input = input("Enter any sentences or word: ")

digit_count = 0
space_count = 0
letter_count = 0
other_count = 0

for char in user_input:
    if char.isdigit():
        digit_count = digit_count+1
    elif char.isspace():
        space_count = space_count+1
    elif char.isalpha():
        letter_count = letter_count+1
    else:
        other_count = other_count + 1
        
print("Total digit count: ", digit_count)
print("Total space count: ", space_count)
print("Total letter count: ", letter_count)
print("Others: ", other_count)

