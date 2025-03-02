import re

def is_valid_password(password):
    if (6 <= len(password) <= 16 and
        re.search(r"[a-z]", password) and
        re.search(r"[A-Z]", password) and
        re.search(r"[0-9]", password) and
        re.search(r"[$#@]", password)):
        return True
    return False

while True:
    password = input("Enter your password: ")
    if is_valid_password(password):
        print("Valid password!")
        break
    else:
        print("Invalid password! Try again.")
