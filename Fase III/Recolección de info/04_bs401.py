from bs4 import BeautifulSoup
import requests

url = input("Ingresa un sitio web: ")
r = requests.get("http://"+url)
data = r.text
#print(data)
#input()
soup = BeautifulSoup(data,'html.parser')
result = soup.find_all('a')
print(type(result))
for link in result:
    if link is not None:
        print(link.get('href'))
