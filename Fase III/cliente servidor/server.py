#!/usr/bin/env python
import socket
from cryptography.fernet import Fernet

# --- Preparamos los datos de la conexión ---
TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 2048

# --- Establecemos la conexión ---
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
print("Servidor escuchando en:", TCP_IP, "puerto:", TCP_PORT)

conn, addr = s.accept()
print("Dirección de conexión:", addr)

# --- Recepción del mensaje cifrado ---
msj_cifrado = conn.recv(BUFFER_SIZE)
conn.send(b"Enterado. Bye!")
conn.close()

# --- Generar el objeto para descifrar ---
with open('clave.key', 'rb') as file:
    clave = file.read()

cipher_suite = Fernet(clave)
mensajeBytes = cipher_suite.decrypt(msj_cifrado)
mensaje = mensajeBytes.decode()

print("Mensaje recibido:\n", mensaje)
