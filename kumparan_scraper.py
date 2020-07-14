import requests
from bs4 import BeautifulSoup

url = requests.get("https://kumparan.com/trending")
soup = BeautifulSoup(url.text, "html.parser")

popular_area = soup.find(attrs={"class": "TrendingView__TrendingListViewContainer-sc-11x2h62-0 jKmbrh"})
titles = popular_area.find_all(attrs={"class": "TextBoxweb__StyledTextBox-n41hy7-0 feePYD"})

for x in titles:
    print(x.text)

images = popular_area.find_all(attrs={"class": "Thumbnailweb__ThumbnailContainer-xodrtt-2 goTQKp"})

# print(images)
