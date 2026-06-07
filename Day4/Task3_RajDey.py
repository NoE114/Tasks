def calculate_attendance(attended_classes, total_classes):
    return (attended_classes / total_classes) * 100


total_classes = int(input("Enter Total Classes: "))
attended_classes = int(input("Enter Attended Classes: "))

attendance_percentage = calculate_attendance(
    attended_classes,
    total_classes
)

print("\n----- ATTENDANCE REPORT -----")
print(f"Attendance Percentage: {attendance_percentage:.2f}%")

required_percentage = 75

if attendance_percentage >= required_percentage:
    print("Status: Attendance Requirement Met")

else:
    print("Status: Attendance Requirement Not Met")

    extra_classes_needed = 0
    current_attended = attended_classes
    current_total = total_classes

    while (current_attended / current_total) * 100 < required_percentage:
        current_attended += 1
        current_total += 1
        extra_classes_needed += 1

    print(
        f"Additional Classes Required: {extra_classes_needed}"
    )