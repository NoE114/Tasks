# BUG 1 — RUNTIME ERROR
# Type  : IndexError
# Cause : Accessing an index that does not exist in the list
# Fix   : Use valid indices (0–4 for a list of 5 marks)

# BUGGY CODE:
marks = [78, 85, 90, 67, 88]
# print(marks[5])  # IndexError

# FIXED CODE:
print("First Mark:", marks[0])


# BUG 2 — LOGICAL ERROR
# Type  : Logical Error
# Cause : Average calculated using wrong divisor (4 instead of 5)
# Fix   : Divide total marks by the number of students

# BUGGY CODE:
# average = sum(marks) / 4

# FIXED CODE:
average = sum(marks) / 5


# PROGRAM: Marks Calculator

marks = []

for i in range(5):
    mark = float(input(f"Enter marks of student {i + 1}: "))
    marks.append(mark)

total = sum(marks)
average = total / len(marks)
highest = max(marks)
lowest = min(marks)

print("\nTotal Marks:", total)
print("Average Marks:", average)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)