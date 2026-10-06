texto = "Físico Matemáticas"

# Codificar texto → bytes
utf8   = texto.encode("utf-8")
utf16  = texto.encode("utf-16")
ascii_ = texto.encode("ascii", errors="replace")

print(f"UTF-8 : {utf8}")
print(f"UTF-16: {utf16}")
print(f"ASCII : {ascii_}")

# Decodificar bytes → str
recuperado = utf16.decode("utf-16")
print(f"Recuperado: {recuperado}")
