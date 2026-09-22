import requests
from bs4 import BeautifulSoup

html = requests.get("https://xkcd.com/").text
sopa = BeautifulSoup(html, "html.parser")
print(sopa.title.string)
enlaces = sopa.find_all("a")
for enlace in enlaces:
    print(enlace.get("href"), enlace.text)
