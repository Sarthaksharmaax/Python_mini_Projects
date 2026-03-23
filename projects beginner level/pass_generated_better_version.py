import random
print("WELCOME TO THE PASSWORD GENERATOR!")
length = int(input("Enter the length of the password you need: "))
numbers = "1234567890"
alphabets = "qwertyuioplkjhgfdsazxcvbnm"
symbols = "!@/-_"
all_chars = alphabets

num_choice = int(input("Do you need numbers in you password?(1 for yes 0 for no): "))
sym_choice = int(input("Do you need symbols in you password?(1 for yes 0 for no): "))

if num_choice == 1:
    all_chars+= numbers
if sym_choice == 1:
    all_chars+= symbols

password = ""

for i in range(length):
    password += random.choice(all_chars)

print(password)

