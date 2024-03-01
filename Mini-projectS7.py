import re

while True:
    password = input("Enter your password: ")

    if len(password) < 8:
        print("Password must be at least 8 characters long.")
    if not re.search("[A-Z]", password):
        print("Password must contain at least one uppercase letter.")
    if not re.search("[a-z]", password):
        print("Password must contain at least one lowercase letter.")
    if not re.search("[0-9]", password):
        print("Password must contain at least one digit.")
    if not re.search("[!@#$%^&*()_+=\-{}[\]:;\"'|\\<>,.?/]", password):
        print("Password must contain at least one special character.")
    else:
        print("Password accepted.")
        break