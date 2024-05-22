import tkinter as tk
import matplotlib.pyplot as plt

def generate_table():
    try:
        num_pairs = int(entry.get())
        for i in range(num_pairs):
            for j in range(2):
                cell = tk.Entry(table_frame, width=10)
                cell.grid(row=i, column=j)
                table_entries.append(cell)
        status_label.config(text="", fg="black")
    except ValueError:
        status_label.config(text="Введіть валідне число", fg="red")

def plot_graph():
    x_values = []
    y_values = []
    if len(table_entries) % 2 != 0:
        status_label.config(text="Будь ласка, введіть як x, так і y для кожної пари", fg="red")
        return
    else:
      status_label.config(text="", fg="black")
      
    for i in range(0, len(table_entries), 2):
        x_entry = table_entries[i].get()
        y_entry = table_entries[i+1].get()
        if x_entry and y_entry:
            try:
                x_values.append(float(x_entry))
                y_values.append(float(y_entry))
                status_label.config(text="", fg="black")
            except ValueError:
                status_label.config(text="Будь ласка, введіть дійсні числові значення", fg="red")
                return
        else:
            status_label.config(text="Будь ласка, введіть як x, так і y для кожної пари", fg="red")
            return
    plt.plot(x_values, y_values)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Графік')
    plt.grid(True)
    plt.show()

root = tk.Tk()
root.title("Побудовник графіків")
root.geometry("400x300")

label = tk.Label(root, text="Введіть кількість пар (x;y):")
label.pack()

entry = tk.Entry(root)
entry.pack()

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

generate_button = tk.Button(button_frame, text="Згенерувати таблицю", command=generate_table)
generate_button.pack(side=tk.LEFT, padx=5)

plot_button = tk.Button(button_frame, text="Згенерувати граф", command=plot_graph)
plot_button.pack(side=tk.LEFT, padx=5)

table_frame = tk.Frame(root)
table_frame.pack()

status_label = tk.Label(root, text="")
status_label.pack()

table_entries = []

root.mainloop()
