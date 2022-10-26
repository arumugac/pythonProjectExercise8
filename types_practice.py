num = int(input("Please Enter a Number:"))

if num > 1:
    for number in range(num):
        for i in range(2, number):
            if number % i == 0:
                break
        else:
            print(number)








