"""
shodan_search.py — Búsqueda en Shodan por palabra clave o IP
Combina shodan1.py (búsqueda) y shodan2.py (lookup por host).
Sin llaves hardcodeadas: usa getpass o variable de entorno SHODAN_KEY
Instalar: pip install shodan
Uso:  python shodan_search.py -q "apache"          # búsqueda por keyword
      python shodan_search.py --host 148.234.5.200  # lookup de un host
"""
import argparse
import getpass
import os
import sys

import shodan


def obtener_api_key() -> str:
    key = os.environ.get("SHODAN_KEY", "")
    if not key:
        key = getpass.getpass("Shodan API key: ")
    return key.strip()


def buscar_keyword(api: shodan.Shodan, query: str) -> None:
    try:
        resultados = api.search(query)
    except shodan.APIError as e:
        print(f"[!] Error Shodan: {e}")
        return

    total = resultados["total"]
    print(f"\n[*] Resultados para '{query}': {total} en total "
          f"(mostrando hasta 10)\n")

    for match in resultados.get("matches", []):
        ip      = match.get("ip_str", "?")
        org     = match.get("org", "sin organización")
        puerto  = match.get("port", "?")
        pais    = match.get("location", {}).get("country_name", "?")
        datos   = match.get("data", "")[:120].replace("\n", " ")
        print(f"  {ip:18s} :{puerto}  [{pais}]  {org}")
        print(f"    Banner: {datos}")
        print()


def lookup_host(api: shodan.Shodan, ip: str) -> None:
    try:
        info = api.host(ip)
    except shodan.APIError as e:
        print(f"[!] Error Shodan: {e}")
        return

    print(f"\n=== Información de {ip} ===")
    print(f"  Organización : {info.get('org', '?')}")
    print(f"  País         : {info.get('country_name', '?')}")
    print(f"  Ciudad       : {info.get('city', '?')}")
    print(f"  OS           : {info.get('os', '?')}")
    print(f"\n  Servicios encontrados:")
    for item in info.get("data", []):
        print(f"    Puerto {item['port']:5d}  {item.get('transport','tcp').upper()}"
              f"  {item.get('product','') or item.get('data','')[:60].replace(chr(10),' ')}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Cliente Shodan")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-q", "--query", help="Búsqueda por keyword")
    group.add_argument("--host",        help="Lookup por IP")
    args = parser.parse_args()

    api_key = obtener_api_key()
    api = shodan.Shodan(api_key)

    if args.query:
        buscar_keyword(api, args.query)
    else:
        lookup_host(api, args.host)


if __name__ == "__main__":
    main()
