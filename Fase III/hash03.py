import bcrypt

password    = "mi_contraseña_segura".encode()
salt_rounds = 12                       # costo computacional (2^12 iteraciones)

# El mismo password hasheado dos veces da resultados distintos
# porque bcrypt genera un salt diferente cada vez
hash1 = bcrypt.hashpw(password,
                      bcrypt.gensalt(rounds=salt_rounds))
hash2 = bcrypt.hashpw(password,
                      bcrypt.gensalt(rounds=salt_rounds))

print(f"Hash 1: {hash1}")
print(f"Hash 2: {hash2}")
print(f"¿Son iguales? {hash1 == hash2}")        # False

# Aun así, checkpw verifica correctamente contra ambos
print(bcrypt.checkpw(password, hash1))           # True
print(bcrypt.checkpw(password, hash2))           # True
