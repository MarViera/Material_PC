from urllib.parse import quote, unquote

url_raw = "https://ejemplo.com/buscar?" +\
    "q=contraseña&usuario=héroe"

codif   = quote(url_raw, safe=':/?&=')
decodif = unquote(codif)

print(f"Original: {url_raw}")
print(f"Encoded : {codif}")
print(f"Decoded : {decodif}")
