import requests
from bs4 import BeautifulSoup

html = requests.get("https://xkcd.com/")
if html.status_code == 200:
    sopa = BeautifulSoup(html.text, "html.parser")
    print(sopa.title.string)
    enlaces = sopa.find_all("a")
    for enlace in enlaces:
        print(enlace.get("href"), enlace.text)
else:
    print(html,html.text,html.status_code)
