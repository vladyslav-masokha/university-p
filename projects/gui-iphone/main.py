import requests, json, re
import tkinter as tk
from tkinter import ttk, filedialog
from bs4 import BeautifulSoup
from PIL import Image, ImageTk

images = {}
iphones = []
color_names = {
    "#000": "Чорний",
    "#33F": "Блакитний",
    "#666": "Сірий",
    "#FFF": "Білий",
    "#30C": "Синій",
    "#181F27": "Чорний",
    "#F9F": "Рожевий",
    "#F00": "Червоний",
    "#f00": "Червоний",
    "#F8F3EF": "Білий",
    "#390": "Зелений",
    "#909": "Рожевий",
    "#FF0": "Жовтий",
    "#FFD700": "Жовтий",
    "#CCC": "Сірий",
}

def get_iphones():
    max_pages = 3
    base_url = "https://rozetka.com.ua/ua/mobile-phones/c80003/"
    
    for page in range(1, max_pages + 1):
        url = f"{base_url}page={page};producer=apple/"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        product_blocks = soup.find_all("div", class_="goods-tile")

        for block in product_blocks:
            id = int(block.find("div", class_="g-id").text.strip())
            name = block.find("span", class_="goods-tile__title").text.strip()
            name = name.replace("Мобільний телефон ", "")

            price_text = block.find("span", class_="goods-tile__price-value").text.strip()
            price = int("".join(filter(str.isdigit, price_text)))

            colors = [re.search(r'#(\w+)', color_elem.find("span", class_="goods-tile__colors-content").get("style")).group(0) for color_elem in block.find_all("li", class_="goods-tile__colors-item")]

            image_url = block.find("img").get("src")
            
            product_url = block.find("a", class_="goods-tile__picture").get("href")
            resp = requests.get(product_url)
            sp = BeautifulSoup(resp.content, "html.parser")

            product_about = sp.find_all("div", class_="product-about")

            for elem in product_about:
                characters_elem = elem.find("p", class_="product-about__brief")
                
                if characters_elem:
                    characters = characters_elem.text.strip()

                    ram_match = re.search(r'RAM (\d+)\s*(?:ГБ|ТБ)', characters)
                    ram = ram_match.group(0) if ram_match else "Немає даних"
                    ram = ram.replace('RAM ', "")

                    storage_match = re.search(r'(\d+)\s*ГБ вбудованої пам\'яті', characters)
                    storage = storage_match.group(0) if storage_match else "Немає даних"
                    storage = storage.replace(" вбудованої пам'яті", "")

                    processor_match = re.search(r'/ (Apple [A-Z]\d+)', characters)
                    processor = processor_match.group(1) if processor_match else "Немає даних"

                    screen_match = re.search(r'Екран \((.*?)\)', characters)
                    display = screen_match.group() if screen_match else "Немає даних"

                    system_match = re.search(r'/ iOS (\d+)', characters)
                    system = system_match.group(0) if system_match else "Немає даних"
                    system = system.replace("/ ", "")

            iphone = {
                "id": id,
                "name": name,
                "price": price,
                "ram": ram,
                "storage": storage,
                "colors": colors,
                "display": display,
                "processor": processor,
                "system": system,
                "url": product_url,
                "image_url": image_url
            }

            iphones.append(iphone)

    save_changes()

def save_changes():
    global iphones
    with open("iphones.json", "w", encoding="utf-8") as f:
        json.dump(iphones, f, ensure_ascii=False, indent=4)
    print("Зміни збережено!")

def display_iphones():
    global selected_image
    selected_image = None

    tree.delete(*tree.get_children())
    for iphone in iphones:
        storage = iphone.get("storage", "Немає даних")
        colors_text = ", ".join(color_names.get(color, color) for color in iphone["colors"])
        image_url = iphone.get("image_url")

        tree.insert("", "end", values=(iphone["id"], iphone["name"], iphone["price"], iphone["ram"], storage, colors_text, iphone["display"], iphone["processor"], iphone["system"], image_url))

    tree.column("Картинка", width=200)
        
def show_selected_image(event):
    global selected_image
    selected_item = tree.selection()
    if selected_item:
        item = tree.item(selected_item)
        image_url = item["values"][9]

        if image_url:
            response = requests.get(image_url, stream=True)
            image = Image.open(response.raw)
            photo = ImageTk.PhotoImage(image.resize((200, 200), Image.LANCZOS))
            selected_image = photo
            image_label.configure(image=photo)
            image_label.image = photo
        else:
            image_label.configure(image=None)
        
