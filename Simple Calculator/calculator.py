num1 = int(input("Enter a number =>"))
op = input("choose /, *, -, + =>")
num2 = int(input("Enter a number =>"))

if op == "+": print(num1 + num2)
elif op == "-": print(num1 - num2)
elif op == "*": print(num1 * num2)
elif op == "/": print(num1 / num2)
else:
    print("That's not a valid operation!")