# Funciones de validación para ciberseguridad

def validar_puerto(puerto):
    # Retorna True si el puerto está en rango válido
    if puerto < 1 or puerto > 65535:
        resultado = False
    else:
        resultado = True
    return resultado

def es_ip_privada(ip):
    # Retorna True si la IP empieza con 192.168
    if ip.startswith("192.168."):
        resultado = True
    else:
        resultado = False
    return resultado
