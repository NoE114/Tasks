def maximum(a, b):
    if a > b:
        return a
    return b

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("Maximum =", maximum(x, y))