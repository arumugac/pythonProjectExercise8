# f = open("new.txt", "a")
# name = input("Enter your name")
# f.write(name)
# f.write(",")
# last = input("Enter your last name")
# f.write(last)
# f.write(",")
# age = int(input("Enter your age"))
# agestr = str(age)
# f.write(agestr + "\n")

# lines = ["this is on line,\n","This is another,\n"]
# f.writelines(lines)

# Example - "How to create a file"

# f = open("new.txt", "w")
# f.write(f)
# print(f)
# f.close()

# Example - "How to read a file"

# f = open("new.txt", "r")
# lines = f.readlines()
# print(lines)
# f.close()

# f = open("newDVLA.txt", "w")
# f.write(f)
# print(f)
# f.close()

# Example - "DVLA Exercise"

# f = open('newDVLA.txt', "r")
# lines = f.readlines()
# target = input("Enter Reg:").upper()
# for line in lines:
#     car = line.strip("\n")
#     car = car.split(",")
#     reg = car[0]
#     name = car[1]
#     address = car[2:5]
#     town = car[3]
#     postcode = car[4]
#     if reg == target:
#         print("File found")
#         print(f"The registered owner of {reg} is "
#               f"{name}")
#         print(f"lives at {address}")
#
#f.close()
# Example - "another way to open a file using 'with' allows you to close explicitly without using a 'f.close',"

# with open("newDVLA.txt", "r") as f:
#     for line in f:
#         print(line)



