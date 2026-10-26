"""
whois_ejemplo.py — Consulta WHOIS de un dominio
Compara las bibliotecas 'whois' y 'whois11'.

  whois   → más popular y activa en PyPI; devuelve objeto con atributos
  whois11 → interfaz más simple, menos mantenida

Instalar UNA de las dos: pip install whois
Uso:  python whois_ejemplo.py -d google.com
"""
import argparse

# Intentamos primero la biblioteca 'whois' (más recomendada)
try:
    import whois as whois_lib
    LIBRERIA = "whois"
except ImportError:
    try:
        import whois11 as whois_lib
        LIBRERIA = "whois11"
    except ImportError:
        print("Instala una de las dos bibliotecas: pip install whois")
        raise


def consultar_dominio(dominio: str) -> None:
    print(f"[*] Consultando WHOIS de '{dominio}' (usando '{LIBRERIA}')...\n")
    info = whois_lib.whois(dominio)
    print(info)

    # Con la biblioteca 'whois', también puedes acceder a campos específicos:
    if LIBRERIA == "whois":
        print(f"\n  Registrador   : {info.registrar}")
        print(f"  Fecha creación: {info.creation_date}")
        print(f"  Vencimiento   : {info.expiration_date}")
        print(f"  Servidores NS : {info.name_servers}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Consulta WHOIS de un dominio")
    parser.add_argument("-d", "--dominio", required=True, help="Dominio a consultar")
    args = parser.parse_args()

    consultar_dominio(args.dominio)


if __name__ == "__main__":
    main()
