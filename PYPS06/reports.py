from utils import load_records

BOOKS_FILE = "books.txt"
STUDENTS_FILE = "students.txt"
ISSUED_FILE = "issued.txt"


def all_books():
    records = load_records(BOOKS_FILE)
    if not records:
        print("No books in library!")
        return
    print(f"{'ID':<6} {'Title':<25} {'Author':<20} {'Category':<15} {'Total':<6} {'Available':<10}")
    print("=" * 82)
    for r in records:
        parts = r.split(",")
        print(f"{parts[0]:<6} {parts[1]:<25} {parts[2]:<20} {parts[3]:<15} {parts[4]:<6} {parts[5]:<10}")


def available_books():
    records = load_records(BOOKS_FILE)
    available = [r for r in records if int(r.split(",")[5]) > 0]
    if not available:
        print("No available books!")
        return
    for r in available:
        print(r)


def borrowed_books():
    issued = load_records(ISSUED_FILE)
    books = load_records(BOOKS_FILE)
    if not issued:
        print("No books currently issued!")
        return
    for rec in issued:
        parts = rec.split(",")
        book_id = parts[2]
        book_info = "Unknown"
        for b in books:
            if b.startswith(book_id + ","):
                book_info = b
                break
        print(f"{parts[0]} | Student: {parts[1]} | Book: {book_info}")


def students_with_borrowed():
    issued = load_records(ISSUED_FILE)
    students = load_records(STUDENTS_FILE)
    if not issued:
        print("No books currently issued!")
        return
    for rec in issued:
        parts = rec.split(",")
        sid = parts[1]
        student_info = "Unknown"
        for s in students:
            if s.startswith(sid + ","):
                student_info = s
                break
        print(f"Issue: {parts[0]} | Student: {student_info} | Book ID: {parts[2]} | Due: {parts[4]}")


def total_books():
    records = load_records(BOOKS_FILE)
    print(f"Total books in library: {len(records)}")


def total_students():
    records = load_records(STUDENTS_FILE)
    print(f"Total registered students: {len(records)}")
