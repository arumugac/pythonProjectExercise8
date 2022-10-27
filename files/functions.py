# def addThis():
#     print("Hello")
#
# addThis()

# def addThis():
#     myvar = 4 +7
#     return myvar
#
# print(addThis())

# def addThis():
#     myvar = 4 +7
#     return
#
# print(addThis())


# def addThis():
#         mylist = ["bob", "jim"]
#         return mylist
#
# mygeneratedlist=addThis()
# print(addThis())

# def hello():
#     print("Hi")
#
# ned to finish this code


# def add(num1):
#     plus10 = num1+10 # creates a new Variable and adds 10
#     return plus10 # returns the new Variable created.
#
# choice = int(input("Enter A number"))
#

# def add(num1, num2, name):
#     new = num1 + num2 # creates a new Variable and adds 10
#     return f" That was {new}, thanks {name}" # returns the new Variable created.
#
# print(add(2,7,"Andy"))

# def make_string(val, times):
#     print("Calculating.........")
#     res = str(val) * times
#     return res
# print(make_string(8,10))

# def print_vat(gross, vatpc=20, message='Summary: '):
#     net = gross / (1 + (vatpc/100))
#     vat = gross - net
#     print(message,'Net: {0:5.2f} Vat: {1:5.2f}'.format(net,vat))
#
# userin = float(input("Enter Cost"))
# print_vat(11.67)
# print_vat(11.67, message="final", vatpc=17.5)


# def my_funct(*,file, dir, user='root'):
#     print('file: {:}, dir {:}, to: {:}'.format(file, dir, user))
#     #print(f'file: {file} dir: {file} to: {to})
#
# #by position
# my_funct('one', 'two', 'three')
#
# #by default
# my_funct('one', 'two')
#
# #by name
# my_funct(file='one', user='bob', dir='two')

# variadic functions
# def myFunct(a,b,c):
#     print(a,b,c)
#     print(a)
#
# mytup = 23,45,88
#
# myFunct(*mytup) #this function will unpack a tuple


# def myfun(dir, *args):  #*args returns tuples
#     print('Dir:', dir, 'Files', args)
#
# myfun('C:/myFiles', 'f1.txt', 'f2.txt', 'f3.pdf')


#**kwargs
#
# def print_vat(**kwargs): #**kwargs returns dictionory
#     print(kwargs)
#
# # print_vat(vatpc = 17.5, gross=9.54, message="sum: ")
#
# argsdict = dict(vatpc = 17.5, gross=9.54, message="sum: ")
# print(argsdict)
# print_vat(**argsdict)


#variables and Scope

# myvar = 7 #Global - used in any part of the code
#
# def scope_test():
#     global myvar
#     myvar = 42 #variable created in subs stay in sub
#     print(myvar)
#     # return None
#
# print(myvar)
# scope_test()
# print(myvar)#after subroutine

# score =46
#
# def score_change(score2, points):
#     global score
#     newscore = score2
#     newscore += points
#     return f"Your new Credit Score is {newscore}"
#
# print(score_change(score,8))
# print(score)



#My Test
# import math

# def circle(R):
#     area = Radius ** 2 * math.pi
#     return area
#
# Radius = float(input("Please enter R:"))
# print("The area of the given circle is:", circle(Radius))

#Calculating Areas of Circ Tri Rect Challenge

import math

def circle(r):
    return f"The area of the circle is {math.pi * r**2:6.2f} cm2"

def triangle():
    base = int(input("Input base"))
    height = int(input("Input Height"))
    area = 0.5*base*height
    return f"The area of that triangle is {area} cm2"

def rectangle(h,l):
    return f"The area of that rectangle is {h*l} cm2"

again = "Yes"
while again == "Yes":
    choice = in ("C") for Circle : T for Triangle : R for