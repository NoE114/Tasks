from utils import load_records, save_records, CATEGORIES

BOOKS_FILE = "books.txt"


def add_book():
    book_id = input("Enter Book ID: ").strip()
    records = load_records(BOOKS_FILE)
    for r in records:
        if r.startswith(book_id + ","):
            print("Error: Book ID already exists!")
            return
    title = input("Enter Title: ").strip()
    author = input("Enter Author: ").strip()
    print("Categories:", ", ".join(CATEGORIES))
    category = input("Enter Category: ").strip()
    try:
        total = int(input("Enter Total Copies: "))
        available = int(input("Enter Available Copies: "))
    except ValueError:
        print("Error: Invalid number!")
        return
    if total < 0 or available < 0:
        print("Error: Copies cannot be negative!")
        return
    record = f"{book_id},{title},{author},{category},{total},{available}"
    records.append(record)
    save_records(BOOKS_FILE, records)
    print("Book added successfully!")


def remove_book():
    book_id = input("Enter Book ID to remove: ").strip()
    records = load_records(BOOKS_FILE)
    new_records = [r for r in records if not r.startswith(book_id + ",")]
    if len(new_records) == len(records):
        print("Error: Book ID not found!")
        return
    save_records(BOOKS_FILE, new_records)
    print("Book removed successfully!")


def update_book():
    book_id = input("Enter Book ID to update: ").strip()
    records = load_records(BOOKS_FILE)
    for i, r in enumerate(records):
        if r.startswith(book_id + ","):
            parts = r.split(",")
            print("Current:", r)
            print("1. Title  2. Author  3. Category  4. Total Copies  5. Available Copies")
            try:
                field = int(input("Select field (1-5): "))
                if field < 1 or field > 5:
                    print("Error: Invalid field!")
                    return
                new_val = input("Enter new value: ").strip()
                if field == 4 or field == 5:
                    try:
                        int(new_val)
                    except ValueError:
                        print("Error: Invalid number!")
                        return
                parts[field] = new_val
                records[i] = ",".join(parts)
                save_records(BOOKS_FILE, records)
                print("Book updated successfully!")
            except ValueError:
                print("Error: Invalid input!")
            return
    print("Error: Book ID not found!")


def search_book():
    print("Search by:")
    print("1. Keyword (ID/Title/Author)")
    print("2. Category")
    try:
        opt = int(input("Choose option: "))
    except ValueError:
        print("Error: Invalid choice!")
        return
    if opt == 2:
        filter_by_category()
        return
    keyword = input("Enter search keyword: ").strip().lower()
    records = load_records(BOOKS_FILE)
    found = [r for r in records if keyword in r.lower()]
    if not found:
        print("No books found!")
        return
    for r in found:
        print(r)


def filter_by_category():
    print("Categories:", ", ".join(CATEGORIES))
    cat = input("Enter category: ").strip().lower()
    records = load_records(BOOKS_FILE)
    found = []
    for r in records:
        parts = r.split(",")
        if len(parts) > 3 and parts[3].strip().lower() == cat:
            found.append(r)
    if not found:
        print("No books found in that category!")
        return
    for r in found:
        print(r)


def display_all_books():
    records = load_records(BOOKS_FILE)
    if not records:
        print("No books in library!")
        return
    print(f"{'ID':<6} {'Title':<25} {'Author':<20} {'Category':<15} {'Total':<6} {'Available':<10}")
    print("=" * 82)
    for r in records:
        parts = r.split(",")
        print(f"{parts[0]:<6} {parts[1]:<25} {parts[2]:<20} {parts[3]:<15} {parts[4]:<6} {parts[5]:<10}")
