import csv

students = [
    [1, "Rahul", 80, 75, 90, 85],
    [2, "Priya", 88, 92, 84, 90],
    [3, "Amit", 70, 65, 72, 68],
    [4, "Sneha", 95, 90, 96, 94],
    [5, "Rohan", 78, 82, 80, 76],
    [6, "Anjali", 85, 87, 89, 90],
    [7, "Karan", 60, 65, 70, 75],
    [8, "Neha", 91, 89, 93, 95],
    [9, "Vikram", 73, 77, 75, 79],
    [10, "Pooja", 86, 88, 90, 84]
]

# Create CSV file
with open("student.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Roll No", "Name", "Math", "Science", "English", "Computer"])
    writer.writerows(students)

print("CSV file created successfully.\n")

# Read and display records
print("Student Records:")
with open("student.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Find highest scorer
highest_student = None
highest_total = 0

for student in students:
    total = sum(student[2:])
    if total > highest_total:
        highest_total = total
        highest_student = student

print("\nHighest Scorer:")
print(f"Roll No: {highest_student[0]}")
print(f"Name: {highest_student[1]}")
print(f"Total Marks: {highest_total}")

# Calculate average marks of all students
grand_total = 0

for student in students:
    grand_total += sum(student[2:])

average_marks = grand_total / len(students)

print("\nAverage Marks of All Students:", round(average_marks, 2))