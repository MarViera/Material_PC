#https://docs.python.org/3/library/hashlib.html
import hashlib
import os

path = input ("Escriba el nombre del archivo: ")

file_obj = open (path,"rb")
file = file_obj.read()

Hash = hashlib.sha512(file)
Hashed = Hash.hexdigest()

print (Hashed)
