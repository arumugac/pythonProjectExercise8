# mytup = ('eggs', 'bacon', 'sausages', 'beans', 'toast')
#
# x, y, *z = mytup
# print(x, y, z)


# t1 = ('cats', 'dogs', 'snakes', 'mice', 'camels')
# t2 = ('kelp', 'crab', 'lobster', 'fish')
#
# for a, *b, c in t1, t2:
#     print(a,b,c)

# myList = ["Liverpool", "Man City", "Arsenal", "Norwich"]

# myList[:0] = ["Newcastle", "Palace"]
# myList.append("Leeds")
# myList.extend(["Everton"])
# myList += ["Man U"]


# myList.insert(2,"Tottenham")
# myList[2:2] = ["Burnley"]
# myList[3] = ["Fulham"]


# myList.pop(1)
# myList.remove("Liverpool")
# try:
#     myList.remove("Fulham")
# except:
#     print("That was not in the list")

# print(myList)

# mynum = [45,55,34,3,14,5,7]
# print(mynum.count(55))
# print(mynum.index(55))
# mynum.reverse()
# print(mynum)

# mySet = {2,4,5,7,8,3}
# print(mySet)
#
# mynewset = set([2,5,7,8,3])
# print(mynewset)

# s4:set[int] = {23, 42, 66, 123}
# s5:set[int] = {56, 24, 42}
# print(s4)
#
# s4.remove(123)
# s5.remove(24)
# print("{:20} :{20}".format(s4)(s5))

# print(f"{:20} {20}".format(s4,s5))

# cheese = ['Cheddar', 'Stilton', 'Cornisk Yarg']
# cheese += ['Oke']
# print(cheese)

# tup = "Hello",
# print(len(tup))

# import random
# numbers = []
# ticket =[]
# for i in range (1,51):
#     numbers.append(i)
#
# for i in range (0,6):
#     number = random.randint(1,51)
#     try:
#         ticket.append(number)
#         numbers.append(number)
#     except:
#         i -= 1
#
# print(f'Your number are: {ticket}')

# import random
# lotto = set()
#
# for i in range (1,51):
#     while len(lotto) < 6:
#         i = random.randint(1,51)
#
# print("Lotto Numbers =", lotto)