import requests
from bs4 import BeautifulSoup as bs

page = requests.get ("https://www.uanl.mx/eventos/")    #Internamente es un método HTTP GET
print (page.status_code)                                #Status code 200 significa "Ok", 
#print (page.content)
input("1")
soup = bs(page.content,"html.parser")                   #Clase beautifulSoup
print (soup.prettify()) #pone bonito
input("2")

##Creamos un archivo html para referencia
fo = open ("pageOct17.html","wb") #w --> write, b --> bytes
fo.write (soup.prettify().encode()) 
fo.close()
##Cerramos el archivo html

po = soup.find_all("p") ##Buscamos todos los párrafos html p = paragraph
print ("Se encontraron",len(po),"resultados tipo párrafo")
print ("Accedemos al párrafo [0]")
potext = po[0].getText()
print (potext)
input()

## Imprime todos los párrafos
for p,i in zip(po,range(len(po))):
    print ("Párrafo",i,":",p.getText())
