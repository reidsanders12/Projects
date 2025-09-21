# Reid Sanders
# Simple Calculator
# 09/21/2025


print("Welcome to the Simple Calculator!")
amount_nums = int(input("How many numbers do you want to calculate? "))
if amount_nums < 2:
    print("Please enter at least two numbers.")
    exit()
elif amount_nums == 2:
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
elif amount_nums == 3:
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    num3 = input("Enter third number: ")
else:
    print("This calculator supports up to 3 numbers only.")
    exit()

operation = input("Enter operation (+, -, *, /): ")
if operation == '+':
    print(f"{num1} + {num2} = {float(num1) + float(num2)}")
elif operation == '-':
    print(f"{num1} - {num2} = {float(num1) - float(num2)}")
elif operation == '*':
    print(f"{num1} * {num2} = {float(num1) * float(num2)}")
elif operation == '/':
    if float(num2) != 0:
        print(f"{num1} / {num2} = {float(num1) / float(num2)}")
    else:
        print("Error: Division by zero is not allowed.")

if amount_nums == 3:
    if operation == '+':
        print(f"{num1} + {num2} + {num3} = {float(num1) + float(num2) + float(num3)}")
    elif operation == '-':
        print(f"{num1} - {num2} - {num3} = {float(num1) - float(num2) - float(num3)}")
    elif operation == '*':
        print(f"{num1} * {num2} * {num3} = {float(num1) * float(num2) * float(num3)}")
    elif operation == '/':
        if float(num2) != 0 and float(num3) != 0:
            print(f"{num1} / {num2} / {num3} = {float(num1) / float(num2) / float(num3)}")
        else:
            print("Error: Division by zero is not allowed.")