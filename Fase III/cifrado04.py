from cryptography.fernet import Fernet

# Generar clave aleatoria —
# guardarla de forma segura
clave = Fernet.generate_key()
f     = Fernet(clave)

mensaje    = b"Datos confidenciales del objetivo"
cifrado    = f.encrypt(mensaje)
descifrado = f.decrypt(cifrado)

print(f"Clave      : {clave}...")
print(f"Cifrado    : {cifrado}...")
print(f"Descifrado : {descifrado}")
