import base64

dato = b"payload secreto" #bytes

hex_ = dato.hex()
b32  = base64.b32encode(dato)
b85  = base64.b85encode(dato)

print(f"Hex    : {hex_}")
print(f"Base32 : {b32}")
print(f"Base85 : {b85}")

# De hex de vuelta a bytes
original = bytes.fromhex(hex_)
print(f"Recuperado: {original}")
