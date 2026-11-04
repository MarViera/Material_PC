# 01_ocultar.py — Docente: preparar la imagen con el mensaje secreto
# pip install pillow

from PIL import Image


def texto_a_bits(texto):
    bits = []
    for char in texto + '\0':       # '\0' marca el fin del mensaje
        for bit in format(ord(char), '08b'):
            bits.append(int(bit))
    return bits


def ocultar_mensaje(ruta_imagen, mensaje, ruta_salida):
    img     = Image.open(ruta_imagen).convert("RGB")
    pixeles = list(img.getdata())
    bits    = texto_a_bits(mensaje)

    nuevos = []
    for idx, (r, g, b) in enumerate(pixeles):
        base = idx * 3
        nr = (r & 0xFE) | (bits[base]     if base     < len(bits) else 0)
        ng = (g & 0xFE) | (bits[base + 1] if base + 1 < len(bits) else 0)
        nb = (b & 0xFE) | (bits[base + 2] if base + 2 < len(bits) else 0)
        nuevos.append((nr, ng, nb))

    salida = Image.new("RGB", img.size)
    salida.putdata(nuevos)
    salida.save(ruta_salida, "PNG")
    print(f"Listo: mensaje oculto guardado en {ruta_salida}")


ocultar_mensaje("foto.png", "FCFM-UANL-2026", "imagen_secreta.png")
