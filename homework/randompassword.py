# Write a Python program to generate a random password consisting of lower case and upper case characters along with numbers. You can also use random module for shuffling the password generated.

import random
import string

def generate_password(length=10):
    # Define character sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits

    # Ensure password has at least one of each
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits)
    ]

    # Fill the rest of the password length
    all_chars = lower + upper + digits
    for _ in range(length - 3):
        password.append(random.choice(all_chars))

    # Shuffle the password list
    random.shuffle(password)

    # Convert list to string
    return ''.join(password)

# Generate and print password
print("Generated Password:", generate_password(12))