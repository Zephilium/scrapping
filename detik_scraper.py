import requests
from bs4 import BeautifulSoup

url = requests.get("https://www.detik.com/terpopuler", params={"tag_from": "wp_cb_mostPopular_more"})

soup = BeautifulSoup(url.text, "html.parser")

popular_area = soup.find(attrs={"class": "grid-row list-content"})

titles = popular_area.find_all(attrs={"class": "media__title"})

for i in titles:
    print(i.text)

images = popular_area.find_all(attrs={"class": "media__image"})

# print(images)
