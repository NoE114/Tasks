def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    return "Odd"

number = int(input("Enter a number: "))
print(check_even_odd(number))