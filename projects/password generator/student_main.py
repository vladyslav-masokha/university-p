import random
import string
import tkinter as tk

# Function generated password
def generate_password():
    try:
        user_upper = int(upper_entry.get())
        user_lower = int(lower_entry.get())
        user_digits = int(digits_entry.get())
        user_characters = int(characters_entry.get())
        
        upper = random.sample(string.ascii_uppercase, user_upper)
        lower = random.sample(string.ascii_lowercase, user_lower)
        digits = random.sample(string.digits, user_digits)
        characters = random.sample(string.punctuation, user_characters)
        
        password = lower + upper + digits + characters
        password = random.sample(password, len(password))
        password = ''.join(password)
        
        # start idk
        password_text.config(state=tk.NORMAL)
        password_text.delete(0, tk.END)
        password_text.insert(tk.END, password)
        password_text.config(state='readonly')
    except ValueError:
        password_text.config(state=tk.NORMAL)
        password_text.delete(0, tk.END)
        password_text.insert(tk.END, 'No Valid Number')
        password_text.config(state='readonly')
        # end idk

# Start module
root = tk.Tk()
root.title('Password generator')
root.geometry('280x200')

# Uppercase letter
upper_label = tk.Label(root, text='Uppercase: ')
upper_label.grid(row=0, column=0, pady=5, sticky='e')
upper_entry = tk.Entry(root)
upper_entry.grid(row=0, column=1, pady=5)
upper_entry.insert(0, '2')

# Lowercase letter
lower_label = tk.Label(root, text='Lowercase: ')
lower_label.grid(row=1, column=0, pady=5, sticky='e')
lower_entry = tk.Entry(root)
lower_entry.grid(row=1, column=1, pady=5)
lower_entry.insert(0, '2')

# Numbers
digits_label = tk.Label(root, text='Digits: ')
digits_label.grid(row=2, column=0, pady=5, sticky='e')
digits_entry = tk.Entry(root)
digits_entry.grid(row=2, column=1, pady=5)
digits_entry.insert(0, '2')

# Characters
characters_label = tk.Label(root, text='Characters: ')
characters_label.grid(row=3, column=0, pady=5, sticky='e')
characters_entry = tk.Entry(root)
characters_entry.grid(row=3, column=1, pady=5)
characters_entry.insert(0, '2')

# Button for generate password
generate_button = tk.Button(root, text='Generate', command=generate_password)
generate_button.grid(row=4, column=0, padx=(15, 5), pady=5, sticky='w')

# Button for close application
cancel_button = tk.Button(root, text='Cancel', command=root.destroy)
cancel_button.grid(row=4, column=1, pady=5, sticky='w')

# Field for generated password
password_label = tk.Label(root, text='Password: ')
password_label.grid(row=6, column=0, pady=5, sticky='e')
password_text = tk.Entry(root, state='readonly', readonlybackground='white')
password_text.grid(row=6, column=1, pady=5, sticky='w')

# Close module
root.mainloop()