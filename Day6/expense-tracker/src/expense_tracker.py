import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE = os.path.join(BASE_DIR, "..", "data", "expenses.json")


def load_expenses():
    if not os.path.exists(FILE):
        return []

    with open(FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def save_expenses(expenses):
    with open(FILE, "w") as f:
        json.dump(expenses, f, indent=4)


def add_expense():
    expenses = load_expenses()

    name = input("Expense Name: ")
    amount = float(input("Amount: "))

    expenses.append({
        "name": name,
        "amount": amount
    })

    save_expenses(expenses)
    print("Expense Added Successfully")


def view_expenses():
    expenses = load_expenses()

    if not expenses:
        print("No expenses found.")
        return

    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense['name']} - ₹{expense['amount']}")


def delete_expense():
    expenses = load_expenses()

    view_expenses()

    if not expenses:
        return

    index = int(input("Enter expense number to delete: ")) - 1

    if 0 <= index < len(expenses):
        removed = expenses.pop(index)
        save_expenses(expenses)
        print(f"{removed['name']} deleted.")
    else:
        print("Invalid choice.")


def total_spending():
    expenses = load_expenses()
    total = sum(expense["amount"] for expense in expenses)
    print("Total Spending: ₹", total)


while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Total Spending")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        delete_expense()
    elif choice == "4":
        total_spending()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")