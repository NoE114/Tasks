import math

def circle_area(radius):
    return math.pi * radius * radius

def rectangle_area(length, width):
    return length * width

choice = input("Circle or Rectangle (c/r): ")

if choice.lower() == "c":
    radius = float(input("Enter radius: "))
    print("Area =", circle_area(radius))

elif choice.lower() == "r":
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    print("Area =", rectangle_area(length, width))