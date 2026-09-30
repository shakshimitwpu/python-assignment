import re
text=input("Enter string: ")
if re.match("^[a-z A-Z 0-9]+$",text):
    print("Valid string")
else:
    print("Invalid string")