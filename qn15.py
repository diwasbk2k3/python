#Remove  bad characters from the given_str = "py:th*on!py;th*on" where bad_char = [":","*","!,";"]
given_str = "py:th*on!py;th*on"
bad_char = [":","*","!",";"]
for char in bad_char:
    given_str = given_str.replace(char,"")
print(given_str)
