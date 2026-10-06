ALFABETO = (
    "abcdefghijklmnopqrstuvwxyz"
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    "0123456789"
    "!@#$%^&*()-_=+[]{}|;:',.<>?/ "
)
N = len(ALFABETO)

def cesar_ampliado(texto, desp):
    resultado = ""
    for c in texto:
        if c in ALFABETO:
            indice  = ALFABETO.index(c)
            nuevo   = (indice + desp) % N
            resultado += ALFABETO[nuevo]
        else:
            resultado += c
    return resultado

msg     = "Pass: C1ber2026!"
cifrado = cesar_ampliado(msg, 7)
claro   = cesar_ampliado(cifrado, -7)

print(f"Original  : {msg}")
print(f"Cifrado   : {cifrado}")
print(f"Descifrado: {claro}")
