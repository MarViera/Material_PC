"""
hibp_check.py — Verificar si un correo fue filtrado (HaveIBeenPwned v3)
Requiere API key de https://haveibeenpwned.com/API/Key
Instalar: pip install requests
Uso:  python hibp_check.py usuario@ejemplo.com
"""
import sys
import logging
import getpass

import requests

# Configuración única de logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)s: %(message)s"
)

HIBP_URL = "https://haveibeenpwned.com/api/v3/breachedaccount/"
HEADERS_BASE = {
    "User-Agent": "Python-HIBP-Checker/1.0"
}


def verificar_correo(correo: str, api_key: str) -> None:
    url = HIBP_URL + correo
    headers = {**HEADERS_BASE, "hibp-api-key": api_key}
    params = {"truncateResponse": "false"}

    try:
        r = requests.get(url, headers=headers, params=params, timeout=10)
        r.raise_for_status()

        brechas = r.json()
        print(f"\n[!] El correo '{correo}' fue encontrado en {len(brechas)} brecha(s):")
        for brecha in brechas:
            print(f"  - {brecha['Name']} ({brecha.get('BreachDate', 'fecha desconocida')})")

    except requests.exceptions.ConnectionError:
        logging.error("No hay conexión a Internet o el servidor no responde.")
    except requests.exceptions.HTTPError as e:
        if r.status_code == 404:
            print(f"\n[✓] Buenas noticias: '{correo}' no aparece en brechas conocidas.")
        elif r.status_code == 401:
            logging.error("API key inválida.")
        elif r.status_code == 429:
            logging.error("Límite de peticiones alcanzado. Espera un momento.")
        else:
            logging.error("Error HTTP: %s", e)
    except requests.exceptions.RequestException as e:
        logging.error("Error de red: %s", e)


def main() -> None:
    if len(sys.argv) < 2:
        print("Uso: python hibp_check.py <correo>")
        sys.exit(1)

    correo = sys.argv[1]
    api_key = getpass.getpass("Ingresa tu HIBP API key: ")
    # ea29fedf3f714c549c6ac6da6b661bf1
    verificar_correo(correo, api_key)


if __name__ == "__main__":
    main()
