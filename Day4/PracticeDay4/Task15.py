def calculate_salary(hours_worked, hourly_rate):
    return hours_worked * hourly_rate

employee_name = input("Enter employee name: ")
hours_worked = float(input("Enter hours worked: "))
hourly_rate = float(input("Enter hourly rate: "))

salary = calculate_salary(hours_worked, hourly_rate)

print("\nEmployee Name:", employee_name)
print("Salary:", salary)