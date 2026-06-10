num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))

if num1==num2:
    print("Both number are same")
elif num1<num2:
    print(f"{num2} is the largest number.")
else:
    print(f"{num1} is the largest number.")
