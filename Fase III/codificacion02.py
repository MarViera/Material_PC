import base64

texto   = "contraseña+secreta_2026"
codif   = base64.b64encode(texto.encode("utf-8"))
decodif = base64.b64decode(codif).decode("utf-8")

print(f"Original  : {texto}")
print(f"Base64    : {codif}")
print(f"Decodif   : {decodif}")

# Variante URL-safe (tokens web, sin +)
url_64 = base64.urlsafe_b64encode(texto.encode())
url_safe = base64.urlsafe_b64decode(url_64)
print(f"URL-64  : {url_64}")
print(f"URL-safe  : {url_safe}")
