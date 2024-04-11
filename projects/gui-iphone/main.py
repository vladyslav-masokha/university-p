import requests, json, re
from bs4 import BeautifulSoup

base_url = "https://rozetka.com.ua/ua/mobile-phones/c80003/"
iphones = []

url = f"{base_url}producer=apple/"
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html, "html.parser")
product_blocks = soup.find_all("div", class_="goods-tile")

for block in product_blocks:
    name = block.find("span", class_="goods-tile__title").text.strip()
    price_text = block.find("span", class_="goods-tile__price-value").text.strip()
    price = int(re.sub(r'[^\d]', '', price_text))

    ram_storage_div = block.find("div", string=re.compile(r"ГБ"))
    if ram_storage_div:
        ram_storage_text = ram_storage_div.text.strip()
        ram, storage = map(lambda x: int(x.replace(" ГБ", "")), ram_storage_text.split("/"))
    else:
        ram = None
        storage = None

    colors = [color.text.strip() for color in block.find_all("div", class_="goods-tile__colors-item-color")]

    product_url = block.find("a", class_="goods-tile__heading").get("href")
    product_page = requests.get(product_url)
    product_soup = BeautifulSoup(product_page.content, "html.parser")

    processor_div = product_soup.find("div", string=re.compile(r"Процесор"))
    processor = processor_div.find_next("div").text.strip() if processor_div else None

    series_div = product_soup.find("div", string=re.compile(r"Серія"))
    series = series_div.find_next("div").text.strip() if series_div else None

    system_div = product_soup.find("div", string=re.compile(r"Операційна система"))
    system = system_div.find_next("div").text.strip() if system_div else None

    camera_div = product_soup.find("div", string=re.compile(r"Основна камера"))
    camera = camera_div.find_next("div").text.strip() if camera_div else None

    iphone = {
        "id": len(iphones) + 1,
        "name": name,
        "price": price,
        "ram": ram,
        "storage": storage,
        "colors": colors,
        "processor": processor,
        "series": series,
        "system": system,
        "camera": camera
    }

    iphones.append(iphone)

page = 2
while page < 4:
    url = f"{base_url}page={page};producer=apple/"
    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html, "html.parser")
    product_blocks = soup.find_all("div", class_="goods-tile")

    if not product_blocks:
        break

    for block in product_blocks:
        name = block.find("span", class_="goods-tile__title").text.strip()
        price_text = block.find("span", class_="goods-tile__price-value").text.strip()
        price = int(re.sub(r'[^\d]', '', price_text))

        ram_storage_div = block.find("div", string=re.compile(r"ГБ"))
        if ram_storage_div:
            ram_storage_text = ram_storage_div.text.strip()
            ram, storage = map(lambda x: int(x.replace(" ГБ", "")), ram_storage_text.split("/"))
        else:
            ram = None
            storage = None

        colors = [color.text.strip() for color in block.find_all("div", class_="goods-tile__colors-item-color")]

        # Отримуємо додаткову інформацію зі сторінки товару
        product_url = block.find("a", class_="goods-tile__heading").get("href")
        product_page = requests.get(product_url)
        product_soup = BeautifulSoup(product_page.content, "html.parser")

        processor_div = product_soup.find("div", string=re.compile(r"Процесор"))
        processor = processor_div.find_next("div").text.strip() if processor_div else None

        series_div = product_soup.find("div", string=re.compile(r"Серія"))
        series = series_div.find_next("div").text.strip() if series_div else None

        system_div = product_soup.find("div", string=re.compile(r"Операційна система"))
        system = system_div.find_next("div").text.strip() if system_div else None

        camera_div = product_soup.find("div", string=re.compile(r"Основна камера"))
        camera = camera_div.find_next("div").text.strip() if camera_div else None

        iphone = {
            "id": len(iphones) + 1,
            "name": name,
            "price": price,
            "ram": ram,
            "storage": storage,
            "colors": colors,
            "processor": processor,
            "series": series,
            "system": system,
            "camera": camera
        }

        iphones.append(iphone)

    page += 1

with open("iphones.json", "w", encoding="utf-8") as f:
    json.dump(iphones, f, ensure_ascii=False, indent=2)