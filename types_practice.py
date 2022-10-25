score = int(input("Enter your Score:"))
if score > 100 or score < 0:
    print("That is invalid")
else:
    if score > 90:
        print("Your grade is an A*")
    elif score > 80:
        print("Your grade is an A")
    elif score > 70:
        print("Your grade is an B")
    elif score > 60:
        print("Your grade is an C")
    elif score > 50:
        print("Your grade is an D")
    elif score > 40:
        print("Your grade is an E")
    else:
        print("You Failed")










