def cifrar_cesar(texto, desp):
    resultado = ""
    for c in texto:
        if c.isalpha():
            if c.isupper():
                base = ord('A')
            else:
                base = ord('a')
            resultado += chr((ord(c) - base + desp) % 26 + base)
        else:
            resultado += c
    return resultado

msg     = "Hola Mundo Secreto"
cifrado = cifrar_cesar(msg, 3)
claro   = cifrar_cesar(cifrado, -3)

print(f"Original  : {msg}")
print(f"Cifrado   : {cifrado}")
print(f"Descifrado: {claro}")
