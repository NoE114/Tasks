products = {}
categories = set()


def add_product():
    product_id = input("Enter Product ID: ")

    if product_id in products:
        print("Product ID already exists!")
        return

    name = input("Enter Product Name: ")
    category = input("Enter Category: ")
    quantity = int(input("Enter Quantity: "))
    price = float(input("Enter Price: "))
    supplier = input("Enter Supplier: ")

    products[product_id] = {
        "name": name,
        "category": category,
        "quantity": quantity,
        "price": price,
        "supplier": supplier
    }

    categories.add(category)

    print("Product Added Successfully!")


def update_inventory():
    product_id = input("Enter Product ID: ")

    if product_id not in products:
        print("Product Not Found!")
        return

    print("1. Update Quantity")
    print("2. Update Price")

    choice = input("Enter Choice: ")

    if choice == "1":
        new_quantity = int(input("Enter New Quantity: "))
        products[product_id]["quantity"] = new_quantity
        print("Quantity Updated!")

    elif choice == "2":
        new_price = float(input("Enter New Price: "))
        products[product_id]["price"] = new_price
        print("Price Updated!")

    else:
        print("Invalid Choice")


def search_product():
    keyword = input("Enter Product ID or Name: ").lower()

    found = False

    for product_id, details in products.items():
        if (
            keyword == product_id.lower()
            or keyword in details["name"].lower()
        ):
            print("\nFound Product")
            print(product_id, details)
            found = True

    if not found:
        print("Product Not Found")


def display_inventory():
    if not products:
        print("Inventory Empty")
        return

    print("\n===== INVENTORY =====")

    for product_id, details in products.items():
        print(
            f"{product_id} | "
            f"{details['name']} | "
            f"{details['category']} | "
            f"Qty:{details['quantity']} | "
            f"₹{details['price']} | "
            f"{details['supplier']}"
        )


def low_stock_alert():
    threshold = 10

    print("\nLow Stock Products")

    found = False

    for product_id, details in products.items():
        if details["quantity"] < threshold:
            print(
                f"{details['name']} "
                f"(ID: {product_id}) "
                f"Qty = {details['quantity']}"
            )
            found = True

    if not found:
        print("No Low Stock Products")


def out_of_stock_alert():
    print("\nOut Of Stock Products")

    found = False

    for product_id, details in products.items():
        if details["quantity"] == 0:
            print(
                f"{details['name']} "
                f"(ID: {product_id})"
            )
            found = True

    if not found:
        print("No Out Of Stock Products")


def category_management():
    print("\nCategories")
    for category in categories:
        print(category)


def inventory_report():
    total_items = 0
    total_value = 0

    category_summary = {}

    for details in products.values():

        total_items += details["quantity"]

        total_value += (
            details["quantity"]
            * details["price"]
        )

        category = details["category"]

        category_summary[category] = (
            category_summary.get(category, 0)
            + details["quantity"]
        )

    print("\n===== INVENTORY REPORT =====")
    print("Total Items:", total_items)
    print("Total Inventory Value: ₹", total_value)

    print("\nCategory Wise Summary")

    for category, quantity in category_summary.items():
        print(category, ":", quantity)


def delete_product():
    product_id = input("Enter Product ID: ")

    if product_id in products:

        snapshot = tuple(products[product_id].items())

        del products[product_id]

        print("Product Deleted")
        print("Snapshot:", snapshot)

    else:
        print("Product Not Found")


while True:

    print("\n===== SMART INVENTORY MANAGEMENT SYSTEM =====")

    print("1. Add Product")
    print("2. Update Inventory")
    print("3. Search Product")
    print("4. Display Inventory")
    print("5. Low Stock Alert")
    print("6. Out Of Stock Alert")
    print("7. Category Management")
    print("8. Inventory Report")
    print("9. Delete Product")
    print("10. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_product()

    elif choice == "2":
        update_inventory()

    elif choice == "3":
        search_product()

    elif choice == "4":
        display_inventory()

    elif choice == "5":
        low_stock_alert()

    elif choice == "6":
        out_of_stock_alert()

    elif choice == "7":
        category_management()

    elif choice == "8":
        inventory_report()

    elif choice == "9":
        delete_product()

    elif choice == "10":
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice")