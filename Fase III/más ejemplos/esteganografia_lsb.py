"""
esteganografia_lsb.py — Esteganografía LSB en imágenes PNG
Módulo: Pillow  |  pip install Pillow

LSB = Least Significant Bit (bit menos significativo)
      Ocultamos 1 bit de mensaje en el bit menos significativo de cada canal R, G, B.
      Cambio visual: ±1 en un valor 0-255 → imperceptible al ojo humano.

Uso:
    python esteganografia_lsb.py ocultar  --imagen foto.png --mensaje "Mensaje secreto" --salida oculto.png
    python esteganografia_lsb.py revelar  --imagen oculto.png

NOTA: Usar siempre PNG (sin pérdidas). JPEG recomprime y destruye los LSBs.
"""

import sys
import argparse
from PIL import Image


# Marcador de fin de mensaje — permite saber dónde termina el texto oculto
DELIMITADOR = "<<<FIN>>>"


# ─── Ocultar ──────────────────────────────────────────────────────────────────

def ocultar_mensaje(ruta_imagen: str, mensaje: str, ruta_salida: str) -> None:
    """Oculta un mensaje en los LSBs de los píxeles de una imagen PNG."""
    img = Image.open(ruta_imagen).convert("RGB")
    pixeles = list(img.getdata())

    # Convertir mensaje a bits
    datos = (mensaje + DELIMITADOR).encode("utf-8")
    bits = "".join(format(byte, "08b") for byte in datos)

    capacidad = len(pixeles) * 3  # 3 canales (R, G, B) × cantidad de píxeles
    if len(bits) > capacidad:
        print(f"[-] Imagen demasiado pequeña.")
        print(f"    Necesario: {len(bits)} bits | Disponible: {capacidad} bits")
        sys.exit(1)

    # Modificar el LSB de cada canal
    nuevos_pixeles = []
    idx = 0
    for r, g, b in pixeles:
        if idx < len(bits):
            r = (r & 0xFE) | int(bits[idx]); idx += 1
        if idx < len(bits):
            g = (g & 0xFE) | int(bits[idx]); idx += 1
        if idx < len(bits):
            b = (b & 0xFE) | int(bits[idx]); idx += 1
        nuevos_pixeles.append((r, g, b))

    img_nueva = Image.new("RGB", img.size)
    img_nueva.putdata(nuevos_pixeles)
    img_nueva.save(ruta_salida, format="PNG")

    print(f"[+] Mensaje oculto en '{ruta_salida}'")
    print(f"    Bits usados : {len(bits)} de {capacidad} disponibles")
    print(f"    Uso de imagen: {len(bits)/capacidad*100:.1f}%")


# ─── Revelar ──────────────────────────────────────────────────────────────────

def revelar_mensaje(ruta_imagen: str) -> str:
    """Extrae el mensaje oculto en los LSBs de una imagen PNG."""
    img = Image.open(ruta_imagen).convert("RGB")
    pixeles = list(img.getdata())

    # Leer el LSB de cada canal
    bits = ""
    for r, g, b in pixeles:
        bits += str(r & 1)
        bits += str(g & 1)
        bits += str(b & 1)

    # Reconstruir bytes y decodificar
    bytes_extraidos = bytearray()
    for i in range(0, len(bits) - 7, 8):
        byte = int(bits[i:i + 8], 2)
        bytes_extraidos.append(byte)

    texto = bytes_extraidos.decode("utf-8", errors="ignore")

    if DELIMITADOR in texto:
        return texto[:texto.index(DELIMITADOR)]

    return "[!] No se encontró delimitador — la imagen podría no tener mensaje oculto"


# ─── Programa principal ───────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Esteganografía LSB en imágenes PNG (ocultar y revelar mensajes)",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    sub = parser.add_subparsers(dest="accion", required=True)

    # Subcomando: ocultar
    p_oc = sub.add_parser("ocultar", help="Esconder un mensaje en una imagen")
    p_oc.add_argument("--imagen",   required=True,                       help="Imagen portadora original (PNG)")
    p_oc.add_argument("--mensaje",  required=True,                       help="Texto a ocultar")
    p_oc.add_argument("--salida",   default="imagen_con_mensaje.png",    help="Imagen de salida con el mensaje")

    # Subcomando: revelar
    p_rv = sub.add_parser("revelar", help="Extraer un mensaje oculto de una imagen")
    p_rv.add_argument("--imagen",   required=True, help="Imagen PNG que contiene el mensaje")

    args = parser.parse_args()

    if args.accion == "ocultar":
        ocultar_mensaje(args.imagen, args.mensaje, args.salida)

    elif args.accion == "revelar":
        mensaje = revelar_mensaje(args.imagen)
        print(f"[+] Mensaje encontrado:\n\n    {mensaje}\n")


if __name__ == "__main__":
    main()
