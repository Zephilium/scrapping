import requests
from bs4 import BeautifulSoup

url = requests.get("https://www.kompas.com/")
soup = BeautifulSoup(url.text, "html.parser")

popular_area = soup.find(attrs={"class": "most ga--most mt1 clearfix"})

titles = popular_area.find_all(attrs={"class": "most__title"})

views = popular_area.find_all(attrs={"class": "most__read"})

z = 0

for i in titles:
    print(f"\n{i.text}\n{views[z].text}")
    z += 1
