def find_maximum(first_number, second_number, third_number):
    return max(first_number, second_number, third_number)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

print("Maximum Number:", find_maximum(num1, num2, num3))