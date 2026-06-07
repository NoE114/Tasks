#Create a List of 5 Fruits and Print All Items
fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]

for fruit in fruits:
    print(fruit)

#Create a Tuple of 3 Colors and Print the First Color
colors = ("Red", "Green", "Blue")

print("First Color:", colors[0])

#Create a Dictionary with Student Names and Marks
students = {
    "Rahul": 85,
    "Priya": 92,
    "Amit": 78
}

print(students)

#Create a Set of 5 Numbers and Print All Unique Values
numbers = {10, 20, 30, 40, 50}

for number in numbers:
    print(number)

#Create a Dictionary of Products and Quantities
products = {
    "Laptop": 10,
    "Mouse": 25,
    "Keyboard": 15
}

print("Stock Details:")

for product, quantity in products.items():
    print(product, ":", quantity)