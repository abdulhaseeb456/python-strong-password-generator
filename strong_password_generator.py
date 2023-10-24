# Random Password Generator

import random
import string

def generate(limit, length):
    character_set = string.ascii_letters + string.punctuation
    passwords = ["".join(random.choices(character_set, k=length)) for _ in range(limit)]
    return passwords

limit = int(input("Enter the number of passwords to generate: "))
length = int(input("Enter the length of each password: "))
passwords = generate(limit, length)

for i, password in enumerate(passwords, start=1):
    print(f"{i}. {password}")

