import hashlib

dato = "mi_contrasena_segura"

md5    = hashlib.md5(dato.encode()).hexdigest()
sha1   = hashlib.sha1(dato.encode()).hexdigest()
sha256 = hashlib.sha256(dato.encode()).hexdigest()

print(f"Dato    : {dato}")
print(f"MD5     : {md5}")
print(f"SHA-1   : {sha1}")
print(f"SHA-256 : {sha256}")
