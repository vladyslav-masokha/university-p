import random
import string

def password_generate(length=12):
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    password = random.choice(lowercase_letters) + \
               random.choice(uppercase_letters) + \
               random.choice(digits) + \
               random.choice(special_characters)

    password += ''.join(random.choice(
      lowercase_letters + uppercase_letters + digits + special_characters
    ) for _ in range(length))

    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    return password

length = int(input("Enter the length of the password: "))
print("Generated Password:", password_generate(length))