def edit_iphone():
    selected_items = tree.selection()
    if not selected_items:
        return

    selected_item = selected_items[0]
    id_ = int(tree.item(selected_item, "values")[0])
    iphone = next((i for i in iphones if i["id"] == id_), None)
    photo = images.get(iphone["id"])
    
    if iphone:
        edit_window = tk.Toplevel()
        edit_window.title("Редагування")
        edit_window.geometry("500x600")

        label_name = tk.Label(edit_window, text="Назва:")
        label_name.pack()
        entry_name = tk.Entry(edit_window, width=50)
        entry_name.pack()
        entry_name.insert(0, iphone["name"])

        label_price = tk.Label(edit_window, text="Ціна:")
        label_price.pack()
        entry_price = tk.Entry(edit_window, width=50)
        entry_price.pack()
        entry_price.insert(0, str(iphone["price"]))

        label_ram = tk.Label(edit_window, text="Оперативна пам'ять:")
        label_ram.pack()
        entry_ram = tk.Entry(edit_window, width=50)
        entry_ram.pack()
        entry_ram.insert(0, iphone["ram"])

        label_storage = tk.Label(edit_window, text="Вбудована пам'ять:")
        label_storage.pack()
        entry_storage = tk.Entry(edit_window, width=50)
        entry_storage.pack()
        entry_storage.insert(0, iphone["storage"])

        label_colors = tk.Label(edit_window, text="Кольори (comma-separated):")
        label_colors.pack()
        entry_colors = tk.Entry(edit_window, width=50)
        entry_colors.pack()
        entry_colors.insert(0, ", ".join(color_names.get(color, color) for color in iphone["colors"]))

        label_display = tk.Label(edit_window, text="Екран:")
        label_display.pack()
        entry_display = tk.Entry(edit_window, width=50)
        entry_display.pack()
        entry_display.insert(0, iphone["display"])

        label_processor = tk.Label(edit_window, text="Процесор:")
        label_processor.pack()
        entry_processor = tk.Entry(edit_window, width=50)
        entry_processor.pack()
        entry_processor.insert(0, iphone["processor"])

        label_system = tk.Label(edit_window, text="Система:")
        label_system.pack()
        entry_system = tk.Entry(edit_window, width=50)
        entry_system.pack()
        entry_system.insert(0, iphone["system"])
        
        label_image = tk.Label(edit_window, text="Картинка (посилання):")
        label_image.pack()
        entry_image = tk.Entry(edit_window, width=50)
        entry_image.pack()
        entry_image.insert(0, iphone["image_url"])
        
        image_url = iphone.get("image_url")
        if image_url:
            image = Image.open(requests.get(image_url, stream=True).raw)
            image = image.resize((100, 100), Image.LANCZOS)
            photo = ImageTk.PhotoImage(image)
            label_image = tk.Label(edit_window, image=photo)
            label_image.image = photo 
            label_image.pack()

        def save_edit():
            nonlocal iphone
            new_iphone = {
                "id": iphone["id"],
                "name": entry_name.get(),
                "price": int(entry_price.get()),
                "ram": entry_ram.get(),
                "storage": entry_storage.get(),
                "colors": entry_colors.get().split(", "),
                "display": entry_display.get(),
                "processor": entry_processor.get(),
                "system": entry_system.get(),
                "image_url": entry_image.get()
            }
            iphones[iphones.index(iphone)] = new_iphone
            edit_window.destroy()
            display_iphones()

        button_save_edit = tk.Button(edit_window, text="Зберегти", command=save_edit)
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
                print("JSON файл успішно завантажений!")
        except FileNotFoundError:
            print("JSON файл не знайдено.")
        
def treeview_sort_column(tv, col, reverse):
    l = [(tv.set(k, col), k) for k in tv.get_children('')]
    l.sort(reverse=reverse)

    for index, (val, k) in enumerate(l):
        tv.move(k, '', index)

    tv.heading(col, command=lambda: treeview_sort_column(tv, col, not reverse))

root = tk.Tk()
root.title("Інформація про iPhone")

window_width = 1120
window_height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

frame = tk.Frame(root)
frame.pack(pady=20, expand=True)
frame.config(height=600)

tree = ttk.Treeview(frame, columns=("ID", "Назва", "Ціна", "Оперативна пам'ять", "Вбудована пам'ять", "Кольори", "Екран", "Процесор", "Система", "Картинка"), show="headings")

tree.heading("ID", text="ID", command=lambda: treeview_sort_column(tree, "ID", False))
tree.heading("Назва", text="Назва", command=lambda: treeview_sort_column(tree, "Назва", False))
tree.heading("Ціна", text="Ціна", command=lambda: treeview_sort_column(tree, "Ціна", False))
tree.heading("Оперативна пам'ять", text="Оперативна пам'ять", command=lambda: treeview_sort_column(tree, "Оперативна пам'ять", False))
tree.heading("Вбудована пам'ять", text="Вбудована пам'ять", command=lambda: treeview_sort_column(tree, "Вбудована пам'ять", False))
tree.heading("Кольори", text="Кольори", command=lambda: treeview_sort_column(tree, "Кольори", False))
tree.heading("Екран", text="Екран", command=lambda: treeview_sort_column(tree, "Екран", False))
tree.heading("Процесор", text="Процесор", command=lambda: treeview_sort_column(tree, "Процесор", False))
tree.heading("Система", text="Система", command=lambda: treeview_sort_column(tree, "Система", False))
tree.heading("Картинка", text="Картинка", command=lambda: treeview_sort_column(tree, "Картинка", False))

tree.pack(fill="both", expand=True)

for col in tree["columns"]:
    tree.heading(col, text=col)
    
tree.column("ID", width=70)
tree.column("Назва", width=150)
tree.column("Ціна", width=60)
tree.column("Оперативна пам'ять", width=100)
tree.column("Вбудована пам'ять", width=70)
tree.column("Кольори", width=120)
tree.column("Екран", width=230)
tree.column("Процесор", width=100)
tree.column("Система", width=70)
tree.column("Картинка", width=50)

tree.bind("<<TreeviewSelect>>", show_selected_image)

button_frame = tk.Frame(root)
button_frame.pack(side=tk.LEFT, padx=20, pady=20)

button_display = tk.Button(button_frame, text="Отримати дані", command=get_iphones)
button_display.pack(pady=10)

button_display = tk.Button(button_frame, text="Завантажити JSON", command=load_iphones)
button_display.pack(pady=10)

button_save = tk.Button(button_frame, text="Зберегти зміни", command=save_changes)
button_save.pack(pady=10)

button_edit = tk.Button(button_frame, text="Редагувати", command=edit_iphone)
button_edit.pack(pady=10)

image_label = tk.Label(root)
image_label.pack(side=tk.RIGHT, padx=20, pady=20)

root.mainloop()
