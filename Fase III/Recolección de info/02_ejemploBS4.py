import bs4 as bs
#pip install urllib
import urllib.request
source = urllib.request.urlopen('https://www.wikipedia.org/').read()
#print("Código HTML:\n",source)
#input()
soup = bs.BeautifulSoup(source,'html.parser')
print("Título:\n", soup.title.getText())
print("Nombre del título:\n", soup.title.name)
print("Nombre del padre:\n", soup.title.parent.name)
print("Párrafo:\n", soup.p.getText())

#<HTML> <HEAD> <TITLE>
