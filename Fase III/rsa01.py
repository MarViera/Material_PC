from cryptography.hazmat.primitives.asymmetric \
     import rsa

# Generar clave privada RSA de 2048 bits
clave_privada = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
) #paso de parámetros por nombre

# Extraer la clave pública
clave_publica = clave_privada.public_key()

nums = clave_publica.public_numbers()
print(f"Tamaño    : {clave_privada.key_size} bits")
print(f"Exponente : {nums.e}")
print(f"Módulo n  : {str(nums.n)[:40]}...")
