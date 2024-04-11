import requests
from bs4 import BeautifulSoup
import re
import json

iphones = []

def get_iphones():
    base_url = "https://rozetka.com.ua/ua/mobile-phones/c80003/"
    
    url = f"{base_url}producer=apple/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    
    product_blocks = soup.find_all("div", class_="goods-tile")

    for block in product_blocks:
        name = block.find("span", class_="goods-tile__title").text.strip()
        
        price_text = block.find("span", class_="goods-tile__price-value").text.strip()
        price = int("".join(filter(str.isdigit, price_text)))

        ram_match = re.search(r'(\d+)\s*GB', name)
        ram = int(ram_match.group(1)) if ram_match else None
            
        colors = [re.search(r'#(\w+)', color_elem.find("span", class_="goods-tile__colors-content").get("style")).group(0) for  color_elem in block.find_all("li", class_="goods-tile__colors-item")]

        # product_url = block.find("a", class_="goods-tile__heading").get("href")
        # product_page = requests.get(product_url)
        # product_soup = BeautifulSoup(product_page.content, "html.parser")

        iphone = {
            "id": len(iphones) + 1,
            "name": name,
            "price": price,
            "ram": ram,
            "colors": colors,
            # "processor": processor,
            # "camera": camera
        }

        iphones.append(iphone)

get_iphones()

with open("iphones.json", "w", encoding="utf-8") as f:
    json.dump(iphones, f, ensure_ascii=False, indent=2)