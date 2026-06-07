def check_eligibility(age):
    return age >= 18

age = int(input("Enter age: "))

if check_eligibility(age):
    print("Eligible to Vote")
else:
    print("Not Eligible to Vote")