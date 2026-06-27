from utils import load_records, save_records

STUDENTS_FILE = "students.txt"


def add_student():
    student_id = input("Enter Student ID: ").strip()
    records = load_records(STUDENTS_FILE)
    for r in records:
        if r.startswith(student_id + ","):
            print("Error: Student ID already exists!")
            return
    name = input("Enter Name: ").strip()
    dept = input("Enter Department: ").strip()
    record = f"{student_id},{name},{dept}"
    records.append(record)
    save_records(STUDENTS_FILE, records)
    print("Student added successfully!")


def remove_student():
    student_id = input("Enter Student ID to remove: ").strip()
    records = load_records(STUDENTS_FILE)
    new_records = [r for r in records if not r.startswith(student_id + ",")]
    if len(new_records) == len(records):
        print("Error: Student ID not found!")
        return
    save_records(STUDENTS_FILE, new_records)
    print("Student removed successfully!")


def search_student():
    keyword = input("Enter search keyword (ID/Name): ").strip().lower()
    records = load_records(STUDENTS_FILE)
    found = [r for r in records if keyword in r.lower()]
    if not found:
        print("No students found!")
        return
    for r in found:
        print(r)


def display_all_students():
    records = load_records(STUDENTS_FILE)
    if not records:
        print("No students registered!")
        return
    print(f"{'ID':<6} {'Name':<25} {'Department':<20}")
    print("=" * 51)
    for r in records:
        parts = r.split(",")
        print(f"{parts[0]:<6} {parts[1]:<25} {parts[2]:<20}")
