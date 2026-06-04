import random

target_units = int(input("Target Units: "))
workers = int(input("Workers Per Shift: "))
defect_rate = float(input("Defect Rate (%): "))

total_produced = 0
total_defects = 0

for shift in range(1, 4):

    shift_produced = 0
    shift_defects = 0

    print(f"\n--- Shift {shift} ---")

    for cycle in range(1, 21):

        if total_produced >= target_units:
            print("Target Achieved")
            break

        item_defective = random.randint(1, 100) <= defect_rate

        if item_defective:
            shift_defects += 1
            total_defects += 1
            continue

        shift_produced += workers
        total_produced += workers

    productivity = shift_produced / workers

    print("Produced:", shift_produced)
    print("Defects:", shift_defects)
    print("Productivity:", productivity)

    if total_produced >= target_units:
        break

print("\n===== FINAL REPORT =====")
print("Total Produced:", total_produced)
print("Total Defects:", total_defects)
print("Target:", target_units)

if total_produced >= target_units:
    print("Status: Target Achieved")
else:
    print("Status: Target Not Reached")