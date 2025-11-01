import random
import string

print("Welcome to the Python Password Generator!")

while True:
    try:
        length = int(input("Please enter the desired password length: "))
        if length <= 0:
            print("Length must be greater than 0. Try again.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a number.")

letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation

all_chars = letters + digits + symbols

password = ""
for i in range(length):
    password += random.choice(all_chars)

print("\nYour strong password is:", password)
print("Tip: Keep your password safe and don't share it with anyone!")
