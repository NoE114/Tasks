bill_amount = float(input("Enter total bill amount: "))
number_of_people = int(input("Enter number of people: "))
tip_percentage = float(input("Enter tip percentage: "))


tip_amount = (bill_amount * tip_percentage) / 100

total_with_tip = bill_amount + tip_amount

amount_per_person = total_with_tip / number_of_people

remainder_example = bill_amount % number_of_people
subtraction_example = total_with_tip - tip_amount


tip_amount = round(tip_amount, 2)
total_with_tip = round(total_with_tip, 2)
amount_per_person = round(amount_per_person, 2)

print("\n===== BILL SUMMARY =====")
print(f"Original Bill      : {bill_amount}")
print(f"Tip Percentage     : {tip_percentage}%")
print(f"Tip Amount         : {tip_amount}")
print(f"Total With Tip     : {total_with_tip}")
print(f"People             : {number_of_people}")
print(f"Amount Per Person  : {amount_per_person}")
print(f"Remainder Example  : {remainder_example}")
print(f"Subtraction Check  : {subtraction_example}")
print("========================")