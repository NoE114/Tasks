import books
import students
import transactions
import reports


def reports_menu():
    while True:
        print("\n--- Reports Menu ---")
        print("1. All Books")
        print("2. Available Books")
        print("3. Borrowed Books")
        print("4. Students with Borrowed Books")
        print("5. Total Books")
        print("6. Total Students")
        print("7. Back to Main Menu")

        try:
            rchoice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid choice! Please enter a number.")
            continue

        if rchoice == 1:
            reports.all_books()
        elif rchoice == 2:
            reports.available_books()
        elif rchoice == 3:
            reports.borrowed_books()
        elif rchoice == 4:
            reports.students_with_borrowed()
        elif rchoice == 5:
            reports.total_books()
        elif rchoice == 6:
            reports.total_students()
        elif rchoice == 7:
            break
        else:
            print("Invalid choice! Please select 1-7.")


def main():
    while True:
        print("\n========= Library Management System =========")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Search Book")
        print("4. Display Books")
        print("5. Add Student")
        print("6. Remove Student")
        print("7. Search Student")
        print("8. Issue Book")
        print("9. Return Book")
        print("10. Reports")
        print("11. Exit")
        print("=" * 45)

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid choice! Please enter a number.")
            continue

        if choice == 1:
            books.add_book()
        elif choice == 2:
            books.remove_book()
        elif choice == 3:
            books.search_book()
        elif choice == 4:
            books.display_all_books()
        elif choice == 5:
            students.add_student()
        elif choice == 6:
            students.remove_student()
        elif choice == 7:
            students.search_student()
        elif choice == 8:
            transactions.issue_book()
        elif choice == 9:
            transactions.return_book()
        elif choice == 10:
            reports_menu()
        elif choice == 11:
            print("Thank you for using Library Management System!")
            break
        else:
            print("Invalid choice! Please select 1-11.")


if __name__ == "__main__":
    main()
