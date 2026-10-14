from cryptography.hazmat.primitives.asymmetric \
     import rsa, padding
from cryptography.hazmat.primitives import \
     hashes, serialization

clave_privada = rsa.generate_private_key(
    public_exponent=65537, key_size=2048)
clave_publica = clave_privada.public_key()

# Serializar a PEM para mostrar cómo se ven las claves
pem_priv = clave_privada.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)
pem_pub = clave_publica.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)
print("--- Clave Pública ---")
print(pem_pub.decode())
print("--- Clave Privada ---")
print(pem_priv.decode())

oaep = padding.OAEP(
    mgf=padding.MGF1(algorithm=hashes.SHA256()),
    algorithm=hashes.SHA256(),
    label=None
)

mensaje    = b"Mensaje secreto RSA"
cifrado    = clave_publica.encrypt(mensaje, oaep)
descifrado = clave_privada.decrypt(cifrado, oaep)

print(f"Original  : {mensaje}")
print(f"Cifrado   : {cifrado.hex()[:40]}...")
print(f"Descifrado: {descifrado}")
