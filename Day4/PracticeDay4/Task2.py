def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))
operation = input("Enter operation (+,-,*,/): ")

if operation == "+":
    print(add(number1, number2))
elif operation == "-":
    print(subtract(number1, number2))
elif operation == "*":
    print(multiply(number1, number2))
elif operation == "/":
    print(divide(number1, number2))