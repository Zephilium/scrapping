import requests
from bs4 import BeautifulSoup

url = requests.get("https://jadwalsholat.pkpu.or.id", params={"id" : "274"})
soup = BeautifulSoup(url.text, "html.parser")
jadwal = soup.find_all(attrs={"class" : "table_highlight"})
jadwal = jadwal[0]

i = 0
sholat = {}

for x in jadwal:
    if i == 1:
        sholat["Subuh"] = x.text
    elif i == 2:
        sholat["Dzuhur"] = x.text
    elif i == 3:
        sholat["Ashar"] = x.text
    elif i == 4:
        sholat["Maghrib"] = x.text
    elif i == 5:
        sholat["Isya"] = x.text
    i+=1

print(sholat)