#!/bin/python3
num1 = int(input("please enter your first number"))
num2 = int(input("please enter your second number"))
result = num1 * num2
print(f"{num1} x {num2} = {result}") 
if result > 0:
    print("result is positive")
elif result < 0:
    print("result is negative")
else:
    print("result is positive and negative")