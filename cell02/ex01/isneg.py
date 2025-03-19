#!/bin/python3
number = int(input("please enter you number: "))
if number < 0:
    print(number)
    print("this number is negative")
elif number > 0:
    print(number)
    print("this number is positive")
elif number == 0:
    print(number)
    print("this number is both positive and negative")


