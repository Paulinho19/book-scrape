from bs4 import BeautifulSoup
import requests
from datetime import datetime
import json

dt = str(datetime.now()).split()

url = "https://books.toscrape.com"

book_request = requests.get(url).text

soup = BeautifulSoup(book_request,"lxml")

books = soup.find_all("article",class_="product_pod")

data = []

for book in books:
    book_title = book.find("h3").a.get("title")
    book_price = book.find("p",class_="price_color").text.strip()

    data.append({
        "book_name":book_title,
        "price": book_price
    })
    
    print(f"Book Name: {book_title} Price: {book_price}\n")
    print("*"*80)
    
with open ("books.json","w") as file:
    json.dump(data,file,indent=4)

print(f"This scrape was made from {url.replace("https://","")} on {dt[0]} at {dt[1]}")
