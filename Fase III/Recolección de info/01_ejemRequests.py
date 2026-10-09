import requests
# https://www.wikipedia.org/
url = input("Ingresa un sitio web (incluye el http): ")
r = requests.get(url)
print(r)
print(type(r))
input()
if r.status_code == 200:
    pagina = r.text
    print(type(pagina))
else:
    print("La pagina no existe, bye!")
    exit()
