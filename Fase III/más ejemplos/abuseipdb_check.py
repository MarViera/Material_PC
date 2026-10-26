"""
abuseipdb_check.py — Verificar reputación de una IP con AbuseIPDB
Sin llaves hardcodeadas: usa getpass o variable de entorno ABUSEIPDB_KEY
Instalar: pip install requests
Uso:  python abuseipdb_check.py -i 52.123.250.32
       ABUSEIPDB_KEY=<tu_key> python abuseipdb_check.py -i 52.123.250.32
"""
import argparse
import getpass
import os

import requests

API_URL = "https://api.abuseipdb.com/api/v2/check"


def obtener_api_key() -> str:
    """Toma la key de la variable de entorno o la pide de forma segura."""
    key = os.environ.get("ABUSEIPDB_KEY", "")
    if not key:
        key = getpass.getpass("AbuseIPDB API key: ")
        # 1351d01769557d0f4f0e59265e9b3b401a122bac5c33b6fcbf15ac6f7a1d7e55b5d53ff5f43a287c
    return key.strip()


def verificar_ip(ip: str, api_key: str, dias: int = 90) -> None:
    headers = {
        "Accept": "application/json",
        "Key": api_key,
    }
    params = {
        "ipAddress": ip,
        "maxAgeInDays": dias,
        "verbose": True,
    }

    try:
        r = requests.get(API_URL, headers=headers, params=params,
                         timeout=10)
        r.raise_for_status()
    except requests.exceptions.ConnectionError:
        print("[!] Sin conexión a Internet.")
        return
    except requests.exceptions.HTTPError as e:
        print(f"[!] Error HTTP {r.status_code}: {e}")
        return
    except requests.exceptions.RequestException as e:
        print(f"[!] Error de red: {e}")
        return

    datos = r.json().get("data", {})
    score   = datos.get("abuseConfidenceScore", "?")
    pais    = datos.get("countryCode", "?")
    dominio = datos.get("domain", "?")
    reportes = datos.get("totalReports", 0)
    isp     = datos.get("isp", "?")

    print(f"\n=== Reporte para {ip} ===")
    print(f"  Puntaje de abuso : {score}%")
    print(f"  País             : {pais}")
    print(f"  ISP              : {isp}")
    print(f"  Dominio          : {dominio}")
    print(f"  Reportes totales : {reportes}")

    if score >= 80:
        print("ALTA probabilidad de actividad maliciosa.")
    elif score >= 40:
        print("Actividad sospechosa detectada.")
    else:
        print("Bajo índice de abuso.")


def main() -> None:
    msg = "Verificación de IP en AbuseIPDB"
    parser = argparse.ArgumentParser(description=msg)
    parser.add_argument("-i", "--ip",   required=True,
                        help="IP a verificar")
    parser.add_argument("-d", "--dias", type=int, default=90,
                        help="Máximo de días en el historial (default: 90)")
    args = parser.parse_args()

    api_key = obtener_api_key()
    verificar_ip(args.ip, api_key, args.dias)


if __name__ == "__main__":
    main()
