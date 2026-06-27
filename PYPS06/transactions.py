from utils import load_records, save_records, get_today, validate_date, get_next_id, LOAN_DAYS, FINE_PER_DAY
from datetime import timedelta, date

BOOKS_FILE = "books.txt"
STUDENTS_FILE = "students.txt"
ISSUED_FILE = "issued.txt"


def issue_book():
    student_id = input("Enter Student ID: ").strip()
    book_id = input("Enter Book ID: ").strip()

    students = load_records(STUDENTS_FILE)
    if not any(s.startswith(student_id + ",") for s in students):
        print("Error: Student ID not found!")
        return

    books = load_records(BOOKS_FILE)
    book_idx = None
    for i, b in enumerate(books):
        parts = b.split(",")
        if parts[0] == book_id:
            book_idx = i
            if int(parts[5]) <= 0:
                print("Error: No copies available!")
                return
            break
    if book_idx is None:
        print("Error: Book ID not found!")
        return

    parts = books[book_idx].split(",")
    parts[5] = str(int(parts[5]) - 1)
    books[book_idx] = ",".join(parts)
    save_records(BOOKS_FILE, books)

    issued = load_records(ISSUED_FILE)
    issue_id = get_next_id(issued, "I")
    issue_date = get_today()
    due_date = (date.today() + timedelta(days=LOAN_DAYS)).strftime("%Y-%m-%d")
    record = f"{issue_id},{student_id},{book_id},{issue_date},{due_date}"
    issued.append(record)
    save_records(ISSUED_FILE, issued)

    print(f"Book issued successfully! Issue ID: {issue_id}, Due Date: {due_date}")


def return_book():
    issue_id = input("Enter Issue ID: ").strip()
    issued = load_records(ISSUED_FILE)

    found = None
    for i, rec in enumerate(issued):
        if rec.startswith(issue_id + ","):
            found = i
            break

    if found is None:
        print("Error: Issue record not found!")
        return

    parts = issued[found].split(",")
    student_id, book_id, issue_date, due_date = parts[1], parts[2], parts[3], parts[4]

    books = load_records(BOOKS_FILE)
    for j, b in enumerate(books):
        bparts = b.split(",")
        if bparts[0] == book_id:
            bparts[5] = str(int(bparts[5]) + 1)
            books[j] = ",".join(bparts)
            break
    save_records(BOOKS_FILE, books)

    issued.pop(found)
    save_records(ISSUED_FILE, issued)

    fine = calculate_fine(due_date)
    if fine > 0:
        print(f"Book returned successfully! Late fine: \u20b9{fine}")
    else:
        print("Book returned successfully! No fine.")


def calculate_fine(due_date_str):
    today = date.today()
    due = validate_date(due_date_str)
    if due is None:
        return 0
    if today > due:
        days_late = (today - due).days
        return days_late * FINE_PER_DAY
    return 0
