def calculate_tax(income):
    tax = 0

    if income <= 250000:
        tax = 0

    elif income <= 500000:
        tax = (income - 250000) * 0.05

    elif income <= 1000000:
        tax = 12500 + ((income - 500000) * 0.20)

    else:
        tax = 112500 + ((income - 1000000) * 0.30)

    return tax


annual_income = float(input("Enter Annual Income: "))

tax_amount = calculate_tax(annual_income)
net_income = annual_income - tax_amount

print("\n----- TAX REPORT -----")
print(f"Annual Income : ₹{annual_income:.2f}")
print(f"Tax Amount    : ₹{tax_amount:.2f}")
print(f"Net Income    : ₹{net_income:.2f}")