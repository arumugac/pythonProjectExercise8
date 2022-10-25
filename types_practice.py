import re

password = input("Insert your password:")
valid = "no"
while valid == "no":
    if len(password) < 6:
        valid = "no"
    elif not re.search("[a-z]", password):
        valid = "no"
    elif not re.search("[0-9]", password):
        valid = "no"
    elif not re.search("[A-Z]", password):
        valid = "no"
    elif not re.search("[!$#@£%&*_+={}?<>]", password):
        valid = "no"

    else:
        valid = "yes"
        print("Valid Password")

    if valid == "no":
        print("Not a Valid Password")
    break
