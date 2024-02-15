import random
import string
import tkinter as tk

def password_generate():
    length = int(length_entry.get())
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation
    
    password = ''
    
    if length < 4:
        password_label.config(text="Password length must be at least 4 characters")
    else:
        for _ in range(length):
            password += random.choice(lowercase_letters + uppercase_letters + digits + special_characters)
        password_label.config(text="Generated Password: " + password)

    return password

root = tk.Tk()
root.title("Password Generator")

length_label = tk.Label(root, text="Password Length:")
length_label.pack()
length_entry = tk.Entry(root)
length_entry.pack()

generate_button = tk.Button(root, text="Generate Password", command=password_generate)
generate_button.pack()

password_label = tk.Label(root, text="")
password_label.pack()

root.mainloop()