def calculate_bill(units):
    if units <= 100:
        return units * 2
    elif units <= 300:
        return (100 * 2) + ((units - 100) * 3)
    else:
        return (100 * 2) + (200 * 3) + ((units - 300) * 5)

units_consumed = int(input("Enter units consumed: "))

print("Electricity Bill =", calculate_bill(units_consumed))