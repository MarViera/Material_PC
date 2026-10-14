from cryptography.hazmat.primitives.asymmetric \
     import rsa, padding
from cryptography.hazmat.primitives import hashes

clave_privada = rsa.generate_private_key(public_exponent=65537, key_size=2048)
clave_publica = clave_privada.public_key()

pss     = padding.PSS(
    mgf=padding.MGF1(hashes.SHA256()),
    salt_length=padding.PSS.MAX_LENGTH
)
mensaje = b"Reporte de auditoria FCFM 2026-10-09"

# Firmar con clave PRIVADA
firma = clave_privada.sign(mensaje, pss,
                           hashes.SHA256())
print(f"Firma (hex): {firma.hex()[:40]}...")

# Verificar con clave PÚBLICA (no lanza excepción = válida)
clave_publica.verify(firma, mensaje, pss,
                     hashes.SHA256())
print("Firma válida")
