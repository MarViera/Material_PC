# 03_extraer.py — Alumno: encontrar el mensaje oculto en la imagen
# pip install pillow

from PIL import Image


def bits_a_texto(bits):
    mensaje = ""
    for i in range(0, len(bits), 8):
        byte = bits[i:i + 8]
        if len(byte) < 8:
            break
        char = chr(int("".join(map(str, byte)), 2))
        if char == '\0':            # fin del mensaje
            break
        mensaje += char
    return mensaje


def extraer_mensaje(ruta_imagen):
    img     = Image.open(ruta_imagen).convert("RGB")
    pixeles = list(img.getdata())

    bits = []
    for r, g, b in pixeles:
        bits.append(r & 1)
        bits.append(g & 1)
        bits.append(b & 1)

    return bits_a_texto(bits)


mensaje = extraer_mensaje("imagen_secreta.png")
print(f"Mensaje encontrado: {mensaje}")
