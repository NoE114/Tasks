def calculate_emi(principal, annual_interest_rate, loan_years):
    monthly_interest_rate = annual_interest_rate / (12 * 100)
    total_months = loan_years * 12

    emi = (
        principal
        * monthly_interest_rate
        * (1 + monthly_interest_rate) ** total_months
    ) / (
        (1 + monthly_interest_rate) ** total_months - 1
    )

    return emi


loan_amount = float(input("Enter Loan Amount: "))
interest_rate = float(input("Enter Annual Interest Rate (%): "))
loan_years = int(input("Enter Loan Tenure (Years): "))

monthly_emi = calculate_emi(
    loan_amount,
    interest_rate,
    loan_years
)

print("\n----- EMI DETAILS -----")
print(f"Loan Amount: ₹{loan_amount:.2f}")
print(f"Interest Rate: {interest_rate}%")
print(f"Loan Tenure: {loan_years} Years")
print(f"Monthly EMI: ₹{monthly_emi:.2f}")