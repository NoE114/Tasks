def validate_password(password):
    return len(password) >= 8

password = input("Enter password: ")

if validate_password(password):
    print("Valid Password")
else:
    print("Password must be at least 8 characters long")