try:
    filename = input("Enter filename: ")

    with open(filename, "r") as file:
        print(file.read())

except FileNotFoundError:
    print("Error: File not found.")