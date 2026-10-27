"""
scanner_os.py — Detección de sistema operativo con python-nmap
Requiere privilegios de root para la detección de OS (-O).
Instalar: pip install python-nmap
Uso:  sudo python scanner_os.py -t 148.234.5.222
"""
import nmap
import argparse
import sys


def detectar_os(target: str) -> None:
    scanner = nmap.PortScanner()

    print(f"[*] Escaneando {target} (detección de OS)...")
    scanner.scan(target, arguments="-O")  # Una sola llamada es suficiente

    hosts = scanner.all_hosts()
    if not hosts:
        print("[!] No se encontraron hosts activos.")
        return

    for ip in hosts:
        print(f"\nHost  : {ip}")
        print(f"Estado: {scanner[ip].state()}")

        if "osmatch" in scanner[ip]:
            for os_match in scanner[ip]["osmatch"]:
                print(f"  OS        : {os_match['name']}")
                print(f"  Precisión : {os_match['accuracy']}%")
                for clase in os_match.get("osclass", []):
                    print(f"    Familia : {clase.get('osfamily', '?')}  "
                          f"Generación : {clase.get('osgen', '?')}")
        else:
            print("  [!] No se pudo determinar el sistema operativo.")
            print("      Asegúrate de ejecutar con sudo.")


def main() -> None:
    parser = argparse.ArgumentParser(description="Detección de OS con nmap (-O)")
    parser.add_argument("-t", "--target", required=True, help="IP o host objetivo")
    args = parser.parse_args()

    if sys.platform != "win32" and __import__("os").geteuid() != 0:
        print("[!] Advertencia: la detección de OS generalmente requiere privilegios root.")

    detectar_os(args.target)


if __name__ == "__main__":
    main()
