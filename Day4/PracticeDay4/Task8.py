def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

choice = input("Convert (C/F): ").upper()

if choice == "C":
    temp = float(input("Enter Celsius: "))
    print("Fahrenheit =", celsius_to_fahrenheit(temp))
elif choice == "F":
    temp = float(input("Enter Fahrenheit: "))
    print("Celsius =", fahrenheit_to_celsius(temp))