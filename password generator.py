import random
import string

def generate_password(length, include_special_chars
=True):
    if length < 5:
        return "Password length should be at least 5 characters."

    all_characters = string.ascii_letters + string.digits
    if include_special_chars:
      all_characters += string.punctuation

    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

try:
    length = int(input("Enter the length of the password: "))
    choice = input("do you want to enter special characters? (yes/no): ").strip().lower()
    include_special_chars = (choice == 'yes')
    password = generate_password(length,include_special_chars)
    print("Generated Password:", password)
except ValueError:
    print("Enter a valid number for password.") 


