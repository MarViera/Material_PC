from cryptography.hazmat.primitives.asymmetric \
     import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.exceptions import \
     InvalidSignature

clave_privada = rsa.generate_private_key(
    public_exponent=65537, key_size=2048)
clave_publica = clave_privada.public_key()

msg_original = b"Calificacion: 70"
msg_alterado = b"Calificacion: 100"

pss   = padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH)
firma = clave_privada.sign(msg_original, pss, hashes.SHA256())

try:
    clave_publica.verify(firma, msg_original, pss, hashes.SHA256())
    print("Firma válida")
except InvalidSignature:
    print("¡Firma inválida! El mensaje fue alterado.")
