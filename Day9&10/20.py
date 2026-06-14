import math

def area_circle(radius):
    return math.pi * radius * radius

r = float(input("Enter radius: "))
print("Area =", area_circle(r))