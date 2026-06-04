n = int(input("Enter n: "))

print("\nRight Triangle")
for i in range(1, n + 1):
    print("* " * i)

print("\nInverted Triangle")
for i in range(n, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

print("\nPascal Triangle")
for i in range(n):
    num = 1
    print(" " * (n - i), end="")
    for j in range(i + 1):
        print(num, end=" ")
        num = num * (i - j) // (j + 1)
    print()

print("\nPrime Numbers")
for num in range(2, n + 1):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            break
    else:
        print(num, end=" ")