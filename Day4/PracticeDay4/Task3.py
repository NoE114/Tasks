def is_prime(number):
    if number < 2:
        return False

    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False

    return True

number = int(input("Enter a number: "))

if is_prime(number):
    print("Prime Number")
else:
    print("Not Prime Number")