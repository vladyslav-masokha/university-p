import requests, json, re
import tkinter as tk
from tkinter import ttk, filedialog
from bs4 import BeautifulSoup

iphones = []

def get_iphones():    
    base_url = "https://rozetka.com.ua/ua/mobile-phones/c80003/"
    url = f"{base_url}producer=apple/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    
    product_blocks = soup.find_all("div", class_="goods-tile")

    for block in product_blocks:
        id = int(block.find("div", class_="g-id").text.strip())
        name = block.find("span", class_="goods-tile__title").text.strip()
        
        price_text = block.find("span", class_="goods-tile__price-value").text.strip()
        price = int("".join(filter(str.isdigit, price_text)))
            
        colors = [re.search(r'#(\w+)', color_elem.find("span", class_="goods-tile__colors-content").get("style")).group(0) for  color_elem in block.find_all("li", class_="goods-tile__colors-item")]
        
        product_url = block.find("a", class_="goods-tile__picture").get("href")
        resp = requests.get(product_url)
        sp = BeautifulSoup(resp.content, "html.parser")
        
        product_about = sp.find_all("div", class_="product-about")
        
        for elem in product_about:
            characters_elem = elem.find("p", class_="product-about__brief")
            if characters_elem:
                characters = characters_elem.text.strip()
                
                ram_match = re.search(r'(\d+)\s*(?:ГБ|ТБ)', characters)
                ram = ram_match.group(0) if ram_match else None

                processor_match = re.search(r'/ (Apple [A-Z]\d+)', characters)
                processor = processor_match.group(1) if processor_match else "Не знайдено"

                screen_match = re.search(r'Екран \((.*?)\)', characters)
                display = screen_match.group(1) if screen_match else "Не знайдено"
                
                system_match = re.search(r'/ iOS (\d+)', characters)
                system = system_match.group(0) if system_match else "Не знайдено"
                system = system.replace("/ ", "")
        
        iphone = {
            "id": id,
            "name": name,
            "price": price,
            "ram": ram,
            "colors": colors,
            "display": display,
            "processor": processor,
            "system": system,
            "url": product_url
        }

        iphones.append(iphone)
    save_changes()

def save_changes():
    global iphones
    with open("iphones.json", "w", encoding="utf-8") as f:
        json.dump(iphones, f, ensure_ascii=False, indent=2)
    print("Changes saved successfully!")

def display_iphones():
    tree.delete(*tree.get_children())
    for iphone in iphones:
        tree.insert("", "end", values=(iphone["id"], iphone["name"], iphone["price"], iphone["ram"], ", ".join(iphone["colors"]), iphone["display"], iphone["processor"], iphone["system"]))
        
def edit_iphone():
    selected_items = tree.selection()
    if not selected_items:
        return

    selected_item = selected_items[0]
    id_ = int(tree.item(selected_item, "values")[0])
    iphone = next((i for i in iphones if i["id"] == id_), None)
    print("Selected iPhone:", iphone)
    if iphone:
        edit_window = tk.Toplevel()
        edit_window.title("Edit iPhone")
        edit_window.geometry("300x300")

        label_name = tk.Label(edit_window, text="Name:")
        label_name.pack()
        entry_name = tk.Entry(edit_window)
        entry_name.pack()
        entry_name.insert(0, iphone["name"])

        label_price = tk.Label(edit_window, text="Price:")
        label_price.pack()
        entry_price = tk.Entry(edit_window)
        entry_price.pack()
        entry_price.insert(0, str(iphone["price"]))

        label_ram = tk.Label(edit_window, text="RAM (GB):")
        label_ram.pack()
        entry_ram = tk.Entry(edit_window)
        entry_ram.pack()
        entry_ram.insert(0, iphone["ram"])

        label_colors = tk.Label(edit_window, text="Colors (comma-separated):")
        label_colors.pack()
        entry_colors = tk.Entry(edit_window)
        entry_colors.pack()
        entry_colors.insert(0, ", ".join(iphone["colors"]))

        label_display = tk.Label(edit_window, text="Display:")
        label_display.pack()
        entry_display = tk.Entry(edit_window)
        entry_display.pack()
        entry_display.insert(0, iphone["display"])
        
        label_processor = tk.Label(edit_window, text="Processor:")
        label_processor.pack()
        entry_processor = tk.Entry(edit_window)
        entry_processor.pack()
        entry_processor.insert(0, iphone["processor"])
        
        label_system = tk.Label(edit_window, text="System:")
        label_system.pack()
        entry_system = tk.Entry(edit_window)
        entry_system.pack()
        entry_system.insert(0, iphone["system"])

        def save_edit():
            nonlocal iphone
            new_iphone = {
                "id": iphone["id"],
                "name": entry_name.get(),
                "price": int(entry_price.get()),
                "ram": entry_ram.get(),
                "colors": entry_colors.get().split(", "),
                "display": entry_display.get(),
                "processor": entry_processor.get(),
                "system": entry_system.get()
            }
            iphones[iphones.index(iphone)] = new_iphone
            edit_window.destroy()
            display_iphones()

        button_save_edit = tk.Button(edit_window, text="Save", command=save_edit)
        button_save_edit.pack()
        entry_name.focus_set()
        
def load_iphones():
    global iphones
    filename = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
    if filename:
        try:
            with open(filename, "r", encoding="utf-8") as f:
                iphones_data = json.load(f)
                iphones = iphones_data
                display_iphones()
                print("JSON file loaded successfully!")
        except FileNotFoundError:
            print("JSON file not found.")

root = tk.Tk()
root.title("iPhone Information")

window_width = 800
window_height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

frame = tk.Frame(root)
frame.pack(pady=20)

tree = ttk.Treeview(frame, columns=("ID", "Name", "Price", "RAM", "Colors", "Display", "Processor", "System"), show="headings")
tree.heading("ID", text="ID")
tree.heading("Name", text="Name")
tree.heading("Price", text="Price")
tree.heading("RAM", text="RAM (GB)")
tree.heading("Colors", text="Colors")
tree.heading("Display", text="Display")
tree.heading("Processor", text="Processor")
tree.heading("System", text="System")

tree.pack(fill="both", expand=True)
        
button_display = tk.Button(frame, text="Get iPhones", command=get_iphones)
button_display.pack(pady=10)
        
button_display = tk.Button(frame, text="Load iPhones", command=load_iphones)
button_display.pack(pady=10)

button_save = tk.Button(frame, text="Save Changes", command=save_changes)
button_save.pack(pady=10)

button_edit = tk.Button(frame, text="Edit iPhone", command=edit_iphone)
button_edit.pack(pady=10)

root.mainloop()
