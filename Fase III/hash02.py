import hashlib, os

password    = "mi_contraseña"
salt        = os.urandom(16)# 16 bytes aleatorios
hash_salted = hashlib.sha256(salt +\
                password.encode()).hexdigest()

print(f"Salt (hex) : {salt.hex()}")
print(f"Hash+salt  : {hash_salted}")

# Verificación: ¿la contraseña coincide?
def verificar(pw, salt, hash_guardado):
    nuevo_hash = hashlib.sha256(salt +\
                    pw.encode()).hexdigest()
    return nuevo_hash == hash_guardado

print(verificar("mi_contraseña",
                salt, hash_salted))  # True
print(verificar("contraseña_mal",
                salt, hash_salted))  # False
