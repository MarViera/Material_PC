#!/usr/bin/env python
import argparse
import socket
from cryptography.fernet import Fernet

# --- Paso de argumentos ---
description = """Modo de uso:
client.py -msj "Mensaje a enviar"
"""
parser = argparse.ArgumentParser(description='Cliente TCP cifrado',
                                 epilog=description,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument("-msj", metavar='MSJ', dest="msj",
                    help="mensaje a enviar", required=True)
params = parser.parse_args()

# --- Generar el objeto para cifrar ---
clave = Fernet.generate_key()
cipher_suite = Fernet(clave)

# --- Almacenamos la clave ---
with open('clave.key', 'wb') as file:
    file.write(clave)

# --- Tomar el argumento y convertirlo a bytes ---
mensaje = params.msj
mensajeBytes = mensaje.encode()

# --- Ciframos el mensaje ---
msj_cifrado = cipher_suite.encrypt(mensajeBytes)
print("Mensaje enviado:\n", mensaje)

# --- Preparamos los datos de la conexión ---
TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 2048

# --- Establecemos la conexión ---
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(msj_cifrado)
respuesta = s.recv(BUFFER_SIZE).decode()
s.close()

print("Respuesta recibida:", respuesta)
